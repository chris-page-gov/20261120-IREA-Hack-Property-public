---
type: Standards assessment
title: England planning application data standard consultation
description: MHCLG's proposed submission and decision specifications and their relevance to the Warwickshire estate retrofit pilot.
resource: https://www.gov.uk/government/consultations/data-standard-for-planning-applications
sources:
  - id: announcement
    resource: https://mhclgdigital.blog.gov.uk/2026/11/18/data-driven-development-management-consulting-on-englands-first-mandatory-application-data-standard/
  - id: consultation
    resource: https://www.gov.uk/government/consultations/data-standard-for-planning-applications/data-standard-for-planning-applications
  - id: consultation-dates
    resource: https://www.gov.uk/government/consultations/data-standard-for-planning-applications
  - id: draft
    resource: https://github.com/digital-land/planning-application-data-specification/tree/3b1dacd63c489abf6b0ee8cc394214711e2b77fd
  - id: lura
    resource: https://www.legislation.gov.uk/ukpga/2023/55/part/3/chapter/1
  - id: wcc
    resource: https://www.warwickshire.gov.uk/planning/applying-planning-permission
observed_on: "2026-11-18"
jurisdiction: England
status: Consultation and technical working draft
consultation_closes_at: "2026-12-30T23:59:00+00:00"
---

# What MHCLG is proposing

MHCLG opened the England-only consultation on 18 November 2026. It closes at
23:59 GMT on 30 December 2026. The proposed standard covers data at submission
and at determination. Conformance in a defined machine-readable National Public
View would be the proposed compliance point for planning authorities. That
view is a subset of the planning register, with redaction still applicable.
The consultation asks whether to include historic applications.[^announcement][^consultation][^consultation-dates]

Sections 84 to 86 of the Levelling-up and Regeneration Act 2023 provide powers
relating to processing, provision and publication of planning data. The
consultation proposes secondary legislation to mandate this specific standard.
Track the final approved specification, the implementing regulations and
commencement before recording an applicable duty. Keep the current planning
register and consent regime as separate legal evidence.[^lura][^consultation]

# What the technical draft establishes

The [snapshot manifest](planning-standard-snapshots.json) records the blog,
GOV.UK consultation content and dates, and a curated technical archive from
commit `3b1dacd63c489abf6b0ee8cc394214711e2b77fd` observed on
18 November 2026. The capture preserves 878 upstream definition files,
including 51 vocabulary CSVs, generated submission schemas and the
`working-draft` National Public View. Upstream examples and analysis
submissions were excluded from the local archive. The draft commit identifies
a technical observation. The mandated version is yet to be specified.[^draft]

The [linked documents and pilot evidence](planning-standard-linked-documents.md)
record the supporting discussion, technical repository documentation and the
field-mapping lessons for Warwickshire.

| Draft component | Relevance to the retrofit evidence map |
| --- | --- |
| Application and site | Use the publishing authority and native application reference together as the application key. The public view marks site boundary `geometry` as `MUST`, with `uprns` and `usrns` as `SHOULD` where known. These identify addressable premises and associated streets. Preserve the source site reference and geometry's CRS. |
| Decision notice and timeline | Keep application type, decision code, issuing organisation, decision date and notice link. Capture process events such as validation and publication separately. The draft outcome list uses `grant` and `refuse`, with descriptions that also cover recommendations. Use an issued notice as decision evidence and keep proposals and recommendations in their own records. |
| Conditions, obligations and documents | The draft joins decision notices to conditions through `decision-condition`. Preserve the link and original wording when permitted. Keep section 106 obligations distinct. The public view supplies a planning application document dataset and source links. Use published, permitted fields for the pilot. |
| Listed building consent | The proposed submission scope includes listed building consent. The draft application type is `lbc`, with modules for grade, materials, alterations and the site. Use the code for the application type. Refer to the Historic England designation and the issued local decision for their respective facts. |


# OKF+ adoption decision

Adopt this as a **candidate planning evidence layer** for Warwickshire. Keep
the estate, certificate and planning records at their native grain. Link
`EstateAsset → candidate PlanningSite → PlanningApplication → DecisionNotice`
and preserve the source authority, reference, evidence date, linking method
and review outcome. Record draft term IDs for application type, decision,
decision-maker, development scale and permission-process event. Keep mappings
versioned. The draft's site schema itself uses a close mapping to IFC
`IfcSite`. A planning boundary can cover multiple plots or buildings, and
its presence, UPRNs or overlap alone cannot establish ownership, a building
identity or consent for new works.[^draft]

For the demo, select one Warwickshire asset with a published register entry.
First cross-check the UPRN against the site boundary. Where the UPRN is
unavailable, use the footprint or asset point as a candidate spatial link
and check it against the register. Show the application type, an issued
decision and any relevant condition with source links. Keep an unmatched or
ambiguous result visible. Ask the planning owner to confirm which evidence
is fit to share. The demo remains useful with the existing LiDAR and estate
records while planning-register access is assessed.

Thursday's review should establish which registers and public views are
available. WCC directs housing, industrial and commercial enquiries to
district and borough councils, and handles minerals and waste with a separate
route for county council applications. For the selected asset, confirm the
determining authority, whether it can supply site geometry, UPRNs, decision
and condition identifiers, and what historic coverage and redaction apply.
The [Domesday checklist](warwickshire-domesday-review.md) records the
handoff.[^wcc][^consultation]

[^announcement]: [MHCLG Digital announcement, 18 November 2026](https://mhclgdigital.blog.gov.uk/2026/11/18/data-driven-development-management-consulting-on-englands-first-mandatory-application-data-standard/).
[^consultation]: [MHCLG consultation document](https://www.gov.uk/government/consultations/data-standard-for-planning-applications/data-standard-for-planning-applications).
[^consultation-dates]: [GOV.UK consultation dates](https://www.gov.uk/government/consultations/data-standard-for-planning-applications).
[^draft]: [Pinned MHCLG technical draft](https://github.com/digital-land/planning-application-data-specification/tree/3b1dacd63c489abf6b0ee8cc394214711e2b77fd) and [National Public View source](https://github.com/digital-land/planning-application-data-specification/blob/3b1dacd63c489abf6b0ee8cc394214711e2b77fd/specification/national-public-view.schema.md).
[^lura]: [Levelling-up and Regeneration Act 2023, Part 3 Chapter 1](https://www.legislation.gov.uk/ukpga/2023/55/part/3/chapter/1).
[^wcc]: [Warwickshire County Council planning application routes](https://www.warwickshire.gov.uk/planning/applying-planning-permission).
