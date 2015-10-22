{
    "attributes": {
        "qos": {
            "description": "QoS primitive that was selected based on inheritance policies", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "ingressAdvFwd": {
            "description": "List of actual Ingress Redirect ACLs that will be applied on the interface of this VM", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "list"
        }, 
        "egressACLs": {
            "description": "List of actual Egress ACLs that will be applied on the interface of this VM", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "list"
        }, 
        "fipACLs": {
            "description": "List of actual Egress ACLs that will be applied on the interface of this VM", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "list"
        }, 
        "ingressExternalServiceACLs": {
            "description": "List of actual Ingress External Service ACLs that will be applied on the interface of this VM", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "list"
        }, 
        "egressQos": {
            "description": "Egress QoS primitive that was selected", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "stats": {
            "description": "Stats primitive that was selected based on inheritance policies", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "ingressACLs": {
            "description": "List of actual Ingress ACLs that will be applied on the interface of this VM", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "list"
        }
    }, 
    "model": {
        "resource_name": "policydecisions", 
        "description": "This object is a read only object that provides the policy decisions for a particular VM interface", 
        "entity_name": "PolicyDecision", 
        "package": "policy", 
        "get": true, 
        "rest_name": "policydecision", 
        "extends": [
            "@base", 
            "@metadata"
        ]
    }, 
    "children": {
        "qos": {
            "relationship": "child", 
            "get": true
        }
    }
}