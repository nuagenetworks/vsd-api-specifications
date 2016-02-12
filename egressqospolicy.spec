{
    "attributes": {
        "assocEgressQosId": {
            "description": "ID of object associated with this QoS object",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "description": {
            "description": "A description of the QoS object",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 255,
            "type": "string",
            "uniqueScope": "no"
        },
        "name": {
            "description": "A unique name of the QoS object",
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
        "parentQueueAssociatedRateLimiterID": {
            "description": "ID of the parent rate limiter associated with this Egress QOS policy.",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "queue1AssociatedRateLimiterID": {
            "description": "ID of the queue1 rate limiter associated with this Egress QOS policy.",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "queue1ForwardingClasses": {
            "allowed_choices": [
                "A",
                "B",
                "C",
                "D",
                "E",
                "F",
                "G",
                "H",
                "NONE"
            ],
            "description": "Queue1 Forwarding Classes for this Egress QOS Policy Possible values are NONE, A, B, C, D, E, F, G, H, .",
            "exposed": true,
            "format": "free",
            "subtype": "enum",
            "type": "list",
            "uniqueScope": "no"
        },
        "queue2AssociatedRateLimiterID": {
            "description": "ID of the queue2 rate limiter associated with this Egress QOS policy.",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "queue2ForwardingClasses": {
            "allowed_choices": [
                "A",
                "B",
                "C",
                "D",
                "E",
                "F",
                "G",
                "H",
                "NONE"
            ],
            "description": "Queue2 Forwarding Classes for this Egress QOS Policy Possible values are NONE, A, B, C, D, E, F, G, H, .",
            "exposed": true,
            "format": "free",
            "subtype": "enum",
            "type": "list",
            "uniqueScope": "no"
        },
        "queue3AssociatedRateLimiterID": {
            "description": "ID of the queue3 rate limiter associated with this Egress QOS policy.",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "queue3ForwardingClasses": {
            "allowed_choices": [
                "A",
                "B",
                "C",
                "D",
                "E",
                "F",
                "G",
                "H",
                "NONE"
            ],
            "description": "Queue3 Forwarding Classes for this Egress QOS Policy Possible values are NONE, A, B, C, D, E, F, G, H, .",
            "exposed": true,
            "format": "free",
            "subtype": "enum",
            "type": "list",
            "uniqueScope": "no"
        },
        "queue4AssociatedRateLimiterID": {
            "description": "ID of the queue4 rate limiter associated with this Egress QOS policy.",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "queue4ForwardingClasses": {
            "allowed_choices": [
                "A",
                "B",
                "C",
                "D",
                "E",
                "F",
                "G",
                "H",
                "NONE"
            ],
            "description": "Queue4 Forwarding Classes for this Egress QOS Policy Possible values are NONE, A, B, C, D, E, F, G, H, .",
            "exposed": true,
            "format": "free",
            "subtype": "enum",
            "type": "list",
            "uniqueScope": "no"
        }
    },
    "model": {
        "delete": true,
        "description": "The object manipulates Egress QoS parameters attached to a Access Port / VLAN or Network port.",
        "entity_name": "EgressQOSPolicy",
        "extends": [
            "@audited",
            "@base",
            "@metadata"
        ],
        "get": true,
        "package": "policy/qos",
        "resource_name": "egressqospolicies",
        "rest_name": "egressqospolicy",
        "update": true
    }
}