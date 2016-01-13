{
    "attributes": {
        "config": {
            "description": "Infrastructure Config",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "object",
            "uniqueScope": "no"
        },
        "configStatus": {
            "description": "Status of the configuration application",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        }
    },
    "model": {
        "description": "Represents Infrastructure Config",
        "entity_name": "InfrastructureConfig",
        "extends": [
            "@base",
            "@metadata"
        ],
        "package": "gateway",
        "resource_name": "infraconfig",
        "rest_name": "infraconfig"
    }
}