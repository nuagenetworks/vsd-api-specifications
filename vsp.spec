{
    "attributes": {
        "productVersion": {
            "description": "Product version number for VSP", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "description": {
            "description": "Description of the VSP", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "name": {
            "description": "Name of the VSP", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "location": {
            "description": "Installed location of the VSP product", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }
    }, 
    "model": {
        "resource_name": "vsps", 
        "description": "System Monitoring details for VSP", 
        "entity_name": "VSP", 
        "package": "sysmon", 
        "get": true, 
        "update": true, 
        "rest_name": "vsp", 
        "extends": [
            "@base", 
            "@metadata"
        ]
    }, 
    "children": {
        "hsc": {
            "relationship": "child", 
            "get": true
        }, 
        "vsc": {
            "relationship": "child", 
            "get": true
        }, 
        "vsd": {
            "relationship": "child", 
            "get": true
        }, 
        "eventlog": {
            "relationship": "child", 
            "get": true
        }
    }
}