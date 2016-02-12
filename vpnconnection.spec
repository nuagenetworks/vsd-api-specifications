{
    "attributes": {
        "associatedWANServiceID": {
            "description": "Assosciated WAN Service",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "description": {
            "description": "A description of the VPNConnect",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 255,
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "name": {
            "description": "Name of the VPNConnect",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 255,
            "min_length": 1,
            "orderable": true,
            "required": true,
            "type": "string",
            "uniqueScope": "no"
        }
    },
    "model": {
        "delete": true,
        "description": "This is the definition of a VPN Connect which holds the PE service assocaition with a DOMAIN.",
        "entity_name": "VPNConnection",
        "extends": [
            "@audited",
            "@base",
            "@metadata"
        ],
        "get": true,
        "package": "network",
        "resource_name": "vpnconnections",
        "rest_name": "vpnconnection",
        "update": true
    }
}