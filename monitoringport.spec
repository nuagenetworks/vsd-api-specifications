{
    "attributes": {
        "access": {
            "description": "Flag to indicate that it is a access port or network port.",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "boolean",
            "uniqueScope": "no"
        },
        "description": {
            "description": "Optional port description.",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "min_length": 1,
            "max_length": 255,
            "uniqueScope": "no"
        },
        "lastStateChange": {
            "description": "Last port state change timestamp.",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "integer",
            "subtype": "long",
            "uniqueScope": "no"
        },
        "name": {
            "description": "Name for the port.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string",
            "min_length": 1,
            "max_length": 255,
            "uniqueScope": "no"
        },
        "resiliencyState": {
            "allowed_choices": [
                "none",
                "master",
                "backup"
            ],
            "description": "",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "enum",
            "uniqueScope": "no"
        },
        "resilient": {
            "description": "Flag to indicate if an ACCESS port is resilient or not.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "boolean",
            "uniqueScope": "no"
        },
        "state": {
            "allowed_choices": [
                "DOWN",
                "UP",
                "ADMIN_DOWN"
            ],
            "description": "The current state of the port. Possible values are UP, DOWN, ADMIN_DOWN, .",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "enum",
            "uniqueScope": "no"
        },
        "uplink": {
            "description": "Flag to indicate that is an uplink or downlink port.",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "boolean",
            "uniqueScope": "no"
        }
    },
    "model": {
        "description": "Encapsulates the port information for system monitor entity.",
        "entity_name": "MonitoringPort",
        "extends": [
            "@base",
            "@metadata"
        ],
        "package": "sysmon",
        "resource_name": "monitoringports",
        "rest_name": "monitoringport"
    }
}