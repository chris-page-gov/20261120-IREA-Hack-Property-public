
# UK public estate decarbonisation screening and evaluation

**Draft v0.2, 20 November 2026.** This revision adds nation-relative
deciles 1 to 5 and bands D to G as the first screening filters. The method supports screening for
opportunities with no active delivery investment, tracking funded work,
evaluating completed work and prioritising evidence checks. The only worked site is Mile End Hospital
within the Tower Hamlets pilot. The [Tower Hamlets screening method](https://chris-page-gov.github.io/20261120-IREA-Hack-Property-public/tower-hamlets/method.html)
governs local validation. The earlier hypothesis about missing energy
evidence still awaits verbatim confirmation.

## 1. Define the population and evidence boundaries

Include current public-facing non-domestic premises delivering services
such as healthcare, culture, community services or justice within the
approved study boundary. Include a mixed-use building only for its
identifiable in-scope part. Record public function, operator, tenure,
reporting date and scope. Retain excluded or undecided records with reasons
such as dwelling, closed service, back office, out of area, aggregate only
or unresolved premises.

Use a verified Unique Property Reference Number (UPRN), nation, estate
owner or operator identifier, local site reference and dated building or
demise scope for linkage. A UPRN identifies an addressable object. It can
be shared by site records, represent a campus or parent building, or differ
from the metering and certificate boundaries. Keep an unresolved match
in the evidence queue. Use an authorised address source and one-to-many
review before accepting any join. Record source identifier, date,
confidence, competing matches and reviewer. [Tower Hamlets identity and join rules](https://chris-page-gov.github.io/20261120-IREA-Hack-Property-public/tower-hamlets/method.html#2-inventory-inputs-and-preserve-identifiers)

| Record grain | Minimum scope |
| --- | --- |
| Facility or service | Public function, operator, site and dates active, agreed service or catchment evidence where available |
| Estate asset or assessed premises | Owner and site reference, UPRN and namespace, building or part, occupancy dates, surveyed area and convention, meter and certificate scope |
| Project and measure | Stable project and measure keys, activity and affected parts or systems, installation and operating dates, shared and overlapping works |
| Award or funding line | Programme, round, award reference, recipient, date and funding type. Link award shares to projects and measures where evidenced |
| Performance observation | Site, building, system or meter key, interval or annual period, fuel, scope, area, units, source, quality and observation date |

Store site-to-asset, site-to-measure and award-to-project links separately,
with effective dates and evidence. A project can span sites and measures.
One measure can have several funding sources or share a meter with another
measure. Aggregate once at the intended grain before joining. Freeze the
cohort, as-of date, source editions, data rights, thresholds and reporting
windows before comparison. The Government Property Estate Building
workbook covers its submitting central estate bodies and ERIC reflects
NHS England reporting. Use nation and owner registers for study coverage
and report omissions. [Estate workbook scope](https://www.data.gov.uk/dataset/a3ad62cf-d8a2-4d3b-b3c6-24c35c5e0f71/the-government-property-estate-including-buildings-and-land) ·
[ERIC coverage](https://digital.nhs.uk/data-and-information/publications/statistical/estates-returns-information-collection/summary-page-and-dataset-for-eric-2025-26)

### Deprivation and energy rating filters

- **Deprivation.** Select deciles **1 to 5 inclusive**, where 1 is the
  most deprived. This is the more deprived half of small areas within
  each nation by rank, subject to the publisher’s grouping convention.
  It is a share of small areas, with no fixed share of people or assets.
  Use the nation’s overall index as the provisional primary screen.
  Retain separate England IMD, IDACI and IDAOPI threshold flags and counts.
  For the other nations, add supplementary indicators only where their
  published scope, population and method suit the same question. Keep
  those results separate and document comparability before making any
  cross-nation comparison. A supplementary flag can prompt investigation
  of service-user needs. For the initial screen it does not change the
  overall-index result. Record the release, area code and vintage, match
  status, scale direction and denominator. If a release gives ranks
  without deciles, use an official published mapping where available.
  Otherwise document and agree the conversion, handling of ties and
  boundary rounding before applying it. Keep unmatched or ambiguous
  locations in the evidence queue.
- **Energy rating.** D or worse means letter bands **D, E, F or G**.
  Run separate screens for a current non-domestic asset EPC and a
  current operational DEC where applicable and comparable. Confirm
  the current register status, reference, issue and expiry dates,
  scope match, and the DEC measurement period where available.
  Record EPC and DEC eligibility, search coverage, distinct premises
  and D–G results by type and nation, alongside A–C and separate
  states for expired, conflicting, unmatched, absent, unavailable,
  out-of-scope and unverified evidence. Record the rating scale and
  method used. Treat a D–G band as a screening lead. Physical energy
  use, cost, carbon and feasible savings require their own evidence.
- **Combine only at the assessed scope.** A positive rating screen for
  a certificate type requires both the primary geography flag and a
  verified comparable D–G rating for the relevant premises. Keep
  supplementary results and separate EPC and DEC outcomes visible.
  Apply investment and evidence queues at site-and-measure scope
  independently of the rating. A screen can flag a funded project, an
  opportunity with confirmed no active investment, or a need to verify
  evidence. Backlog and spend remain separate decision inputs.

[English index definitions and published supplements](https://www.gov.uk/government/statistics/english-indices-of-deprivation-2025) ·
[Certificate lookup and scope procedure](https://chris-page-gov.github.io/20261120-IREA-Hack-Property-public/tower-hamlets/method.html#certificate-lookup-procedure)

## 2. Use nation-specific sources

All source routes below were checked on 20 November 2026. Check editions,
area codes, licences and authority to handle fields for each run. In Great
Britain, use the applicable OS Open UPRN source or authorised address
products for identity. In Northern Ireland, use Land & Property Services
Pointer subject to its access and reuse terms. Record the identifier
source and verify the relationship to the assessed premises. Access to a
lookup is separate from redistribution rights. [OS UPRN guidance](https://www.ordnancesurvey.co.uk/public/unique-property-reference-numbers) ·
[Northern Ireland Pointer](https://www.nidirect.gov.uk/articles/pointer)

| Nation | Neighbourhood evidence | Certificate route | Investment discovery leads | Health estate leads |
| --- | --- | --- | --- | --- |
| England | 2025 English indices on their published LSOA geography. Keep IMD, IDACI and IDAOPI distinct. [English indices 2025](https://www.gov.uk/government/statistics/english-indices-of-deprivation-2025) | MHCLG individual register and eligible England and Wales bulk route. [Public lookup](https://www.gov.uk/find-energy-certificate) · [Bulk service](https://get-energy-performance-data.communities.gov.uk/) | DESNZ and Salix PSDS project awards, local grants and owner capital plans. [PSDS Phase 4 awards](https://www.gov.uk/government/publications/public-sector-decarbonisation-scheme-phase-4) | Use published NHS England ERIC data at its reported trust and site grains. [ERIC 2025/26](https://digital.nhs.uk/data-and-information/publications/statistical/estates-returns-information-collection/summary-page-and-dataset-for-eric-2025-26) |
| Wales | Welsh Index of Multiple Deprivation 2025 on its published Welsh LSOAs. [WIMD 2025](https://www.gov.wales/welsh-index-multiple-deprivation-wimd-2025-guidance-html) | MHCLG England and Wales routes. Check applicable certificate type, dates and scope. [Bulk service](https://get-energy-performance-data.communities.gov.uk/) | Welsh Government Energy Service, case studies and owner or local capital records. [Impact report](https://www.gov.wales/energy-service-impact-report-2025-2026-html) · [Case studies](https://www.gov.wales/energy-service-case-studies) | NHS Wales Shared Services Partnership’s Estates and Facilities Performance Management System (EFPMS) dashboard report covers 2024/25. Check health board coverage, access and output grain. Comparable open site data remain unverified. [EFPMS publication notice](https://nwssp.nhs.wales/ourservices/specialist-estates-services/specialist-estates-services-documents/specialist-estates-services-notifications-sesns/sesn-25-10-publication-of-estates-and-facilities-performance-management-system-efpms-nhs-estate-dashboard-report-2024-25/) |
| Scotland | Scottish Index of Multiple Deprivation 2020 v2 data zones. [SIMD 2020](https://www.gov.scot/collections/scottish-index-of-multiple-deprivation-2020/) | Scottish EPC register and separate non-domestic extract, titled Dataset to Q3 2026 at observation. [Scottish non-domestic EPC dataset](https://data.gov.scot/dataset/non_domestic_energy_performance_certificates___dataset_to_q1_2026) | Public Sector Heat Decarbonisation Fund, named awards and owner capital records. The Clean Heat Development Fund supports development and excludes capital works. [Heat in Buildings progress](https://www.gov.scot/publications/heat-buildings-progress-report-2026/pages/6/) · [Named awards](https://www.gov.scot/news/reducing-emissions-and-cutting-energy-bills/) · [Development fund](https://www.gov.scot/publications/public-sector-clean-heat-development-fund/) | National Services Scotland supports health board condition, backlog and life-cycle appraisals. Public access to site meter or project extracts remains unverified. [NHSScotland asset management services](https://www.nss.nhs.scot/health-facilities/property-and-capital-planning/asset-management-services/) |
| Northern Ireland | Northern Ireland Multiple Deprivation Measure 2017 Super Output Areas. [NIMDM 2017](https://www.nisra.gov.uk/statistics/deprivation-and-poverty/northern-ireland-multiple-deprivation-measure-2017-nimdm2017) | Individual GOV.UK lookup and Department of Finance guidance. The MHCLG England and Wales bulk service excludes Northern Ireland. [Department of Finance](https://www.finance-ni.gov.uk/articles/energy-performance-certificates) · [Public lookup](https://www.gov.uk/find-energy-certificate) | Department for the Economy’s Energy Invest to Save Fund for public-sector buildings, DAERA climate reporting for required bodies, and estate owner capital records. Public fund completeness and a building-level award register remain unverified. Ministerial aggregates do not provide site outcomes. [Fund update](https://www.economy-ni.gov.uk/articles/ministers-speech-ni-energy-forum-2026-9-september-2026) · [Central government energy strategy](https://www.economy-ni.gov.uk/topics/energy-efficiency) · [DAERA reporting](https://www.daera-ni.gov.uk/articles/public-body-reporting-climate-change) | The Northern Ireland Audit Office’s 2026 review describes condition, backlog and Health and Social Care estate returns, including condition data for 2023/24. Corroborate current trust condition and investment with estate owners. [Northern Ireland health estate review](https://www.niauditoffice.gov.uk/publications/html-document/health-estate-northern-ireland) |

Record the assigned area code, boundary edition, lookup method and
confidence. Within each nation, use its published rank or bands with the
appropriate reference population and direction. Equal-numbered deciles
across nations can represent different levels and definitions of
deprivation. Do not create a UK deprivation ranking from them. Combine
only explicitly harmonised measures with documented comparability. Where
intended service-user evidence is available, retain its method, period and
disclosure boundary. Location alone provides neighbourhood context and
does not establish who uses a service. Preserve the distinct national
certificate methodologies, applicability, area conventions, measurement
periods and status. Use comparable physical measures where rating scales
or assessment methods differ. [ONS guidance on comparing England and Wales deprivation analyses](https://www.ons.gov.uk/peoplepopulationandcommunity/healthandsocialcare/causesofdeath/articles/measuringsocioeconomicinequalitiesinavoidablemortalityinenglandandwales/latest) ·
[Certificate lookup and rights](https://chris-page-gov.github.io/20261120-IREA-Hack-Property-public/tower-hamlets/evidence.html#finding-energy-certificates)

GovS 004 Property calls for sufficient sub-area measurement on larger
buildings and campuses. Use it when discussing meter scope with the estate
owner. Its guidance does not establish equivalent devolved datasets.
A common method is feasible. Comparable UK-wide availability of building,
investment and energy data remains unvalidated.
[Government Functional Standard GovS 004 Property](https://www.gov.uk/government/publications/government-standard-for-property-govs-004/government-functional-standard-govs-004-property)

### National small-area reference

The 20 November 2026 reference applies the overall threshold within each
nation using its official small-area release. It supplies an area
denominator and an area flag for later work.

| Nation | Published index and geography | Areas in overall deciles 1–5 | All published areas | Rule and source |
| --- | --- | ---: | ---: | --- |
| England | IoD 2025, 2021 LSOAs | 16,877 | 33,755 | Use the published overall decile in File 7. [IoD 2025 File 7](https://www.gov.uk/government/statistics/english-indices-of-deprivation-2025) |
| Wales | WIMD 2025, 2021 LSOAs | 958 | 1,917 | Use the published overall decile in the `Deciles_quintiles_quartiles` worksheet. Published ranks 1–958 qualify. [WIMD ranks workbook](https://www.gov.wales/welsh-index-multiple-deprivation-2025) · [StatsWales group definitions](https://stats.gov.wales/en-GB/9706edd9-73ad-4902-bb12-7ccd7038626e/pivot) |
| Scotland | SIMD 2020 v2, 2011 Data Zones | 3,488 | 6,976 | Use the published `SIMD2020v2_Decile` in the official lookup. [SIMD 2020 v2 lookup](https://www.gov.scot/publications/scottish-index-of-multiple-deprivation-2020v2-data-zone-look-up/) |
| Northern Ireland | NIMDM 2017, Super Output Areas | 445 | 890 | Derive 10 groups of 89 from the published overall ranks, with rank 1 most deprived. Deciles 1–5 are ranks 1–445. [NISRA SOA results](https://www.nisra.gov.uk/publications/nimdm17-soa-level-results) |
| Sum of national counts | Four independent releases | **21,768** | **43,538** | Sum of areas selected by separate national thresholds. It gives no common UK ranking or estimate of premises or population coverage. |

England has 16,877 areas in IDACI deciles 1–5 and 16,877 in IDAOPI deciles
1–5. Each uses its own published decile. The supplementary ranks can tie.
Northern Ireland’s `IDAC and IDAP` worksheet gives independent ranks for
children aged 15 and under and people aged 65 and over living in
households below 60% of Northern Ireland median equivalised income.
Applying the same rule of 89 areas per decile to each rank separately
selects 445 areas per indicator. These are optional Northern Ireland
indicators with their own definitions and edition. Equal counts do not
imply that the same areas qualify. Blank supplementary fields for Wales
and Scotland mean the indicators were not applied in this reference.
[England supplementary indices](https://www.gov.uk/government/statistics/english-indices-of-deprivation-2025) ·
[Northern Ireland supplementary workbook](https://www.nisra.gov.uk/publications/nimdm17-soa-level-results)

Checked that each nation’s area codes are unique, its overall ranks are
continuous, the decile counts reconcile and the four source file hashes
match the manifest. The local files are
`/private/tmp/irea-uk-deprivation-threshold-20261120/uk-deprivation-area-summary.json`
for exact download URLs, source hashes and counts, and
`uk-deprivation-area-reference.csv` in the same directory for derived area
flags. The raw downloads and derived CSV sit outside version control.
Use dataset ID `uk-deprivation-area-reference` in the [visualisation
catalogue](https://chris-page-gov.github.io/20261120-IREA-Hack-Property-public/tower-hamlets/data/visualisation-specifications.json) for view recommendations
and the boundary inputs needed before mapping.

Resolve the exact boundary edition and code namespace before any
position-to-area join. In particular, preserve Northern Ireland’s
`SOA2001` source field and confirm the matching geometry before joining.
Where the estate geography uses a different vintage, record and review
the appropriate official lookup or reassign positions against the
versioned boundaries. The national check covered published area data.
Premises screening and any selection or join for another study area
remain subject to the Tower Hamlets validation gate.

## 3. Record investment by site and measure

For every proposed, active and historic project record the matched site or
part, system and measure scope, actor, provenance and discovery route.
Check relevant government awards, local funds, procurement notices and
the owner’s capital, maintenance and programme records. Include
self-funded and co-funded projects. Public lists provide leads. Request
or reuse owner confirmation only under an authorised route. Record each
source checked, scope, search date, lookback, identifiers and held or
unavailable records. A search with no public award found gives only the
result of that search.

| Ledger field | What to record |
| --- | --- |
| Identity and coverage | Site, asset or part, building, service and meter relationship, measure type, coverage dates, match evidence and any competing or rejected match |
| Stage and dates | Application or feasibility, announcement or potential award, approved or committed delivery, underway, disruption or commissioning, operational or completed, cancelled, and historic work. Record stage effective date, award and funding secured dates, planned and actual starts, practical completion, commissioning and confirmed operating dates. Use unknown for missing dates |
| Money | Approved budget, grant awarded, secured co-funding, contractual commitment and actual payments or final outturn as distinct fields. Record fiscal period, currency, source and whether values cover the whole project or a measure |
| Evidence | Observation date, stage evidence, authority, conflict or supersession, reviewer and confirmation date, system coverage, whether baseline is verified and overlapping measures or works |
| No active investment check | Owner, programme and capital records checked for the defined site, system, measure and time window. Record relevant grant or local fund checks, affirmative owner confirmation, date and search expiry. Keep the confirmed scope explicit |

Review changes against the evidence effective at the as-of date. An
announced or conditional award without approved delivery belongs in a
development watchlist. Feasibility funding remains separately visible.
A grant can support delivery without proving work started or establishing
completion. Use verified actual commissioning or operation for entry to
evaluation. Expired checks, absent coverage and unresolved conflicts
return to unknown, with the original observations retained. Propose a
lookback and recertification interval by source and programme for reviewer
approval. Ordinary evidence checks can proceed while the intervals are
agreed.

Avoid adding programme-wide awards to site awards or counting a co-funded
project twice. Match recipient, scope, award IDs and dates before rolling
up. Allocate only evidenced shares. Keep unidentified overlaps unresolved.
Flag a building with any known current work. A separately defined measure
outside that work can be reviewed for the opportunity shortlist with
affirmative confirmation for that measure and its scope.

## 4. Assign a queue deterministically

The selection unit is one assessed premises, one defined candidate
measure and one as-of date. Evaluate the rules in order and use the first
applicable row. Maintain site-wide investment flags and a history of other
projects separately. Classification thresholds, data sufficiency and
screening windows are draft policy choices to approve before ranking.

| Condition in order | Queue and treatment |
| --- | --- |
| Evidence shows out of scope | Retain the exclusion, reason and date. |
| Identity, measure scope or a conflicting stage claim is unresolved | Needs verification. Retain known building work flags and conflicting or expired evidence while resolving the case. |
| Relevant approved or committed delivery, work underway, disruption or commissioning | Investment pipeline. Keep funding evidence, baseline readiness and milestones. Hold that measure out of the no-active-investment shortlist. |
| Relevant work is confirmed operational or completed | Later outcome evaluation. Record historic or recent completion and data readiness. Quarantine non-comparable periods and wait for stable follow-up where needed. A different unaddressed measure gets its own assessment. |
| Application, feasibility or announced potential award, with delivery unconfirmed | Needs verification, with a development flag. Record the grant phase. If the records independently confirm no active delivery for a separately defined measure, apply the next rule to that measure. |
| Affirmative, in-date confirmation of no active relevant delivery, and the assessed measure meets the deprivation and rating screen and comparable energy evidence criteria | No-active-investment shortlist for the assessed measure and scope. Any unrelated current work stays visible in the building flag. |
| Affirmative no active relevant delivery, with energy screening evidence insufficient | Needs verification. Keep the investment confirmation and specify the missing energy evidence. |
| Remaining cases including a public search with no award, or a cancelled project with current evidence gaps | Needs verification. A cancelled project can be recorded as inactive. Apply the shortlist rule only after checking for replacement work and confirming current no-active status. |

Keep annual hard FM or routine repairs, soft FM, utility bills and metered
consumption, decarbonisation capital, and estimated backlog and risk as
separate measures. Backlog estimates describe deferred work. Safety or
service-critical escalation remains visible in its own queue, without
altering an energy or carbon rank. Where maintenance explicitly includes
decarbonisation, tag the evidenced measure and cost portion and avoid
double counting. Annual bills and realised carbon are based on observed
energy and prices. Do not offset them with backlog, maintenance, capital
awards or estimated savings.

Treat major repair, planned shutdown, commissioning, PV, changed service
activity and new or changed meter coverage as possible changes to
comparability. Declare affected periods ineligible for comparison or use
a justified non-routine adjustment and report its effect and uncertainty.

## 5. Freeze the baseline and evaluate delivered work

1. **Before works.** Record the measure theory, system and meter boundary,
   surveyed floor-area basis and comparator or controls. Freeze the
   baseline period, input hashes, quality checks, adjustment model and
   reporting design. Use matched 12-month baseline and follow-up windows
   as a proposed default where stable data are available. Approve another
   window only with a clear seasonal and scope rationale.
2. **During works.** Record actual installation, commissioning and service
   changes. Track concurrent capital, maintenance, building extension,
   clinical or community service changes and disruptions. Record actual
   outturn separately from project value and funding approvals.
3. **After stable operation.** Obtain complete monthly data for gas,
   electricity, heat and any other material fuel, with actual or estimated
   reads, floor area and meter coverage. Record heating degree days from a
   documented weather series, service hours, occupancy or activity and
   changes in relevant loads. Capture actual invoices, tariffs, standing
   and other charges. Match scope and periods across fuels and bills.
4. **Calculate separate outcomes.** Keep fuel-specific kWh, measured-area
   intensity and raw utility spend. Estimate a comparable baseline under
   follow-up weather and usage using a documented model where supported.
   Compare adjusted baseline with follow-up and show raw results,
   uncertainty and boundaries. For PV, retain grid imports, generation,
   exports and self-use. In a simple site without material storage flows,
   electricity demand equals imports plus on-site generation used on site.
   Account for storage and other flows where present. A reduction in grid
   imports alone does not establish lower site demand. For heat pumps,
   assess gas reduction and electricity increases together. Report actual
   bill movement and cost change at a common tariff separately, with the
   treatment of fixed charges documented.
5. **Calculate carbon consistently.** Calculate operational tonnes CO₂e by
   multiplying each fuel and electricity activity by its applicable factor
   and converting units. Document the boundary, geographic applicability,
   factor series, year and reporting basis. Use a frozen common factor set
   when isolating the effect of changes in activity. Use year-specific
   factors for realised emissions in each reporting year. Show these
   results separately and record the treatment of exports, electricity
   accounting basis and any out-of-scope emissions.
6. **State strength of evidence.** Use distinct labels for anticipated or
   modelled savings, observed change, adjusted change, and causally
   attributable impact. For causal attribution use a credible comparator
   or pre-specified evaluation design with checks on baseline trends,
   selection, concurrent work and service changes. If overlapping works
   cannot be disentangled, evaluate their package with a qualification.
   If a robust counterfactual is unavailable, describe the adjusted
   change and plausible competing explanations. Leave savings unclaimed
   when monitoring data or essential scope checks are missing.

[DESNZ monitoring and evaluation framework](https://www.gov.uk/government/publications/desnz-monitoring-and-evaluation-framework/department-for-energy-security-and-net-zero-monitoring-and-evaluation-framework-accessible-webpage) ·
[PSDS Phase 3 evaluation](https://www.gov.uk/government/publications/public-sector-decarbonisation-scheme-psds-evaluation-of-phase-3) ·
[UK 2026 conversion factor methodology](https://assets.publishing.service.gov.uk/media/6a2940543b15d05a7ce3202e/2026-GHG-conversion-factors-methodology-report.pdf) ·
[Tower Hamlets energy and area checks](https://chris-page-gov.github.io/20261120-IREA-Hack-Property-public/tower-hamlets/method.html#6-establish-energy-area-and-emissions-at-the-same-scope)

## 6. Worked application at Mile End Hospital

| Evidence | Draft method decision |
| --- | --- |
| Barts Health reports a £360,000 grant-supported solar project, with expected annual generation of about 94,500 kWh. | Flag known investment and put solar in the delivery pipeline for review. Confirm actual commissioning date and meter arrangements before opening an outcome window. Leave measured benefit unknown. Heat remains a distinct measure that needs its own investment check. |
| ERIC 2025/26 reports £74.18m estimated backlog, £1.12m backlog investment, £966,034 estates and property maintenance and £864,024 in named utilities. | Maintain separate condition, investment, annual maintenance and utility observations. The desktop backlog estimate does not establish solar cost, savings or heating investment. Any safety or service-critical work stays visible on its own evidence. |
| The Community Diagnostic Centre opened in September 2025 with phased capacity. ERIC reported GIA rose to 30,748 m². The public Mile End DEC is rated B and describes 23,977 m² useful floor area. | Check use, dates, meters and premises footprint before comparing periods or normalising. The area conventions and scopes can differ. Flag concurrent change and withhold any causal claim about solar or measured efficiency. |

[Mile End Hospital evidence and source links](https://chris-page-gov.github.io/20261120-IREA-Hack-Property-public/tower-hamlets/evidence.html#mile-end-hospital-costs-and-estate-condition)

### Tower Hamlets threshold dry run

The 20 November 2026 check uses the frozen Government Property Estate
workbook and the reviewed Tower Hamlets 2021 LSOA join with English
Indices of Deprivation 2025. From the 63 borough rows we removed one
dwelling. The denominator is 62 non-domestic workbook rows and 38
distinct groups of identical workbook coordinates, spanning 29 mapped
LSOAs. These groups can contain more than one premises or service. The
same row or location can qualify for several indices. Counts reflect
coverage in this convenience snapshot.

| Index filter | All Tower Hamlets LSOAs in band (of 169) | LSOAs containing retained groups | Workbook rows | Grouped locations |
| --- | ---: | ---: | ---: | ---: |
| Overall IMD deciles 1–5 | 139 | 24 | **51** | **30** |
| IDACI deciles 1–5 | 158 | 28 | **61** | **37** |
| IDAOPI deciles 1–5 | 165 | 29 | **62** | **38** |

Read each workbook band column as filed. Count a row if the leading
letter of the recorded band is D, E, F or G. Count a location once per
column if any linked row qualifies. The two types are shown separately.
Every D–G count below is expressed as workbook rows and grouped locations.
The counts reflect raw bands before date, status and scope checks.

| Filter | EPC D–G rows / locations | DEC D–G rows / locations | D–G date evidence on 20 November 2026 |
| --- | ---: | ---: | --- |
| All non-domestic rows | 2 / 2 | 1 / 1 | EPC: one expiry field blank and one future-dated. DEC: one expired. |
| IMD deciles 1–5 | 0 / 0 | 1 / 1 | DEC: the sole entry was expired. |
| IDACI deciles 1–5 | 2 / 2 | 1 / 1 | EPC: one expiry field blank and one future-dated. DEC: one expired. |
| IDAOPI deciles 1–5 | 2 / 2 | 1 / 1 | EPC: one expiry field blank and one future-dated. DEC: one expired. |

Across the unfiltered rows, six record an EPC band and five a DEC band.
The corresponding counts are 1 EPC and 2 DEC under IMD, 6 and 4 under
IDACI, and 6 and 5 under IDAOPI. The D–G workbook DEC is the London Import
Building’s E entry, with recorded expiry on 31 May 2026. The tribunal
occupancy is on the second floor and needs a separate scope check. The
two D–G workbook EPCs are City Tower Jobcentre G, with expiry recorded
as 2 September 2034, and 120 Leman Street E, with expiry blank. Both are
in IMD decile 8. A future workbook expiry alone gives no verification of
register status or occupied scope. The conflicting White Chapel DEC
remains an exception outside the D–G workbook counts. This run established
zero **scope-verified current D–G workbook-row matches**. The actual
number of premises with a current D–G certificate remains unknown.

The separate public register check found a D EPC and an E DEC at the
Gill Street site address, within the stated validity dates. The workbook
coordinate is IMD 2, IDACI 1 and IDAOPI 1. The two workbook rows remain
blank and the area, meter and individual row matches remain unresolved.
Mile End’s workbook coordinate is IMD 4, IDACI 1 and IDAOPI 1. The
existing public B DEC and the expired C EPC reviewed via the authorised
API do not meet the D–G screen. The certificate and ERIC areas differ
and the funded solar project remains separately flagged. Treat those
observations as site-specific evidence. There is no verified
no-active-investment shortlist from this dry run.
[Gill Street register check](https://chris-page-gov.github.io/20261120-IREA-Hack-Property-public/tower-hamlets/evidence.html#gill-street-health-centre-public-register-check) ·
[Mile End evidence](https://chris-page-gov.github.io/20261120-IREA-Hack-Property-public/tower-hamlets/evidence.html#mile-end-hospital-costs-and-estate-condition)

Recounted the frozen grouped review and read back workbook row values
from the original snapshot. Reapplied BNG-to-CRS84 transformation and
point-in-polygon to the saved geometries, reproducing the counts.
The [pilot verification record](https://chris-page-gov.github.io/20261120-IREA-Hack-Property-public/tower-hamlets/method.html#verification-status-for-this-draft)
gives source hashes, geometry caveats and independent review requirements.
This dry run does not test the pending missing-evidence hypothesis.

## 7. Test the rules before applying them elsewhere

Use the following hypothetical cases to test queue outcomes. They are
expected outcomes for review and do not represent additional sites.

| Test case | Expected outcome |
| --- | --- |
| Certified premises, verified comparable baseline and current owner confirmation of no relevant delivery after checks | Shortlist the eligible measure if it meets the approved criteria. |
| No award found and owner’s records unavailable | Needs verification. The search does not establish absence of active investment. |
| Feasibility-only award | Development flag and needs verification for delivery. Keep the funding type distinct. |
| Solar funded and heat untouched by the solar project | Solar in pipeline. Flag the building. Assess heat separately and keep it in verification until its own evidence meets the shortlist rules. |
| Overlapping funded fabric projects | Investment pipeline. Deduplicate funding and meter scope. Evaluate the package if individual outcomes cannot be isolated. |
| Capital project cancelled, current replacement status unclear | Record cancellation and route to verification until current checks establish whether another project is active. |
| Historic commissioning with stable baseline and suitable follow-up | Later outcome evaluation. Verify meter scope and the comparator before attributing savings. |
| Same site-wide UPRN on several contracts with a shared meter and different starts | Verify premises and measure scope. Keep contracts separate, reconcile the meter once and use package evaluation if appropriate. |
| Routine maintenance with a documented energy element | Keep annual repair and backlog separate. Flag only the evidenced energy portion and adjust or exclude disturbed energy periods. |

Generate a versioned coverage table by nation, source, facility type and
investment stage. Report counts and denominators for discovered,
eligible, scope verified, search complete, no active investment confirmed,
in pipeline, evaluation ready, out of scope and unknown. Include a site
view and a measure view to avoid implying that measure totals count sites.
Keep the evidence check queue separate from priority for carbon funding.
Run sensitivity checks on source coverage, recertification and lookback,
site versus measure scope, area and meter assumptions, proxy thresholds,
cohort mix and choice of baseline models or emission factors. Record the
effect on queue assignments and any proposed ranking.

After the validation gate, propose a staged rollout. For each future
nation or agreed area, first pin the official small-area index and area
denominator, an evidenced estate inventory, applicable certificate and
investment sources, data access terms and sample review design. Record
`source ready`, `partial coverage`, `access pending` or `unavailable`
for each source. Check an outcome sample against owner, survey and meter
evidence before any expansion. Publish only the approved eligible
coverage, thresholds, exceptions and outcomes at the appropriate unit.
A UK-wide coverage or ranking claim would require separately evidenced
representativeness and comparability.

Before any other area is selected or run, freeze the specification and
Tower Hamlets baseline, review the tabletop outcomes and validate source
coverage, identity and missingness on the existing pilot. Require an
independent review of the Mile End classifications, outcome claims and licensing
boundaries. Log deviations and evidence gaps, and record reviewer and
programme owner sign-off against the version. The present scope is Tower Hamlets validation. Replication awaits signed
review.
[Tower Hamlets repeat checklist](https://chris-page-gov.github.io/20261120-IREA-Hack-Property-public/tower-hamlets/method.html#9-repeat-checklist-and-stop-or-go-decision)
