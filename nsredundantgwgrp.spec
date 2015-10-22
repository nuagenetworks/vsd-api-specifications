{
    "attributes": {
        "consecutiveFailuresCount": {
            "description": "Consecutive failure count. Default 3", 
            "exposed": true, 
            "type": "integer", 
            "uniqueScope": "no"
        }, 
        "description": {
            "description": " Description of the Redundancy Group", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "enterpriseID": {
            "description": "The enterprise associated with this Redundant Group. This is a read only attribute", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "gatewayPeer1AutodiscoveredGatewayID": {
            "description": "The Auto Discovered Gateway configuration owner in this Redundant Group. ", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "gatewayPeer1ID": {
            "description": "The gateway configuration owner in this Redundant Group. when Redundant Group is deleted this gateway will recieve vport associations ", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "gatewayPeer1Name": {
            "description": "The gateway   configuration owner name in this Redundant Group", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "gatewayPeer2AutodiscoveredGatewayID": {
            "description": "The Auto Discovered Gateway  peer in this Redundant Group", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "gatewayPeer2ID": {
            "description": "The gateway peer in this Redundant Group. when Redundant Group is deleted this gateway will not recieve vport associations ", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "gatewayPeer2Name": {
            "description": "The gateway peer name in this Redundant Group", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "heartbeatInterval": {
            "description": "Heartbeat interval in milliseconds to declare the neighbor dead. Default 500 milliseconds", 
            "exposed": true, 
            "type": "float", 
            "uniqueScope": "no"
        }, 
        "heartbeatVLANID": {
            "description": "Heartbeat VLAN used for BFD. Default 4094", 
            "exposed": true, 
            "type": "integer", 
            "uniqueScope": "no"
        }, 
        "name": {
            "description": "Name of the Redundancy Group ", 
            "exposed": true, 
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
            "type": "enum", 
            "uniqueScope": "no"
        }, 
        "redundancyPortIDs": {
            "description": "Collections resilient port ids associated with this redundant group.", 
            "exposed": true, 
            "type": "list", 
            "uniqueScope": "no"
        }, 
        "redundantGatewayStatus": {
            "allowed_choices": [
                "SUCCESS", 
                "FAILED"
            ], 
            "description": "The status of  Redundant Group, possible values are FAILED, SUCCESS Possible values are FAILED, SUCCESS, .", 
            "exposed": true, 
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
    "delete": true, 
    "description": "Represents Redundant Group formed by two VNS Gateways", 
    "entity_name": "NSRedundantGWGrp", 
    "extends": [
        "@base", 
        "@metadata"
    ], 
    "get": true, 
    "package": "/nsg", 
    "resource_name": "nsgredundancygroups", 
    "rest_name": "nsgredundancygroup", 
    "update": true
}