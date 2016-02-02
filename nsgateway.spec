{
    "attributes": {
        "NATTraversal": {
            "allowed_choices": [
                "FULLNAT",
                "NONE"
            ],
            "description": "",
            "exposed": true,
            "format": "free",
            "type": "enum",
            "uniqueScope": "no"
        },
        "associatedGatewaySecurityID": {
            "description": "Readonly Id of the associated gateway security object",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "associatedGatewaySecurityProfileID": {
            "description": "Readonly Id of the associated gateway security profile object",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "autoDiscGatewayID": {
            "description": "The Auto Discovered Gateway associated with this Gateway Instance",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "bootstrapID": {
            "description": "The bootstrap details associated with this NSGateway. NOTE: this is a read only property, it can only be set during creation of an NSG",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "bootstrapStatus": {
            "allowed_choices": [
                "INACTIVE",
                "NOTIFICATION_APP_REQ_SENT",
                "NOTIFICATION_APP_REQ_ACK",
                "CERTIFICATE_SIGNED",
                "ACTIVE"
            ],
            "description": "The bootstrap status of this NSGateway. NOTE: this is a read only property",
            "exposed": true,
            "format": "free",
            "type": "enum",
            "uniqueScope": "no"
        },
        "configurationReloadState": {
            "allowed_choices": [
                "PENDING",
                "SENT",
                "APPLIED",
                "UNKNOWN"
            ],
            "description": "",
            "exposed": true,
            "format": "free",
            "type": "enum",
            "uniqueScope": "no"
        },
        "configurationStatus": {
            "allowed_choices": [
                "UNKNOWN",
                "SUCCESS",
                "FAILURE"
            ],
            "description": "",
            "exposed": true,
            "format": "free",
            "type": "enum",
            "uniqueScope": "no"
        },
        "datapathID": {
            "description": "Identifier of the Gateway, based on the systemId",
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
        "locationID": {
            "description": "The NSGateway's Location. NOTE: this is a read only property, it can only be set through the location object",
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
                "EXTEND",
                "INSTANTIATE",
                "DEPLOY",
                "USE",
                "READ",
                "ALL"
            ],
            "description": "The permitted  action to USE/EXTEND  this Gateway Possible values are USE, READ, ALL, INSTANTIATE, EXTEND, DEPLOY, .",
            "exposed": true,
            "format": "free",
            "type": "enum",
            "uniqueScope": "no"
        },
        "personality": {
            "allowed_choices": [
                "VSG",
                "VSA",
                "VRSG",
                "DC7X50",
                "NSG",
                "HARDWARE_VTEP",
                "OTHER"
            ],
            "description": "Personality of the Gateway - NSG, cannot be changed after creation.",
            "exposed": true,
            "format": "free",
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
        "bootstrap": {
            "get": true,
            "relationship": "child"
        },
        "bootstrapactivation": {
            "create": true,
            "relationship": "child"
        },
        "enterprisepermission": {
            "get": true,
            "relationship": "child"
        },
        "eventlog": {
            "get": true,
            "relationship": "child"
        },
        "infraconfig": {
            "get": true,
            "relationship": "child",
            "update": true
        },
        "job": {
            "create": true,
            "get": true,
            "relationship": "child"
        },
        "location": {
            "get": true,
            "relationship": "child"
        },
        "nsport": {
            "create": true,
            "get": true,
            "relationship": "child",
            "update": true
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
        }
    },
    "model": {
        "delete": true,
        "description": "Represents Network Service Gateway object.",
        "entity_name": "NSGateway",
        "extends": [
            "@audited",
            "@base",
            "@metadata"
        ],
        "get": true,
        "package": "nsg",
        "resource_name": "nsgateways",
        "rest_name": "nsgateway",
        "update": true
    }
}