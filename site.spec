{
    "attributes": {
        "address": {
            "description": "unique fqdn/address of the remote site",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "required": true,
            "type": "string",
            "min_length": 1,
            "max_length": 255,
            "uniqueScope": "no"
        },
        "description": {
            "description": "Description of the Remote Site.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string",
            "min_length": 0,
            "max_length": 255,
            "uniqueScope": "no"
        },
        "name": {
            "description": "name of the Remote Site.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "required": true,
            "type": "string",
            "min_length": 1,
            "max_length": 255,
            "uniqueScope": "no"
        },
        "siteIdentifier": {
            "description": "unique identifier of the remote site",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string",
            "min_length": 1,
            "max_length": 255,
            "uniqueScope": "no"
        },
        "xmppDomain": {
            "description": "unique xmpp domain name of the remote site",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "required": true,
            "type": "string",
            "min_length": 1,
            "max_length": 255,
            "uniqueScope": "no"
        }
    },
    "model": {
        "delete": true,
        "description": "Remote Site info",
        "entity_name": "SiteInfo",
        "extends": [
            "@base",
            "@audited",
            "@metadata"
        ],
        "get": true,
        "package": "common",
        "resource_name": "sites",
        "rest_name": "site",
        "update": true
    }
}