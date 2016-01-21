{
    "attributes": {
        "IPAddress": {
            "description": null, 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string"
        }, 
        "associatedEnterpriseID": {
            "description": null, 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string"
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
            "description": null, 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string"
        }
    }, 
    "children": {
        "ikev2subnet": {
            "create": true, 
            "get": true, 
            "relationship": "child"
        }
    }, 
    "model": {
        "delete": true, 
        "entity_name": "IKEv2Gateway", 
        "extends": [
            "@base", 
            "@metadata"
        ], 
        "get": true, 
        "resource_name": "ikev2gateways", 
        "rest_name": "ikev2gateway", 
        "update": true
    }
}