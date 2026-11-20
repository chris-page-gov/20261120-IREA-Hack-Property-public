"""Build a reviewed, aggregate dashboard snapshot from the Cabinet Office Building workbook.

The input workbook stays in the ignored snapshots directory. No NGD features or
private OS credentials enter this output. Run with the bundled Python runtime.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from datetime import datetime, timezone
import json
from pathlib import Path
import re

from openpyxl import load_workbook

from ons_estate_geography import EstateGeography, SOURCE as ONS_SOURCE, TOLERANCE_METRES, UNASSIGNED


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "sources/snapshots/2026-11-17/Building.xlsx"
OUTPUT = ROOT / "analysis/reviewed-dashboard-data.json"
APP_DATA = ROOT / "dashboard/src/data.json"
MAP_DATA = ROOT / "dashboard/src/content/dashboard/ons-area-map.json"
SOURCE_URL = (
    "https://www.data.gov.uk/dataset/a3ad62cf-d8a2-4d3b-b3c6-24c35c5e0f71/"
    "the-government-property-estate-including-buildings-and-land"
)
COUNT_FIELDS = (
    "records", "areaPositive", "areaOne", "areaUsable", "niaUsable",
    "epc", "dec", "energyEither", "epcPoor", "decPoor", "poorEither",
    "poorWithNia", "unratedLargeNia", "listedKnown", "listed",
    "coordinates", "constructionDate", "epcExpiryKnown", "epcExpired",
    "decExpiryKnown", "decExpired",
)


def text(value: object, fallback: str = "Not recorded") -> str:
    value = str(value or "").strip()
    return value or fallback


def number(value: object) -> float | None:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return None
    return float(value)


def rating_band(value: object) -> str | None:
    match = re.match(r"^([A-G])(?:\+|\b)", text(value, ""))
    return match.group(1) if match else None


def date(value: object) -> datetime | None:
    if isinstance(value, datetime):
        return value
    if isinstance(value, str) and value.strip():
        try:
            return datetime.fromisoformat(value.strip().replace("Z", "+00:00"))
        except ValueError:
            return None
    return None


def source(label: str, method: str) -> dict:
    return {
        "label": label,
        "url": SOURCE_URL,
        "tables": ["Cabinet Office Building.xlsx, Building sheet"],
        "filters": ["Snapshot observed 17 November 2026; source file last modified 1 November 2026."],
        "metricDefinitions": [{"label": "Method", "definition": method}],
    }


def main() -> None:
    geography = EstateGeography()
    sheet = load_workbook(INPUT, read_only=True, data_only=True).active
    records = sheet.values
    headers = next(records)
    cells: dict[tuple[str, str, str], Counter] = defaultdict(Counter)
    area_cells: dict[tuple[str, str, str, str], Counter] = defaultdict(Counter)
    assignments = Counter()
    bins: dict[tuple[str, str, str, float, float], int] = defaultdict(int)
    candidates: list[dict] = []
    unique_ids = set()
    ref_counts = Counter()
    as_of = datetime(2026, 11, 20)

    for values in records:
        row = dict(zip(headers, values))
        sector = text(row["Sector"])
        region = text(row["Region"])
        usage = text(row["Usage"])
        cell = cells[sector, region, usage]
        cell["records"] += 1
        ref = text(row["Insite Building Reference"], "")
        if ref:
            unique_ids.add(ref)
            ref_counts[ref] += 1

        area = number(row["Floor Area"])
        area_positive = area is not None and area > 0
        area_one = area == 1
        area_usable = area is not None and area > 1
        nia = area_usable and row["Floor Area Measurement"] == "IPMS 3 Net Internal area"
        epc = rating_band(row["EPC Property Rating"])
        dec = rating_band(row["DEC Operational Rating"])
        epc_poor = epc in {"E", "F", "G"}
        dec_poor = dec in {"E", "F", "G"}
        poor = epc_poor or dec_poor
        listed_value = text(row["Listed Building"], "")
        lat = number(row["Latitude"])
        lon = number(row["Longitude"])
        coordinate = lat is not None and lon is not None and 49 <= lat <= 61 and -9 <= lon <= 3
        area_code = geography.assign(lon, lat)
        assignments[area_code] += 1
        area_cell = area_cells[sector, region, usage, area_code]
        poor_with_nia = poor and nia
        unrated_large_nia = not (epc or dec) and nia and area >= 1000
        area_cell.update({"records": 1, "energyEither": bool(epc or dec), "niaUsable": nia,
                          "poorWithNia": poor_with_nia, "unratedLargeNia": unrated_large_nia})

        for field, yes in (
            ("areaPositive", area_positive), ("areaOne", area_one),
            ("areaUsable", area_usable), ("niaUsable", nia),
            ("epc", bool(epc)), ("dec", bool(dec)),
            ("energyEither", bool(epc or dec)),
            ("epcPoor", epc_poor), ("decPoor", dec_poor),
            ("poorEither", poor), ("poorWithNia", poor_with_nia),
            ("unratedLargeNia", unrated_large_nia),
            ("listedKnown", bool(listed_value)),
            ("listed", bool(listed_value) and listed_value != "Not Listed"),
            ("coordinates", coordinate),
            ("constructionDate", bool(row["Construction Date"])),
        ):
            if yes:
                cell[field] += 1
        if nia:
            cell["niaAreaM2"] += area

        for prefix, present in (("epc", epc), ("dec", dec)):
            if present:
                cell[f"{prefix}{present}"] += 1
            expiry = date(row["EPC Expiry Date"] if prefix == "epc" else row["DEC Expiry Date"])
            if expiry:
                cell[f"{prefix}ExpiryKnown"] += 1
                expiry = expiry.replace(tzinfo=None)
                if expiry.date() < as_of.date():
                    cell[f"{prefix}Expired"] += 1

        if coordinate:
            # 0.2-degree bins show broad distribution, not building footprints.
            lat_bin = round(round(lat * 5) / 5, 1)
            lon_bin = round(round(lon * 5) / 5, 1)
            bins[sector, region, usage, lat_bin, lon_bin] += 1

        if poor_with_nia or unrated_large_nia:
            candidates.append({
                "sector": sector, "region": region, "usage": usage,
                "areaCode": area_code if area_code in geography.areas else None,
                "onsArea": geography.name(area_code),
                "buildingReference": ref or "Not recorded",
                "propertyName": text(row["Property Name"]),
                "floorAreaM2": round(area, 1), "areaMethod": "IPMS 3 net internal area",
                "epcBand": epc or "Not recorded", "decBand": dec or "Not recorded",
                "listedStatus": listed_value or "Not recorded",
                "signal": "Recorded E–G rating and measured area" if poor else "Large measured area; energy rating absent",
            })

    cell_rows = []
    for (sector, region, usage), counts in sorted(cells.items()):
        cell_rows.append({"sector": sector, "region": region, "usage": usage,
                          **{field: counts[field] for field in COUNT_FIELDS},
                          "niaAreaM2": round(counts["niaAreaM2"], 1),
                          **{f"{prefix}{band}": counts[f"{prefix}{band}"]
                             for prefix in ("epc", "dec") for band in "ABCDEFG"}})
    bin_rows = [
        {"sector": sector, "region": region, "usage": usage,
         "latitude": lat, "longitude": lon, "records": count}
        for (sector, region, usage, lat, lon), count in sorted(bins.items())
    ]
    area_rows = [
        {"sector": sector, "region": region, "usage": usage, "areaCode": code,
         "onsArea": geography.name(code), "assigned": code in geography.areas, **counts}
        for (sector, region, usage, code), counts in sorted(area_cells.items())
    ]
    candidates.sort(key=lambda row: (row["signal"], -row["floorAreaM2"], row["buildingReference"]))

    result = {
        "surface": "dashboard",
        "title": "Government property estate: retrofit investigation",
        "generatedAt": datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z"),
        "status": "reviewed-local-snapshot",
        "filters": [
            {"id": "sector", "label": "Sector", "field": "sector", "defaultValue": "all"},
            {"id": "region", "label": "Region", "field": "region", "defaultValue": "all"},
            {"id": "usage", "label": "Use", "field": "usage", "defaultValue": "all"},
        ],
        "queries": {
            "building_cells": {
                "rows": cell_rows,
                "source": source("Building records by sector, region and use", "One row per sector × region × recorded use. Counts refer to workbook rows, not distinct buildings. Area above 1 m² is treated as usable for screening; 1 m² values are flagged as suspicious. Only IPMS 3 net internal area is summed."),
            },
            "location_bins": {
                "rows": bin_rows,
                "source": source("Approximate location bins", "Workbook latitude and longitude grouped into 0.2-degree bins. Points show broad concentration, not building outlines or exact sites. Invalid or out-of-range coordinates are excluded."),
            },
            "investigation_records": {
                "rows": candidates,
                "source": source("Investigation prompts", "Rows with an E–G EPC or DEC band and usable IPMS 3 area, or no EPC/DEC band and at least 1,000 m² usable IPMS 3 area. These are prompts for review, not retrofit recommendations. Certificate currency and building identity require checking."),
            },
            "area_cells": {
                "rows": area_rows,
                "source": {
                    "label": "Estate records by ONS county or unitary area",
                    "url": ONS_SOURCE,
                    "tables": ["Cabinet Office Building.xlsx, Building sheet", "ONS December 2025 UK CTYUA BFC boundaries"],
                    "filters": ["Workbook snapshot observed 17 November 2026. UK boundaries at December 2025."],
                    "metricDefinitions": [
                        {"label": "Area assignment", "definition": "Workbook longitude and latitude transformed from WGS84 to British National Grid. Assignment requires the point to be strictly within one full resolution polygon with no competing intersection. Unassigned records remain in the totals."},
                        {"label": "Display geometry", "definition": f"The map uses {TOLERANCE_METRES} m simplification for display only. Counts use the full resolution join."},
                        {"label": "Investigation prompts", "definition": "E–G EPC or DEC band with usable measured NIA, or no band with at least 1,000 m² measured NIA. These are workbook rows."},
                    ],
                },
            },
        },
        "metadata": {"records": sum(row["records"] for row in cell_rows),
                     "uniqueBuildingReferences": len(unique_ids),
                     "repeatedBuildingReferences": sum(v > 1 for v in ref_counts.values()),
                     "asOf": "2026-11-20", "sourceObservedOn": "2026-11-17",
                     "sourceLastModified": "2026-11-01",
                     "onsGeography": {"edition": "2025-12", "variant": "BFC", "analysisCrs": 27700,
                                      "boundaryArchiveSha256": geography.digest,
                                      "boundariesRepaired": geography.repaired,
                                      "assigned": sum(assignments[code] for code in geography.areas),
                                      "unassigned": {reason: assignments[reason] for reason in UNASSIGNED}}},
    }
    for field in ("records", "energyEither", "niaUsable", "poorWithNia", "unratedLargeNia"):
        if sum(row[field] for row in area_rows) != sum(row[field] for row in cell_rows):
            raise ValueError(f"ONS comparison does not reconcile to the workbook for {field}")
    if sum(row["poorWithNia"] + row["unratedLargeNia"] for row in area_rows) != len(candidates):
        raise ValueError("ONS comparison does not reconcile to the investigation records")

    app = json.loads(APP_DATA.read_text())
    app.update(result, buildStatus="updating")
    map_data = geography.map_data()
    for path, data in ((OUTPUT, result), (APP_DATA, app), (MAP_DATA, map_data)):
        path.write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":")) + "\n")
    print(json.dumps({"cells": len(cell_rows), "bins": len(bin_rows), "areaCells": len(area_rows),
                      "investigationRecords": len(candidates), **result["metadata"]}))


if __name__ == "__main__":
    main()
