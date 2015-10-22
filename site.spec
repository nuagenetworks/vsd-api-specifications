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
            "uniqueScope": "no"
        },
        "description": {
            "description": "Description of the Remote Site.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string",
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
            "uniqueScope": "no"
        },
        "siteIdentifier": {
            "description": "unique identifier of the remote site",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string",
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
            "uniqueScope": "no"
        }
    },
    "delete": true,
    "description": "Remote Site info",
    "entity_name": "SiteInfo",
    "extends": [
        "@base",
        "@metadata"
    ],
    "get": true,
    "package": "/common",
    "resource_name": "sites",
    "rest_name": "site",
    "update": true
}