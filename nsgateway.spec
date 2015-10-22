{
    "attributes": {
        "NATTraversalEnabled": {
            "description": "Boolean value that states if the NSG instance is in a network that is behind a NAT device and will use NAT Traversal procedures to talk to other NSGs and the Internet.", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "boolean", 
            "uniqueScope": "no"
        }, 
        "associatedGatewaySecurityID": {
            "description": "Readonly Id of the associated gateway security object", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "associatedGatewaySecurityProfileID": {
            "description": "Readonly Id of the associated gateway security profile object", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "autoDiscGatewayID": {
            "description": "The Auto Discovered Gateway associated with this Gateway Instance", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "bootstrapID": {
            "description": "The bootstrap details associated with this NSGateway. NOTE: this is a read only property, it can only be set during creation of an NSG", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "configurationReloadState": {
            "description": "", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "enum", 
            "uniqueScope": "no"
        }, 
        "configurationStatus": {
            "description": "", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "enum", 
            "uniqueScope": "no"
        }, 
        "datapathID": {
            "description": "Identifier of the Gateway, based on the systemId", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
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
            "uniqueScope": "no"
        }, 
        "enterpriseID": {
            "description": "The enterprise associated with this Gateway. This is a read only attribute", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "locationID": {
            "description": "The NSGateway's Location. NOTE: this is a read only property, it can only be set through the location object", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
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
            "uniqueScope": "no"
        }, 
        "pending": {
            "description": "Indicates that this gateway is pending state or state. When in pending state it cannot be modified from REST.", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
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
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "enum", 
            "uniqueScope": "no"
        }, 
        "personality": {
            "description": "Personality of the Gateway - NSG, cannot be changed after creation.", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "ports": {
            "description": "Collection of ports associated with the NSG.", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "list", 
            "uniqueScope": "no"
        }, 
        "redundancyGroupID": {
            "description": "The Redundancy Gateway Group associated with this Gateway Instance. This is a read only attribute", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
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
            "uniqueScope": "no"
        }, 
        "templateID": {
            "description": "The ID of the template that this Gateway was created from. This should be set when instantiating a Gateway", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
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
    "delete": true, 
    "description": "Represents Network Service Gateway object.", 
    "entity_name": "NSGateway", 
    "extends": [
        "@base", 
        "@metadata"
    ], 
    "get": true, 
    "package": "/nsg", 
    "resource_name": "nsgateways", 
    "rest_name": "nsgateway", 
    "update": true
}