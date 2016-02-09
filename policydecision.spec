{
    "attributes": {
        "egressACLs": {
            "description": "List of actual Egress ACLs that will be applied on the interface of this VM",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "list",
            "subtype": "object",
            "uniqueScope": "no"
        },
        "egressQos": {
            "description": "Egress QoS primitive that was selected",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "object",
            "uniqueScope": "no"
        },
        "fipACLs": {
            "description": "List of actual Egress ACLs that will be applied on the interface of this VM",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "list",
            "subtype": "object",
            "uniqueScope": "no"
        },
        "ingressACLs": {
            "description": "List of actual Ingress ACLs that will be applied on the interface of this VM",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "list",
            "subtype": "object",
            "uniqueScope": "no"
        },
        "ingressAdvFwd": {
            "description": "List of actual Ingress Redirect ACLs that will be applied on the interface of this VM",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "list",
            "subtype": "object",
            "uniqueScope": "no"
        },
        "ingressExternalServiceACLs": {
            "description": "List of actual Ingress External Service ACLs that will be applied on the interface of this VM",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "list",
            "subtype": "object",
            "uniqueScope": "no"
        },
        "qos": {
            "description": "QoS primitive that was selected based on inheritance policies",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "object",
            "uniqueScope": "no"
        },
        "stats": {
            "description": "Stats primitive that was selected based on inheritance policies",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
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
        "description": "This object is a read only object that provides the policy decisions for a particular VM interface",
        "entity_name": "PolicyDecision",
        "extends": [
            "@base",
            "@audited",
            "@metadata"
        ],
        "get": true,
        "package": "policy",
        "resource_name": "policydecisions",
        "rest_name": "policydecision"
    }
}