---
type: Dataset
title: The Government Property Estate including Buildings and Land
description: Cabinet Office property transparency dataset linked in the organiser’s briefing.
resource: https://www.data.gov.uk/dataset/a3ad62cf-d8a2-4d3b-b3c6-24c35c5e0f71/the-government-property-estate-including-buildings-and-land
sources:
  - id: estate-catalogue
    resource: https://www.data.gov.uk/dataset/a3ad62cf-d8a2-4d3b-b3c6-24c35c5e0f71/the-government-property-estate-including-buildings-and-land
    title: National Data Library catalogue record
  - id: eventbrite-listing
    resource: ./eventbrite-listing.md
    title: Organiser’s briefing
observed_on: "2026-11-17"
catalogue_id: a3ad62cf-d8a2-4d3b-b3c6-24c35c5e0f71
---

# Challenge dataset

The organiser links to the Cabinet Office catalogue entry. It covers property
held by UK central government and arm’s-length bodies, with some overseas
assets. It excludes sensitive property records. Departments supply the
underlying data and a property can appear more than once when there are
multiple government interests. Buildings and land link to the property by
property reference.[^eventbrite-listing][^estate-catalogue]

The catalogue states a monthly refresh and lists the UK Open Government
Licence (OGL). The catalogue entry showed an update of 9 November 2026. The
two downloaded workbooks both returned a server Last-Modified date of
1 November 2026. These dates describe the catalogue and files respectively.
The organiser has yet to identify a pinned edition for the challenge.[^estate-catalogue]

# Resources

| Catalogue workbook | Local collection |
| --- | --- |
| [Building](https://stinsiteservicesprod01.blob.core.windows.net/insite/Building.xlsx) | Downloaded for building-level analysis |
| [Property Contract](https://stinsiteservicesprod01.blob.core.windows.net/insite/PropertyContract.xlsx) | Downloaded for property and tenure context |
| [Land](https://stinsiteservicesprod01.blob.core.windows.net/insite/Land.xlsx) | Downloaded in the second intake |
| [Occupation](https://stinsiteservicesprod01.blob.core.windows.net/insite/Occupation.xlsx) | Downloaded in the second intake |
| [Disposal](https://stinsiteservicesprod01.blob.core.windows.net/insite/Surplus.xlsx) | Downloaded in the second intake |
| [Vacant Space](https://stinsiteservicesprod01.blob.core.windows.net/insite/VacantSpace.xlsx) | Downloaded in the second intake |

The two downloaded files are in `sources/snapshots/2026-11-17/`. The
[workbook manifest](workbook-snapshots.json) records their hashes and upstream
metadata. Git ignores the local workbook files. ZIP integrity was checked.
The [estate OKF+ assessment](estate-okf-domain.md) records profiling findings.
Refer to the [second intake](ndl-estate-intake.md) for the four additional
workbooks, their hashes and the supporting datasets. Sharing rights for
derived outputs and individual fields still need review. The publisher’s links can
serve different bytes after a refresh.

[^estate-catalogue]: [Cabinet Office dataset in the National Data Library](https://www.data.gov.uk/dataset/a3ad62cf-d8a2-4d3b-b3c6-24c35c5e0f71/the-government-property-estate-including-buildings-and-land).
[^eventbrite-listing]: [Organiser’s briefing](eventbrite-listing.md).
