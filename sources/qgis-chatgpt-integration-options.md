# Options for a Warwickshire geospatial ChatGPT plugin

Observed on 20 November 2026, after the [QGIS MCP security
review](qgis-mcp-security-review.md) was merged. This is a design assessment,
not an installed plugin, approved WCC connection or legal opinion. The
recommended first use is a private, read-only demonstration using public
evidence and synthetic test cases where rights are uncertain.

## What a ChatGPT plugin means here

OpenAI's current route is a [custom MCP server registered as a
plugin](https://help.openai.com/en/articles/12584461-connecting-custom-mcp-servers-in-chatgpt).
It can expose tools without a custom interface. An [Apps SDK
interface](https://help.openai.com/en/articles/12515353-building-with-the-apps-sdk)
is optional. ChatGPT does not connect directly to a local MCP server; a
[Secure MCP Tunnel](https://developers.openai.com/api/docs/guides/secure-mcp-tunnels)
can carry a private connection without an inbound public port. The tunnel is
a transport path, not a substitute for authorisation in the MCP server.
Public directory submission has separate [stable HTTPS, authentication and
review requirements](https://developers.openai.com/plugins/build/mcp-server).

At the observation date, OpenAI says full MCP connections are available on
Business and Enterprise/Edu workspaces, while Pro supports custom read/fetch
connections. Workspace permissions must be checked before testing or sharing
a connection. [Source: connecting custom MCP servers in
ChatGPT](https://help.openai.com/en/articles/12584461-connecting-custom-mcp-servers-in-chatgpt).

## Licence position

The reviewed upstream project [licenses its components
separately](https://github.com/nkarasiak/qgis-mcp/blob/8a23eb05449d5dcdadaa0df032b6a17b2c859443/README.md#L444-L449):
the QGIS plugin is GPL v2 or later and its MCP bridge is MIT. The MIT bridge
may be reused with its copyright and licence notice. A modified QGIS plugin
can be built and used locally; distribution requires a GPL-compatible source
and notice plan. The [GNU GPL FAQ](https://www.gnu.org/licenses/gpl-faq.en.html)
also explains that separate programs communicating over a socket are often
separate works, but their actual interaction matters. Check the concrete
architecture before assigning a licence to a combined release. Neither
software licence grants permission to expose WCC, OS or other source data.

## Strategy comparison

| Approach | What it would do | Security and rights position | Decision |
| --- | --- | --- | --- |
| **A. Independent evidence and GIS MCP plugin** | Serve a small, versioned set of Warwickshire asset, UPRN, planning and geometry checks from reviewed public snapshots. QGIS may prepare data offline but is not controlled by ChatGPT. | Exposes only purpose-built read-only tools. No QGIS socket, arbitrary Python, file path or database connection is reachable from ChatGPT. Keep source licences and derived geometry rights with each result. | **Preferred first prototype.** A new server can be independently authored; any MIT code copied from the bridge retains its notice. |
| **B. Restricted fork of the QGIS plugin** | Support live QGIS projects after removing dangerous operations and enforcing a narrow command policy inside the QGIS process. | Requires a GPL distribution plan, per-user or authenticated local transport, server-side read-only enforcement, URI redaction and fail-closed approval for any later writes. It still gives a remote client a path into a privileged desktop process. | Consider only when the public-snapshot service cannot meet a verified user need. Review and test the fork as a new product. |
| **C. Thin wrapper around the existing 125-tool server** | Filter the advertised tools while leaving the current QGIS listener and handlers in place. | The direct local socket and plugin-side dispatch remain reachable. Client annotations and a wrapper do not close the three recorded findings. | Do not use this as the security boundary. |
| **D. GIS AI GO catalogue adapter** | Use governed product metadata and, where available, approved data access routes to inform the prototype. | The current experimental Explorer confirmed OS Open UPRN release metadata but supplied no planning polygon lookup or spatial overlay for the worked case. Access and output rights still need checking. | Useful evidence source, not yet the calculation engine. [Worked case](avon-valley-school/site.md#boundary-and-point-check). |

## Preferred first prototype

Build a small MCP server with explicit input schemas and source-linked
outputs. It should use the pinned evidence already recorded in this repo and
return a clear `observed_on`, dataset edition, method, rights status and
confidence for each result. Suggested read-only operations are:

| Tool | Bounded result |
| --- | --- |
| `get_asset_evidence(asset_id)` | Public WCC asset identifier, address and UPRN assertions, each tied to its source edition. |
| `get_planning_evidence(application_ref)` | Public application, decision and condition references, with documentary versus spatial links distinguished. |
| `check_site_point(application_ref, uprn)` | Point-in-polygon result and distance only for an admitted, versioned boundary; disclose whether the geometry is source GIS or derived from a plan. |
| `estimate_envelope_volume(building_id, footprint_edition, surface_edition, terrain_edition)` | Deterministic area and above-ground envelope volume estimate, calculation footprint, raster coverage, method and uncertainty. No claim that this is heated or usable internal volume. |
| `search` and `fetch` | Source-linked summaries for the ChatGPT knowledge journey, if that integration mode is wanted. |

The [Avon Valley School worked case](warwickshire-worked-example.md) can test
the first three operations: asset 3051 has an exact UPRN match, a public
planning decision and conditions, and an indicative point about 59 m outside
the plan-derived red line. The source planning polygon is still unavailable.
The [local 1 m DSM and DTM](ndl-estate-intake.md#downloaded-data) cover a
3 km by 3 km pilot near Warwick. Avon Valley School in Rugby is outside that
tile, so it is **not** a valid volume test case with the current rasters.
Choose a separately verified building within the tile. Match a permitted
footprint, align the surface and terrain rasters, then integrate positive
surface-minus-terrain height within the footprint. Retain survey vintage,
coverage and rights limits as the [domain assessment](estate-okf-domain.md)
requires.

Record-level non-domestic EPC and DEC data have not been acquired because the
current service requires sign-in and access conditions. A certificate lookup
must remain out of the first plugin until a permitted dataset and its
address-data terms are verified. [Intake gap](ndl-estate-intake.md#catalogue-evidence-and-gaps).

## Controls to prove before a private connection

The MCP server should enforce the read-only list itself and accept stable
identifiers, never arbitrary code, SQL, filesystem paths or connection URIs.
Return only the minimum source fields needed for the task; redact credentials
and unnecessary personal data. Bound geometry sizes, coordinate systems,
search area and output rows. Test invalid identifiers, ambiguous UPRNs,
missing geometry, out-of-tile rasters and rights restrictions. Use synthetic
credentials for leakage checks. These requirements follow the [OpenAI MCP
server guidance](https://developers.openai.com/plugins/build/mcp-server),
which says tool annotations aid client behaviour but do not replace server
authorisation, validation or confirmation.

For a private trial, register the reviewed read-only server through a Secure
MCP Tunnel and check the actual account and workspace permissions. If WCC
internal data is ever introduced, authenticate each user and authorise each
request against the owner's agreed access rules. Do not assume that the
tunnel, a ChatGPT confirmation prompt or `readOnlyHint` protects data by
itself. A public plugin would require a separate release, privacy and source
rights review. No paid service, plugin connection or deployment is authorised
by this assessment.
