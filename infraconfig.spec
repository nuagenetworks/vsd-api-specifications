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
            "allowed_choices": [
                "UNKNOWN",
                "SUCCESS",
                "FAILURE"
            ],
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "enum",
            "uniqueScope": "no"
        }
    },
    "model": {
        "description": "Represents Infrastructure Config",
        "entity_name": "InfrastructureConfig",
        "extends": [
            "@base",
            "@audited",
            "@metadata"
        ],
        "package": "gateway",
        "resource_name": "infraconfig",
        "rest_name": "infraconfig"
    }
}