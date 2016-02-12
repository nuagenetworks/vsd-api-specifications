{
    "attributes": {
        "URLEndPoint": {
            "description": "URL endpoint to post Alarm data to when TCA is triggered",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "description": {
            "description": "Desription of the TCA",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 255,
            "min_length": 1,
            "type": "string",
            "uniqueScope": "no"
        },
        "metric": {
            "allowed_choices": [
                "ADDRESS_MAP_EGRESS_PKT_CNT",
                "ADDRESS_MAP_INGRESS_BYTE_CNT",
                "ADDRESS_MAP_INGRESS_PKT_CNT",
                "BYTES_IN",
                "BYTES_OUT",
                "EGRESS_BYTE_COUNT",
                "EGRESS_PACKET_COUNT",
                "INGRESS_BYTE_COUNT",
                "INGRESS_PACKET_COUNT",
                "PACKETS_DROPPED_BY_RATE_LIMIT",
                "PACKETS_IN",
                "PACKETS_IN_DROPPED",
                "PACKETS_IN_ERROR",
                "PACKETS_OUT",
                "PACKETS_OUT_DROPPED",
                "PACKETS_OUT_ERROR"
            ],
            "description": "The metric associated with the TCA - PACKETS_IN, BYTES_IN, PACKETS_IN_DROPPED, PACKETS_IN_ERROR, PACKETS_OUT, BYTES_OUT PACKETS_OUT_DROPPED, PACKETS_OUT_ERROR and PACKETS_DROPPED_BY_RATE_LIMIT Possible values are PACKETS_IN, BYTES_IN, PACKETS_IN_DROPPED, PACKETS_IN_ERROR, PACKETS_OUT, BYTES_OUT, PACKETS_OUT_DROPPED, PACKETS_OUT_ERROR, PACKETS_DROPPED_BY_RATE_LIMIT, INGRESS_BYTE_COUNT, INGRESS_PACKET_COUNT, EGRESS_BYTE_COUNT, EGRESS_PACKET_COUNT, .",
            "exposed": true,
            "required": true,
            "type": "enum",
            "uniqueScope": "no"
        },
        "name": {
            "description": "The name of the TCA",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 255,
            "min_length": 1,
            "orderable": true,
            "required": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "period": {
            "description": "The averaging period",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "min_value": 1,
            "orderable": true,
            "required": true,
            "subtype": "long",
            "type": "integer",
            "uniqueScope": "no"
        },
        "scope": {
            "allowed_choices": [
                "GLOBAL",
                "LOCAL"
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
            "format": "free",
            "min_value": 1,
            "orderable": true,
            "required": true,
            "subtype": "long",
            "type": "integer",
            "uniqueScope": "no"
        },
        "type": {
            "allowed_choices": [
                "BREACH",
                "ROLLING_AVERAGE"
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
        "description": "Provides the definition of the Threshold Control Alarms.",
        "entity_name": "TCA",
        "extends": [
            "@audited",
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