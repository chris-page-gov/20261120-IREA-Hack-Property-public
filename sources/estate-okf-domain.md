---
type: Domain assessment
title: Estate retrofit evidence as OKF+
description: Proposed domain model, source authority and validation for a Warwickshire estate retrofit evidence pilot.
sources:
  - id: pds
    resource: https://www.gov.uk/government/publications/government-property-data-standard/government-property-data-standard-govs004-pds010-html
  - id: local-assets
    resource: https://schemas.opendata.esd.org.uk/LandAssets
  - id: estate
    resource: ./government-property-estate.md
  - id: intake
    resource: ./ndl-estate-intake.md
observed_on: "2026-11-17"
status: Candidate
---

# Decision

Use OKF+ to record **what is known about an asset, how it was linked, and what
question the evidence can support**. Start with an indicator of readiness for
retrofit review. Keep the join and volume calculation deterministic. Keep
the bulk files in local snapshots, with a small evidence record per asset,
certificate, geometry, measurement, and decision. Maintain four independent
authorities: estate owner, certificate register, authoritative geography or
geometry producer, and legislation publisher.[^pds][^local-assets][^estate][^intake]

The central government and council registers have different responsibilities and
grains. In the February 2026 WCC transparency workbook, 648 rows are council
asset records. A syntactically usable UPRN is present on 588 rows, representing
582 distinct UPRNs. Four of those UPRNs also appear in the central estate
Property Contract workbook. This is an exact identifier overlap and requires a
manual identity check. All 648 WCC DEC values are `To Follow`. The two identically named
`unique_asset_id` columns agree on every row. Confirm the canonical field
with the source owner before import. The [Thursday checklist](warwickshire-domesday-review.md) lists the
source questions these findings raise.

# Concepts and relationships

| Concept | Identity or grain | Evidence to retain |
| --- | --- | --- |
| Organisation and portfolio | Native publisher ID and reporting period | Owner, holder, occupier and reporting body have distinct roles. Use an organisation register alias only with evidence. |
| Land parcel, property, site | Source-scoped asset ID or InSite property reference | Land-only, land with buildings, and building-only are distinct. Title number identifies a title. A site can encompass several titles and buildings. |
| Building, building part, space | InSite building reference or WCC asset ID plus source edition. OSID/TOID identifies a geometry feature in its namespace | Separate footprint, roof form, volume estimate, floor count and GIA. An addressable unit can occupy part of a building. |
| Addressable object | UPRN as a string, with separate source version | Link the property to the UPRN with provenance. Record matched, unmatched, ambiguous and out-of-scope cases. |
| Interest, contract, occupation | Native agreement ID plus effective interval | Type, organisational roles and spatial extent. One building may have multiple records. Preserve floor-area measurement method. |
| Certificate and recommendation report | Register jurisdiction, scheme and native certificate/RRN. Keep prior lodgements | Record assessment and lodgement dates, expiry or supersession, assessor methodology, area basis, assessment scope and rating scale. Separate EPC asset rating from DEC operational rating. |
| Energy activity and carbon result | Meter/supply or building with period, fuel and measure | Consumption in kWh by fuel. Retain boundaries, conversion-factor year and kgCO₂e basis. Carbon estimate is a derived observation. |
| Building or area constraint | Native designation or area identifier and edition | List entry number, grade, authority, geometry and overlay method. A nearby designation or flood zone is a screening flag. |
| Planning site, application and decision | Source site reference and geometry, publishing authority plus application reference, and native notice reference | Retain separate condition and process-event records. Assess UPRN and spatial links to estate assets against the source register. [Planning standard assessment](planning-application-data-standard.md) |
| Evidence assertion | Subject, relationship, object, source edition and observation | Record the join path, CRS, authority, uncertainty, date, rights and review status. A source declaration and an inference have separate provenance. |
| Rule or screening question | Jurisdiction, provision or policy version and date | Applicability facts, evidence gaps, reason and reviewer. Preserve unknowns and route decisions to estates, energy or planning specialists. |

## Identity and measurement rules

- Use an explicit `hasAddressableObject` relation for an inherited UPRN, an
  `assesses` relation for a certificate, and an `associatedGeometry` relation
  for OS geometry. Reserve identity equivalence for proven equivalence.
  OS Linked Identifiers method 5 associates an address with a topographic area.
  Check the feature type and exact part-to-building relationship separately.
- Keep original values and missingness reasons. Distinguish blank, publisher
  placeholder, invalid identifier, no matching record, withheld and unavailable.
  Keep `0` as an observed source value until its field-specific semantics are
  checked. Aggregate at the chosen building or holding grain.
- Retain dimensions and units. GIA, NIA, DEC total useful floor area, polygon
  plan area, and volume have different meanings. For OS building parts,
  estimate above-ground envelope volume as the sum of disjoint plan areas times
  relative roof-base heights. For aligned LiDAR, integrate positive
  surface-minus-terrain height across the verified footprint and retain survey
  epoch, cell size, NoData, edge treatment, spillover and tree contamination.
  Validate the height source and matching method. Conditioned volume requires
  separate evidence.
- Retain the separate geography code, boundary edition, CRS, location kind and
  match rule. A point or footprint overlay supports spatial screening. Use
  versioned, issuer-defined geography codes for reporting.

## Minimal profile and acceptance

An OKF 0.2 evidence note can point to a source asset ID, a UPRN assertion, the
source certificate, one geometry and one measurement. Use
[the vocabulary and ontology register](estate-vocabularies.md) to type
these records and [the legislation register](estate-regulation-register.md) to
link review questions to authority. The provenance record binds input hashes,
query or transform, calculation units and review owner. A short dashboard
projection can display those same assertions.

For the event, use one small Warwickshire cohort and prove one checked join,
one ambiguous shared-site case, one date/scope gap and one reproducible volume
estimate. Keep WCC benchmark outputs and central government outputs labelled as
separate populations. Require unique source-scoped IDs, known units, no silent
row multiplication, distinct rating schemes, and resolvable evidence links.
Treat a later UK profile as four jurisdiction-specific rules and certificate
sources which share an evidence model.

[^pds]: [Government Property Data Standard](https://www.gov.uk/government/publications/government-property-data-standard/government-property-data-standard-govs004-pds010-html).
[^local-assets]: [LG Inform Plus land and building assets schema](https://schemas.opendata.esd.org.uk/LandAssets).
[^estate]: [Government Property Estate workbook note](government-property-estate.md).
[^intake]: [NDL estate data intake](ndl-estate-intake.md).
