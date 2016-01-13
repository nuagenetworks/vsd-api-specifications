{
    "attributes": {
        "consecutiveFailuresCount": {
            "description": "Consecutive failure count. Default 3",
            "exposed": true,
            "filterable": false,
            "orderable": false,
            "type": "integer",
            "min_value": 3,
            "max_value": 3,
            "default_value": 3,
            "uniqueScope": "no"
        },
        "description": {
            "description": " Description of the Redundancy Group",
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
            "description": "The enterprise associated with this Redundant Group. This is a read only attribute",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        },
        "gatewayPeer1AutodiscoveredGatewayID": {
            "description": "The Auto Discovered Gateway configuration owner in this Redundant Group. ",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        },
        "gatewayPeer1ID": {
            "description": "The gateway configuration owner in this Redundant Group. when Redundant Group is deleted this gateway will recieve vport associations ",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        },
        "gatewayPeer1Name": {
            "description": "The gateway   configuration owner name in this Redundant Group",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        },
        "gatewayPeer2AutodiscoveredGatewayID": {
            "description": "The Auto Discovered Gateway  peer in this Redundant Group",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        },
        "gatewayPeer2ID": {
            "description": "The gateway peer in this Redundant Group. when Redundant Group is deleted this gateway will not recieve vport associations ",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        },
        "gatewayPeer2Name": {
            "description": "The gateway peer name in this Redundant Group",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        },
        "heartbeatInterval": {
            "description": "Heartbeat interval in milliseconds to declare the neighbor dead. Default 500 milliseconds",
            "exposed": true,
            "filterable": false,
            "orderable": false,
            "type": "integer",
            "min_value": 500,
            "max_value": 2000,
            "default_value": 500,
            "uniqueScope": "no"
        },
        "heartbeatVLANID": {
            "description": "Heartbeat VLAN used for BFD. Default 4094",
            "exposed": true,
            "filterable": false,
            "orderable": false,
            "type": "integer",
            "min_value": 0,
            "max_value": 4095,
            "default_value": 4094,
            "uniqueScope": "no"
        },
        "name": {
            "description": "Name of the Redundancy Group ",
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
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "list",
            "subtype": "string",
            "uniqueScope": "no"
        },
        "redundantGatewayStatus": {
            "allowed_choices": [
                "SUCCESS",
                "FAILED"
            ],
            "description": "The status of  Redundant Group, possible values are FAILED, SUCCESS Possible values are FAILED, SUCCESS, .",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
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
        "description": "Represents Redundant Group formed by two VNS Gateways",
        "entity_name": "NSRedundantGatewayGroup",
        "extends": [
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