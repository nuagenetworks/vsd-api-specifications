{
    "attributes": {
        "associatedDomainID": {
            "description": "Domain id where the application is running.", 
            "format": "free", 
            "filterable": true, 
            "uniqueScope": "no", 
            "required": true, 
            "exposed": true, 
            "orderable": true, 
            "type": "string"
        }, 
        "description": {
            "description": "Description of the application.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "associatedNetworkObjectType": {
            "description": "Type of network object this App is associated with (ENTERPRISE, DOMAIN) Refer to API section for supported types.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "enum"
        }, 
        "associatedDomainType": {
            "description": "Type of domain (DOMAIN, L2DOMAIN). Refer to API section for supported types.", 
            "format": "free", 
            "filterable": true, 
            "uniqueScope": "no", 
            "required": true, 
            "exposed": true, 
            "orderable": true, 
            "type": "enum"
        }, 
        "associatedNetworkObjectID": {
            "description": "ID of the network object that this App is associated with.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "assocIngressACLTemplateId": {
            "description": "The ID of the ACL template that this application is pointing to", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "assocEgressACLTemplateId": {
            "description": "The ID of the ACL template that this application is pointing to", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "name": {
            "description": "Name of the application.", 
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
        "resource_name": "applications", 
        "description": "Represents a real life application like a vendor website, or a social network.", 
        "entity_name": "App", 
        "package": "appd", 
        "get": true, 
        "update": true, 
        "rest_name": "application", 
        "extends": [
            "@base", 
            "@metadata"
        ], 
        "delete": true
    }, 
    "children": {
        "tier": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }, 
        "job": {
            "create": true, 
            "relationship": "child"
        }, 
        "flow": {
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