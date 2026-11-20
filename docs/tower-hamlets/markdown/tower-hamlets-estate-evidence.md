
# Tower Hamlets estate map evidence

## Estate and geography

Use the Cabinet Office Government Property Estate Building workbook downloaded
on 17 November 2026. Retain the original workbook under the ignored snapshot
directory and use its recorded SHA-256 to identify the edition. The prototype
covers what that workbook records, with no assurance of complete public-estate
coverage, current occupation or pin accuracy. [Workbook manifest](https://chris-page-gov.github.io/20261120-IREA-Hack-Property-public/tower-hamlets/evidence.html#estate-and-geography) · [Estate dataset scope](https://www.data.gov.uk/dataset/a3ad62cf-d8a2-4d3b-b3c6-24c35c5e0f71/the-government-property-estate-including-buildings-and-land)

Compare workbook eastings and northings in British National Grid (EPSG:27700)
with ONS May 2026 full clipped boundaries. Use Tower Hamlets local authority
district `E09000030` and Poplar ward `E05009328`. The ward contains the London
Import Building workbook point. Use the borough polygon to include records
beyond the ward. A pier coded to the borough lies outside the clipped boundary.
The spatial join yields 63 building rows across 41 property references. Omit one
dwelling for the non-domestic screen and group the remaining 62 rows at 38
exact workbook coordinates. Coordinate groups can contain different buildings
or holdings. The local join retains the selected boundary geometries and
source rows. [ONS Open Geography Portal](https://geoportal.statistics.gov.uk/)

Nine rows carry an EPC or DEC band, including none of the 48 NHS rows. For
investigation, compare the historic DEC entries for East London Family Court
(B, 38), Thames Magistrates' Court (C, 64) and London Import Building (E, 121).
Check certificate dates, occupancy and metering scope before drawing a
comparison across these justice sites. The White Chapel Building workbook
record shows DEC B alongside operating rating 100. Check the underlying
certificate before using either value. [Energy certificate register](https://www.gov.uk/find-energy-certificate)

## Neighbourhood context

- Join the English indices of deprivation 2025 File 7 to 169 Tower Hamlets
  2021 LSOAs by code. The map shades published IMD, IDACI or IDAOPI deciles,
  with 1 most deprived nationally. IDACI and IDAOPI describe income
  deprivation for children and older people respectively. The input archive
  URLs and hashes are in the [local neighbourhood JSON](https://chris-page-gov.github.io/20261120-IREA-Hack-Property-public/tower-hamlets/runbook.html#local-inputs-and-rebuild).
  [Official release and File 7](https://www.gov.uk/government/statistics/english-indices-of-deprivation-2025) · [ONS LSOA geometry service](https://services1.arcgis.com/ESMARspQHYMw9BZ9/arcgis/rest/services/LSOA_2021_EW_BFE_V10_RUC/FeatureServer/3)
- Join Census 2021 TS007a and TS011 by code to 913 Output Areas nested in
  those LSOAs. TS007a gives the under-5 and 60-and-over counts and population
  denominators. TS011 gives households deprived in at least two of the four
  Census dimensions and the household denominator. Show the published parent
  indices separately on selection. Keep the indices at LSOA resolution and
  use the OA figures as local context only. Aggregate characteristics do not
  establish the health, access or needs of a particular household or building.
  [TS007a age table](https://www.nomisweb.co.uk/output/census/2021/census2021-ts007a.zip) · [TS011 household table](https://www.nomisweb.co.uk/output/census/2021/census2021-ts011.zip) · [ONS OA geometry service](https://services1.arcgis.com/ESMARspQHYMw9BZ9/arcgis/rest/services/OA_2021_EW_BFE_V9_RUC/FeatureServer/3)

## Building identity and quantities

| Local example | Evidence and next check |
| --- | --- |
| Gill Street Health Centre | The named address UPRN and workbook point were matched spatially to the NGD footprint. Confirm the current holding and area scope for any proposed measure. |
| Young V&A | The named address UPRN and workbook point were matched spatially to the NGD footprint. Complex roofs and building parts need separate geometry for a quantity estimate. [Venue address](https://www.vam.ac.uk/young/visit) |
| East London Tribunal Hearing Centre | The address evidence identifies a parent-building UPRN. The tribunal is on the second floor. The footprint covers London Import Building as a whole and a tribunal unit UPRN remains unconfirmed. [HMCTS venue listing](https://www.find-court-tribunal.service.gov.uk/courts/east-london-tribunal-hearing-centre) |
| Aberfeldy Practice | The practice moved in August 2024. The historic workbook point falls on a different building from the former surgery. Check the new premises and current holding. [Practice move notice](https://www.aberfeldypractice.nhs.uk/patient-engagement-session-practice-move/) |
| Community Paediatrics | The workbook point falls on a mixed-use building. The clinic's address and UPRN remain unconfirmed. NHS referral material points to Mile End Hospital. Leave the workbook footprint unassigned to the service. [NHS referral pathway](https://primarycare.northeastlondon.icb.nhs.uk/wp-content/uploads/2024/09/Tower-Hamlets-GP-paediatric-referral-pathway-New.pdf) |

Use verified address and building-part matches before applying NGD footprint
or height to estimate quantities. Use measured areas and correctly scoped
building parts and storeys first. Keep net internal area and gross floor area
distinct. For a complex building, use per-part footprints and heights for
indicative volume and label assumptions, scope and confidence. Keep missing
measurements and confidence visible. A quote needs evidence of the specific
measure, the applicable area and scope, and appropriate rates.

GB Built Address v3 includes nullable `floorlevel`, `lowestfloorlevel` and
`highestfloorlevel` through OS Select+Build. An extract is currently
unavailable. NGD Building `numberoffloors` is a whole-building maximum of
occupiable floors at or above ground level. Coverage is mainly eligible
offices and homes. Values can come from observations, certificate evidence
or modelling. Check the evidence and capture method for each value. An OS
Data Hub Support enquiry on floors and UPRNs was sent from Outlook on
20 November 2026 and its reply is pending. [GB Built Address](https://docs.os.uk/osngd/data-structure/address/gb-address/built-address) · [NGD Building](https://docs.os.uk/osngd/data-structure/buildings/building-features/building)

OS Road and NGD evidence are for authorised local use under the applicable
OS terms. Keep raw licensed data, derived measurements embedded in the
temporary preview and credentials out of Git and any public share pending a
rights review. Retain the attribution and source editions for any approved
reuse. [Repository licensing decisions](https://chris-page-gov.github.io/20261120-IREA-Hack-Property-public/tower-hamlets/evidence.html#building-identity-and-quantities)

## Finding energy certificates

- **Public lookup.** MHCLG’s individual property service covers England,
  Wales and Northern Ireland and is sufficient for the Gill Street case.
  Use the non-domestic route and open each relevant EPC and DEC. The EPC
  rates the building asset under modelled conditions. The DEC rates
  operational energy performance for its assessed scope. Keep the ratings
  and their dates separate. [Find an energy certificate](https://www.gov.uk/find-energy-certificate)
- **Bulk data.** Use the current MHCLG service for England and Wales when
  an authorised analysis needs non-domestic EPC and DEC records at scale.
  CSV downloads require GOV.UK One Login. The developer API has separate
  access instructions. Check publication and eligibility terms before
  reuse. The service lists non-address fields under OGL v3.0 and specifies
  permitted uses and a notice for sharing address and postcode fields
  subject to OS and Royal Mail rights. [Bulk service](https://get-energy-performance-data.communities.gov.uk/) ·
  [Developer API guidance](https://get-energy-performance-data.communities.gov.uk/guidance/energy-certificate-data-apis) ·
  [Licensing restrictions](https://get-energy-performance-data.communities.gov.uk/guidance/licensing-restrictions)
- **Catalogue discovery.** The National Data Library record-level listing
  is MHCLG metadata updated on 26 February 2018. On 20 November 2026 its
  `epc.opendatacommunities.org` link redirected to the current MHCLG bulk
  service. Use the listing to discover the source. The older combined
  non-domestic listing, updated on 18 January 2017, flags Royal Mail rights.
  [Record-level catalogue entry](https://www.data.gov.uk/dataset/020403de-af6a-49a2-ae06-3b3a7eff4b97/record-level-energy-performance-certificate-data) ·
  [Older non-domestic listing](https://www.data.gov.uk/dataset/f1249e41-0afe-4b19-9357-8b4c66821a11/non-domestic-energy-performance-certificate-and-display-energy-certificate-data)

### Gill Street Health Centre public register check

Observed on **20 November 2026**. Both frozen workbook rows have blank EPC
and DEC fields. CQC lists Limehouse Practice at Gill Street Health Centre,
11 Gill Street, London E14 8HQ. The public non-domestic postcode results
contain multiple addresses. Opening the individual certificates confirmed a
site-address match. Both records were within the validity dates shown at
observation. [CQC premises listing](https://www.cqc.org.uk/location/1-574169355/contact) ·
[Public postcode search](https://find-energy-certificate.service.gov.uk/find-a-non-domestic-certificate/search-by-postcode?postcode=E14%208HQ)

| Register evidence | Rating | Recorded dates | Published area |
| --- | --- | --- | --- |
| [Non-domestic EPC 0510-0333-4669-9224-5006](https://find-energy-certificate.service.gov.uk/energy-certificate/0510-0333-4669-9224-5006) | Asset rating D (91) | Assessed 25 April 2017, certificate dated 5 May 2017, valid to 4 May 2027 | 831 m² total floor area |
| [DEC 2037-1026-3863-7506-7205](https://find-energy-certificate.service.gov.uk/energy-certificate/2037-1026-3863-7506-7205) | Operational rating E (112) | Issued 3 June 2026, nominated date 30 June 2026, valid to 29 June 2027 | 1,136.07 m² total useful floor area |

The DEC reports annual energy use of **81.67 kWh/m²/year for electricity**
and **180.51 kWh/m²/year for other fuels**. It names natural gas as the main
heating fuel. The published other-fuels figure remains a grouped intensity.
Meter totals and the dates and boundaries of the underlying readings still
need verification. The nominated date is a separate certificate field.
The two area definitions and values differ. Ask estates which spaces,
floors and supplies each certificate covers and whether the 2017 EPC still
describes the occupied premises. The site-address match leaves the link to
each workbook row, the shared supply boundary and current premises-level
performance unresolved.

For synthesis, retain the frozen workbook coverage and record these two
register observations separately at site-address level. Use the
[certificate lookup procedure](https://chris-page-gov.github.io/20261120-IREA-Hack-Property-public/tower-hamlets/method.html#certificate-lookup-procedure)
to record status and scope. For the public static companion, use the
source links and reviewed summary with these caveats. Any bulk extract or
address-field reuse needs a separate rights check. No assessor details
are reproduced.

## Non-domestic energy consumption

The DESNZ 2024 subnational release publishes non-domestic gas and electricity
down to Middle Layer Super Output Area (MSOA). Its LSOA tables cover domestic
meters only. A proposed map layer would show published non-domestic figures as
separately labelled MSOA context, using the official stacked CSVs. Use the
published geography codes, year, fuel, units and sector definition. The
Tower Hamlets extract has 34 named MSOA rows for gas and 34 named MSOA
rows for non-half-hourly electricity. Label any mapped electricity
non-half-hourly only. Keep the single half-hourly electricity row labelled
“All MSOAs” at borough level. Keep missing or suppressed values unknown. Do not allocate MSOA figures to LSOAs or
attribute them to a site. This layer is pending. [DESNZ 2024 release, accompanying tables](https://www.gov.uk/government/statistics/subnational-electricity-and-gas-consumption-summary-report-2024/subnational-electricity-and-gas-consumption-summary-report-2024--2#accompanying-tables) · [Stacked electricity data](https://www.gov.uk/government/statistical-data-sets/stacked-electricity-consumption-statistics-data) · [Stacked gas data](https://www.gov.uk/government/statistical-data-sets/stacked-gas-consumption-statistics-data)

ND-NEED 2026 gives public metered gas and electricity benchmarks by building
use and size. Choose a cohort comparable to the facility and keep any benchmark
distinct from the facility's consumption. A DEC uses actual energy, with scope
and period to check against the facility, especially in shared premises.
[ND-NEED 2026](https://www.gov.uk/government/statistics/non-domestic-national-energy-efficiency-data-framework-nd-need-2026) · [Certificate access routes](#finding-energy-certificates)

## UK modelled end uses for community buildings

DESNZ Energy Consumption in the UK 2026 End Uses Table U6 estimates 2025
UK consumption for “Clubs & community centres” at 112.0 ktoe of
electricity and 170.7 ktoe of natural gas. Heating accounts for 83.5%
of the category's estimated natural gas use. The seven-row extract also
covers leisure centres, museums, places of worship, theatres, health
centres and law courts. The five community, arts and leisure rows
reconcile to their parent totals in Table U5.

Ktoe means thousand tonnes of oil equivalent. These are modelled national
totals using service-sector proportions from the 2015 Building Energy
Efficiency Survey (BEES). Use them for national end-use context. They
provide no local or site consumption, energy intensity or site benchmark.
[ECUK 2026 release](https://www.gov.uk/government/statistics/energy-consumption-in-the-uk-2026) ·
[End Uses workbook](https://assets.publishing.service.gov.uk/media/6aac067444ec1aa417346c38/ECUK_2026_End_Use_tables.xlsx) ·
[Methodology](https://assets.publishing.service.gov.uk/media/6ab0fb1ace3f006bd4346d4c/Energy_Consumption_in_the_UK_2026_Methodology_Note.pdf)

Workbook SHA-256 recorded on 20 November 2026

`c2b5723055960875a1bcc383d35a1bc088ba04f90f0fa107a853fdfe6175f122`

## Mile End Hospital costs and estate condition

Mile End Hospital is Barts Health NHS Trust site `R1H13` in NHS England’s
Estates Returns Information Collection (ERIC). Observed on 20 November
2026. The 2025/26 site return covers 1 April 2025 to 31 March 2026 and
reports 30,748 m² gross internal area (GIA). The figures below relate to
that return unless stated otherwise. [ERIC 2025/26 release](https://digital.nhs.uk/data-and-information/publications/statistical/estates-returns-information-collection/summary-page-and-dataset-for-eric-2025-26) ·
[Site CSV v3](https://files.digital.nhs.uk/75/EEA227/ERIC%20-%202025_26%20-%20Site%20data%20-%20v3.csv)

### Annual spending and backlog

| ERIC item | 2025/26 | Interpretation |
| --- | ---: | --- |
| Estates and property maintenance | £966,034 | Reported annual cost |
| Other hard facilities management (FM) | £426,013 | The two named hard services lines subtotal £1,392,047. |
| Cleaning | £805,487 | Reported separately |
| Other soft FM (hotel services) | £1,356,217 | Reported separately |
| Management of hard and soft FM | £229,495 | Shared management line |
| Contracted laundry and linen | £32,415 | Full-service contract line |
| Electricity | £529,424 | 1,953,363 kWh. Sum of green tariff and other electricity fields. |
| Gas | £203,025 | 3,344,144 kWh |
| Other energy | £10,169 | Separate cost line |
| Water and sewerage | £121,406 | Separate cost line |
| Named utilities subtotal | **£864,024** | Electricity, gas, other energy and water and sewerage |
| Investment to reduce backlog | £1,120,000 | £1m for critical infrastructure risk and £120,000 for other backlog |
| Estimated cost to eradicate backlog | **£74,180,000** | £31.65m high, £35.05m significant, £3.88m moderate and £3.60m low risk |

The high and significant backlog bands total **£66.70m**, about **90%** of the
estimated cost. ERIC records a desktop exercise as the method for reviewing
costs. Treat it as an estimate of deferred maintenance work. Keep it separate
from in-year maintenance, backlog investment, capital budgets and liabilities
in the accounts. A risk-band estimate does not establish which buildings,
assets or projects account for the cost.

### What the utility bills tell us

| Reported ERIC figure or derived screen | 2024/25 | 2025/26 |
| --- | ---: | ---: |
| Gross internal area | 25,211 m² | 30,748 m² |
| Estates and property maintenance | £1,591,255 | £966,034 |
| Estimated cost to eradicate backlog | £45,100,252 | £74,180,000 |
| Electricity spend | £720,662 | £529,424 |
| Electricity consumption | 1,856,278 kWh | 1,953,363 kWh |
| Gas spend | £292,855 | £203,025 |
| Gas consumption | 4,069,132 kWh | 3,344,144 kWh |
| Implied electricity cost per kWh | 38.8p | 27.1p |
| Combined electricity and gas divided by reported GIA | 235.0 kWh/m²/year | 172.3 kWh/m²/year |

The 2024/25 denominator is GIA. The row reports 23,261 m² of occupied
floor area separately. Electricity use rose by about 5% while electricity
spend fell by about 27%. The cost per kWh divides annual spend by consumption
and can include charges beyond the energy tariff. The apparent change in
intensity also reflects a larger reported floor area and might reflect
changes in coverage, use or operating hours. The movements identify which
questions to investigate. They establish neither an efficiency improvement
nor a tariff explanation. [ERIC 2024/25 release](https://digital.nhs.uk/data-and-information/publications/statistical/estates-returns-information-collection/summary-page-and-dataset-for-eric-2024-25) ·
[2024/25 site CSV](https://files.digital.nhs.uk/AA/2375EE/ERIC%20-%202024_25%20-%20Site%20data.csv)

Use high utility spend as a prompt to check demand, unit costs and fixed
charges independently. An efficiency assessment would reconcile monthly
bills and actual reads by fuel, check buildings and meters covered,
separate fixed and variable charges, weather-normalise heating, and
account for clinical use, loads and operating hours. Match the energy
boundary to verified floor area before comparing intensity. Assess
condition and backlog separately so the team can consider where
maintenance and energy measures overlap.

A previously verified authorised MHCLG API query on the ERIC site UPRN
returned one expired non-domestic EPC rated C and 23 DEC records, including
one separately named for the Emily Graham Building. The public Mile End
Hospital DEC is rated B and valid to 29 June 2027. Its 23,977 m² total
useful floor area differs in definition and value from ERIC’s 30,748 m²
GIA. Check the building and meter boundaries, certificate periods and
any overlapping supply before using either figure for benchmarking.
[Public Mile End DEC](https://find-energy-certificate.service.gov.uk/energy-certificate/0951-1234-6117-7353-1990) ·
[Certificate lookup procedure](https://chris-page-gov.github.io/20261120-IREA-Hack-Property-public/tower-hamlets/method.html#certificate-lookup-procedure)

### Building projects and the national context

The [UK draft method](https://chris-page-gov.github.io/20261120-IREA-Hack-Property-public/tower-hamlets/uk-method.html#6-worked-application-at-mile-end-hospital)
uses the site to illustrate how to classify funded solar, keep backlog
separate and check boundaries before evaluating savings.

- Barts Health reports a **£360,000 grant-supported solar installation**
  at Mile End, with estimated annual output of about **94,500 kWh**.
  This is a forecast. The trust also records the Community Diagnostic
  Centre opening in September 2025, with capacity introduced in phases.
  Its **£173.063m gross capital expenditure** is a trust-wide accounts
  figure. The reviewed accounts do not establish total Mile End capital
  spend or final Centre expenditure. [Barts Health 2025/26 annual report and accounts, PDF pages 38, 65 and 99](https://www.bartshealth.nhs.uk/download/annual-report-accounts-202526pdf.pdf?ver=62282&doc=docm93jijm4n30371)
- The scheme architect gives **£6.8m** as the project value for the
  Community Diagnostic Centre ground-floor reconfiguration. This is a
  project value reported by the architect. Final audited expenditure,
  campus-wide investment and the amount of backlog addressed remain
  unestablished. [Ansell and Bailey, Community Diagnostic Centre](https://www.ansellandbailey.com/featured-projects/)
- The Cabinet Office’s **State of the Estate 2024/25** condition metrics
  exclude NHS England secondary care because the sector collects
  condition data using different definitions. The companion Annual
  Data Publication’s Health Portfolio table reports **£14.7bn running
  costs, £2.1bn hard FM and £6.1bn soft FM** for 2024/25. These totals
  provide portfolio context. [State of the Estate condition coverage](https://www.gov.uk/government/publications/state-of-the-estate-in-202425/state-of-the-estate-2024-25-html) ·
  [Health Portfolio Table 7](https://www.gov.uk/government/publications/state-of-the-estate-in-202425/government-estate-annual-data-publication-2024-25-html--2#table-7-health-portfolio-summary)
- The NAO’s January 2025 review estimated **at least £49bn** in
  cross-government maintenance backlog as of October 2024. Its NHS
  England estimate for 2023/24 was **£13.8bn** in 2023/24 prices.
  NHS England’s 2025/26 ERIC release reports **£17.3bn**. The different
  reporting periods and price bases preclude a like-for-like real-terms
  comparison of these two figures. [NAO report](https://www.nao.org.uk/reports/maintaining-public-service-facilities/) ·
  [NAO Figures 5 and 6](https://www.nao.org.uk/wp-content/uploads/2025/01/maintaining-public-service-facilities.pdf#page=25) ·
  [ERIC 2025/26 national figures](https://digital.nhs.uk/data-and-information/publications/statistical/estates-returns-information-collection/summary-page-and-dataset-for-eric-2025-26)

## Domestic grants and performance

For the separate domestic question, DESNZ Detailed Household Energy Efficiency
Statistics 2025 Table 4.4 reports before-and-after EPC evidence. The domestic
NEED 2026 impact tables use measured consumption for their analysis of
installed measures. Use the restricted Energy Efficiency Installation Checker
(EEIC) only if authorised for the specific per-UPRN installation enquiry.
No EEIC data was used here. [Household energy efficiency detailed report](https://www.gov.uk/government/statistics/household-energy-efficiency-statistics-detailed-report-2025) · [NEED 2026 impact tables](https://www.gov.uk/government/statistics/national-energy-efficiency-data-framework-need-impact-of-measures-data-tables-2026) · [EEIC data-sharing agreement](https://assets.publishing.service.gov.uk/media/67ed060c199d1cd55b48c629/warm-homes-social-housing-fund-wave-3-data-sharing-agreement.pdf)

## Assessment against the hackathon brief

The prototype meets the organiser’s discovery and triage brief. It shows
geographic patterns, evidence gaps and locations worth investigating. A
ranking of decarbonisation need in the highest-deprivation areas still
requires verified building performance and retrofit evidence.
Organiser’s challenge (unlisted source; see the public source note)

The review transformed all 38 workbook coordinate groups (62 non-domestic
rows) from EPSG:27700 to OGC:CRS84 with PROJ and matched each point to an
official ONS 2021 LSOA polygon. The national 2025 decile 1 groups overlap
and should be read independently.

| Indicator | Locations | Workbook rows | Certificate evidence in the workbook |
| --- | ---: | ---: | --- |
| IMD | 6 | 11 | One EPC C with no recorded expiry. No DEC. |
| IDACI | 28 | 48 | Four rows with a recorded band, including expired or inconsistent evidence. |
| IDAOPI | 33 | 56 | Eight rows with a recorded band. |

To rank need, confirm the current premises and meter boundaries. Obtain
12 months of verified consumption by fuel, measured floor area, use and
operating hours. Account for weather and use like-for-like benchmarks.
Survey technical feasibility and estimate likely carbon savings for each
specific measure. Apply an explicit shortlist method that sets out how
neighbourhood equity and building need affect the decision.
[Draft data requests](https://chris-page-gov.github.io/20261120-IREA-Hack-Property-public/tower-hamlets/access.html)
