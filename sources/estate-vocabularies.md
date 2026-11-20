---
type: Vocabulary register
title: Controlled vocabularies and ontologies for estate retrofit
description: Source-specific code lists, semantic standards and proposed adoption decisions for the Warwickshire pilot.
sources:
  - id: pds
    resource: https://www.gov.uk/government/publications/government-property-data-standard/government-property-data-standard-govs004-pds010-html
  - id: land-assets
    resource: https://schemas.opendata.esd.org.uk/LandAssets
  - id: epb
    resource: https://get-energy-performance-data.communities.gov.uk/guidance
  - id: os
    resource: https://docs.os.uk/osngd/code-lists/code-lists-overview
observed_on: "2026-11-17"
status: Candidate
---

# Use in the first profile

Preserve issuer, code or original literal, label, vocabulary version, validity
and mapping confidence. Represent a local scheme in SKOS only where it has a
defined scope and owner. Use proposed, exact, close, broad or unmapped as
appropriate. Validate any published exact mapping against the source definitions
and sample records. Keep certificate rating and suitability scales in separate
schemes even when labels overlap.

| Vocabulary or authority | What to carry into OKF+ |
| --- | --- |
| Cabinet Office GovS004-PDS010 | Field reference, definition and version. Sections 9.1–9.5 cover physical, contractual and financial, vacant-space, other and facilities-management fields. Appendix usage and disposal method supply source classifications. Use the definitions for construction date, tenure, condition/date and area basis. Preserve values from the InSite export when their mapping to the standard is unverified.[^pds] |
| LG Inform Plus Land and building assets schema | Local asset ID, UPRN, tenure/holding type, coordinate reference and publication rights, GIA, local service function, suitability, DEC rating, title number and INSPIRE link. The WCC workbook follows many of these field names. Capture its code column as missing when it says `To Follow`. Resolve the service-list concept using the schema's links and a WCC owner.[^land-assets] |
| OS and ONS | UPRN/USRN for addressable object/street, TOID and OSID in their own namespaces, OS association method and height-confidence codes; ONS GSS identifiers, boundary family and vintage. Preserve OS Building and Building Part feature-type version. Distinguish an exact point-in-boundary result from a statistical best-fit lookup.[^os] [Identifying property and street information](https://www.gov.uk/government/publications/open-standards-for-government/identifying-property-and-street-information) · [ONS Open Geography](https://geoportal.statistics.gov.uk/) |
| Register certificate schemes | Data dictionary and API field names, assessment type, certificate ID/RRN, UPRN, property type, rating bands and score, recommendation, lodgement and expiry. The captured non-domestic dictionary has `ASSET_RATING_BAND` on an A+ to G scale. The DEC dictionary has `OPERATIONAL_RATING_BAND` on an A to G scale and a separate building-category code. Both dictionaries define `UPRN_SOURCE` as Energy Assessor or Address Matched. Preserve that provenance and method version.[^epb] [Government DEC methodology](https://www.gov.uk/government/publications/government-methodology-for-producting-operational-ratings-display-energy-certificates-and-advisory-reports/the-government-methodology-for-operational-ratings-display-energy-certificates-and-recommendation-reports) |
| Property and energy measurement | Preserve the named floor-area basis from source. Reference IPMS or RICS NRM when source documentation establishes use. Use explicit units for plan area, GIA, DEC total useful floor area, volume, fuels and consumption. Keep reported or estimated status, period and denominator. [RICS IPMS](https://www.rics.org/profession-standards/rics-standards-and-guidance/sector-standards/real-estate-standards/international-property-measurement-standards) · [RICS NRM](https://www.rics.org/profession-standards/rics-standards-and-guidance/sector-standards/construction-standards/nrm) |
| Historic England and Environment Agency | Keep NHLE list-entry identifier, designation type and grade. FISH thesauri support monument and building-type discovery. Keep EA product, scenario and annual exceedance probability for the flood screen. Policy terms such as designation, exposure and susceptibility have different meanings. [Heritage Data Standards and Terminology](https://historicengland.org.uk/advice/technical-advice/information-management/data-standards-terminology/) · [EA surface-water extent dataset](https://www.data.gov.uk/dataset/dfd734fb-cc68-4229-b60d-8c0280398052/flood-map-for-planning-surface-water-spatial-planning-extents-present-day) |

Observed WCC `tenure_type` values are Freehold, External, Leasehold,
Both Freehold & Leasehold, Ground Lease and Licence. The two
`holding_type` values are Land with a permanent building and Land only.
These are observed values from one workbook. Ask WCC for authoritative
picklists, the meaning of External and the intended handling of compound
tenure. Confirm whether its internal premises-use or service classifications
are sourced from local codes, the government service function list, or a
sector scheme before deriving crosswalks.

# Semantic and interoperability decisions

| Standard | Decision |
| --- | --- |
| [SKOS](https://www.w3.org/TR/skos-reference/) and [PROV-O](https://www.w3.org/TR/prov-o/) | Adopt for named schemes, mappings, source artefacts and derivation activities where the repo builds a semantic projection. Keep original labels and review status. |
| [DCAT 3](https://www.w3.org/TR/vocab-dcat-3/) and [Dublin Core Terms](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/) | Use for dataset, distribution, licence, rights, temporal scope and versions. A catalogue record can describe a dataset available under separate access conditions. |
| [GeoSPARQL](https://www.ogc.org/standards/geosparql/) and [QUDT](https://www.qudt.org/) | Reuse geometry/CRS and quantity/unit conventions. Carry the native geometry identifier and measurement method. GeoJSON or GeoPackage can hold the actual geometry. |
| [SHACL](https://www.w3.org/TR/shacl/) | Add after a graph projection exists. Check typed endpoints, valid quantity/unit pair, dates, scheme membership and mandatory provenance. Validate file formats and source identifiers at ingestion. |
| [BOT](https://w3c-lbd-cg.github.io/bot/) | Candidate lightweight topology for site, building, storey and space. A W3C community group publication. Adopt after confirming the building-part and site relations with WCC. |
| [buildingSMART IFC](https://technical.buildingsmart.org/standards/ifc/), [bSDD](https://technical.buildingsmart.org/services/bsdd/using-the-bsdd-api/), [IDS](https://technical.buildingsmart.org/projects/information-delivery-specification-ids/), COBie, ISO 19650 and [NBS Uniclass](https://uniclass.thenbs.com/download) | Conditional import and validation route if estates has BIM or structured asset handover. Keep native IFC GUID, schema version, classifications, property definitions and unit convention. Uniclass Entities, Spaces/locations, Elements/functions, Systems and Products answer different questions. Review table edition and terms before copying vocabulary files. |
| [Brick](https://docs.brickschema.org/) and [SOSA/SSN](https://www.w3.org/TR/vocab-ssn/) | Candidate for equipment, meters, points, observations and topology when building management or metered evidence is available. Retain interval, fuel and aggregation boundary. |
| [CityGML 3.0](https://www.ogc.org/standards/citygml/) | Consider for exchange of validated 3D geometry or semantic surfaces. Simple height-volume estimates can be represented with provenance and GeoSPARQL without introducing a CityGML producer. |

## Sector-specific extensions to assess with owners

- The [England planning application data standard consultation](planning-application-data-standard.md)
  supplies draft application type, decision, decision-maker, development scale,
  process event and public-register codes. Use the pinned draft for candidate
  crosswalks and keep the original publisher term and version.
- Look up the [English National Calculation Methodology](https://www.gov.uk/government/publications/methodologies-for-expressing-the-energy-performance-of-buildings-in-england-and-wales-notice-of-approval-24-march-2026), the applicable approved model/activity database and DEC methodology for comparability. Retain source benchmark, year and permitted adjustments. Use [ND-NEED](https://www.gov.uk/government/statistics/non-domestic-national-energy-efficiency-data-framework-nd-need-2026) for cohort comparison with its scope and denominator. Use published [government conversion factors](https://www.gov.uk/government/publications/greenhouse-gas-reporting-conversion-factors-2026) only with a dated activity observation and fuel/method choice.
- Check WCC's classifications for schools, highways depots, libraries, offices
  and leased premises. If a sector register contributes an identifier such as
  a DfE URN, preserve its issuing authority and relation to sites before
  joining. Likewise establish title, lease, meter and cost-centre mappings
  with their owners.
- Treat BREEAM, DEC, EPC, statutory designation grade and local suitability as
  separate schemes. Use PAS 2038 for discussion with retrofit specialists and
  check the appropriate edition and rights. Historic England's guidance
  identifies separate standards for traditional buildings.
  [Historic England standards and guidance](https://historicengland.org.uk/advice/climate-change/your-organisation-to-net-zero/developing-a-decarbonisation-plan/templates-and-guides/factsheet-standards-guidance/)

[^pds]: [Government Property Data Standard](https://www.gov.uk/government/publications/government-property-data-standard/government-property-data-standard-govs004-pds010-html).
[^land-assets]: [LG Inform Plus land and building assets schema](https://schemas.opendata.esd.org.uk/LandAssets).
[^epb]: [MHCLG guidance, data dictionary and APIs](https://get-energy-performance-data.communities.gov.uk/guidance).
[^os]: [OS NGD code lists](https://docs.os.uk/osngd/code-lists/code-lists-overview).
