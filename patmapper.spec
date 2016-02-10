{
    "attributes": {
        "description": {
            "description": null,
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string"
        },
        "name": {
            "description": null,
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string",
            "unique": true
        }
    },
    "children": {
        "sharednetworkresource": {
            "get": true,
            "relationship": "member"
        }
    },
    "model": {
        "delete": true,
        "entity_name": "PATMapper",
        "get": true,
        "resource_name": "patmappers",
        "rest_name": "patmapper",
        "update": true
    }
}