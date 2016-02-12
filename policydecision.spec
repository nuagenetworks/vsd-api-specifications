{
    "attributes": {
        "egressACLs": {
            "description": "List of actual Egress ACLs that will be applied on the interface of this VM",
            "exposed": true,
            "format": "free",
            "subtype": "object",
            "type": "list",
            "uniqueScope": "no"
        },
        "egressQos": {
            "description": "Egress QoS primitive that was selected",
            "exposed": true,
            "format": "free",
            "type": "object",
            "uniqueScope": "no"
        },
        "fipACLs": {
            "description": "List of actual Egress ACLs that will be applied on the interface of this VM",
            "exposed": true,
            "format": "free",
            "subtype": "object",
            "type": "list",
            "uniqueScope": "no"
        },
        "ingressACLs": {
            "description": "List of actual Ingress ACLs that will be applied on the interface of this VM",
            "exposed": true,
            "format": "free",
            "subtype": "object",
            "type": "list",
            "uniqueScope": "no"
        },
        "ingressAdvFwd": {
            "description": "List of actual Ingress Redirect ACLs that will be applied on the interface of this VM",
            "exposed": true,
            "format": "free",
            "subtype": "object",
            "type": "list",
            "uniqueScope": "no"
        },
        "ingressExternalServiceACLs": {
            "description": "List of actual Ingress External Service ACLs that will be applied on the interface of this VM",
            "exposed": true,
            "format": "free",
            "subtype": "object",
            "type": "list",
            "uniqueScope": "no"
        },
        "qos": {
            "description": "QoS primitive that was selected based on inheritance policies",
            "exposed": true,
            "format": "free",
            "type": "object",
            "uniqueScope": "no"
        },
        "stats": {
            "description": "Stats primitive that was selected based on inheritance policies",
            "exposed": true,
            "format": "free",
            "type": "object",
            "uniqueScope": "no"
        }
    },
    "children": {
        "qos": {
            "get": true,
            "relationship": "child"
        }
    },
    "model": {
        "description": "This object is a read only object that provides the policy decisions for a particular VM interface.",
        "entity_name": "PolicyDecision",
        "extends": [
            "@audited",
            "@base",
            "@metadata"
        ],
        "get": true,
        "package": "policy",
        "resource_name": "policydecisions",
        "rest_name": "policydecision"
    }
}