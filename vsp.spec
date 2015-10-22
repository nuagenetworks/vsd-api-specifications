{
    "attributes": {
        "description": {
            "description": "Description of the VSP", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "location": {
            "description": "Installed location of the VSP product", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "name": {
            "description": "Name of the VSP", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "productVersion": {
            "description": "Product version number for VSP", 
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
        "hsc": {
            "get": true, 
            "relationship": "child"
        }, 
        "vsc": {
            "get": true, 
            "relationship": "child"
        }, 
        "vsd": {
            "get": true, 
            "relationship": "child"
        }
    }, 
    "description": "System Monitoring details for VSP", 
    "entity_name": "VSP", 
    "extends": [
        "@base", 
        "@metadata"
    ], 
    "get": true, 
    "package": "sysmon", 
    "resource_name": "vsps", 
    "rest_name": "vsp", 
    "update": true
}