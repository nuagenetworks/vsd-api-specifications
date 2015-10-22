{
    "attributes": {
        "statsData": {
            "description": "Map&lt;TCAMetric, Long[]&gt; TCAMetric is an Enum. Possible values are packets_in, bytes_in, packets_in_dropped, packets_in_errors, packets_out, bytes_out, packets_out_dropped, packets_out_errors, packets_dropped_rate_limit", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "version": {
            "description": "Version of this Sequence number.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "float"
        }, 
        "endTime": {
            "description": "End time for the statistics to be retrieved", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "float"
        }, 
        "startTime": {
            "description": "Start time for the statistics to be retrieved", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "float"
        }, 
        "numberOfDataPoints": {
            "description": "Number of data points between start time and end time", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "integer"
        }
    }, 
    "model": {
        "resource_name": "statistics", 
        "description": "Retrieves the statistics for a particular domain, zone, subnet, or VM", 
        "entity_name": "Statistics", 
        "package": "stats", 
        "rest_name": "statistics", 
        "extends": [
            "@base", 
            "@metadata"
        ]
    }
}