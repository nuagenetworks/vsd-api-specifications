{
    "attributes": {
        "description": {
            "description": "A description of the Gateway", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "enterpriseID": {
            "description": "The enterprise associated with this Gateway. This is a read only attribute", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "name": {
            "description": "Name of the Gateway", 
            "exposed": true, 
            "required": true, 
            "type": "string", 
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
            "description": "Personality of the Gateway - VSG,VRSG,NSG,NONE,OTHER, cannot be changed after creation. Possible values are VSG, VSA, VRSG, DC7X50, NSG, HARDWARE_VTEP, OTHER, .", 
            "exposed": true, 
            "required": true, 
            "type": "enum", 
            "uniqueScope": "no"
        }
    }, 
    "children": {
        "porttemplate": {
            "create": true, 
            "get": true, 
            "relationship": "child"
        }
    }, 
    "delete": true, 
    "description": "Represents Gateway Template object", 
    "entity_name": "GatewayTemplate", 
    "extends": [
        "@base", 
        "@metadata"
    ], 
    "get": true, 
    "package": "/gateway", 
    "resource_name": "gatewaytemplates", 
    "rest_name": "gatewaytemplate", 
    "update": true
}