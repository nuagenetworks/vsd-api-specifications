{
    "attributes": {
        "VLANRange": {
            "description": "VLAN Range of the Port.  Format must conform to a-b,c,d-f where a,b,c,d,f are integers between 0 and 4095.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 255,
            "type": "string",
            "uniqueScope": "no"
        },
        "associatedEgressQOSPolicyID": {
            "description": "ID of the Egress QOS Policy associated with this Vlan.",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "associatedRedundantPortID": {
            "description": "ID of the redundant port to which the Port is associated to.",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "associatedVSCProfileID": {
            "description": "The ID of the infrastructure VSC profile this is associated with this instance of a port or port template.",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "description": {
            "description": "A description of the Port",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 255,
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "infrastructureProfileID": {
            "description": "The ID of the infrastructure profile this instance is associated with.",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "name": {
            "description": "Name of the Port",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 255,
            "min_length": 1,
            "orderable": true,
            "required": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "permittedAction": {
            "allowed_choices": [
                "ALL",
                "DEPLOY",
                "EXTEND",
                "INSTANTIATE",
                "READ",
                "USE"
            ],
            "description": "The permitted  action to USE/EXTEND  this Gateway Possible values are USE, READ, ALL, INSTANTIATE, EXTEND, DEPLOY, .",
            "exposed": true,
            "format": "free",
            "type": "enum",
            "uniqueScope": "no"
        },
        "physicalName": {
            "description": "Identifier of the Port",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 255,
            "min_length": 1,
            "orderable": true,
            "required": true,
            "type": "string",
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
            "max_length": 255,
            "orderable": true,
            "required": true,
            "type": "enum",
            "uniqueScope": "no"
        },
        "status": {
            "allowed_choices": [
                "INITIALIZED",
                "MISMATCH",
                "ORPHAN",
                "READY"
            ],
            "description": "Status of the port. Possible values are - INITIALIZED, ORPHAN, READY, MISMATCH Possible values are INITIALIZED, ORPHAN, READY, MISMATCH, .",
            "exposed": true,
            "format": "free",
            "type": "enum",
            "uniqueScope": "no"
        },
        "templateID": {
            "description": "The ID of the template that this Port was created from",
            "exposed": true,
            "format": "free",
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
            "max_length": 255,
            "orderable": true,
            "required": true,
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
        "nsportstaticconfiguration": {
            "create": true,
            "get": true,
            "relationship": "child",
            "update": true
        },
        "permission": {
            "create": true,
            "get": true,
            "relationship": "child"
        },
        "statistics": {
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
        "description": "Represents a Port of a particular NS gateway object.",
        "entity_name": "NSPort",
        "extends": [
            "@audited",
            "@base",
            "@metadata"
        ],
        "get": true,
        "package": "nsg",
        "resource_name": "nsports",
        "rest_name": "nsport",
        "update": true
    }
}