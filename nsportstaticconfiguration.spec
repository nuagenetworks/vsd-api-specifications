{
    "attributes": {
        "DNSAddress": {
            "description": "DNS Address for Network NSPort.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 255,
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "address": {
            "description": "IP address of the Network NSPort.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 255,
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "enabled": {
            "description": "Boolean value that states if the NSG Port static configuration needs to be applied.",
            "exposed": true,
            "format": "free",
            "type": "boolean",
            "uniqueScope": "no"
        },
        "gateway": {
            "description": "IP address of the gateway bound to the Network NSPort.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 255,
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "netmask": {
            "description": "IP address netmask of the Network NSPort.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 255,
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        }
    },
    "model": {
        "delete": true,
        "description": "Represents a network port static configuration in the context of an Network Services Gateway.",
        "entity_name": "NSPortStaticConfiguration",
        "extends": [
            "@audited",
            "@base",
            "@metadata"
        ],
        "get": true,
        "package": "nsg",
        "resource_name": "nsportstaticconfigurations",
        "rest_name": "nsportstaticconfiguration",
        "update": true
    }
}