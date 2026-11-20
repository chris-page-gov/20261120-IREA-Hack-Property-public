---
type: Runbook
title: Tower Hamlets estate map runbook
description: Open, check and recover the local prototype and trace its inputs.
observed_on: "2026-11-20"
---

# Tower Hamlets estate map runbook

## Open and check the preview

1. On the demo Mac, open the [Tower Hamlets map](http://127.0.0.1:4175/tower-hamlets-estate-map.html)
   in Edge. The preview is served from
   `$HOME/tmp/tower-hamlets-estate-map.html` on loopback port 4175.
2. In Terminal, check that the listener is bound to `127.0.0.1:4175`, the page
   returns HTTP 200 and the OS Road sample tile returns HTTP 200 and
   `image/png`.

   ```sh
   lsof -nP -iTCP:4175 -sTCP:LISTEN
   curl -fsS -o /dev/null -w '%{http_code}\n' \
     http://127.0.0.1:4175/tower-hamlets-estate-map.html
   curl -fsS -o /dev/null -w '%{http_code} %{content_type}\n' \
     http://127.0.0.1:4175/tiles/12/2048/1362.png
   ```

3. Check that the map starts with OS Road and shows 38 mapped locations and 62
   non-domestic workbook records. Search for `London Import Building`, then
   select East London Tribunal and check the parent-building and second-floor
   notes. Check an annotated health or culture example.
4. Switch the LSOA shading from IMD to IDACI and then IDAOPI. Toggle Output
   Area outlines and select an area clear of the markers. Check that the
   Output Area Census figures and parent LSOA indices have separate labels.
   Use the [quick guide](tower-hamlets-estate-guide.md) for the interpretation.

## Restart and recover

1. If there is no listener, confirm that the local server script and live HTML
   still exist. Start the existing server in a dedicated terminal. Leave it
   running during the demonstration.

   ```sh
   cd $HOME/tmp && /opt/homebrew/bin/python3 /private/tmp/serve_th_map.py
   ```

2. If the port is already occupied, identify the listener using `lsof`. If the
   preview and tile checks pass, reuse the listener. If the existing preview
   process needs restarting, stop it in its own terminal with Ctrl+C or send
   TERM to its verified PID, then start it again. Leave unrelated processes
   alone.
3. Reload the Edge tab and repeat the preview checks. If the page loads and
   the sample tile fails, switch to OpenStreetMap in the layer control for the
   live walkthrough. Check the machine's network and the authorised local OS
   Maps API configuration before retrying OS Road. The server reads the
   configured key from a local file and passes it upstream. Keep the key
   out of URLs, Terminal output, Git and screenshots. A blank map with a
   successful tile check may also indicate that Edge could not load Leaflet
   or Proj4 from the external CDN.
4. If the server script has gone, a plain loopback file server can restore
   access to surviving HTML and the OpenStreetMap option. Put a copy of the
   HTML in a dedicated local directory, then start this fallback from that
   directory once port 4175 is free.

   ```sh
   /opt/homebrew/bin/python3 -m http.server 4175 --bind 127.0.0.1
   ```

   The fallback serves files only. Select OpenStreetMap in Edge. If the OS
   proxy script survives, keep it on loopback. Its static handler serves
   files relative to the directory it starts in. The command above uses the
   directory containing the preview HTML.

## Local inputs and rebuild

On 20 November 2026 the working assets were in
`/private/tmp/tower-hamlets-estate-k3tuzffp/`, except where shown below.
Temporary directories may be cleared after the session.

| Local item | Role |
| --- | --- |
| `analysis.json` | BNG workbook point join against the Tower Hamlets and Poplar boundaries, including grouped source rows and geometry |
| `tower-hamlets-neighbourhoods.json` | 169 LSOAs and 913 Output Areas. Its `provenance` records the source URLs and SHA-256 for the IMD CSV and two Census archives |
| `tower-hamlets-desnz-msoa-2024.json` | Filtered official DESNZ records with exact CSV URLs. Contains 34 named gas MSOAs and 34 named non-half-hourly electricity MSOAs, plus one borough-only half-hourly electricity row. The live preview does not use this file |
| `build-neighbourhoods.py` | Python standard-library script that fetches official ONS boundaries, IMD File 7 and Nomis tables, checks code coverage and writes the neighbourhood JSON alongside the script |
| `tower-hamlets-building-evidence.json` | Annotated shortlist and location caveats, with local OS-derived measurements |
| `/private/tmp/build_th_map.py` | Base workbook map renderer |
| `/private/tmp/extend_th_map.py`, `add_spatial_hit.py`, `add_building_notes.py` | Sequential scratch edits for neighbourhoods, area selection and building annotations. All three scripts are under `/private/tmp/` |
| `/private/tmp/serve_th_map.py` | Local-only preview and OS Road raster proxy |

- For a repeat demo, use the existing HTML or an approved local copy. The
  checked-in repository contains the documentation and workbook manifest.
  Keep the generated HTML with embedded evidence, raw NGD data and credentials
  out of Git and any public share.
- To rebuild neighbourhood context, work on a copy of the temporary directory.
  Run `/opt/homebrew/bin/python3 build-neighbourhoods.py` from that copy with
  network access. Check the 169 and 913 feature counts, full child-to-parent
  code coverage and input hashes against the saved JSON. Current service
  responses can differ from the original capture.
- To rebuild the estate base, use the captured `analysis.json` with
  `build_th_map.py`. Redirect the hard-coded output path in a scratch copy
  before running it. If the join is lost, use the November workbook and May
  boundary editions in the [source notes](tower-hamlets-estate-evidence.md#estate-and-geography).
  Join in EPSG:27700, check the counts before filtering, drop the dwelling for
  this use case, then group by exact easting and northing.
- The scratch edit chain expects a manual OS Road change between the base
  renderer and `extend_th_map.py`. A trial rebuild stopped at the latter
  script's footer assertion. On a scratch copy, bring across the
  `const tileStatus=` line from the saved preview and use the footer in
  `extend_th_map.py`'s `needle2` for the intermediate HTML. This lets the
  three edits run in sequence. The live preview also includes later
  changes to visible labels and site pop-ups. Keep its HTML as the reference
  for an exact repeat. Recreate the annotated
  evidence only under the relevant OS entitlement and verify current service
  and address scope again. See the [source notes](tower-hamlets-estate-evidence.md#building-identity-and-quantities).

- To repeat the DESNZ extract, use the two non-domestic MSOA stacked CSVs
  linked from the [energy source note](tower-hamlets-estate-evidence.md#non-domestic-energy-consumption).
  Filter to Tower Hamlets and 2024, preserving the source area code, fuel,
  meter class, units and any missing or suppressed values. Check the row
  counts above. Keep the half-hourly “All MSOAs” row at borough level. Any
  future map join should use named MSOA codes for gas and non-half-hourly
  electricity only.
