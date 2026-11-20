# Public estate retrofit investigation

[Open the public site](https://chris-page-gov.github.io/20261120-IREA-Hack-Property-public/) · [National candidate screen](https://chris-page-gov.github.io/20261120-IREA-Hack-Property-public/national/) · [Tower Hamlets pilot](https://chris-page-gov.github.io/20261120-IREA-Hack-Property-public/tower-hamlets/)

This static research prototype helps a public budget holder find candidate non-domestic estate records for energy efficiency investigation. It does **not** approve retrofits or spending. Public ownership is an explicit working assumption, because the Cabinet Office source includes freehold and leasehold interests.

The opening page gives the 150-word journey and a one-page screening diagram. It leads to the full provisional register, the separate Tower Hamlets pilot, methods, evidence gaps and rights. Technical abbreviations open short definitions in a side panel. The site needs no account or application server and never calls OS NGD.

## What the screen establishes

- Cabinet Office Building workbook: 53,009 rows, not confirmed distinct premises.
- Usable measured-area rows under the current dashboard rule: 10,992.
- Investigation prompts: 492 with an E–G rating and measured area, plus 1,775 with a large measured area and no recorded band; 2,267 in total.
- Tower Hamlets is a separate local sample: 51 rows at 30 locations meet the English IMD decile 1–5 check, but no retrofit shortlist is verified.
- The later draft method proposes D–G while the dashboard applies E–G. National small-area deprivation has not been joined.

Read [the source register](sources/index.md), [the funnel and Mermaid source](sources/estate-screening-funnel.md), [the national method](sources/national-estate-dashboard.md), [the Tower Hamlets evidence gaps](sources/tower-hamlets-evidence-gaps.md), and [licensing decisions](LICENSE_DECISIONS.md). Original downloaded workbooks, licensed OS NGD extracts, credentials and user correspondence are excluded.

## Files and reproducibility

`docs/` is the complete GitHub Pages edition. `docs/national/data/candidates.json` preserves every field of the 2,267-row working register; `candidates.csv` is a flat export. `docs/national/data/dashboard.json` holds the reviewed dashboard aggregate and location snapshot, and `ons-area-map.json` holds simplified ONS display boundaries. `docs/tower-hamlets/` is the reviewed static notebook and its open-data assets. `analysis/` contains the count and geography code, fixed derived data and the A4 diagram. The [workbook manifest](sources/workbook-snapshots.json) identifies the original locally held edition by source URL and checksum.

The static site can be served from `docs/` without a build step. Regenerating the national snapshot requires the exact source workbooks recorded in the manifest. Rebuilding the Tower Hamlets notebook requires its separately saved static source distribution. `analysis/build_public_site.py` assembles a reviewed local copy when those inputs are present; committed `docs/` is the deployable output.

## Rights and limits

The Cabinet Office estate data and ONS boundaries have source-specific Open Government Licence terms and attribution. Other sources, photographs and authored text keep their own rights; there is no blanket licence for the whole repository. See [sources and rights](https://chris-page-gov.github.io/20261120-IREA-Hack-Property-public/rights/) and [licensing decisions](LICENSE_DECISIONS.md). The three slide photographs are included with their owner's express public-publication permission. The figures printed on the slides have not been verified.

A funded shortlist still needs confirmed ownership and works authority, current certificate and meter scope, measured energy use, surveys, feasible measures, costs, savings and current investment checks.
