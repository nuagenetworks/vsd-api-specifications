{
    "attributes": {
        "DSCP": {
            "description": "DSCP match condition to be set in the rule. It is either * or from 0-63. Required for etherType 0x0800",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "description": {
            "description": "Description of the application service.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 255,
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "destinationPort": {
            "description": "The destination port to be matched if protocol is UDP or TCP. Value should be either * or single port number or a port range.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "required": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "direction": {
            "allowed_choices": [
                "REFLEXIVE",
                "UNIDIRECTIONAL"
            ],
            "description": "Direction of the service. Default is UNIDIRECTIONAL. Possible values are UNIDIRECTIONAL, REFLEXIVE, .",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "required": true,
            "type": "enum",
            "uniqueScope": "no"
        },
        "etherType": {
            "description": "Ether type of the packet to be matched. Ether type can be * or a valid hexadecimal value",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "required": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "name": {
            "description": "Name of the application service.",
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
        "protocol": {
            "description": "Protocol that must be matched.  Needs to be 6 (TCP) or 17 (UDP)",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "required": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "sourcePort": {
            "description": "Source port to be matched if protocol is UDP or TCP. Value can be either * or single port number or a port range.",
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
        "description": "Represents a networking communication service.",
        "entity_name": "ApplicationService",
        "extends": [
            "@audited",
            "@base",
            "@metadata"
        ],
        "get": true,
        "package": "appd",
        "resource_name": "applicationservices",
        "rest_name": "applicationservice",
        "update": true
    }
}