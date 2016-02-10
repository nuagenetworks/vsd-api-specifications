{
    "attributes": {
        "privatePort": {
            "description": null,
            "exposed": true,
            "filterable": true,
            "orderable": true,
            "type": "integer"
        },
        "publicPort": {
            "description": null,
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string"
        }
    },
    "model": {
        "delete": true,
        "entity_name": "PortMapping",
        "get": true,
        "resource_name": "portmappings",
        "rest_name": "portmapping",
        "update": true
    }
}