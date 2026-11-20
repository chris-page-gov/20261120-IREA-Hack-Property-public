---
type: Data intake
title: UK estate and Warwickshire pilot data intake
description: Verified public publisher files, National Data Library catalogue evidence and outstanding access routes.
sources:
  - id: estate
    resource: https://www.data.gov.uk/dataset/a3ad62cf-d8a2-4d3b-b3c6-24c35c5e0f71/the-government-property-estate-including-buildings-and-land
  - id: epb
    resource: https://get-energy-performance-data.communities.gov.uk/
  - id: scotland
    resource: https://data.gov.scot/dataset/non_domestic_energy_performance_certificates___dataset_to_q1_2026
  - id: northern-ireland
    resource: https://www.finance-ni.gov.uk/publications/foi-dof2026-0254-eir-response-re-request-all-available-domestic-and-non-domestic-energy-performance-epc-data-northern-ireland-machine-processable-format
  - id: wcc
    resource: https://www.warwickshire.gov.uk/directory-record/8957/property-and-asset-list-february-2026
observed_on: "2026-11-17"
---

# Downloaded data

The [intake manifest](ndl-estate-snapshots.json) records 26 verified new files
and the prior [Building and Property Contract manifest](workbook-snapshots.json).
The raw payloads are local and Git-ignored. Use the manifest to find the
publisher URL, scope, byte count, checksum, and update evidence for each file.
Keep package dates and query dates separate from source validity.

| Coverage | Verified files and intended use |
| --- | --- |
| UK central government estate | All six Cabinet Office workbooks are local. The four new ones are Land, Occupation, Disposal (Surplus), and Vacant Space. The publisher includes some overseas assets. Retain the Cabinet Office scope exclusions and table grains. State of the Estate and property portfolio tables provide an aggregate baseline.[^estate] |
| UK boundary | ONS December 2025 Counties and Unitary Authorities BFC shapefile, 218 features. The separate Warwickshire county polygon uses code E10000031 and the same boundary product. |
| Great Britain address and identifier links | OS Open UPRN October 2026 CSV and OS Open Linked Identifiers November 2026 method 5 CSV. Publisher checksums passed. The latter gives the BLPU-to-TopographicArea relationship. Feature identity and geometry coverage still require checks. |
| Warwickshire and adjacent area | OS OpenMap Local vector archives for SP and SK, with SO for adjoining context. Generalised building footprints support coarse screening. WCC's February 2026 published property and asset workbook provides the council cohort.[^wcc] |
| Warwick pilot | Aligned Environment Agency 1 m DSM and DTM GeoTIFFs, 3,000 by 3,000 cells, EPSG:27700, bounding box 427000, 264000, 430000, 267000. Match footprints and check terrain and survey vintage before computing volumes. Historic England returned 353 listed-building polygons intersecting that box. These are designation geometries. |
| England and Wales energy | Non-domestic EPC and DEC aggregate tables, the current service's two field dictionaries, and ND-NEED 2026 consumption benchmarks. Aggregate tables have no building-level certificate join. The UK Government 2026 conversion-factor file is local.[^epb] |
| Scotland energy | Scottish Government non-domestic EPC management-information archive, October 2026 extract. The publisher title and reference metadata say Q3 2026. The body description says Q2, so confirm the last assessment date before reporting coverage. Address fields have separate Royal Mail conditions.[^scotland] |
| Definitions | The Government Property Data Standard GOV.UK content JSON and LG Inform Plus Land and building assets schema are local. The original LG Inform Plus schema bytes are UTF-16LE. |

## Catalogue evidence and gaps

The private NDL OKF learning sample returned no property matches. The fuller
local OKF's 11 November successor view contains ten exact catalogue identities
used in this research. The manifest retains their native IDs, routes and
catalogue-row hashes. Publisher files were acquired from live sources and have
separate checksums. The NDL record-level EPC page retains a legacy service
pointer. Use the current MHCLG register route below.

| Source | Status |
| --- | --- |
| MHCLG non-domestic EPC and DEC records | Bulk download and bearer-token access require GOV.UK One Login. No live record-level acquisition or match test was made. Use a permitted Warwickshire sample for the prototype. Follow the provider's separate certificate address-data terms.[^epb] |
| Northern Ireland certificate data | The Department of Finance's June 2026 disclosure points to a Box folder covering through March 2026. The shared URL returned HTTP 404. No Northern Ireland bulk records were obtained.[^northern-ireland] |
| Older NDL public sector assets demonstrator | Its catalogue records discontinued underlying map access, partial participation and a historical snapshot. Use owner registers for current holdings. [NDL demonstrator record](https://www.data.gov.uk/dataset/c86f9536-5225-45be-bde1-7f4aa2b7920b/public-sector-land-and-building-assets-demonstrator) |
| Detailed NGD Building Parts and heights | Entitlement and permitted sharing to confirm via WCC/GIS AI GO. Use the local generalised footprints and matched LiDAR rasters for an offline experiment. |
| Flood layers | Source and screening purpose recorded. The NDL link leads to an area download tool or a WMS map. No analytic flood geometry was admitted. [Environment Agency surface-water planning extents](https://www.data.gov.uk/dataset/dfd734fb-cc68-4229-b60d-8c0280398052/flood-map-for-planning-surface-water-spatial-planning-extents-present-day) |

National thematic layers have publisher-specific geographic coverage.
High-volume terrain, footprints and heritage geometries were scoped to the
Warwickshire use case. Council internal sources and rights are for the
[Thursday Domesday review](warwickshire-domesday-review.md).

[^estate]: [Government Property Estate catalogue](https://www.data.gov.uk/dataset/a3ad62cf-d8a2-4d3b-b3c6-24c35c5e0f71/the-government-property-estate-including-buildings-and-land).
[^epb]: [MHCLG energy performance data service](https://get-energy-performance-data.communities.gov.uk/).
[^scotland]: [Scottish Government non-domestic EPC extract](https://data.gov.scot/dataset/non_domestic_energy_performance_certificates___dataset_to_q1_2026).
[^northern-ireland]: [Department of Finance disclosure DOF/2026-0254](https://www.finance-ni.gov.uk/publications/foi-dof2026-0254-eir-response-re-request-all-available-domestic-and-non-domestic-energy-performance-epc-data-northern-ireland-machine-processable-format).
[^wcc]: [Warwickshire property and asset list](https://www.warwickshire.gov.uk/directory-record/8957/property-and-asset-list-february-2026).
