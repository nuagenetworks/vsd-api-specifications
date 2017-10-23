{
    "attributes": [
        {
            "description": "Map&lt;TCAMetric, Long[]&gt; TCAMetric is an Enum. Possible values are packets_in, bytes_in, packets_in_dropped, packets_in_errors, packets_out, bytes_out, packets_out_dropped, packeMaprs, packets_dropped_rate_limit",
            "exposed": true,
            "name": "data",
            "subtype": "object",
            "type": "list",
            "uniqueScope": "no"
        },
        {
            "description": "End time for the statistics to be retrieved",
            "exposed": true,
            "name": "endTime",
            "subtype": "long",
            "type": "integer",
            "uniqueScope": "no"
        },
        {
            "description": "Number of data points between start time and end time",
            "exposed": true,
            "name": "numberOfDataPoints",
            "type": "integer",
            "uniqueScope": "no"
        },
        {
            "description": "Version of this Sequence number.",
            "exposed": true,
            "name": "version",
            "subtype": "long",
            "type": "integer",
            "uniqueScope": "no"
        },
        {
            "description": "Start time for the statistics to be retrieved",
            "exposed": true,
            "name": "startTime",
            "subtype": "long",
            "type": "integer",
            "uniqueScope": "no"
        }
    ],
    "children": [],
    "model": {
        "description": "Retrieves the statistics for a particular Entity and its immediate child entity.",
        "entity_name": "BulkStatistics",
        "extends": [
            "@metadata"
        ],
        "package": "stats",
        "resource_name": "bulkstatistics",
        "rest_name": "bulkstatistics",
        "userlabel": "Bulk Statistics"
    }
}