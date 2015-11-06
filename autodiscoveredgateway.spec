{
    "attributes": {
        "controllers": {
            "description": "Controllers to which this gateway instance is associated with.", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "list", 
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
        "gatewayID": {
            "description": "The Gateway associated with this  Auto Discovered Gateway  . This is a read only attribute", 
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
            "description": "Personality of the Gateway - VSG,VRSG,NONE,OTHER, cannot be changed after creation. Possible values are VSG, VSA, VRSG, DC7X50, NSG, HARDWARE_VTEP, OTHER, .", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "required": true, 
            "type": "enum", 
            "uniqueScope": "no"
        }, 
        "systemID": {
            "description": "Identifier of the Gateway", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }
    }, 
    "children": {
        "eventlog": {
            "get": true, 
            "relationship": "child"
        }, 
        "nsport": {
            "get": true, 
            "relationship": "child"
        }, 
        "port": {
            "get": true, 
            "relationship": "child"
        }, 
        "service": {
            "get": true, 
            "relationship": "child"
        }
    }, 
    "model": {
        "description": "Represents Auto discovered Gateway", 
        "entity_name": "AutoDiscoveredGateway", 
        "extends": [
            "@base", 
            "@metadata"
        ], 
        "get": true, 
        "package": "gateway", 
        "resource_name": "autodiscoveredgateways", 
        "rest_name": "autodiscoveredgateway"
    }
}