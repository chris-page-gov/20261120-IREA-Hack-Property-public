"""Assign workbook points to the pinned December 2025 ONS boundaries."""

from functools import lru_cache
import hashlib
import json
from pathlib import Path
from zipfile import ZipFile

from pyproj import CRS, Transformer
import shapefile
from shapely import Point, STRtree, is_valid, make_valid
from shapely.geometry import MultiPolygon, shape


ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = "sources/snapshots/2026-11-17/ndl/ons-uk-counties-unitaries-2025-bfc-shapefile.zip"
LAYER = "CTYUA_DEC_2025_UK_BFC"
SOURCE = "https://www.data.gov.uk/dataset/fb2b3c66-0902-4900-be64-09057aafc634/counties-and-unitary-authorities-december-2025-boundaries-uk-bfc"
TOLERANCE_METRES = 350
UNASSIGNED = {
    "missing": "Missing or unusable coordinates",
    "outside": "Outside the clipped UK boundaries",
    "boundary": "On or in more than one boundary",
}


def polygons(geometry):
    if geometry.geom_type == "Polygon":
        if not geometry.is_empty:
            yield geometry
    elif hasattr(geometry, "geoms"):
        for part in geometry.geoms:
            yield from polygons(part)


class EstateGeography:
    def __init__(self):
        manifest = json.loads((ROOT / "sources/ndl-estate-snapshots.json").read_text())
        asset = next(row for row in manifest["snapshots"] if row["file"] == ARCHIVE)
        with (ROOT / ARCHIVE).open("rb") as archive:
            digest = hashlib.file_digest(archive, "sha256").hexdigest()
            if digest != asset["sha256"]:
                raise ValueError("ONS archive does not match the snapshot manifest")
        self.digest = digest
        self.areas = {}
        self.repaired = 0
        with ZipFile(ROOT / ARCHIVE) as data:
            crs = CRS.from_wkt(data.read(f"{LAYER}.prj").decode())
            if crs.to_epsg() != 27700:
                raise ValueError("Expected British National Grid ONS boundaries")
            with shapefile.Reader(
                shp=data.open(f"{LAYER}.shp"), shx=data.open(f"{LAYER}.shx"), dbf=data.open(f"{LAYER}.dbf")
            ) as reader:
                for record in reader.iterShapeRecords():
                    code = record.record["CTYUA25CD"]
                    if code in self.areas:
                        raise ValueError(f"Duplicate ONS area code {code}")
                    geometry = shape(record.shape.__geo_interface__)
                    if not is_valid(geometry):
                        geometry = MultiPolygon(list(polygons(make_valid(geometry, method="structure"))))
                        self.repaired += 1
                    if geometry.is_empty or not is_valid(geometry):
                        raise ValueError(f"Invalid ONS geometry for {code}")
                    self.areas[code] = (record.record["CTYUA25NM"], geometry)
        if len(self.areas) != asset["features"]:
            raise ValueError("Unexpected ONS boundary count")
        self.codes = tuple(self.areas)
        self.tree = STRtree([geometry for _, geometry in self.areas.values()])
        self.transformer = Transformer.from_crs(4326, crs, always_xy=True)

    @lru_cache(maxsize=65536)
    def assign(self, longitude, latitude):
        if longitude is None or latitude is None or not (-180 <= longitude <= 180 and -90 <= latitude <= 90):
            return "missing"
        if not (-9 <= longitude <= 3 and 49 <= latitude <= 61):
            return "outside"
        point = Point(*self.transformer.transform(longitude, latitude, errcheck=True))
        intersections = self.tree.query(point, predicate="intersects")
        if len(intersections) == 0:
            return "outside"
        code = self.codes[int(intersections[0])]
        if len(intersections) != 1 or not self.areas[code][1].contains(point):
            return "boundary"
        return code

    def name(self, code):
        return UNASSIGNED[code] if code in UNASSIGNED else self.areas[code][0]

    def map_data(self):
        # One SVG unit is 2 km in British National Grid. Simplification is for display only.
        def draw_ring(ring):
            points = [(round(x / 2000 + 10, 1), round((1230000 - y) / 2000 + 5, 1)) for x, y in ring.coords[:-1]]
            return "M" + "L".join(f"{x:g},{y:g}" for x, y in points) + "Z" if len(set(points)) >= 3 else ""

        features = []
        for code, (name, geometry) in sorted(self.areas.items()):
            simplified = geometry.simplify(TOLERANCE_METRES, preserve_topology=True)
            svg_path = "".join(
                draw_ring(polygon.exterior) + "".join(draw_ring(ring) for ring in polygon.interiors)
                for polygon in polygons(simplified)
                if polygon.area >= 40_000
            )
            if not svg_path:
                raise ValueError(f"No display geometry for {code}")
            features.append({"code": code, "name": name, "path": svg_path})
        return {"viewBox": "0 0 350 630", "areas": features}
