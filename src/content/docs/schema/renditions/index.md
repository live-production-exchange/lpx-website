---
title: Rendition Properties
---

# Rendition Properties



Renditions provide the technical details about available feeds and how to access them.

| Property | Lvl 2 | Lvl 3 | Type | Description |
| --- | --- | --- | --- | --- |
| topic |  |  | String | Indicates subject of the event |
| renditions |  |  | Object | An array of objects, each of which is a rendition of the event |
|  | name |  | String | Live event rendition name |
|  | videoCodec |  | String | Rendition video codec |
|  | frameRate |  | String | Rendition frame rate |
|  | scanType |  | Enum | Rendition scan type. Values:“progressive”, “interlaced tff”, “interlaced bff” |
|  | aspectRatio |  | String | Rendition aspect ratio |
|  | width |  | Int | Rendition frame width |
|  | height |  | Int | Rendition frame height |
|  | bitrate |  | Int |  |
|  | transportProtocol |  | String | Rendition delivery protocol |
|  | href |  | String |  |