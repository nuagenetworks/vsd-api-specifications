{
    "attributes": {
        "lastRequestTimestamp": {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "Time of the last timestamp received",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "orderable": true,
            "read_only": false,
            "required": false,
            "subtype": "long",
            "transient": false,
            "type": "integer",
            "unique": false,
            "uniqueScope": "no"
        },
        "lastTimeResyncInitiated": {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "Time that the resync was initiated",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "orderable": true,
            "read_only": false,
            "required": false,
            "subtype": "long",
            "transient": false,
            "type": "integer",
            "unique": false,
            "uniqueScope": "no"
        },
        "status": {
            "allowed_chars": null,
            "allowed_choices": [
                "IN_PROGRESS",
                "SUCCESS"
            ],
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "Status of the resync",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "orderable": true,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "enum",
            "unique": false,
            "uniqueScope": "no"
        }
    },
    "children": {},
    "model": {
        "create": false,
        "delete": false,
        "description": "Provide information about the state of a VM resync request",
        "entity_name": "VMResync",
        "extends": [
            "@metadata",
            "@base",
            "@audited"
        ],
        "get": false,
        "package": "vm",
        "resource_name": "resync",
        "rest_name": "resync",
        "root": false,
        "update": false
    }
}