{
    "attributes": {
        "description": {
            "description": "A description field provided by the user that identifies the MultiCast Channel Map",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": false,
            "type": "string",
            "min_length": 0,
            "max_length": 255,
            "uniqueScope": "no"
        },
        "name": {
            "description": "Name of the current entity",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "required": true,
            "type": "string",
            "min_length": 1,
            "max_length": 64,
            "uniqueScope": "no"
        }
    },
    "children": {
        "eventlog": {
            "get": true,
            "relationship": "child"
        },
        "multicastrange": {
            "create": true,
            "get": true,
            "relationship": "child"
        }
    },
    "model": {
        "delete": true,
        "description": "This is the definition of a MultiCast Channel Map",
        "entity_name": "MultiCastChannelMap",
        "extends": [
            "@base",
            "@metadata"
        ],
        "get": true,
        "package": "network",
        "resource_name": "multicastchannelmaps",
        "rest_name": "multicastchannelmap",
        "update": true
    }
}