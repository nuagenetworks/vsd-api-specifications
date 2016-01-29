{
    "attributes": {
        "IPType": {
            "allowed_choices": [
                "IPV6",
                "IPV4"
            ],
            "description": "IPv4 or IPv6(only IPv4 is supported in R1.0) Possible values are IPV4, IPV6, .",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "enum",
            "uniqueScope": "no"
        },
        "address": {
            "description": "IP address of the subnet defined. In case of zone, this is an optional field for and allows users to allocate an IP address range to a zone. The VSD will auto-assign IP addresses to subnets from this range if a specific IP address is not defined for the subnet",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "required": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "name": {
            "description": "Name of the current entity(Zone or zone template or subnet etc..) Valid characters are alphabets, numbers, space and hyphen( - ).",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "required": true,
            "type": "string",
            "min_length": 1,
            "max_length": 64,
            "uniqueScope": "no"
        },
        "netmask": {
            "description": "Netmask of the subnet defined",
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
        },
        "networkmacrogroup": {
            "get": true,
            "relationship": "child",
            "update": true
        }
    },
    "model": {
        "delete": true,
        "description": "Administrators of an enterprise can define macros that are set of IP addresses that identify enterprise networks. These macros can be used in the ACL definitions by network designers and other users to identify access restrictions towards specific enterprise networks",
        "entity_name": "EnterpriseNetwork",
        "extends": [
            "@base",
            "@audited",
            "@metadata"
        ],
        "get": true,
        "package": "network",
        "resource_name": "enterprisenetworks",
        "rest_name": "enterprisenetwork",
        "update": true
    }
}