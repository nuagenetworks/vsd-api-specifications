{
    "attributes": {
        "name": {
            "description": "Name of the cloud management system", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }
    }, 
    "model": {
        "resource_name": "cms", 
        "description": "Object that identifies a cloud management system", 
        "entity_name": "CloudMgmtSystem", 
        "package": "cms", 
        "get": true, 
        "rest_name": "cms", 
        "extends": [
            "@base", 
            "@metadata"
        ], 
        "delete": true
    }
}