{
    "attributes": {
        "description": {
            "description": "A description of the Gateway", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "autoDiscGatewayID": {
            "description": "The Auto Discovered Gateway associated with this Gateway Instance", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "enterpriseID": {
            "description": "The enterprise associated with this Gateway. This is a read only attribute", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "redundancyGroupID": {
            "description": "The Redundancy Gateway Group associated with this Gateway Instance. This is a read only attribute", 
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
        "templateID": {
            "description": "The ID of the template that this Gateway was created from. This should be set when instantiating a Gateway", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "systemID": {
            "description": "Identifier of the Gateway, cannot be modified after creation", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "personality": {
            "required": true, 
            "description": "Personality of the Gateway - VSG,VRSG,NSG,NONE,OTHER, cannot be changed after creation. Possible values are VSG, VSA, VRSG, DC7X50, NSG, HARDWARE_VTEP, OTHER, .", 
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
        "pending": {
            "description": "Indicates that this gateway is pending state or state. When in pending state it cannot be modified from REST.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "boolean"
        }, 
        "name": {
            "description": "Name of the Gateway", 
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
        "resource_name": "gateways", 
        "description": "Represents Gateway object.", 
        "entity_name": "Gateway", 
        "package": "gateway", 
        "get": true, 
        "update": true, 
        "rest_name": "gateway", 
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
        "job": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }, 
        "patnatpool": {
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