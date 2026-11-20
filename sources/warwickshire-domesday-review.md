---
type: Review checklist
title: Warwickshire Domesday estate evidence review
description: Questions and public evidence for the review on Thursday 19 November 2026.
sources:
  - id: wcc-public
    resource: https://www.warwickshire.gov.uk/directory-record/8957/property-and-asset-list-february-2026
  - id: local-intake
    resource: ./ndl-estate-intake.md
  - id: planning-standard
    resource: ./planning-application-data-standard.md
observed_on: "2026-11-17"
updated_on: "2026-11-18"
review_on: "2026-11-19"
---

# Public baseline

The February 2026 WCC asset list has 648 rows. Of these, 555 are marked land
with a permanent building and 93 land only. There are 588 rows with a
syntactically usable UPRN, 582 distinct UPRNs and five UPRNs on multiple rows.
All DEC ratings and service-function codes are `To Follow`. Suitability is
`Not Currently Available` throughout. The workbook has GIA, tenure, easting,
northing, title and INSPIRE fields. There are four distinct UPRNs in common
with the central estate Property Contract workbook. Treat the cohorts
separately and investigate those four as identity candidates. The two
identically labelled asset-ID columns agree on every row. The Warwick LiDAR
box contains 45 WCC asset points, including 40 building-bearing assets.
Of those 40, 39 carry a candidate UPRN.[^wcc-public][^local-intake]

The current local Domesday source-reference bundle already has an OS/ONS
metadata discovery route. Its local documentation distinguishes source
references, admitted area-profile data and generated reports. Use the
Domesday source admission process for any new evidence. The hackathon
workspace has the public baseline only.

# Thursday review

Start with the [Avon Valley School worked example](warwickshire-worked-example.md).
It links WCC asset 3051 and its published UPRN to a county grant notice and
11 numbered conditions. The [spatial check](avon-valley-school/site.md#boundary-and-point-check)
places the OS UPRN point about 59 m outside the red line derived from
approved drawing P08. Check that result against the WCC planning-system
polygon, if held, and confirm the source revision and sharing rights.
Review the separate Biodiversity Gain Plan approval and the decision date
fields before attempting a draft public-view export.

| Owner or route | Check and record |
| --- | --- |
| Property and estates | Identify the authoritative estate, land, leases and building registers and their extract dates. Ask which local ID is stable for sites, buildings and interests. Clarify the two `unique_asset_id` columns, the six observed tenure labels, GIA basis, missingness markers, schools/academies and the scope of the public extract. |
| Energy and climate | Check for the actual EPC/DEC register, report reference, scope/date, survey evidence, meter data, annual consumption by fuel and council-approved carbon factors. Confirm which fields can be used locally and which can be included in a showcase. |
| GIS and addressing | Establish WCC's approved route to address gazetteer, UPRN history, OS NGD Building and Building Part, height confidence, heritage and flood data. Confirm PSGA entitlement and derived-output sharing rights. Inspect multi-building campuses and repeat UPRNs. Check the BNG position against the December 2025 Warwickshire boundary. |
| Domesday owner | Find the owning source, current refresh, rights and field-level restrictions. Keep source discovery distinct from verified evidence. Decide whether a limited WCC extract can be admitted for the pilot and how the receipts would be recorded. |
| Planning, building control and information governance | Agree which constraints may be displayed as screening evidence, who can review applicability and what to suppress from a hackathon demonstration. Use the [regulation register](estate-regulation-register.md) as the starting review. |
| Planning registers | For one asset, identify the determining authority and a permitted register record. Check what the register exposes for the application reference, site boundary, UPRN, issued decision and conditions. Record historic coverage and redaction. Note the proposed England data standard when discussing future export formats.[^planning-standard] |

Use the [pilot-derived field check](planning-standard-linked-documents.md#what-to-bring-to-the-warwickshire-review)
to record structured fields, mapping gaps, system or collection changes and
open questions for the selected planning record. The
[pilot reuse assessment](planning-pilot-reuse.md#warwickshire-pilot-decision)
identifies the verified county register route and the separate district
register and estates works-approval checks.

Demo selection after the review should include a checked Warwickshire asset
with a plausible certificate and geometry, a multi-building or shared-UPRN
case, and an asset with missing certificate evidence. Use only admitted
sources and permitted fields. The public WCC asset workbook and the matched
Warwick LiDAR pair provide an offline rehearsal route.

[^wcc-public]: [WCC published asset workbook listing](https://www.warwickshire.gov.uk/directory-record/8957/property-and-asset-list-february-2026).
[^local-intake]: [Local intake and coverage](ndl-estate-intake.md).
[^planning-standard]: [Planning application data standard assessment](planning-application-data-standard.md).
