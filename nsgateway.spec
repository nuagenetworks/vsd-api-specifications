{
    "attributes": {
        "configurationReloadState": {
            "description": "", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "enum"
        }, 
        "bootstrapID": {
            "description": "The bootstrap details associated with this NSGateway. NOTE: this is a read only property, it can only be set during creation of an NSG", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "associatedGatewaySecurityProfileID": {
            "description": "Readonly Id of the associated gateway security profile object", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "description": {
            "description": "A description of the Gateway", 
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
        "NATTraversalEnabled": {
            "description": "Boolean value that states if the NSG instance is in a network that is behind a NAT device and will use NAT Traversal procedures to talk to other NSGs and the Internet.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "boolean"
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
        "configurationStatus": {
            "description": "", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "enum"
        }, 
        "associatedGatewaySecurityID": {
            "description": "Readonly Id of the associated gateway security object", 
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
        "locationID": {
            "description": "The NSGateway's Location. NOTE: this is a read only property, it can only be set through the location object", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
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
        "templateID": {
            "description": "The ID of the template that this Gateway was created from. This should be set when instantiating a Gateway", 
            "format": "free", 
            "filterable": true, 
            "uniqueScope": "no", 
            "required": true, 
            "exposed": true, 
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
        "personality": {
            "description": "Personality of the Gateway - NSG, cannot be changed after creation.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "datapathID": {
            "description": "Identifier of the Gateway, based on the systemId", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "ports": {
            "description": "Collection of ports associated with the NSG.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "list"
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
        "resource_name": "nsgateways", 
        "description": "Represents Network Service Gateway object.", 
        "entity_name": "NSGateway", 
        "package": "nsg", 
        "get": true, 
        "update": true, 
        "rest_name": "nsgateway", 
        "extends": [
            "@base", 
            "@metadata"
        ], 
        "delete": true
    }, 
    "children": {
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
        "bootstrap": {
            "relationship": "child", 
            "get": true
        }, 
        "enterprisepermission": {
            "relationship": "child", 
            "get": true
        }, 
        "job": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }, 
        "infraconfig": {
            "update": true, 
            "relationship": "child", 
            "get": true
        }, 
        "location": {
            "relationship": "child", 
            "get": true
        }, 
        "bootstrapactivation": {
            "create": true, 
            "relationship": "child"
        }, 
        "patnatpool": {
            "update": true, 
            "relationship": "child", 
            "get": true
        }, 
        "nsport": {
            "create": true, 
            "update": true, 
            "relationship": "child", 
            "get": true
        }
    }
}