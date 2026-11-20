---
type: Source register
title: Linked planning standard documents and pilot evidence
description: Document chain from the MHCLG consultation through the discussion, technical repository and implementation reports.
resource: https://github.com/digital-land/data-standards-backlog/discussions/94
sources:
  - id: discussion
    resource: https://github.com/digital-land/data-standards-backlog/discussions/94
  - id: repository
    resource: https://github.com/digital-land/planning-application-data-specification/tree/3b1dacd63c489abf6b0ee8cc394214711e2b77fd
  - id: pilots
    resource: https://mhclgdigital.blog.gov.uk/2025/11/18/testing-new-planning-data-specifications-with-industry-5-pilot-partnerships-paving-the-way/
  - id: phase-1
    resource: https://mhclgdigital.blog.gov.uk/2026/01/30/testing-new-planning-data-standards-with-industry-what-we-learned-from-phase-1-and-where-we-go-next/
  - id: implementation
    resource: https://github.com/digital-land/planning-application-data-specification/blob/3b1dacd63c489abf6b0ee8cc394214711e2b77fd/documentation/materials/What%20we%20are%20learning%20about%20implementing%20the%20Open%20Data%20Standards.pdf
  - id: refinement
    resource: https://github.com/digital-land/planning-application-data-specification/blob/3b1dacd63c489abf6b0ee8cc394214711e2b77fd/documentation/materials/Refining%20the%20planning%20application%20data%20specification.pdf
observed_on: "2026-11-18"
---

# Capture

The [linked-document register](planning-linked-documents.json) records
81 additional local artefacts, checksums, outgoing source links, archive
members and retrieval results. It extends the [original consultation
assessment](planning-application-data-standard.md) and its four snapshots.

- **Discussion chain.** Archived the opening post of GitHub discussion #94,
  and the opening posts it links to on submissions (#98), decisions (#25)
  and conditions (#40). The captures retain the source links and opening
  text. Replies and account data were excluded to keep personal contact
  details out of the workspace. The decisions discussion links to the
  Planning Inspectorate's register guide, which was also captured.[^discussion]
- **Technical repository.** The original archive contains 878 definition
  files. A second archive from the same commit contains 518 linked files,
  including the repository readme, changelog, application scope, data model,
  National Public View guidance, design decisions, user-needs records,
  generated Markdown and spreadsheets, and the two September reports.
  The register traces links from those reports to the relevant code-list
  and guidance files. It also records metadata for four issues cited in
  the refinement report.[^repository][^implementation][^refinement]
- **Consultation and delivery.** Saved the Citizen Space landing page,
  Planning Data platform and API documentation, the existing decision
  catalogue entry, and the official planning forms publication with all
  29 attachments, including listed building consent and fire statement
  templates. Captured the linked parliamentary publications through the
  Parliament API and the primary planning data provisions as legislation XML.
- **Capture boundary.** The register covers the substantive direct links
  and selected references through the community, repository and pilot
  reports. Further community documents, live trackers and worked cases
  with identifiable-looking details remain source links. The ICO guidance
  and Local Digital programme page returned HTTP 403 on download.
  The ICO homepage is indexed as a general reference. The interactive
  consultation is represented by its landing page and published paper.

# The five pilots

The November 2025 launch named the following pairings. Planning Portal also
participated. These are the original partnerships, as announced.[^pilots]

| Planning authority | Back-office supplier |
| --- | --- |
| Dorset Council | DEF |
| Leeds City Council | Idox |
| London Borough of Hounslow | NEC |
| London Borough of Redbridge | IEG4 |
| Salford City Council | Arcus Global |

**January 2026.** All five partnerships had compared draft submission
fields with current systems and workflows. Planning Portal contributed
mapping and validation findings. Datetime conventions, address structure
and differences between national and local requirements needed work.
Historic data and the practical meaning of compliance remained open.
This phase established a field-level analysis for implementation.[^phase-1]

**September 2026.** The published funding update describes four authority
and supplier mappings of the National Public View and more than 100
questions or observations. It distinguishes clarifications to the draft,
mapping or configuration, changes to product or data collection, and
remaining implementation barriers. The report leaves the identities of
the four pairings unspecified. The companion refinement report describes
changes to requirement levels, identifiers and linked applications,
timeline events, decisions, conditions and document publication.
Deployment and WCC compatibility remain unverified.[^implementation][^refinement]

The [pilot output audit](planning-pilot-reuse.md) checks each partnership for
public datasets and mappings and tests the draft public-view rules on a
publisher example.

## What to bring to the Warwickshire review

Use the pilot method on one proposed Domesday asset and one public planning
record. Ask the determining authority or system owner to trace each of these
fields from source to proposed public view:

1. Application reference and responsible authority. Keep received,
   validation, publication and decision dates in their own fields.
2. Site reference, boundary and UPRNs where known. Check a case with several
   UPRNs or no UPRN, and record the method and result of the estate link.
3. Issued decision reference and outcome, linked condition and reason, and
   any permitted source document reference. Exercise the case of a document
   with publication status withheld or awaiting assessment.

For each field, record whether it is available as structured data, needs a
mapping, requires a system or capture change, or needs clarification. Save
the source evidence and version with the finding. This gives the team a
small fit-gap test to run on Thursday and a case it can explain at the
hackathon. The [Domesday checklist](warwickshire-domesday-review.md) now
points to this test.

[^discussion]: [Planning application data specifications discussion #94](https://github.com/digital-land/data-standards-backlog/discussions/94).
[^repository]: [Pinned planning application data specification repository](https://github.com/digital-land/planning-application-data-specification/tree/3b1dacd63c489abf6b0ee8cc394214711e2b77fd).
[^pilots]: [MHCLG announcement of the five pilot partnerships](https://mhclgdigital.blog.gov.uk/2025/11/18/testing-new-planning-data-specifications-with-industry-5-pilot-partnerships-paving-the-way/).
[^phase-1]: [MHCLG phase 1 findings](https://mhclgdigital.blog.gov.uk/2026/01/30/testing-new-planning-data-standards-with-industry-what-we-learned-from-phase-1-and-where-we-go-next/).
[^implementation]: [September Development Management Software Funding update](https://github.com/digital-land/planning-application-data-specification/blob/3b1dacd63c489abf6b0ee8cc394214711e2b77fd/documentation/materials/What%20we%20are%20learning%20about%20implementing%20the%20Open%20Data%20Standards.pdf).
[^refinement]: [September specification refinement report](https://github.com/digital-land/planning-application-data-specification/blob/3b1dacd63c489abf6b0ee8cc394214711e2b77fd/documentation/materials/Refining%20the%20planning%20application%20data%20specification.pdf).
