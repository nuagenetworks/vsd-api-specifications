{
    "attributes": {
        "defaultAction": {
            "allowed_choices": [
                "REJECT", 
                "ACCEPT"
            ], 
            "description": "accept/reject", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "required": true, 
            "type": "enum"
        }, 
        "description": {
            "description": null, 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string"
        }, 
        "name": {
            "creation_only": true, 
            "description": "policy name, unique within an enterprise", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "required": true, 
            "type": "string"
        }, 
        "policyDefinition": {
            "description": "String blob", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string"
        }
    }, 
    "model": {
        "delete": true, 
        "entity_name": "RoutingPolicy", 
        "get": true, 
        "resource_name": "routingpolicies", 
        "rest_name": "routingpolicies", 
        "update": true
    }
}