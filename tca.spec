{
    "attributes": {
        "description": {
            "description": "Desription of the TCA", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "metric": {
            "required": true, 
            "description": "The metric associated with the TCA - PACKETS_IN, BYTES_IN, PACKETS_IN_DROPPED, PACKETS_IN_ERROR, PACKETS_OUT, BYTES_OUT PACKETS_OUT_DROPPED, PACKETS_OUT_ERROR and PACKETS_DROPPED_BY_RATE_LIMIT Possible values are PACKETS_IN, BYTES_IN, PACKETS_IN_DROPPED, PACKETS_IN_ERROR, PACKETS_OUT, BYTES_OUT, PACKETS_OUT_DROPPED, PACKETS_OUT_ERROR, PACKETS_DROPPED_BY_RATE_LIMIT, INGRESS_BYTE_COUNT, INGRESS_PACKET_COUNT, EGRESS_BYTE_COUNT, EGRESS_PACKET_COUNT, .", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
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
            "orderable": true, 
            "type": "enum"
        }, 
        "period": {
            "description": "The averaging period", 
            "format": "free", 
            "filterable": true, 
            "uniqueScope": "no", 
            "required": true, 
            "exposed": true, 
            "orderable": true, 
            "type": "float"
        }, 
        "URLEndPoint": {
            "description": "URL endpoint to post Alarm data to when TCA is triggered", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "threshold": {
            "description": "The threshold that must be exceeded before an alarm is issued", 
            "format": "free", 
            "filterable": true, 
            "uniqueScope": "no", 
            "required": true, 
            "exposed": true, 
            "orderable": true, 
            "type": "float"
        }, 
        "scope": {
            "required": true, 
            "description": "GLOBAL or LOCAL scope. Global refers to aggregate values across subnets, zones or domains. Local refers to traffic from/to individual VMs Possible values are GLOBAL, LOCAL, .", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "allowed_choices": [
                "LOCAL", 
                "GLOBAL"
            ], 
            "orderable": true, 
            "type": "enum"
        }, 
        "type": {
            "required": true, 
            "description": "Rolling average or sequence of samples over the averaging period - ROLLING_AVERAGE or BREACH Possible values are ROLLING_AVERAGE, BREACH, .", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "allowed_choices": [
                "ROLLING_AVERAGE", 
                "BREACH"
            ], 
            "orderable": true, 
            "type": "enum"
        }, 
        "name": {
            "description": "The name of the TCA", 
            "format": "free", 
            "filterable": true, 
            "uniqueScope": "no", 
            "required": true, 
            "exposed": true, 
            "orderable": true, 
            "type": "string"
        }
    }, 
    "model": {
        "resource_name": "tcas", 
        "description": "Provides the definition of the Threshold Control Alarms", 
        "entity_name": "TCA", 
        "package": "stats", 
        "get": true, 
        "update": true, 
        "rest_name": "tca", 
        "extends": [
            "@base", 
            "@metadata"
        ], 
        "delete": true
    }, 
    "children": {
        "alarm": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }, 
        "eventlog": {
            "relationship": "child", 
            "get": true
        }
    }
}