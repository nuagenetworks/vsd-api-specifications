{
    "attributes": {
        "VLANRange": {
            "description": "VLAN Range of the Port.  Format must conform to a-b,c,d-f where a,b,c,d,f are integers between 0 and 4095.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": false,
            "type": "string",
            "min_length": 0,
            "max_length": 255,
            "uniqueScope": "no"
        },
        "associatedEgressQOSPolicyID": {
            "description": "ID of the Egress QOS Policy associated with this Vlan.",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        },
        "description": {
            "description": "A description of the Port",
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
            "description": "Name of the Port",
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
        "permittedAction": {
            "allowed_choices": [
                "EXTEND",
                "INSTANTIATE",
                "DEPLOY",
                "USE",
                "READ",
                "ALL"
            ],
            "description": "The permitted  action to USE/EXTEND  this Gateway Possible values are USE, READ, ALL, INSTANTIATE, EXTEND, DEPLOY, .",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "enum",
            "uniqueScope": "no"
        },
        "physicalName": {
            "description": "Identifier of the Port",
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
        "portType": {
            "allowed_choices": [
                "ACCESS",
                "NETWORK"
            ],
            "description": "Type of the Port - NETWORK, ACCESS Possible values are ACCESS, NETWORK, .",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "required": true,
            "type": "enum",
            "uniqueScope": "no"
        },
        "status": {
            "allowed_choices": [
                "ORPHAN",
                "MISMATCH",
                "INITIALIZED",
                "READY"
            ],
            "description": "Status of the port. Possible values are - INITIALIZED, ORPHAN, READY, MISMATCH Possible values are INITIALIZED, ORPHAN, READY, MISMATCH, .",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "enum",
            "uniqueScope": "no"
        },
        "templateID": {
            "description": "The ID of the template that this Port was created from",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        },
        "useUserMnemonic": {
            "description": "determines whether to use user mnemonic of the Port",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "boolean",
            "uniqueScope": "no"
        },
        "userMnemonic": {
            "description": "user mnemonic of the Port",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "required": true,
            "type": "string",
            "min_length": 0,
            "max_length": 255,
            "uniqueScope": "no"
        }
    },
    "children": {
        "alarm": {
            "get": true,
            "relationship": "child"
        },
        "enterprisepermission": {
            "create": true,
            "get": true,
            "relationship": "child"
        },
        "eventlog": {
            "get": true,
            "relationship": "child"
        },
        "permission": {
            "create": true,
            "get": true,
            "relationship": "child"
        },
        "vlan": {
            "create": true,
            "get": true,
            "relationship": "child"
        }
    },
    "model": {
        "delete": true,
        "description": "Represents Port under a particular gateway object or redundant group object.",
        "entity_name": "Port",
        "extends": [
            "@base",
            "@audited",
            "@metadata"
        ],
        "get": true,
        "package": "gateway",
        "resource_name": "ports",
        "rest_name": "port",
        "update": true
    }
}