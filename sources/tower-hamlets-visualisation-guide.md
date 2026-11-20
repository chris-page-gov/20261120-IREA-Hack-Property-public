---
type: Guide
title: Visualisation metadata for the estate evidence
description: Dataset and view identifiers, interpretation rules and prerequisites for future visualisation.
observed_on: "2026-11-20"
---

# Visualisation metadata for the estate evidence

The [dataset and view catalogue](visualisation-specifications.json), version
1.0.0, travels alongside the data. It answers what a later view should show,
which fields to use and when the evidence is ready. It is a project-owned
declarative specification. The datasets and the existing evidence notes
remain the sources for values, scope and rights.

| Contract field | How to use it |
| --- | --- |
| `datasets.<dataset ID>`, `edition`, `references` | Use the stable dataset ID to resolve its edition, method and source links. Notebook paths are relative to the public static Site origin. Local paths refer to ignored or scratch inputs. |
| `grain`, `measure`, `rules` | Check the unit of observation, units and denominators before filtering, grouping or comparing. Retain the scope and source edition with the result. |
| `physicalFields`, `semanticFields` | Physical names were checked against the identified input. Materialise semantic fields through the stated derivation or review. An empty physical list denotes a proposed data contract. |
| `views[].id`, `role`, `question`, `mark`, `encoding` | Select a view ID within a dataset. The channels identify the fields for axes, colour, facet, detail, tooltip, geometry or table columns. Where a view lists alternatives, follow its design note and use one compatible field per panel or selection. |
| `availability`, `needs` | `available` means the captured input or documented evidence supports the view. `conditional` needs an additional verified input, join or rights decision. `planned` describes a future dataset or evidence collection. |

## Dataset and view choices

| Dataset ID | Start here |
| --- | --- |
| `uk-deprivation-area-reference` | Use `national-area-counts` with all four nation denominators. The CSV has no geometry. Use `national-decile-map` once the versioned boundaries and joins are verified. |
| `tower-hamlets-lsoa-deprivation` · `tower-hamlets-oa-census` | Shade one LSOA index at a time, with 1 most deprived. Show OA outlines and Census detail separately. Label the missing category and the 1–5 selection. |
| `tower-hamlets-estate-workbook-locations` · `tower-hamlets-certificate-evidence` | Count workbook rows, coordinate groups and verified premises separately. Use a point layer for discovery and a table for EPC and DEC evidence and exceptions. |
| `mile-end-eric-site-year` · `premises-meter-bills` | Keep energy use and costs in separate panels with aligned periods. Use ordered risk bands for backlog. Detailed billed and metered series need authorised inputs and comparable boundaries. |
| `tower-hamlets-desnz-subnational-energy` · `uk-ecuk-community-estate-2025` | Keep named MSOA gas and non-half-hourly electricity apart from borough-only half-hourly electricity. Label ECUK as modelled UK category totals in ktoe. |
| `public-estate-investment-ledger` · `public-estate-measure-outcomes` | Start with dated review tables. Use stage counts only with a declared denominator. Show before and after only for stable, scope-matched measurement windows. |

Record the catalogue pointer and stable ID `uk-deprivation-area-reference`
alongside `/data/uk-deprivation-area-reference.csv` and its manifest on the
notebook. A consumer should check the data edition, selected view, source
terms and prerequisites before rendering. Keep current, expired,
unmatched, unavailable, suppressed and ineligible states visible. Use
tables where scope, matching or readiness needs to be read precisely.

[UK screening method](uk-public-estate-decarbonisation-method.md) ·
[Tower Hamlets evidence](tower-hamlets-estate-evidence.md)
