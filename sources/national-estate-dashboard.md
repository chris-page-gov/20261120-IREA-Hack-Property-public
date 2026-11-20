---
type: Data analysis
title: National estate retrofit investigation dashboard
description: Estate dashboard, local NGD enrichment, ONS area join and evidence for the next phase.
sources:
  - id: estate
    resource: https://www.data.gov.uk/dataset/a3ad62cf-d8a2-4d3b-b3c6-24c35c5e0f71/the-government-property-estate-including-buildings-and-land
  - id: ons-boundaries
    resource: https://www.data.gov.uk/dataset/fb2b3c66-0902-4900-be64-09057aafc634/counties-and-unitary-authorities-december-2025-boundaries-uk-bfc
  - id: os-building
    resource: https://docs.os.uk/more-than-maps/data-demonstrators/topography-demonstrators/os-ngd-buildings/building-feature-type
  - id: os-address
    resource: https://docs.os.uk/osngd/data-structure/address
  - id: haduk-grid
    resource: https://catalogue.ceda.ac.uk/uuid/4dc8450d889a491ebb20e724debe2dfb/
  - id: energy-trends-weather
    resource: https://www.gov.uk/government/statistics/energy-trends-section-7-weather
  - id: eeic
    resource: https://dms.beis.gov.uk/eeic
  - id: eeic-sharing-agreement
    resource: https://assets.publishing.service.gov.uk/media/67ed060c199d1cd55b48c629/warm-homes-social-housing-fund-wave-3-data-sharing-agreement.pdf
observed_on: "2026-11-20"
---

# National estate retrofit investigation dashboard

The dashboard explores the Cabinet Office Building workbook across the
national estate. It identifies records worth checking for possible retrofit,
not savings estimates or investment decisions. The Warwickshire case is not
part of this dashboard. The workbook is recorded in the
[snapshot manifest](workbook-snapshots.json); the analysis reads the ignored
local copy and produces `analysis/reviewed-dashboard-data.json` and
`dashboard/src/data.json`. Neither output contains OS NGD feature bodies or a
credential. A fixed snapshot was deployed on 20 November 2026 to the
[owner-restricted Site](https://government-estate-retrofit-2026.crpage.chatgpt.site/?view=1&tab=dashboard).
The later [public static national screen](https://chris-page-gov.github.io/20261120-IREA-Hack-Property-public/national/)
uses the reviewed analysis JSON, a simplified ONS map and the full provisional
candidate register. It makes no request to the local NGD service.
The deployment and full HTML and snapshot asset readback passed. The live HTML
and snapshot routes returned HTTP 200, and the snapshot hash matched the
reviewed upload. The signed-in opening view rendered the overview, map and
investigation table. Filtering to NHS Bodies gave 8,543 building records and
161 investigation prompts. Clearing the filter restored the national view.
The owner editor opened and was closed without saving. On-demand NGD checks
run locally. The hosted snapshot excludes licensed OS NGD building fields and
the key. OKF semantic generation, CI and corpus publication remain disabled.

## Snapshot and screening method

The workbook had 53,009 rows and 52,977 distinct non-empty building references.
There were 29 references repeated across rows. The dashboard counts rows, and
does not treat them as confirmed unique buildings. It groups records by sector,
region and recorded use, then plots broad 0.2-degree location bins from the
workbook coordinates.

For area screening, only values above 1 m² labelled `IPMS 3 Net Internal area`
are treated as usable measured net internal area (NIA). This yields 10,992
rows (20.7%). Another 5,145 rows have a 1 m² area, which is suspicious rather
than evidence of a very small building. An EPC or DEC band is recorded on 2,313
rows (4.4%). An E–G band with usable measured NIA yields 492 prompts; a further
1,775 have at least 1,000 m² measured NIA but no band. These 2,267 prompts
need certificate, identity, energy-use and site review. EPC and DEC are distinct
schemes; many expiry dates are missing. The evidence radar shows field coverage
and is not a retrofit suitability score.

## Local OS NGD retrieval

The dashboard server runs on `127.0.0.1` and reads the existing OS key only when
the user selects a building. It queries the fixed NGD Building feature type in
a 30 m British National Grid window around the workbook point. It follows
offset pages, up to five pages or 500 features, and rejects incomplete,
oversized, repeated or wrong-CRS results. It returns selected attributes only
after exactly one building polygon contains the estate point. No raw NGD
geometry is written to disk or returned to the browser. This is an on-demand
local check, not a national NGD extract or a proven estate-wide join. The
OS PSGA rights and any external reuse require separate review.

On 20 November 2026, a diagnostic `limit=5` returned 12 features across three
pages; the normal `limit=100` returned the same 12 in one page. Both found one
containing polygon. The matched feature had footprint area, height, roof shape,
roof material and connectivity, but no `numberoffloors`. The browser button
showed these same fields. The first apparent truncation was the deliberate
five-feature diagnostic page size, not lost data.

The local draft shows the spatial match separately from OS height confidence.
It shows the feature version date, height and roof shape evidence dates, and
the floor count source and evidence date where returned. A single containing
polygon gives a spatial match to the workbook point. Building identity still
needs checking. Where both footprint area and floor count are available, the
draft shows their product as indicative gross area alongside the workbook's
measured NIA. Floorplates may vary in size and the floor count may be modelled.
On 20 November 2026, two selected office records returned single matches with
floor counts. Two selected dwelling records had no containing polygon. These
four checks establish that both outcomes occur on the local route.
[OS Building field definitions](https://docs.os.uk/osngd/data-structure/buildings/building-features/building).

OS defines `numberoffloors` as the maximum occupiable above-ground floors for
eligible residential and office buildings. It may be observed, taken from EPC
data or modelled, so a missing value cannot be filled from height alone without
an explicit estimate and uncertainty. OS says its model uses building height,
local authority address data, EPC data and topography. [OS Building feature
type](https://docs.os.uk/more-than-maps/data-demonstrators/topography-demonstrators/os-ngd-buildings/building-feature-type)
and [creation method](https://docs.os.uk/osngd/using-os-ngd-data/os-ngd-buildings/how-building-data-is-created).

The newer NGD Address theme has `floorlevel`, `lowestfloorlevel` and
`highestfloorlevel` for address records where supplied by local authority
custodians. These describe an address, not the count of occupiable floors in
its whole building. The theme is available through OS Select+Build, not the
NGD Features API used here. A licensed address extract and a verified UPRN or
related-entity join could provide a cross-check, with nulls and multi-address
buildings handled explicitly. The Building workbook has a `Postcode` field but
no UPRN field. [NGD Address theme](https://docs.os.uk/osngd/data-structure/address),
[Built Address fields](https://docs.os.uk/osngd/data-structure/address/gb-address/built-address)
and [OS floor-level FAQ](https://docs.os.uk/osngd/getting-started/faqs).

## ONS area comparison and other material held locally

The local draft assigns workbook points to the December 2025 ONS counties and
unitary authority boundaries. It checks the archive against the intake
checksum and transforms workbook longitude and latitude from WGS84 to British
National Grid (EPSG:27700). A record is assigned only if its point is strictly
inside exactly one polygon with no other intersection. The join uses all 218
full resolution boundaries clipped at mean high water. The map uses separate
display shapes simplified by 350 m. The assignment is evidence about the
recorded point. Coordinate errors and the clipped coastline can affect it.

The join assigned 52,881 of 53,009 rows (99.8%), covering 212 areas. It left
128 rows unassigned, including 3 investigation prompts. Five had missing or
unusable coordinates. The remaining 123 fell outside the clipped boundaries,
including 33 with the workbook region `International`. The join reconciles
to the national total of 2,267 investigation prompts. Area comparisons use
aggregate counts and shares. The data adds the area code and name to individual
investigation prompts. The browser showed the map, area table and original
national totals. The NHS Bodies filter gave 8,540 assignments from 8,543 rows
and kept all 161 prompts. Selecting a table row by keyboard highlighted its
area on the map. These changes are in the local draft.

| Material | Coverage and possible use | Limit |
| --- | --- | --- |
| ONS December 2025 counties and unitary authorities BFC shapefile | 218 UK boundary features in British National Grid. The ignored copy and checksum are in the [NDL intake manifest](ndl-estate-snapshots.json). The local draft shows the boundary join alongside the existing workbook region labels and broad bins. | These are December 2025 areas and they vary in size. Compare evidence shares and record counts together. [ONS digital boundary terms and attribution](https://www.ons.gov.uk/methodology/geography/geographicalproducts/digitalboundaries). |
| ONS geography cache in `mcp-geo` | Its index dated 10 April 2026 records 2,721,178 ONSPD postcode rows and the NSPL best-fit counterpart, plus UPRN lookup products, code history and geographic-code registers. The estate workbook has 52,687 non-empty postcodes, making a postcode-to-area join practical after validation. | The actual 145 GB SQLite cache is on the external drive; the dashboard itself does not need that drive. The cache marks itself degraded because its December 2025 UPRN products lag later AddressBase epochs. Postcode allocation can misassign an address near a boundary. The estate workbook has no UPRN for a direct UPRN lookup. See the [ONS postcode products guide](https://www.ons.gov.uk/methodology/geography/geographicalproducts/postcodeproducts). |
| 2021 Census accommodation type (TS044) in the separate WCC Domesday demo | A small Nomis extract has detached, semi-detached, terraced and flat categories for nine named areas including England, the West Midlands and Warwickshire. It can illustrate residential area context. | It is 2021 household-level aggregate evidence, not the form of an estate building, and does not cover all national small areas in this local extract. [ONS TS044 definition](https://www.ons.gov.uk/datasets/TS044/editions/2021/versions/3). |

The local GIS AI GO ONS bundle mainly contains dataset and service metadata;
its approved observation cache concerns weekly deaths and is irrelevant here.
On 20 November 2026, a read-only lookup of the first non-empty workbook
postcode found one ONSPD cache row with output area, LSOA, MSOA, local authority,
ward, country and region fields. This checks the route for one record, not
national match coverage or currency.
No cached ONS temperature, heating-degree-day, building-floor or measured
retrofit-savings layer was found. The separate ND-NEED workbook and EPC/DEC
aggregate tables in the intake are UK government energy sources, not ONS.

## Climate and benefit evidence

Met Office HadUK-Grid is a candidate for comparing local heating demand. The
published collection provides UK gridded observations and its `v1.3.2.ceda`
release adds daily mean temperature. A first pass can calculate annual heating
degree days for a shared period and declared base temperature. Report the grid
resolution and incomplete coverage, then compare comparable building uses
across the resulting climate bands. DESNZ Energy Trends table 7.1 supplies a
UK heating degree day benchmark. Neither series has been joined to the estate
in this draft. [Met Office HadUK-Grid collection](https://catalogue.ceda.ac.uk/uuid/4dc8450d889a491ebb20e724debe2dfb/),
[DESNZ Energy Trends weather data](https://www.gov.uk/government/statistics/energy-trends-section-7-weather).

For benefit and cost effectiveness, the next evidence would be measured
building-level energy use by fuel and period, tariff, actual construction and
fabric, occupancy, feasible measures, installed cost and local climate. Area
Census dwelling type cannot substitute for these. The dashboard should keep
provenance, geographic edition, joining method and unknowns visible when any
of these layers is added.

### Energy Efficiency Installation Checker

On 20 November 2026, the DESNZ portal displayed an email and password sign-in.
The Warm Homes Social Housing Fund Wave 3 data sharing agreement describes a
restricted tool used by approved scheme users for checks on fraud, error and
non-compliance. It describes records that can include property attributes,
UPRN, funding scheme, installation dates, measure type, size and cost. That
is evidence about scheme installations. The portal check established no estate
coverage, extract availability or permission to reuse records in this project.
No EEIC records were acquired. Any future use needs DESNZ approval for the
proposed purpose and an agreed extract and linkage method. The workbook lacks
UPRN, so an address or spatial identity check would still be needed.
[EEIC portal](https://dms.beis.gov.uk/eeic),
[DESNZ data sharing agreement](https://assets.publishing.service.gov.uk/media/67ed060c199d1cd55b48c629/warm-homes-social-housing-fund-wave-3-data-sharing-agreement.pdf).

### Sources for a benefits assessment

| Input | Benchmark or reference | Evidence needed for an individual building |
| --- | --- | --- |
| Local weather | HadUK-Grid for local heating degree days, with DESNZ Energy Trends table 7.1 for context. | Match the building location and metering period to the weather grid. |
| Fuel and consumption | [ND-NEED 2026](https://www.gov.uk/government/statistics/non-domestic-national-energy-efficiency-data-framework-nd-need-2026) gives metered gas and electricity benchmarks by use and size for England and Wales. The supporting workbook is cached. | Dated meter readings or bills for each fuel, with meter coverage, occupancy, hours and material changes in use. |
| Tariffs and carbon | [DESNZ non-domestic prices](https://www.gov.uk/government/statistical-data-sets/gas-and-electricity-prices-in-the-non-domestic-sector) give price scenarios by fuel and consumption band. The [UK 2026 conversion factors](https://www.gov.uk/government/publications/greenhouse-gas-reporting-conversion-factors-2026) are cached. | Contract tariffs and standing or demand charges where relevant. Use energy by fuel and document the factor year and emissions boundary. |
| Measure costs and feasibility | [Public Sector Decarbonisation Scheme Phase 1 evaluation](https://www.gov.uk/government/publications/public-sector-decarbonisation-scheme-psds-evaluation-of-phase-1) gives evidence from prior public sector projects. | A building survey, costed options, enabling works and a proposed or measured energy change by fuel. |

Start with a metered baseline for one building and a feasible, costed measure.
Document any weather and occupancy adjustment. Estimate the change in energy
by fuel first, then price and carbon using the chosen tariffs and factors.
