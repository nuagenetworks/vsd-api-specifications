{
    "attributes": {
        "assocEgressQosId": {
            "description": "ID of object associated with this QoS object", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "name": {
            "description": "A unique name of the QoS object", 
            "format": "free", 
            "filterable": true, 
            "uniqueScope": "no", 
            "required": true, 
            "exposed": true, 
            "orderable": true, 
            "type": "string"
        }, 
        "queue4AssociatedRateLimiterID": {
            "description": "ID of the queue4 rate limiter associated with this Egress QOS policy.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "queue1AssociatedRateLimiterID": {
            "description": "ID of the queue1 rate limiter associated with this Egress QOS policy.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "queue2AssociatedRateLimiterID": {
            "description": "ID of the queue2 rate limiter associated with this Egress QOS policy.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "queue2ForwardingClasses": {
            "description": "Queue2 Forwarding Classes for this Egress QOS Policy Possible values are NONE, A, B, C, D, E, F, G, H, .", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "allowed_choices": [
                "D", 
                "E", 
                "F", 
                "G", 
                "A", 
                "B", 
                "C", 
                "H", 
                "NONE"
            ], 
            "orderable": true, 
            "type": "enum"
        }, 
        "queue3ForwardingClasses": {
            "description": "Queue3 Forwarding Classes for this Egress QOS Policy Possible values are NONE, A, B, C, D, E, F, G, H, .", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "allowed_choices": [
                "D", 
                "E", 
                "F", 
                "G", 
                "A", 
                "B", 
                "C", 
                "H", 
                "NONE"
            ], 
            "orderable": true, 
            "type": "enum"
        }, 
        "queue4ForwardingClasses": {
            "description": "Queue4 Forwarding Classes for this Egress QOS Policy Possible values are NONE, A, B, C, D, E, F, G, H, .", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "allowed_choices": [
                "D", 
                "E", 
                "F", 
                "G", 
                "A", 
                "B", 
                "C", 
                "H", 
                "NONE"
            ], 
            "orderable": true, 
            "type": "enum"
        }, 
        "queue3AssociatedRateLimiterID": {
            "description": "ID of the queue3 rate limiter associated with this Egress QOS policy.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "parentQueueAssociatedRateLimiterID": {
            "description": "ID of the parent rate limiter associated with this Egress QOS policy.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "assocEgressQos": {
            "description": "Object associated with this Qos object.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "queue1ForwardingClasses": {
            "description": "Queue1 Forwarding Classes for this Egress QOS Policy Possible values are NONE, A, B, C, D, E, F, G, H, .", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "allowed_choices": [
                "D", 
                "E", 
                "F", 
                "G", 
                "A", 
                "B", 
                "C", 
                "H", 
                "NONE"
            ], 
            "orderable": true, 
            "type": "enum"
        }, 
        "description": {
            "description": "A description of the QoS object", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }
    }, 
    "model": {
        "resource_name": "egressqospolicies", 
        "description": "The object manipulates Egress QoS parameters attached to a Access Port / VLAN or Network port", 
        "entity_name": "EgressQOSPolicy", 
        "package": "policy/qos", 
        "get": true, 
        "update": true, 
        "rest_name": "egressqospolicy", 
        "extends": [
            "@base", 
            "@metadata"
        ], 
        "delete": true
    }
}