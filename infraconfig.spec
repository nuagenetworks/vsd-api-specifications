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
            "allowed_choices": [
                "FAILURE",
                "SUCCESS",
                "UNKNOWN"
            ],
            "description": "Status of the configuration application",
            "exposed": true,
            "format": "free",
            "type": "enum",
            "uniqueScope": "no"
        }
    },
    "model": {
        "description": "Represents Infrastructure Config.",
        "entity_name": "InfrastructureConfig",
        "extends": [
            "@audited",
            "@base",
            "@metadata"
        ],
        "package": "gateway",
        "resource_name": "infraconfig",
        "rest_name": "infraconfig"
    }
}