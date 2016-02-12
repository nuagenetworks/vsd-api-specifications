{
    "attributes": {
        "description": {
            "description": "Description of the External Service.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 255,
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "name": {
            "description": "unique name of the External Service. ",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 255,
            "min_length": 1,
            "orderable": true,
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
    "model": {
        "description": "Representation of End Point.",
        "entity_name": "EndPoint",
        "extends": [
            "@audited",
            "@base",
            "@metadata"
        ],
        "get": true,
        "package": "policy",
        "resource_name": "endpoints",
        "rest_name": "endpoint"
    }
}