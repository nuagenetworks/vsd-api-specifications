{
    "attributes": {
        "description": {
            "description": "Description of the External Service.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "name": {
            "description": "unique name of the External Service. ", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }
    }, 
    "model": {
        "resource_name": "endpoints", 
        "description": "Representation of End Point", 
        "entity_name": "EndPoint", 
        "package": "policy", 
        "get": true, 
        "rest_name": "endpoint", 
        "extends": [
            "@base", 
            "@metadata"
        ]
    }, 
    "children": {
        "eventlog": {
            "relationship": "child", 
            "get": true
        }
    }
}