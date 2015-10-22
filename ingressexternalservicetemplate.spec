{
    "attributes": {
        "description": {
            "description": "A description of the entity", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "priorityType": {
            "description": "", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "enum"
        }, 
        "priority": {
            "description": "The priority of the ACL entry that determines the order of entries", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "integer"
        }, 
        "associatedLiveEntityID": {
            "description": "In the draft mode, the ACL entry refers to this LiveEntity. In non-drafted mode, this is null.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "active": {
            "description": "If enabled, it means that this ACL or QOS entry is active", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "boolean"
        }, 
        "policyState": {
            "description": "", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "enum"
        }, 
        "name": {
            "description": "The name of the entity", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }
    }, 
    "model": {
        "resource_name": "ingressexternalservicetemplates", 
        "description": "Defines the template for an Ingress External Service Acls", 
        "entity_name": "IngressExternalServiceTemplate", 
        "package": "policy/acl", 
        "get": true, 
        "update": true, 
        "rest_name": "ingressexternalservicetemplate", 
        "extends": [
            "@base", 
            "@metadata"
        ], 
        "delete": true
    }, 
    "children": {
        "job": {
            "create": true, 
            "relationship": "child"
        }, 
        "ingressexternalserviceentrytemplate": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }
    }
}