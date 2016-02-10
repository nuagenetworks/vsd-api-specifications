{
    "attributes": {
        "associatedGatewayId": {
            "description": "Default PAT IP Address, must belong to the pool above",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "associatedGatewayType": {
            "allowed_choices": [
                "GATEWAY",
                "NSGATEWAY",
                "AUTO_DISC_GATEWAY",
                "IKEV2_GATEWAY"
            ],
            "description": "",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "enum",
            "uniqueScope": "no"
        },
        "associatedVlanId": {
            "description": "",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "type": "string"
        },
        "defaultPATIP": {
            "description": "Default PAT IP Address, must belong to the pool above",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "description": {
            "description": "A description of the PATNATPool",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 255,
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "dynamicSourceEnabled": {
            "description": "Set to True if the address translation pool at the address translation pool definition level",
            "exposed": true,
            "filterable": true,
            "type": "boolean"
        },
        "endAddressRange": {
            "description": "Ending IP Address for the pool of available addresses for use",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "name": {
            "description": "Name of the PATNATPool",
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
                "EXTEND",
                "INSTANTIATE",
                "DEPLOY",
                "USE",
                "READ",
                "ALL"
            ],
            "description": "The permitted  action to USE/EXTEND  this Gateway Possible values are USE, READ, ALL, INSTANTIATE, EXTEND, DEPLOY, .",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "enum",
            "uniqueScope": "no"
        },
        "startAddressRange": {
            "description": "Starting IP Address for the pool of available addresses for use",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "translationTimeout": {
            "description": "Used to clear out the dynamic address translations and free up the IP addresses for re-assignment.  Units are in second",
            "exposed": true,
            "filterable": true,
            "orderable": true,
            "type": "integer"
        }
    },
    "children": {
        "addressmap": {
            "create": true,
            "get": true,
            "relationship": "child"
        },
        "enterprisepermission": {
            "create": true,
            "get": true,
            "relationship": "child"
        }
    },
    "model": {
        "delete": true,
        "description": "Represents PAT NAT Pool object.",
        "entity_name": "PATNATPool",
        "extends": [
            "@audited",
            "@base",
            "@metadata"
        ],
        "get": true,
        "package": "gateway",
        "resource_name": "patnatpools",
        "rest_name": "patnatpool",
        "update": true
    }
}