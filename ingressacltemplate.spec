{
    "attributes": {
        "active": {
            "description": "If enabled, it means that this ACL or QOS entry is active", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "boolean", 
            "uniqueScope": "no"
        }, 
        "allowL2AddressSpoof": {
            "description": "If enabled, it will disable the default anti-spoof ACL for this domain that essentially prevents any VM to send packets that do not originate from that particular VM", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "boolean", 
            "uniqueScope": "no"
        }, 
        "assocAclTemplateId": {
            "description": "ID of the ACL template associated with this ACL template", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "associatedLiveEntityID": {
            "description": "In the draft mode, the ACL entry refers to this LiveEntity. In non-drafted mode, this is null.", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "defaultAllowIP": {
            "description": "If enabled a default ACL of Allow All is added as the last entry in the list of ACL entries", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "boolean", 
            "uniqueScope": "no"
        }, 
        "defaultAllowNonIP": {
            "description": "If enabled, non ip traffic will be dropped", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "boolean", 
            "uniqueScope": "no"
        }, 
        "description": {
            "description": "A description of the entity", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "name": {
            "description": "The name of the entity", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "required": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "policyState": {
            "description": "", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "enum", 
            "uniqueScope": "no"
        }, 
        "priority": {
            "description": "The priority of the ACL entry that determines the order of entries", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "integer", 
            "uniqueScope": "no"
        }, 
        "priorityType": {
            "description": "", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "enum", 
            "uniqueScope": "no"
        }
    }, 
    "children": {
        "eventlog": {
            "get": true, 
            "relationship": "child"
        }, 
        "ingressaclentrytemplate": {
            "create": true, 
            "get": true, 
            "relationship": "child"
        }, 
        "job": {
            "create": true, 
            "relationship": "child"
        }, 
        "vm": {
            "get": true, 
            "relationship": "child"
        }
    }, 
    "delete": true, 
    "description": "Defines the template for an Ingress ACL", 
    "entity_name": "IngressACLTemplate", 
    "extends": [
        "@base", 
        "@metadata"
    ], 
    "get": true, 
    "package": "/policy/acl", 
    "resource_name": "ingressacltemplates", 
    "rest_name": "ingressacltemplate", 
    "update": true
}