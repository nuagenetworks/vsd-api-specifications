{
    "attributes": {
        "active": {
            "description": "If enabled, it means that this ACL or QOS entry is active", 
            "exposed": true, 
            "type": "boolean", 
            "uniqueScope": "no"
        }, 
        "associatedLiveEntityID": {
            "description": "In the draft mode, the ACL entry refers to this LiveEntity. In non-drafted mode, this is null.", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "description": {
            "description": "A description of the entity", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "name": {
            "description": "The name of the entity", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "policyState": {
            "description": "", 
            "exposed": true, 
            "type": "enum", 
            "uniqueScope": "no"
        }, 
        "priority": {
            "description": "The priority of the ACL entry that determines the order of entries", 
            "exposed": true, 
            "type": "integer", 
            "uniqueScope": "no"
        }, 
        "priorityType": {
            "description": "", 
            "exposed": true, 
            "type": "enum", 
            "uniqueScope": "no"
        }
    }, 
    "children": {
        "ingressexternalserviceentrytemplate": {
            "create": true, 
            "get": true, 
            "relationship": "child"
        }, 
        "job": {
            "create": true, 
            "relationship": "child"
        }
    }, 
    "delete": true, 
    "description": "Defines the template for an Ingress External Service Acls", 
    "entity_name": "IngressExternalServiceTemplate", 
    "extends": [
        "@base", 
        "@metadata"
    ], 
    "get": true, 
    "package": "/policy/acl", 
    "resource_name": "ingressexternalservicetemplates", 
    "rest_name": "ingressexternalservicetemplate", 
    "update": true
}