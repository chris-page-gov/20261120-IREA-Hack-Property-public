# QGIS MCP security review and threat model

Observed on 20 November 2026. This is a research assessment of a possible
integration for the Warwickshire property prototype. It does not approve an
installation, a connection to WCC data or publication of an app.

## Source and method

The reviewed source is [nkarasiak/qgis-mcp at commit
`8a23eb05449d5dcdadaa0df032b6a17b2c859443`](https://github.com/nkarasiak/qgis-mcp/tree/8a23eb05449d5dcdadaa0df032b6a17b2c859443),
identified as version 0.15.3. The commit archive was downloaded from
`https://codeload.github.com/nkarasiak/qgis-mcp/zip/8a23eb05449d5dcdadaa0df032b6a17b2c859443`.
Its SHA-256 is
`8f8c9eb2c7998de34afdae89c4f90bdf0250d89adc572473884dbea268de5fbb`.
Extraction checked for path traversal. The source was reviewed offline; no
third-party code was installed or executed.

Codex Security scan `fcc61218-9e4d-4737-9c18-cac5aaa512d4` completed on
20 November 2026 using GPT-6 Sol Ultra, as authorised for this single scan.
Its canonical report and threat model are retained in the local Codex Security
workbench under that scan ID; this note retains the portable research result.
The scan used static source and upstream test inspection. There was no live
QGIS test, WCC data access, dependency advisory audit or HTTP deployment test.

## System and trust boundaries

```text
MCP client or model
    │ tool call and returned data
    ▼
Python MCP bridge (stdio by default; optional streamable HTTP)
    │ framed JSON over local TCP, normally localhost:9876
    ▼
QGIS plugin inside the QGIS user's process
    │ PyQGIS commands
    ▼
Open project, layers, files, settings and saved data connections
```

The bridge is [a FastMCP server with optional HTTP
transport](https://github.com/nkarasiak/qgis-mcp/blob/8a23eb05449d5dcdadaa0df032b6a17b2c859443/src/qgis_mcp/server.py#L3584-L3589).
The normal QGIS UI [creates its socket server without a host
override](https://github.com/nkarasiak/qgis-mcp/blob/8a23eb05449d5dcdadaa0df032b6a17b2c859443/qgis_mcp_plugin/plugin.py#L369-L377),
so the plugin's default `localhost` bind applies. The listener is a separate
trust boundary: other local processes can talk to it without going through
the MCP bridge or its tool annotations. The plugin includes a command that
[runs supplied Python inside
QGIS](https://github.com/nkarasiak/qgis-mcp/blob/8a23eb05449d5dcdadaa0df032b6a17b2c859443/qgis_mcp_plugin/handlers/system.py#L167-L218).

The protected assets would be a QGIS user's project, local files and spatial
data, and any saved database connections. WCC estate data is a possible future
asset, not data observed in this scan. The plausible attackers are a separate
local user or process able to reach the loopback port, and a lower-trust MCP
client or model induced to call a tool outside its intended task. Remote
attackers require an additional exposure path; none was observed.

The desired controls are: authenticate and authorise every caller at the
QGIS-side boundary; make read-only access a server-enforced capability; keep
credentials out of tool results; require an effective approval gate for writes;
and install only the reviewed code and dependencies. Client annotations and
natural-language instructions do not enforce these controls.

## Findings

| Finding | Evidence and precondition | Assessment for the prototype |
| --- | --- | --- |
| **High: unauthenticated local command socket** | The [token check runs only when `QGIS_MCP_TOKEN` is set](https://github.com/nkarasiak/qgis-mcp/blob/8a23eb05449d5dcdadaa0df032b6a17b2c859443/qgis_mcp_plugin/server.py#L537-L572); [the upstream documentation confirms the default is open to local processes](https://github.com/nkarasiak/qgis-mcp/blob/8a23eb05449d5dcdadaa0df032b6a17b2c859443/README.md#L373-L394). A running listener on a shared machine permits a different local account to invoke `execute_code` with the QGIS user's authority. | Do not connect the default server to the prototype. A strong token on both sides reduces cross-account risk but is not isolation from processes running as the same user. Prefer a per-user socket or equivalent OS control plus a QGIS-side command allowlist. |
| **Medium: confirmation is incomplete** | [Optional elicitation proceeds after `McpError`](https://github.com/nkarasiak/qgis-mcp/blob/8a23eb05449d5dcdadaa0df032b6a17b2c859443/src/qgis_mcp/server.py#L477-L522). [Feature write tools send commands without that helper](https://github.com/nkarasiak/qgis-mcp/blob/8a23eb05449d5dcdadaa0df032b6a17b2c859443/src/qgis_mcp/server.py#L1029-L1064). The client may have its own approval gate, but this was not tested. | A read-only prototype needs an enforced server-side allowlist. Do not treat `destructiveHint` or `QGIS_MCP_AUTO_CONFIRM=0` as sufficient for unattended use. |
| **Medium, conditional: raw layer source in metadata** | [`get_layer_info` returns `layer.source()`](https://github.com/nkarasiak/qgis-mcp/blob/8a23eb05449d5dcdadaa0df032b6a17b2c859443/qgis_mcp_plugin/handlers/layers.py#L222-L240), also through a [read-only MCP resource](https://github.com/nkarasiak/qgis-mcp/blob/8a23eb05449d5dcdadaa0df032b6a17b2c859443/src/qgis_mcp/server.py#L3360-L3367). The [connection handler recognises credentials in URIs and redacts them](https://github.com/nkarasiak/qgis-mcp/blob/8a23eb05449d5dcdadaa0df032b6a17b2c859443/qgis_mcp_plugin/handlers/connections.py#L57-L85). A credential-bearing layer URI was not observed, and provider-specific masking is untested. | Omit raw source URIs from model-facing results or apply provider-aware redaction. Test with synthetic credential-bearing layers before any live data is opened. |

The first two findings have high source-code confidence; the metadata finding
has medium confidence because its impact depends on an actual layer URI. A
local check found no process listening on TCP port 9876 at the time of review.
That observation does not establish the machine's later state.

## Controls observed and unresolved deployment risks

The plugin [refuses a non-loopback bind without a
token](https://github.com/nkarasiak/qgis-mcp/blob/8a23eb05449d5dcdadaa0df032b6a17b2c859443/qgis_mcp_plugin/server.py#L263-L279).
The ordinary UI does not offer such a bind. A custom non-loopback deployment
would send the token over a [plain TCP
socket](https://github.com/nkarasiak/qgis-mcp/blob/8a23eb05449d5dcdadaa0df032b6a17b2c859443/qgis_mcp_plugin/server.py#L281-L299)
and needs a separate network and transport review. The optional streamable
HTTP mode also needs its own authentication, exposure and SDK-default review
before use. Neither path was observed in the intended local setup.

The code limits frame sizes and clients, validates command names, and blocks
some high-risk operations through batch calls. Those are useful controls but
do not identify the caller or make the full tool surface read-only. In
particular, [compound tools preserve access to granular
actions](https://github.com/nkarasiak/qgis-mcp/blob/8a23eb05449d5dcdadaa0df032b6a17b2c859443/README.md#L341-L348),
so a client-side list of apparently harmless compound tools is not an
adequate read-only boundary.

The [documented bridge refresh command fetches a mutable `main.zip`
archive](https://github.com/nkarasiak/qgis-mcp/blob/8a23eb05449d5dcdadaa0df032b6a17b2c859443/README.md#L305-L314).
The declared MCP and Pydantic dependencies are version ranges in
[`pyproject.toml`](https://github.com/nkarasiak/qgis-mcp/blob/8a23eb05449d5dcdadaa0df032b6a17b2c859443/pyproject.toml#L1-L24).
Before any trial, pin the plugin and bridge to reviewed bytes, resolve
dependencies reproducibly and compare installed hashes. No dependency
vulnerability assessment is claimed here.

## Licence and reuse boundary

The upstream project [assigns separate
licences](https://github.com/nkarasiak/qgis-mcp/blob/8a23eb05449d5dcdadaa0df032b6a17b2c859443/README.md#L444-L449):
the [QGIS plugin is GNU GPL v2 or
later](https://github.com/nkarasiak/qgis-mcp/blob/8a23eb05449d5dcdadaa0df032b6a17b2c859443/qgis_mcp_plugin/LICENSE)
and the [MCP bridge is
MIT](https://github.com/nkarasiak/qgis-mcp/blob/8a23eb05449d5dcdadaa0df032b6a17b2c859443/src/qgis_mcp/LICENSE).
The MIT text permits reuse subject to retaining its copyright and licence
notice. A modified and distributed QGIS plugin needs a GPL-compatible
distribution and source code plan. These are component-level observations,
not a legal conclusion about a combined future product. The [GNU licence
FAQ](https://www.gnu.org/licenses/gpl-faq.en.html) explains
that communication over sockets often separates programs, but the substance
of their interaction can still matter. Review the actual design before
assigning its licence. The licences permit research and local modification;
they do not by themselves make the current integration safe or grant rights
to WCC datasets.

## Decision and follow-up evidence

The current third-party plugin should not be linked to live WCC material or
presented as a safe ChatGPT integration. A future design should start with
the minimum Warwickshire task, prove server-side read-only behaviour, remove
raw source URIs and arbitrary code execution from the exposed surface, and
review the resulting code and deployment. Record the exact client, its
approval behaviour, account access boundary and any tunnel or HTTP endpoint
before moving beyond local test data. Publication and CI remain disabled in
this repository pending review.

The scan was run under the user's one-scan, US$50 paid-credit authorisation.
The local scan record has token usage but no per-scan billed amount; the
account's paid-credit balance did not fall in the observations made during
the scan. This is not a hard billing cap or a zero-cost guarantee.
