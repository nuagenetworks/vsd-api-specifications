{
    "attributes": {
        "description": {
            "description": "A description field provided by the user that identifies the MultiCast Channel Map", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "name": {
            "description": "Name of the current entity", 
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
        "resource_name": "multicastchannelmaps", 
        "description": "This is the definition of a MultiCast Channel Map", 
        "entity_name": "MultiCastChannelMap", 
        "package": "network", 
        "get": true, 
        "update": true, 
        "rest_name": "multicastchannelmap", 
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
        }, 
        "multicastrange": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }
    }
}