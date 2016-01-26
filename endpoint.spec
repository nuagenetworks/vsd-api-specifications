{
    "attributes": {
        "description": {
            "description": "Description of the External Service.", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "min_length": 0,
            "max_length": 255,
            "uniqueScope": "no"
        }, 
        "name": {
            "description": "unique name of the External Service. ", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "min_length": 1,
            "max_length": 255,
            "uniqueScope": "no"
        }
    }, 
    "children": {
        "eventlog": {
            "get": true, 
            "relationship": "child"
        }
    }, 
    "model": {
        "description": "Representation of End Point", 
        "entity_name": "EndPoint", 
        "extends": [
            "@base", 
            "@audited",
            "@metadata"
        ], 
        "get": true, 
        "package": "policy", 
        "resource_name": "endpoints", 
        "rest_name": "endpoint"
    }
}