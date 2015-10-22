{
    "attributes": {
        "maxAddress": {
            "description": "Highest address in the MultiCast range", 
            "format": "free", 
            "filterable": true, 
            "uniqueScope": "no", 
            "required": true, 
            "exposed": true, 
            "orderable": true, 
            "type": "string"
        }, 
        "minAddress": {
            "description": "Lowest address in the MultiCast range", 
            "format": "free", 
            "filterable": true, 
            "uniqueScope": "no", 
            "required": true, 
            "exposed": true, 
            "orderable": true, 
            "type": "string"
        }
    }, 
    "model": {
        "resource_name": "multicastranges", 
        "description": "This is the definition of a MultiCast Range associated with a MultiCast Channel Map", 
        "entity_name": "MultiCastRange", 
        "package": "network", 
        "get": true, 
        "update": true, 
        "rest_name": "multicastrange", 
        "extends": [
            "@base", 
            "@metadata"
        ], 
        "delete": true
    }, 
    "children": {
        "eventlog": {
            "relationship": "child", 
            "get": true
        }
    }
}