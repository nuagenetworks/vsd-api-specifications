{
    "attributes": {
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
        "resource_name": "redundancygroups", 
        "description": "Represents Redundant Group formed by two Gateways", 
        "entity_name": "RedundancyGroup", 
        "package": "gateway", 
        "get": true, 
        "update": true, 
        "rest_name": "redundancygroup", 
        "extends": [
            "@base", 
            "@metadata"
        ], 
        "delete": true
    }, 
    "children": {
        "service": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }, 
        "eventlog": {
            "relationship": "child", 
            "get": true
        }, 
        "permission": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }, 
        "alarm": {
            "relationship": "child", 
            "get": true
        }, 
        "enterprisepermission": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }, 
        "gateway": {
            "update": true, 
            "relationship": "child", 
            "get": true
        }, 
        "port": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }
    }
}