"""Assemble the static public Pages edition from reviewed local outputs.

The Tower Hamlets source is a separately saved, static notebook directory.
This script copies its public assets; it never reads the local OS NGD service.
The committed docs/ tree is the complete deployable edition.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
NATIONAL = DOCS / "national" / "data"
TOWER = DOCS / "tower-hamlets"
PUBLIC_BASE = "https://chris-page-gov.github.io/20261120-IREA-Hack-Property-public/"


def candidate_csv(register: dict) -> None:
    columns = [
        "candidateNumber", "evaluationStatus", "propertyReference",
        "reportedTenureClass", "reportedTenures",
        "reportedContractOrganisations", "reportedContractReferences",
    ]
    screen_columns = list(register["records"][0]["screeningRecord"])
    path = NATIONAL / "candidates.csv"
    with path.open("w", encoding="utf-8-sig", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=columns + screen_columns)
        writer.writeheader()
        for item in register["records"]:
            row = {key: item.get(key) for key in columns}
            for key in ("reportedTenures", "reportedContractOrganisations", "reportedContractReferences"):
                row[key] = json.dumps(row[key], ensure_ascii=False)
            row.update(item["screeningRecord"])
            writer.writerow(row)


def rewrite_tower_html(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    # The notebook was built for a domain root. Pages serves it below /tower-hamlets/.
    text = re.sub(r'((?:href|src)=["\'])/(?!/)', r'\1./', text)
    text = text.replace(
        "https://government-estate-retrofit-2026.crpage.chatgpt.site/?view=1&amp;tab=dashboard",
        "../national/",
    ).replace(
        "https://government-estate-retrofit-2026.crpage.chatgpt.site/?view=1&tab=dashboard",
        "../national/",
    )
    text = text.replace("https://tower-hamlets-retrofit-notebook.crpage.chatgpt.site/", "./")
    text = text.replace("public static", "public static")
    text = text.replace("in any browser", "in any browser")
    text = text.replace("from a signed-in browser", "in any browser")
    text = re.sub(r'<a href="https://www\.eventbrite\.com/e/[^"]+">Organiser’s challenge</a>',
                  'Organiser’s challenge (unlisted source; see the source note in the repository)', text)
    extra = '<link rel="stylesheet" href="../assets/terms.css"><script src="../assets/terms.js" defer></script>'
    text = text.replace("</head>", extra + "</head>", 1)
    hub = '<div class="public-hub"><a href="../">Start with the journey</a><a href="../national/">National candidates</a><a href="./">Tower Hamlets notebook</a><a href="../methods/">Methods and gaps</a><a href="../rights/">Sources and rights</a></div>'
    text = text.replace("<body>", "<body>" + hub, 1)
    path.write_text(text, encoding="utf-8")


def copy_tower_notebook(source: Path) -> None:
    if not (source / "index.html").is_file() or not (source / "map-assets" / "estate.json").is_file():
        raise SystemExit("Tower Hamlets static notebook directory is incomplete")
    if TOWER.exists():
        shutil.rmtree(TOWER)
    shutil.copytree(source, TOWER)
    for path in TOWER.rglob("*.html"):
        rewrite_tower_html(path)
    for path in TOWER.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        text = text.replace(
            "https://tower-hamlets-retrofit-notebook.crpage.chatgpt.site/",
            PUBLIC_BASE + "tower-hamlets/",
        ).replace(
            "https://government-estate-retrofit-2026.crpage.chatgpt.site/",
            PUBLIC_BASE + "national/",
        )
        text = text.replace("public static", "public static")
        text = text.replace("in any browser", "in any browser")
        text = re.sub(r'\[Organiser’s challenge\]\(https://www\.eventbrite\.com/e/[^)]+\)',
                      'Organiser’s challenge (unlisted source; see the public source note)', text)
        path.write_text(text, encoding="utf-8")
    catalogue = TOWER / "data" / "visualisation-specifications.json"
    if catalogue.is_file():
        def public_fields(value):
            if isinstance(value, dict):
                return {key: public_fields(item) for key, item in value.items() if key != "local"}
            if isinstance(value, list):
                return [public_fields(item) for item in value]
            if isinstance(value, str):
                return value.replace("public static Site origin", "public site origin")
            return value
        catalogue.write_text(json.dumps(public_fields(json.loads(catalogue.read_text())),
                                        indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tower-dist", type=Path, required=True,
                        help="Reviewed static Tower Hamlets notebook distribution")
    args = parser.parse_args()
    NATIONAL.mkdir(parents=True, exist_ok=True)
    register = json.loads((ROOT / "analysis" / "candidate-register-2026-11-20.json").read_text())
    if register["counts"]["screeningRows"] != 2267 or len(register["records"]) != 2267:
        raise SystemExit("Candidate register count does not match the reviewed screen")
    shutil.copy2(ROOT / "analysis" / "candidate-register-2026-11-20.json", NATIONAL / "candidates.json")
    shutil.copy2(ROOT / "dashboard" / "src" / "data.json", NATIONAL / "dashboard.json")
    shutil.copy2(ROOT / "dashboard" / "src" / "content" / "dashboard" / "ons-area-map.json", NATIONAL / "ons-area-map.json")
    candidate_csv(register)
    for source, dest in (
        (ROOT / "analysis" / "estate-screening-funnel-a4.pdf", DOCS / "assets" / "estate-screening-funnel-a4.pdf"),
        (ROOT / "analysis" / "estate-screening-funnel.png", DOCS / "assets" / "estate-screening-funnel.png"),
        (ROOT / "sources" / "estate-screening-funnel.md", DOCS / "assets" / "estate-screening-funnel.md"),
    ):
        shutil.copy2(source, dest)
    funnel = DOCS / "assets" / "estate-screening-funnel.md"
    funnel.write_text(funnel.read_text(encoding="utf-8")
                      .replace("../analysis/estate-screening-funnel-a4.pdf", "estate-screening-funnel-a4.pdf")
                      .replace("../analysis/estate-screening-funnel.png", "estate-screening-funnel.png"),
                      encoding="utf-8")
    copy_tower_notebook(args.tower_dist)
    print(f"Built {DOCS} from reviewed snapshots and {args.tower_dist}")


if __name__ == "__main__":
    main()
