---
title: Event Properties
---

# Event Properties



These properties provide the details for the event the live feed provides

| Property | Lvl 2 | Lvl 3 | Type | Description |
| --- | --- | --- | --- | --- |
| eventDetails |  |  | Object | A container for properties related to a planned event |
|  | dates |  | Object | A container for properties related to dates and times for this event. |
|  |  | startDate | DateTime | Date and time of start of event |
|  |  | endDate | DateTime | Date and time of end of event |
|  |  | expectedStartDate | Truncated DateTime | Expected start date and time (can be truncated) |
|  |  | expectedEndDate | Truncated DateTime | Expected end date and time (can be truncated) |
|  | eventStatus |  | String | Current status of live event. Suggested values are from: <https://cv.iptc.org/newscodes/eventstatus/> |
|  | planned CoverageStatus |  | String | Status of planned coverage. Suggested  values are from: <https://cv.iptc.org/newscodes/eventoccurstatus/> |