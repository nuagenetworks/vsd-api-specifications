{
    "attributes": {
        "addressRange": {
            "description": "Pool of IP Address that is available for use ex : 130.12.0.0/16",
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
        "endAddress": {
            "description": "Pool ends at this IP Address",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string"
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
        "startAddress": {
            "description": "Pool start at this address",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string"
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