{
    "attributes": [
        {
            "name": "data",
            "type": "list",
            "subtype": "object",
            "description": "Map&lt;TCAMetric, Long[]&gt; TCAMetric is an Enum. Possible values are packets_in, bytes_in, packets_in_dropped, packets_in_errors, packets_out, bytes_out, packets_out_dropped, packeMaprs, packets_dropped_rate_limit",
            "exposed": true,
            "uniqueScope": "no"
        },
        {
            "name": "endTime",
            "type": "integer",
            "subtype": "long",
            "description": "End time for the statistics to be retrieved",
            "exposed": true,
            "uniqueScope": "no"
        },
        {
            "name": "numberOfDataPoints",
            "type": "integer",
            "description": "Number of data points between start time and end time",
            "exposed": true,
            "uniqueScope": "no"
        },
        {
            "name": "version",
            "type": "integer",
            "subtype": "long",
            "description": "Version of this Sequence number.",
            "exposed": true,
            "uniqueScope": "no"
        },
        {
            "name": "startTime",
            "type": "integer",
            "subtype": "long",
            "description": "Start time for the statistics to be retrieved",
            "exposed": true,
            "uniqueScope": "no"
        }
    ],
    "children": [

    ],
    "model": {
        "description": "Retrieves the statistics for a particular Entity and its immediate child entity.",
        "entity_name": "BulkStatistics",
        "extends": [
            "@metadata"
        ],
        "package": "stats",
        "resource_name": "bulkstatistics",
        "rest_name": "bulkstatistics"
    }
}