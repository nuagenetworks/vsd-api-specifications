{
    "attributes": {
        "URLEndPoint": {
            "description": "URL endpoint to post Alarm data to when TCA is triggered",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        },
        "description": {
            "description": "Desription of the TCA",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": false,
            "type": "string",
            "min_length": 1,
            "max_length": 255,
            "uniqueScope": "no"
        },
        "metric": {
            "allowed_choices": [
                "BYTES_IN",
                "EGRESS_BYTE_COUNT",
                "PACKETS_IN_ERROR",
                "PACKETS_OUT_DROPPED",
                "BYTES_OUT",
                "PACKETS_IN_DROPPED",
                "INGRESS_BYTE_COUNT",
                "PACKETS_IN",
                "PACKETS_OUT_ERROR",
                "PACKETS_DROPPED_BY_RATE_LIMIT",
                "INGRESS_PACKET_COUNT",
                "PACKETS_OUT",
                "EGRESS_PACKET_COUNT"
            ],
            "description": "The metric associated with the TCA - PACKETS_IN, BYTES_IN, PACKETS_IN_DROPPED, PACKETS_IN_ERROR, PACKETS_OUT, BYTES_OUT PACKETS_OUT_DROPPED, PACKETS_OUT_ERROR and PACKETS_DROPPED_BY_RATE_LIMIT Possible values are PACKETS_IN, BYTES_IN, PACKETS_IN_DROPPED, PACKETS_IN_ERROR, PACKETS_OUT, BYTES_OUT, PACKETS_OUT_DROPPED, PACKETS_OUT_ERROR, PACKETS_DROPPED_BY_RATE_LIMIT, INGRESS_BYTE_COUNT, INGRESS_PACKET_COUNT, EGRESS_BYTE_COUNT, EGRESS_PACKET_COUNT, .",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "required": true,
            "type": "enum",
            "uniqueScope": "no"
        },
        "name": {
            "description": "The name of the TCA",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "required": true,
            "type": "string",
            "min_length": 1,
            "max_length": 255,
            "uniqueScope": "no"
        },
        "period": {
            "description": "The averaging period",
            "exposed": true,
            "filterable": true,
            "format": "long",
            "orderable": true,
            "required": true,
            "type": "integer",
            "min_value": 1,
            "uniqueScope": "no"
        },
        "scope": {
            "allowed_choices": [
                "LOCAL",
                "GLOBAL"
            ],
            "description": "GLOBAL or LOCAL scope. Global refers to aggregate values across subnets, zones or domains. Local refers to traffic from/to individual VMs Possible values are GLOBAL, LOCAL, .",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "required": true,
            "type": "enum",
            "uniqueScope": "no"
        },
        "threshold": {
            "description": "The threshold that must be exceeded before an alarm is issued",
            "exposed": true,
            "filterable": true,
            "format": "long",
            "orderable": true,
            "required": true,
            "type": "integer",
            "min_value": 1,
            "uniqueScope": "no"
        },
        "type": {
            "allowed_choices": [
                "ROLLING_AVERAGE",
                "BREACH"
            ],
            "description": "Rolling average or sequence of samples over the averaging period - ROLLING_AVERAGE or BREACH Possible values are ROLLING_AVERAGE, BREACH, .",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "required": true,
            "type": "enum",
            "uniqueScope": "no"
        }
    },
    "children": {
        "alarm": {
            "create": true,
            "get": true,
            "relationship": "child"
        },
        "eventlog": {
            "get": true,
            "relationship": "child"
        }
    },
    "model": {
        "delete": true,
        "description": "Provides the definition of the Threshold Control Alarms",
        "entity_name": "TCA",
        "extends": [
            "@base",
            "@metadata"
        ],
        "get": true,
        "package": "stats",
        "resource_name": "tcas",
        "rest_name": "tca",
        "update": true
    }
}