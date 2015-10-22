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
        "name": {
            "description": "Name of the Gateway", 
            "format": "free", 
            "filterable": true, 
            "uniqueScope": "no", 
            "required": true, 
            "exposed": true, 
            "orderable": true, 
            "type": "string"
        }, 
        "controllers": {
            "description": "Controllers to which this gateway instance is associated with.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "list"
        }, 
        "systemID": {
            "description": "Identifier of the Gateway", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "gatewayID": {
            "description": "The Gateway associated with this  Auto Discovered Gateway  . This is a read only attribute", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "personality": {
            "required": true, 
            "description": "Personality of the Gateway - VSG,VRSG,NONE,OTHER, cannot be changed after creation. Possible values are VSG, VSA, VRSG, DC7X50, NSG, HARDWARE_VTEP, OTHER, .", 
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
        }
    }, 
    "model": {
        "resource_name": "autodiscoveredgateways", 
        "description": "Represents Auto discovered Gateway", 
        "entity_name": "AutoDiscoveredGateway", 
        "package": "gateway", 
        "get": true, 
        "rest_name": "autodiscoveredgateway", 
        "extends": [
            "@base", 
            "@metadata"
        ]
    }, 
    "children": {
        "nsport": {
            "relationship": "child", 
            "get": true
        }, 
        "service": {
            "relationship": "child", 
            "get": true
        }, 
        "port": {
            "relationship": "child", 
            "get": true
        }, 
        "eventlog": {
            "relationship": "child", 
            "get": true
        }
    }
}