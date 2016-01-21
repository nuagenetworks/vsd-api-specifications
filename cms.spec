{
    "attributes": {
        "name": {
            "description": "Name of the cloud management system", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }
    }, 
    "model": {
        "delete": true, 
        "description": "Object that identifies a cloud management system", 
        "entity_name": "CloudMgmtSystem", 
        "extends": [
            "@base", 
            "@audited",
            "@metadata"
        ], 
        "get": true, 
        "package": "cms", 
        "resource_name": "cms", 
        "rest_name": "cms"
    }
}