{
    "attributes": {
        "autoDiscGatewayID": {
            "description": "The Auto Discovered Gateway associated with this Gateway Instance",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        },
        "description": {
            "description": "A description of the Gateway",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string",
            "min_length": 0,
            "max_length": 255,
            "uniqueScope": "no"
        },
        "enterpriseID": {
            "description": "The enterprise associated with this Gateway. This is a read only attribute",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        },
        "name": {
            "description": "Name of the Gateway",
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
        "pending": {
            "description": "Indicates that this gateway is pending state or state. When in pending state it cannot be modified from REST.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": false,
            "type": "boolean",
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
        "personality": {
            "allowed_choices": [
                "DC7X50",
                "OTHER",
                "VRSG",
                "VSG",
                "VSA",
                "HARDWARE_VTEP",
                "NSG"
            ],
            "description": "Personality of the Gateway - VSG,VRSG,NSG,NONE,OTHER, cannot be changed after creation. Possible values are VSG, VSA, VRSG, DC7X50, NSG, HARDWARE_VTEP, OTHER, .",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "required": true,
            "type": "enum",
            "uniqueScope": "no"
        },
        "redundancyGroupID": {
            "description": "The Redundancy Gateway Group associated with this Gateway Instance. This is a read only attribute",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        },
        "systemID": {
            "description": "Identifier of the Gateway, cannot be modified after creation",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string",
            "min_length": 1,
            "max_length": 255,
            "uniqueScope": "no"
        },
        "templateID": {
            "description": "The ID of the template that this Gateway was created from. This should be set when instantiating a Gateway",
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
        "job": {
            "create": true,
            "get": true,
            "relationship": "child"
        },
        "patnatpool": {
            "get": true,
            "relationship": "child",
            "update": true
        },
        "permission": {
            "create": true,
            "get": true,
            "relationship": "child"
        },
        "port": {
            "create": true,
            "get": true,
            "relationship": "child"
        },
        "service": {
            "create": true,
            "get": true,
            "relationship": "child"
        }
    },
    "model": {
        "delete": true,
        "description": "Represents Gateway object.",
        "entity_name": "Gateway",
        "extends": [
            "@base",
            "@metadata"
        ],
        "get": true,
        "package": "gateway",
        "resource_name": "gateways",
        "rest_name": "gateway",
        "update": true
    }
}