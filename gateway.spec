{
    "attributes": {
        "autoDiscGatewayID": {
            "description": "The Auto Discovered Gateway associated with this Gateway Instance",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "description": {
            "description": "A description of the Gateway",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 255,
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "enterpriseID": {
            "description": "The enterprise associated with this Gateway. This is a read only attribute",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "name": {
            "description": "Name of the Gateway",
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
        "peer": {
            "description": "The System ID of the peer gateway associated with this Gateway instance when it is discovered by the network manager (VSD) as being redundant.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 255,
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "pending": {
            "description": "Indicates that this gateway is pending state or state. When in pending state it cannot be modified from REST.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "type": "boolean",
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
        "personality": {
            "allowed_choices": [
                "DC7X50",
                "HARDWARE_VTEP",
                "NSG",
                "OTHER",
                "VRSG",
                "VSA",
                "VSG"
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
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "systemID": {
            "description": "Identifier of the Gateway, cannot be modified after creation",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 255,
            "min_length": 1,
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "templateID": {
            "description": "The ID of the template that this Gateway was created from. This should be set when instantiating a Gateway",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "vtep": {
            "description": "Represent the system ID or the Virtual IP of a service used by a Gateway (VSG for now) to establish a tunnel with a remote VSG or hypervisor.  The format of this field is consistent with an IP address.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 255,
            "orderable": true,
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
            "@audited",
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