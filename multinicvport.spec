{
    "attributes": {
        "name": {
            "description": "Name for the Multi NIC VPort.", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }
    }, 
    "children": {
        "vport": {
            "get": true, 
            "relationship": "child"
        }
    }, 
    "model": {
        "description": "Encapsulates the Multi NIC VPort information for system monitor entity.", 
        "entity_name": "MultiNICVPort", 
        "extends": [
            "@base", 
            "@metadata"
        ], 
        "get": true, 
        "package": "sysmon", 
        "resource_name": "multinicvports", 
        "rest_name": "multinicvport"
    }
}