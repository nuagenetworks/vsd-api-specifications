{
    "attributes": {
        "DHCPManaged": {
            "description": "decides whether L2Domain / L2Domain template DHCP is managed by VSD",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "boolean",
            "uniqueScope": "no"
        },
        "IPType": {
            "allowed_choices": [
                "IPV6",
                "IPV4"
            ],
            "description": "IPv4 or IPv6(only IPv4 is supported in R2.0) Possible values are IPV4, IPV6, .",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "enum",
            "uniqueScope": "no"
        },
        "address": {
            "description": "Network address of the L2Domain / L2Domain template defined. ",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "associatedMulticastChannelMapID": {
            "description": "The ID of the Multi Cast Channel Map this L2Domain / L2Domain template template is associated with. This has to be set when  enableMultiCast is set to ENABLED",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        },
        "description": {
            "description": "A description field provided by the user that identifies the L2Domain / L2Domain template.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        },
        "gateway": {
            "description": "The IP address of the gateway of this l2 domain",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "multicast": {
            "allowed_choices": [
                "ENABLED",
                "INHERITED",
                "DISABLED"
            ],
            "description": "multicast is enum that indicates multicast policy on L2Domain / L2Domain template. Possible values are ENABLED and DISABLED Possible values are INHERITED, ENABLED, DISABLED, .",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": false,
            "type": "enum",
            "uniqueScope": "no"
        },
        "name": {
            "description": "Name of the L2Domain / L2Domain template,has to be unique within a Enterprise. Valid characters are alphabets, numbers, space and hyphen( - ).",
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
            "description": "Netmask of the L2Domain / L2Domain template defined",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "policyChangeStatus": {
            "allowed_choices": [
                "STARTED",
                "DISCARDED",
                "APPLIED"
            ],
            "description": "",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": false,
            "type": "enum",
            "uniqueScope": "no"
        },
        "encryption": {
            "allowed_choices": [
                "ENABLED",
                "DISABLED"
            ],
            "description": "Determines whether IPSEC is enabled Possible values are ENABLED, DISABLED, .",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": false,
            "type": "enum",
            "uniqueScope": "no"
        }
    },
    "children": {
        "addressrange": {
            "create": true,
            "get": true,
            "update": true,
            "delete": true,
            "relationship": "child"
        },
        "egressacltemplate": {
            "create": true,
            "get": true,
            "relationship": "child"
        },
        "eventlog": {
            "get": true,
            "relationship": "child"
        },
        "group": {
            "get": true,
            "relationship": "child",
            "update": true
        },
        "ingressacltemplate": {
            "create": true,
            "get": true,
            "relationship": "child"
        },
        "ingressadvfwdtemplate": {
            "create": true,
            "get": true,
            "relationship": "child"
        },
        "ingressexternalservicetemplate": {
            "create": true,
            "get": true,
            "relationship": "child"
        },
        "job": {
            "create": true,
            "relationship": "child"
        },
        "l2domain": {
            "get": true,
            "relationship": "child"
        },
        "permission": {
            "create": true,
            "get": true,
            "relationship": "child"
        },
        "policygrouptemplate": {
            "create": true,
            "get": true,
            "relationship": "child"
        },
        "qos": {
            "create": true,
            "get": true,
            "relationship": "child"
        },
        "redirectiontargettemplate": {
            "create": true,
            "get": true,
            "relationship": "child"
        }
    },
    "model": {
        "delete": true,
        "description": "L2 Domain in VSD as derived by templates. This object describes the L2 Domain template",
        "entity_name": "L2DomainTemplate",
        "extends": [
            "@base",
            "@audited",
            "@metadata"
        ],
        "get": true,
        "package": "network",
        "resource_name": "l2domaintemplates",
        "rest_name": "l2domaintemplate",
        "update": true
    }
}