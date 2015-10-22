{
    "attributes": {
        "infrastructureProfileID": {
            "description": "The ID of the infrastructure gateway profile this instance of a Gateway is associated with.", 
            "format": "free", 
            "filterable": true, 
            "uniqueScope": "no", 
            "required": true, 
            "exposed": true, 
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
        "resource_name": "nsgatewaytemplates", 
        "description": "Represents Network Service Gateway Template object", 
        "entity_name": "NSGatewayTemplate", 
        "package": "nsg", 
        "get": true, 
        "update": true, 
        "rest_name": "nsgatewaytemplate", 
        "extends": [
            "@base", 
            "@metadata"
        ], 
        "delete": true
    }, 
    "children": {
        "nsporttemplate": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }
    }
}