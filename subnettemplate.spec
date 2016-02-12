{
    "attributes": {
        "IPType": {
            "allowed_choices": [
                "IPV4",
                "IPV6",
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
        "IPv6address": {
            "description": "IPv6 address of the subnet defined. In case of zone, this is an optional field for and allows users to allocate an IP address range to a zone. The VSD will auto-assign IP addresses to subnets from this range if a specific IP address is not defined for the subnet",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "associatedMulticastChannelMapID": {
            "description": "The ID of the Multi Cast Channel Map  this Subnet/Subnet Template is associated with. This has to be set when  enableMultiCast is set to ENABLED",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "description": {
            "description": "A description field provided by the user that identifies the subnet",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 255,
            "type": "string",
            "uniqueScope": "no"
        },
        "encryption": {
            "allowed_choices": [
                "DISABLED",
                "ENABLED",
                "INHERITED"
            ],
            "description": "Determines whether or not IPSEC is enabled. Possible values are INHERITED, ENABLED, DISABLED, .",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "type": "enum",
            "uniqueScope": "no"
        },
        "gateway": {
            "description": "The IP address of the gateway of this subnet",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "IPv6Gateway": {
            "description": "The IPv6 address of the gateway of this subnet",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "multicast": {
            "allowed_choices": [
                "DISABLED",
                "ENABLED",
                "INHERITED"
            ],
            "description": "multicast is enum that indicates multicast policy on Subnet/Subnet Template. Possible values are ENABLED,DISABLED and INHERITED Possible values are INHERITED, ENABLED, DISABLED, .",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "type": "enum",
            "uniqueScope": "no"
        },
        "name": {
            "description": "Name of the current entity(Zone or zone template or subnet etc..) Valid characters are alphabets, numbers, space and hyphen( - ).",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 64,
            "min_length": 1,
            "orderable": true,
            "required": true,
            "type": "string",
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
        },
        "proxyARP": {
            "description": " when set VRS will act as  ARP Proxy",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "boolean",
            "uniqueScope": "no"
        },
        "splitSubnet": {
            "description": "Need to add correct description",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "boolean",
            "uniqueScope": "no"
        }
    },
    "children": {
        "addressrange": {
            "create": true,
            "get": true,
            "relationship": "child"
        },
        "eventlog": {
            "get": true,
            "relationship": "child"
        },
        "qos": {
            "create": true,
            "get": true,
            "relationship": "child"
        },
        "subnet": {
            "get": true,
            "relationship": "child"
        }
    },
    "model": {
        "delete": true,
        "description": "As domain and zone objects, subnet objects are created in VSD as derived by templates. This object describes the subnet template.",
        "entity_name": "SubnetTemplate",
        "extends": [
            "@audited",
            "@base",
            "@metadata"
        ],
        "get": true,
        "package": "network",
        "resource_name": "subnettemplates",
        "rest_name": "subnettemplate",
        "update": true
    }
}