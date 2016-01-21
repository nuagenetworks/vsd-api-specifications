{
    "attributes": {
        "associatedBGPProfileID": {
            "description": "The ID of the associated BGP profile",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string",
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
        "gatewayID": {
            "description": "The Gateway associated with this  VLAN  . This is a read only attribute",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
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
        "readonly": {
            "description": "Determines whether this entity is read only.  Read only objects cannot be modified or deleted.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "boolean",
            "uniqueScope": "no"
        },
        "restricted": {
            "description": "Determines whether this entity can be used in associations with other properties.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "boolean",
            "uniqueScope": "no"
        },
        "status": {
            "allowed_choices": [
                "ORPHAN",
                "MISMATCH",
                "INITIALIZED",
                "READY"
            ],
            "description": "Status of the VLAN. Possible values are - INITIALIZED, ORPHAN, READY, MISMATCH Possible values are INITIALIZED, ORPHAN, READY, MISMATCH, .",
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
        },
        "value": {
            "description": "value of VLAN",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "required": true,
            "type": "integer",
            "min_value": 0,
            "max_value": 4096,
            "uniqueScope": "no"
        },
        "vportID": {
            "description": "The Vport associated with this  VLAN  . This is a read only attribute",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
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
        "ikev2gatewayconnection": {
            "create": true, 
            "get": true, 
            "relationship": "child"
        }, 
        "permission": {
            "create": true,
            "get": true,
            "relationship": "child"
        }
    },
    "model": {
        "delete": true,
        "description": "Represents VLAN object under a given PORT object",
        "entity_name": "VLAN",
        "extends": [
            "@base",
            "@audited",
            "@metadata"
        ],
        "get": true,
        "package": "gateway",
        "resource_name": "vlans",
        "rest_name": "vlan",
        "update": true
    }
}