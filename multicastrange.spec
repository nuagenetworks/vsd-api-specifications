{
    "attributes": {
        "maxAddress": {
            "description": "Highest address in the MultiCast range", 
            "exposed": true, 
            "required": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "minAddress": {
            "description": "Lowest address in the MultiCast range", 
            "exposed": true, 
            "required": true, 
            "type": "string", 
            "uniqueScope": "no"
        }
    }, 
    "children": {
        "eventlog": {
            "get": true, 
            "relationship": "child"
        }
    }, 
    "delete": true, 
    "description": "This is the definition of a MultiCast Range associated with a MultiCast Channel Map", 
    "entity_name": "MultiCastRange", 
    "extends": [
        "@base", 
        "@metadata"
    ], 
    "get": true, 
    "package": "/network", 
    "resource_name": "multicastranges", 
    "rest_name": "multicastrange", 
    "update": true
}