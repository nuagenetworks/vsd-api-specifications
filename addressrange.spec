{
    "attributes": {
        "IPType": {
            "allowed_choices": [
                "IPV6",
                "IPV4",
                "DUALSTACK"
            ],
            "description": "IPv4 or IPv6(only IPv4 is supported in R1.0) Possible values are IPV4, IPV6, DUALSTACK.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "enum",
            "uniqueScope": "no"
        },
        "DHCPPoolType": {
            "allowed_choices": [
                "HOST", 
                "BRIDGE"
            ],
            "description": "DHCPPoolType is an enum that indicates if the DHCP Pool is for HOST/BRIDGE. Possible values are HOST, BRIDGE Possible values are HOST, BRIDGE, .",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "enum",
            "uniqueScope": "no"
        },
        "maxAddress": {
            "description": "Higest address in the address range",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "required": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "minAddress": {
            "description": "Lowest address in the address range",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "required": true,
            "type": "string",
            "uniqueScope": "no"
        }
    },
    "children": {
        "eventlog": {
            "get": true,
            "relationship": "child"
        }
    },
    "model": {
        "delete": true,
        "description": "This is the definition of a Address Range associated with a Network",
        "entity_name": "AddressRange",
        "extends": [
            "@base", 
            "@audited",
            "@metadata"
        ],
        "get": true,
        "package": "network",
        "resource_name": "addressranges",
        "rest_name": "addressrange",
        "update": true
    }
}