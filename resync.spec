{
    "attributes": {
        "lastRequestTimestamp": {
            "description": "Time of the last timestamp received",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "subtype": "long",
            "type": "integer",
            "uniqueScope": "no"
        },
        "lastTimeResyncInitiated": {
            "description": "Time that the resync was initiated",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "subtype": "long",
            "type": "integer",
            "uniqueScope": "no"
        },
        "status": {
            "allowed_choices": [
                "IN_PROGRESS",
                "SUCCESS"
            ],
            "description": "Status of the resync",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "enum",
            "uniqueScope": "no"
        }
    },
    "model": {
        "description": "Provide information about the state of a VM resync request.",
        "entity_name": "VMResync",
        "extends": [
            "@audited",
            "@base",
            "@metadata"
        ],
        "package": "vm",
        "resource_name": "resync",
        "rest_name": "resync"
    }
}