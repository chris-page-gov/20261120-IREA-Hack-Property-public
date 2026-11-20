---
type: Planning Site
title: Avon Valley School application site
"@id": "urn:okf:irea-property:avon-valley:planning-site"
sources:
  - id: register
    resource: https://planning.warwickshire.gov.uk/swiftlg/apas/run/WPHAPPDETAIL.DisplayUrl?theApnID=RBC%2F26CC001
  - id: plan
    resource: https://planning.warwickshire.gov.uk/swiftlg/apas/run/WCHDISPLAYMEDIA.showImage?theSeqNo=27604&theApnkey=8411&theModule=1
  - id: notice
    resource: https://planning.warwickshire.gov.uk/swiftlg/apas/run/WCHDISPLAYMEDIA.showImage?theSeqNo=29034&theApnkey=8411&theModule=1
  - id: os-openmap-local
    resource: https://www.ordnancesurvey.co.uk/products/os-open-map-local
observed_on: "2026-11-18"
site_reference_status: Local example identifier
geometry_status: Indicative vector derived from approved drawing P08
---

# Site identification

The [application](application.md) identifies Avon Valley School on Newbold
Road, Rugby, CV21 1EH. This matches the school name, street and postcode of
the [estate asset](asset.md). The [UPRN](uprn.md) comes from the asset and
OS records. The match associates the estate record with this planning site
at school level.[^register]

Condition 2 of the [decision](decision.md) lists approved drawing
`XXXX-CWA-ZZ-00-D-A-0101` revision P08. The plan shows a red application
boundary within a separately shown blue landownership boundary. It labels
the red-line site area approximately **8,573 m²**. The site IRI in this
example is local.[^plan][^notice]

## Boundary and point check

**UPRN 100071399702 falls outside the P08 red line in the indicative
overlay, about 59 m from its nearest edge.** The estate workbook point
also falls outside, about 56 m from the edge. Both reference points are
in British National Grid (EPSG:27700). The school name and address still
support the documentary association with the application.[^plan][^os-openmap-local][^uprn]

On 18 November 2026, GIS AI GO confirmed the October 2026 release of OS
Open UPRN through live product metadata. The WebMCP Explorer offered no
planning polygon lookup or spatial overlay, and the v0.2 catalogue search
returned a connection error. The UPRN coordinates came from the local
OS CSV. The council case register, public Compass layer list and exact
Planning Data reference searches yielded no source GIS polygon. The
published WFS endpoint returned HTTP 404. WCC's internal planning GIS
coverage remains unverified.[^os-product][^register][^compass][^wfs][^national]

The calculation used the red vector stroke embedded on page 1 of the
approved PDF. Its 273 segments form a valid closed polygon. At the
drawing's 1:500 scale its area is 8,573.3 m², consistent with the plan
label. A similarity transform fitted eight existing building corners
to OS OpenMap Local in British National Grid. The fit residual was
0.84 m RMS. Omitting each control in turn put the UPRN outside by
58.1 to 59.8 m. These checks measure fit consistency with the mapped
building and give an indicative distance for this drawing.[^plan][^os-openmap-local]

The [case record](case.json) contains the control pairs, transform,
receipt and point-in-polygon results. The local
[review GeoPackage](../snapshots/2026-11-18/avon-valley-school/rbc-26cc001-review.gpkg)
contains the derived red line and two source points. In Thursday’s review,
compare it with the planning-system polygon for the same application and
drawing revision. Check the drawing rights before sharing the derived layer.
Contains OS data © Crown copyright and database rights 2026.

[^register]: [WCC public planning case](https://planning.warwickshire.gov.uk/swiftlg/apas/run/WPHAPPDETAIL.DisplayUrl?theApnID=RBC%2F26CC001).
[^plan]: [Approved proposed site plan, P08, page 1](https://planning.warwickshire.gov.uk/swiftlg/apas/run/WCHDISPLAYMEDIA.showImage?theSeqNo=27604&theApnkey=8411&theModule=1).
[^notice]: [Issued notice, condition 2 on pages 1–2](https://planning.warwickshire.gov.uk/swiftlg/apas/run/WCHDISPLAYMEDIA.showImage?theSeqNo=29034&theApnkey=8411&theModule=1).
[^os-openmap-local]: [OS OpenMap Local](https://www.ordnancesurvey.co.uk/products/os-open-map-local), SP tile, feature `157054EC-FAD2-4B18-9670-DFEE01FB175F` in `SP_Building`.
[^uprn]: [OS UPRN reference point](uprn.md) and [estate workbook reference point](asset.md).
[^os-product]: [Ordnance Survey live product metadata endpoint](https://api.os.uk/downloads/v1/products/OpenUPRN).
[^compass]: [WCC Compass public layer list](https://maps.warwickshire.gov.uk/inspire/layers.json).
[^wfs]: [WCC public GIS services](https://www.warwickshire.gov.uk/data-council-services/web-map-gis-services/2).
[^national]: [Planning Data application query](https://www.planning.data.gov.uk/entity.json?dataset=planning-application&reference=RBC%2F26CC001&limit=1) and [site query](https://www.planning.data.gov.uk/entity.json?dataset=site&reference=RBC%2F26CC001&limit=1).
