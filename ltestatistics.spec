{
    "attributes": [
        {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "End time for the statistics to be retrieved",
            "exposed": true,
            "filterable": false,
            "format": null,
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "endTime",
            "orderable": false,
            "read_only": false,
            "required": false,
            "subtype": "long",
            "transient": false,
            "type": "integer",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "End Time"
        },
        {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "Start time for the statistics to be retrieved",
            "exposed": true,
            "filterable": false,
            "format": null,
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "startTime",
            "orderable": false,
            "read_only": false,
            "required": false,
            "subtype": "long",
            "transient": false,
            "type": "integer",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Start time"
        },
        {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "A list of statistical data returned for a selected LTE interface.  Information returned will contain the cellular signal strength and the current technology used (LTE, HSPA+, 3G, ...).",
            "exposed": true,
            "filterable": false,
            "format": null,
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "statsData",
            "orderable": false,
            "read_only": false,
            "required": false,
            "subtype": "object",
            "transient": false,
            "type": "list",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Stats Data"
        },
        {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "Version of this Sequence number.",
            "exposed": true,
            "filterable": false,
            "format": null,
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "version",
            "orderable": false,
            "read_only": false,
            "required": false,
            "subtype": "long",
            "transient": false,
            "type": "integer",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Version"
        }
    ],
    "children": [],
    "model": {
        "allowed_job_commands": null,
        "create": null,
        "delete": false,
        "description": "Retrieves statistical information for LTE uplinks.",
        "entity_name": "Ltestatistics",
        "extends": [
            "@metadata",
            "@permission"
        ],
        "get": false,
        "package": "stats",
        "resource_name": "ltestatistics",
        "rest_name": "ltestatistics",
        "root": null,
        "template": false,
        "update": false,
        "userlabel": "LTE Statistics"
    }
}