{
    "attributes": {
        "access": {
            "description": "Flag to indicate that it is a access port or network port.",
            "exposed": true,
            "format": "free",
            "type": "boolean",
            "uniqueScope": "no"
        },
        "description": {
            "description": "Optional port description.",
            "exposed": true,
            "format": "free",
            "max_length": 255,
            "min_length": 1,
            "type": "string",
            "uniqueScope": "no"
        },
        "lastStateChange": {
            "description": "Last port state change timestamp.",
            "exposed": true,
            "format": "free",
            "subtype": "long",
            "type": "integer",
            "uniqueScope": "no"
        },
        "name": {
            "description": "Name for the port.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 255,
            "min_length": 1,
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "resiliencyState": {
            "allowed_choices": [
                "backup",
                "master",
                "none"
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
                "ADMIN_DOWN",
                "DOWN",
                "UP"
            ],
            "description": "The current state of the port. Possible values are UP, DOWN, ADMIN_DOWN, .",
            "exposed": true,
            "format": "free",
            "type": "enum",
            "uniqueScope": "no"
        },
        "uplink": {
            "description": "Flag to indicate that is an uplink or downlink port.",
            "exposed": true,
            "format": "free",
            "type": "boolean",
            "uniqueScope": "no"
        }
    },
    "model": {
        "description": "Encapsulates the port information for system monitoring entity.",
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