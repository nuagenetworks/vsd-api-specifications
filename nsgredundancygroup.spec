{
    "attributes": {
        "consecutiveFailuresCount": {
            "description": "Consecutive failure count. Default 3",
            "exposed": true,
            "format": "free",
            "max_value": 3,
            "min_value": 3,
            "type": "integer",
            "uniqueScope": "no"
        },
        "description": {
            "description": " Description of the Redundancy Group",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 255,
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "enterpriseID": {
            "description": "The enterprise associated with this Redundant Group. This is a read only attribute",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "gatewayPeer1AutodiscoveredGatewayID": {
            "description": "The Auto Discovered Gateway configuration owner in this Redundant Group. ",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "gatewayPeer1ID": {
            "description": "The gateway configuration owner in this Redundant Group. when Redundant Group is deleted this gateway will recieve vport associations ",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "gatewayPeer1Name": {
            "description": "The gateway   configuration owner name in this Redundant Group",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "gatewayPeer2AutodiscoveredGatewayID": {
            "description": "The Auto Discovered Gateway  peer in this Redundant Group",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "gatewayPeer2Name": {
            "description": "The gateway peer name in this Redundant Group",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "heartbeatInterval": {
            "description": "Heartbeat interval in milliseconds to declare the neighbor dead. Default 500 milliseconds",
            "exposed": true,
            "format": "free",
            "max_value": 2000,
            "min_value": 500,
            "subtype": "long",
            "type": "integer",
            "uniqueScope": "no"
        },
        "heartbeatVLANID": {
            "description": "Heartbeat VLAN used for BFD. Default 4094",
            "exposed": true,
            "format": "free",
            "max_value": 4095,
            "type": "integer",
            "uniqueScope": "no"
        },
        "name": {
            "description": "Name of the Redundancy Group ",
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
            "description": "derived personality of the Redundancy Group - VSG,VRSG,NSG,OTHER Possible values are VSG, VSA, VRSG, DC7X50, NSG, HARDWARE_VTEP, OTHER, .",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "enum",
            "uniqueScope": "no"
        },
        "redundancyPortIDs": {
            "description": "Collections resilient port ids associated with this redundant group.",
            "exposed": true,
            "format": "free",
            "subtype": "string",
            "type": "list",
            "uniqueScope": "no"
        },
        "redundantGatewayStatus": {
            "allowed_choices": [
                "FAILED",
                "SUCCESS"
            ],
            "description": "The status of  Redundant Group, possible values are FAILED, SUCCESS Possible values are FAILED, SUCCESS, .",
            "exposed": true,
            "format": "free",
            "type": "enum",
            "uniqueScope": "no"
        }
    },
    "children": {
        "alarm": {
            "get": true,
            "relationship": "child"
        },
        "eventlog": {
            "get": true,
            "relationship": "child"
        },
        "nsgateway": {
            "get": true,
            "relationship": "child",
            "update": true
        },
        "nsredundantport": {
            "create": true,
            "get": true,
            "relationship": "child",
            "update": true
        }
    },
    "model": {
        "delete": true,
        "description": "Represents Redundant Group formed by two VNS Gateways.",
        "entity_name": "NSRedundantGatewayGroup",
        "extends": [
            "@audited",
            "@base",
            "@metadata"
        ],
        "get": true,
        "package": "nsg",
        "resource_name": "nsgredundancygroups",
        "rest_name": "nsgredundancygroup",
        "update": true
    }
}