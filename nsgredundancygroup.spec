{
    "attributes": {
        "heartbeatInterval": {
            "description": "Heartbeat interval in milliseconds to declare the neighbor dead. Default 500 milliseconds", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "float"
        }, 
        "redundancyPortIDs": {
            "description": "Collections resilient port ids associated with this redundant group.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "list"
        }, 
        "description": {
            "description": " Description of the Redundancy Group", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "permittedAction": {
            "description": "The permitted  action to USE/EXTEND  this Gateway Possible values are USE, READ, ALL, INSTANTIATE, EXTEND, DEPLOY, .", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "allowed_choices": [
                "EXTEND", 
                "INSTANTIATE", 
                "DEPLOY", 
                "USE", 
                "READ", 
                "ALL"
            ], 
            "orderable": true, 
            "type": "enum"
        }, 
        "gatewayPeer2AutodiscoveredGatewayID": {
            "description": "The Auto Discovered Gateway  peer in this Redundant Group", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "gatewayPeer2ID": {
            "description": "The gateway peer in this Redundant Group. when Redundant Group is deleted this gateway will not recieve vport associations ", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "enterpriseID": {
            "description": "The enterprise associated with this Redundant Group. This is a read only attribute", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "redundantGatewayStatus": {
            "description": "The status of  Redundant Group, possible values are FAILED, SUCCESS Possible values are FAILED, SUCCESS, .", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "allowed_choices": [
                "SUCCESS", 
                "FAILED"
            ], 
            "orderable": true, 
            "type": "enum"
        }, 
        "gatewayPeer2Name": {
            "description": "The gateway peer name in this Redundant Group", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "gatewayPeer1ID": {
            "description": "The gateway configuration owner in this Redundant Group. when Redundant Group is deleted this gateway will recieve vport associations ", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "heartbeatVLANID": {
            "description": "Heartbeat VLAN used for BFD. Default 4094", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "integer"
        }, 
        "gatewayPeer1Name": {
            "description": "The gateway   configuration owner name in this Redundant Group", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "personality": {
            "description": "derived personality of the Redundancy Group - VSG,VRSG,NSG,OTHER Possible values are VSG, VSA, VRSG, DC7X50, NSG, HARDWARE_VTEP, OTHER, .", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "allowed_choices": [
                "DC7X50", 
                "OTHER", 
                "VRSG", 
                "VSG", 
                "VSA", 
                "HARDWARE_VTEP", 
                "NSG"
            ], 
            "orderable": true, 
            "type": "enum"
        }, 
        "consecutiveFailuresCount": {
            "description": "Consecutive failure count. Default 3", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "integer"
        }, 
        "gatewayPeer1AutodiscoveredGatewayID": {
            "description": "The Auto Discovered Gateway configuration owner in this Redundant Group. ", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "name": {
            "description": "Name of the Redundancy Group ", 
            "format": "free", 
            "filterable": true, 
            "uniqueScope": "no", 
            "required": true, 
            "exposed": true, 
            "orderable": true, 
            "type": "string"
        }
    }, 
    "model": {
        "resource_name": "nsgredundancygroups", 
        "description": "Represents Redundant Group formed by two VNS Gateways", 
        "entity_name": "NSRedundantGatewayGroup", 
        "package": "nsg", 
        "get": true, 
        "update": true, 
        "rest_name": "nsgredundancygroup", 
        "extends": [
            "@base", 
            "@metadata"
        ], 
        "delete": true
    }, 
    "children": {
        "nsgateway": {
            "update": true, 
            "relationship": "child", 
            "get": true
        }, 
        "alarm": {
            "relationship": "child", 
            "get": true
        }, 
        "nsredundantport": {
            "create": true, 
            "update": true, 
            "relationship": "child", 
            "get": true
        }, 
        "eventlog": {
            "relationship": "child", 
            "get": true
        }
    }
}