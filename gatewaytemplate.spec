{
    "attributes": {
        "enterpriseID": {
            "description": "The enterprise associated with this Gateway. This is a read only attribute", 
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
        }
    }, 
    "model": {
        "resource_name": "gatewaytemplates", 
        "description": "Represents Gateway Template object", 
        "entity_name": "GatewayTemplate", 
        "package": "gateway", 
        "get": true, 
        "update": true, 
        "rest_name": "gatewaytemplate", 
        "extends": [
            "@base", 
            "@metadata"
        ], 
        "delete": true
    }, 
    "children": {
        "porttemplate": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }
    }
}