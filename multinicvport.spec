{
    "attributes": {
        "name": {
            "description": "Name for the Multi NIC VPort.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }
    }, 
    "model": {
        "resource_name": "multinicvports", 
        "description": "Encapsulates the Multi NIC VPort information for system monitor entity.", 
        "entity_name": "MultiNICVPort", 
        "package": "sysmon", 
        "get": true, 
        "rest_name": "multinicvport", 
        "extends": [
            "@base", 
            "@metadata"
        ]
    }, 
    "children": {
        "vport": {
            "relationship": "child", 
            "get": true
        }
    }
}