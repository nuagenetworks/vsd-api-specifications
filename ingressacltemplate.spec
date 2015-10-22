{
    "attributes": {
        "assocAclTemplateId": {
            "description": "ID of the ACL template associated with this ACL template", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "description": {
            "description": "A description of the entity", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "allowL2AddressSpoof": {
            "description": "If enabled, it will disable the default anti-spoof ACL for this domain that essentially prevents any VM to send packets that do not originate from that particular VM", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "boolean"
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
        "defaultAllowNonIP": {
            "description": "If enabled, non ip traffic will be dropped", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "boolean"
        }, 
        "defaultAllowIP": {
            "description": "If enabled a default ACL of Allow All is added as the last entry in the list of ACL entries", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "boolean"
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
            "uniqueScope": "no", 
            "required": true, 
            "exposed": true, 
            "orderable": true, 
            "type": "string"
        }
    }, 
    "model": {
        "resource_name": "ingressacltemplates", 
        "description": "Defines the template for an Ingress ACL", 
        "entity_name": "IngressACLTemplate", 
        "package": "policy/acl", 
        "get": true, 
        "update": true, 
        "rest_name": "ingressacltemplate", 
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
        "ingressaclentrytemplate": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }, 
        "vm": {
            "relationship": "child", 
            "get": true
        }, 
        "eventlog": {
            "relationship": "child", 
            "get": true
        }
    }
}