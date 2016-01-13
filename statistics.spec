{
    "attributes": {
        "endTime": {
            "description": "End time for the statistics to be retrieved",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "float",
            "uniqueScope": "no"
        },
        "numberOfDataPoints": {
            "description": "Number of data points between start time and end time",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "integer",
            "uniqueScope": "no"
        },
        "startTime": {
            "description": "Start time for the statistics to be retrieved",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "float",
            "uniqueScope": "no"
        },
        "statsData": {
            "description": "Map&lt;TCAMetric, Long[]&gt; TCAMetric is an Enum. Possible values are packets_in, bytes_in, packets_in_dropped, packets_in_errors, packets_out, bytes_out, packets_out_dropped, packets_out_errors, packets_dropped_rate_limit",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        },
        "version": {
            "description": "Version of this Sequence number.",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "float",
            "uniqueScope": "no"
        }
    },
    "model": {
        "description": "Retrieves the statistics for a particular domain, zone, subnet, or VM",
        "entity_name": "Statistics",
        "extends": [
            "@base",
            "@metadata"
        ],
        "package": "stats",
        "resource_name": "statistics",
        "rest_name": "statistics"
    }
}