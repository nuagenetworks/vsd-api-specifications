{
    "attributes": {
        "xmppDomain": {
            "description": "unique xmpp domain name of the remote site", 
            "format": "free", 
            "filterable": true, 
            "uniqueScope": "no", 
            "required": true, 
            "exposed": true, 
            "orderable": true, 
            "type": "string"
        }, 
        "siteIdentifier": {
            "description": "unique identifier of the remote site", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "description": {
            "description": "Description of the Remote Site.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "name": {
            "description": "name of the Remote Site.", 
            "format": "free", 
            "filterable": true, 
            "uniqueScope": "no", 
            "required": true, 
            "exposed": true, 
            "orderable": true, 
            "type": "string"
        }, 
        "address": {
            "description": "unique fqdn/address of the remote site", 
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
        "resource_name": "sites", 
        "description": "Remote Site info", 
        "entity_name": "SiteInfo", 
        "package": "common", 
        "get": true, 
        "update": true, 
        "rest_name": "site", 
        "extends": [
            "@base", 
            "@metadata"
        ], 
        "delete": true
    }
}