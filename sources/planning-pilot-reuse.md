---
type: Evidence assessment
title: Public outputs of the five planning data pilots
description: Verified public material, live data checks and what Warwickshire can reuse.
sources:
  - id: programme
    resource: ./planning-standard-linked-documents.md
  - id: leeds
    resource: https://datamillnorth.org/dataset/planning-applications-exkkr
  - id: dorset
    resource: https://gi.dorsetcouncil.gov.uk/dorsetexplorer
  - id: hounslow
    resource: https://www.hounslow.gov.uk/find-data-information/open-data/5
  - id: redbridge
    resource: https://data.redbridge.gov.uk/Download/planning-and-land/planning-applications
  - id: salford
    resource: https://ckan.publishing.service.gov.uk/dataset/scc-planning-applications
  - id: gla
    resource: https://www.london.gov.uk/programmes-strategies/planning/digital-planning/planning-london-datahub?ac-60574=60566
  - id: technical
    resource: https://github.com/digital-land/planning-application-data-specification/tree/3b1dacd63c489abf6b0ee8cc394214711e2b77fd
  - id: wcc
    resource: https://www.warwickshire.gov.uk/planning/commenting-planning-application/4
observed_on: "2026-11-18"
---

# What the pilots delivered

All five authority–supplier pairs completed the first phase of comparing
draft fields with their systems and workflows. Planning Portal added
mapping and validation input. The September 2026 report describes four
unnamed authority–supplier mappings against the National Public View that
raised more than 100 questions and observations. Its companion refinement
report records resulting changes in the working specification and guidance.
The public reports give programme-level findings. The partner workbooks,
per-pair mappings, test exports and completion reports were not found in the
checked sources. The five January partners and September's four anonymous
pairs therefore cannot be reconciled individually from the published evidence.[^programme]

## What is publicly available by partner

| Partnership | Found and checked | Warwickshire reuse |
| --- | --- | --- |
| Dorset Council and DEF | Dorset's service and DorsetExplorer expose planning and local spatial context. The original phase 1 account confirms mapping work. Dorset's published local validation-checklist route returned HTTP 403 to the automated download. The earlier DEF and Planning Portal validation project is described separately by the [Planning Software Improvement Fund](https://www.localdigital.gov.uk/digital-planning/digital-planning-software/funding/).[^programme][^dorset] | Reference the authority's validation approach. No verified pilot CSV, schema mapping or bulk application geometry from this route. |
| Leeds City Council and Idox | The publisher's legacy [CSV](https://opendata.leeds.gov.uk/downloads/planning/applications/apps.csv) returned a 32.2 MB extract dated 1 November 2026, although the catalogue page shows a 2021 update. The payload has **38,853 rows and unique nonblank case references**, 36,549 populated decision dates and 36,504 populated decisions. Its columns include dates, labels and a register URL. There are no UPRN, site geometry, condition or condition-reason columns.[^leeds] | Use it to test indexing native references, preserving raw decisions and parsing UK two-digit-year dates. Confirm the field definitions and meaning of `caseDate` before treating it as receipt date. It supplies no geometry join for a Warwickshire asset. |
| London Borough of Hounslow and NEC | The council's register route supports application searches and weekly and monthly lists. The older [LG Inform Plus catalogue](https://datasets.opendata.esd.org.uk/details?datasetId=127614) advertises a 2019 CSV. A probe served HTML, and the definition and JSON endpoints returned 404. The GLA describes a separate London-wide Datahub covering Hounslow.[^hounslow][^gla] | Use the register to inspect the publishing pattern. Treat the London-wide platform as a separate interoperability comparator; its payload and borough coverage were not sampled. |
| London Borough of Redbridge and IEG4 | The DataShare application schema endpoint returned XML with a disabled message. Its dataset endpoint returned an empty list. Redbridge also has a district register route and the GLA's London-wide Datahub. A [public specification issue](https://github.com/digital-land/planning-application-data-specification/issues/235) identifies additional London questions as a mapping concern.[^redbridge][^gla] | Keep London-specific fields as a source extension. The DataShare route supplied no downloadable rows. The issue supplies a question for assessment, with no confirmed crosswalk. |
| Salford City Council and Arcus Global | The legacy CKAN entry describes a CSV in the earlier LG Inform schema and separate terms for UPRNs. The listed CSV returned HTTP 502. Salford publishes a [decision-notice search](https://www.salford.gov.uk/planning-building-and-regeneration/planning-applications/planning-decisions/). The Arcus-linked analysis records in the technical sample cite Manchester, a different authority.[^salford][^technical] | Use the legacy schema and licensing notes as context. Confirm the current provider's export and the rights for a UPRN-bearing extract before attempting a join. |

The government Planning Data API returned zero entities for the
[`planning-application` check](https://www.planning.data.gov.uk/entity.json?dataset=planning-application&limit=1)
and the [`planning-decision` check](https://www.planning.data.gov.uk/entity.json?dataset=planning-decision&limit=1)
on 18 November 2026. These two checks establish the result for these
endpoints at that time. The Planning London Datahub describes its own API
and regional schema. It should carry separate lineage from the England
working draft and from the DMSF pilot programme.[^gla]

# What can be reused now

1. **An end-to-end worked example.** I applied the pinned draft public-view
   field and record-inclusion rules to MHCLG's householder example. The
   result retained one site, one application, one decision, two conditions
   and two condition links. Three of four document records passed the
   explicit publication filter. The withheld document, officer name and
   submission-payload dataset were left out of the projection. All six
   timeline rows were in the selected usage profile. This checks the
   projection rules using the publisher's example. Production conformance
   needs separate validation.[^technical]
2. **The application types and code lists.** The pinned combined full and
   listed building consent example carries `full` and `lbc` together.
   Use the draft application types, decision codes and process events as
   candidate mappings, keeping source values and an unresolved state for
   local labels. The reported address refinement is traceable through
   [issue #307](https://github.com/digital-land/planning-application-data-specification/issues/307)
   and the [address design decision](https://github.com/digital-land/planning-application-data-specification/blob/3b1dacd63c489abf6b0ee8cc394214711e2b77fd/documentation/design-decisions/0019-addresses-use-text-identifiers-and-site-boundaries.md).[^technical]
3. **Schema analysis cases.** The public repository contains 21 worked
   analysis application rows, 20 notices, 294 condition rows and 21 site
   rows. Authority codes and register hosts identify other councils.
   For example, `LBH` is Lambeth, and Hounslow uses `HNS` in the pinned
   code list. The site table lacks an `uprns` column. These cases can inform
   edge-case design. The audit retains counts and source references.[^technical]

# Warwickshire pilot decision

Use the tested public-view pattern with **one verified local case**. WCC's
county and minerals/waste register links both resolve to the same public
search and weekly-list service. For Warwick District decisions, start
with the [district register](https://www.warwickdc.gov.uk/info/20374/planning_applications/249/view_or_comment_on_a_planning_application).
Confirm the determining authority first. Record the native application and
site references, source geometry, decision date, conditions and the public
notice link. Use a UPRN link only if the source supports it; otherwise label
the spatial association and its uncertainty. WCC's
[works approval process](https://www.warwickshire.gov.uk/data-council-services/works-approval-process-properties)
is a separate estates check for council property.[^wcc]

Use the [machine-readable evidence and candidate crosswalk](planning-pilot-reuse-evidence.json)
at the [Domesday review](warwickshire-domesday-review.md). It retains the
Leeds payload hash, row profile and source checks without retaining raw case
rows. The [Avon Valley School worked example](warwickshire-worked-example.md)
now demonstrates the documentary link on a local case. It records the
available decision and conditions and the limitations to a vector geometry
join or draft public-view export.

[^programme]: [Programme reports and the five named partnerships](planning-standard-linked-documents.md).
[^leeds]: [Leeds City Council dataset catalogue and OGL terms](https://datamillnorth.org/dataset/planning-applications-exkkr).
[^dorset]: [DorsetExplorer council platform](https://gi.dorsetcouncil.gov.uk/dorsetexplorer).
[^hounslow]: [Hounslow planning applications open data page](https://www.hounslow.gov.uk/find-data-information/open-data/5).
[^redbridge]: [Redbridge DataShare planning applications](https://data.redbridge.gov.uk/Download/planning-and-land/planning-applications).
[^salford]: [Salford legacy planning applications catalogue](https://ckan.publishing.service.gov.uk/dataset/scc-planning-applications).
[^gla]: [Greater London Authority Planning London Datahub](https://www.london.gov.uk/programmes-strategies/planning/digital-planning/planning-london-datahub?ac-60574=60566).
[^technical]: [Pinned MHCLG working specification and examples](https://github.com/digital-land/planning-application-data-specification/tree/3b1dacd63c489abf6b0ee8cc394214711e2b77fd).
[^wcc]: [WCC public register routes](https://www.warwickshire.gov.uk/planning/commenting-planning-application/4).
