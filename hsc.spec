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
            "deprecated": true,
            "description": "The IP of the VRS entity",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "max_length": 50,
            "max_value": null,
            "min_length": 1,
            "min_value": null,
            "name": "address",
            "orderable": false,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "string",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Address"
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
            "description": "The Control IPv4 or IPv6 addresses of the HSC. Example: [10.10.18.10, 2001:10:10:18::10].",
            "exposed": true,
            "filterable": false,
            "format": null,
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "addresses",
            "orderable": false,
            "read_only": false,
            "required": false,
            "subtype": "string",
            "transient": false,
            "type": "list",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Addresses"
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
            "description": "Flag to indicate that it is already marked a unavailable.",
            "exposed": true,
            "filterable": false,
            "format": null,
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "alreadyMarkedForUnavailable",
            "orderable": false,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "boolean",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Already Marked For Unavailable"
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
            "description": "Average CPU usage percentage.",
            "exposed": true,
            "filterable": false,
            "format": null,
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "averageCPUUsage",
            "orderable": false,
            "read_only": false,
            "required": false,
            "subtype": "double",
            "transient": false,
            "type": "float",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Average CPU Usage"
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
            "description": "Average memory usage percentage.",
            "exposed": true,
            "filterable": false,
            "format": null,
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "averageMemoryUsage",
            "orderable": false,
            "read_only": false,
            "required": false,
            "subtype": "double",
            "transient": false,
            "type": "float",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Average Memory Usage"
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
            "description": "Current CPU usage percentage.",
            "exposed": true,
            "filterable": false,
            "format": null,
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "currentCPUUsage",
            "orderable": false,
            "read_only": false,
            "required": false,
            "subtype": "double",
            "transient": false,
            "type": "float",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Current CPU Usage"
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
            "description": "Current memory usage percentage.",
            "exposed": true,
            "filterable": false,
            "format": null,
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "currentMemoryUsage",
            "orderable": false,
            "read_only": false,
            "required": false,
            "subtype": "double",
            "transient": false,
            "type": "float",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Current Memory Usage"
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
            "description": "Description of the entity.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 255,
            "max_value": null,
            "min_length": 0,
            "min_value": null,
            "name": "description",
            "orderable": false,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "string",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Description"
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
            "description": "Set of disk usage details.",
            "exposed": true,
            "filterable": false,
            "format": null,
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "disks",
            "orderable": false,
            "read_only": false,
            "required": false,
            "subtype": "JSON",
            "transient": false,
            "type": "list",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Disks"
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
            "description": "Last state change timestamp (in millis).",
            "exposed": true,
            "filterable": false,
            "format": null,
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "lastStateChange",
            "orderable": false,
            "read_only": false,
            "required": false,
            "subtype": "long",
            "transient": false,
            "type": "integer",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Last State Change"
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
            "description": "Identifies the entity to be associated with a location.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 128,
            "max_value": null,
            "min_length": 0,
            "min_value": null,
            "name": "location",
            "orderable": true,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "string",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Location"
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
            "description": "The management IP of the VSC/HSC entity",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 50,
            "max_value": null,
            "min_length": 1,
            "min_value": null,
            "name": "managementIP",
            "orderable": false,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "string",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Management IP"
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
            "description": "An array of degraded messages.",
            "exposed": true,
            "filterable": false,
            "format": null,
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "messages",
            "orderable": false,
            "read_only": false,
            "required": false,
            "subtype": "string",
            "transient": false,
            "type": "list",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Messages"
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
            "description": "The model of the hardware service controller",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 255,
            "max_value": null,
            "min_length": 1,
            "min_value": null,
            "name": "model",
            "orderable": false,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "string",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Model"
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
            "description": "Identifies the entity with a name.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 128,
            "max_value": null,
            "min_length": 1,
            "min_value": null,
            "name": "name",
            "orderable": true,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "string",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Name"
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
            "description": "Peek CPU usage percentage.",
            "exposed": true,
            "filterable": false,
            "format": null,
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "peakCPUUsage",
            "orderable": false,
            "read_only": false,
            "required": false,
            "subtype": "double",
            "transient": false,
            "type": "float",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Peak CPU Usage"
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
            "description": "Peek memory usage percentage.",
            "exposed": true,
            "filterable": false,
            "format": null,
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "peakMemoryUsage",
            "orderable": false,
            "read_only": false,
            "required": false,
            "subtype": "double",
            "transient": false,
            "type": "float",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Peak Memory Usage"
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
            "description": "Product version supported by this entity.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 50,
            "max_value": null,
            "min_length": 1,
            "min_value": null,
            "name": "productVersion",
            "orderable": true,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "string",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Product Version"
        },
        {
            "allowed_chars": null,
            "allowed_choices": [
                "ADMIN_DOWN",
                "DOWN",
                "UP"
            ],
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "Computed status of the entity. Possible values are UP, DOWN, ADMIN_DOWN, .",
            "exposed": true,
            "filterable": true,
            "format": null,
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "status",
            "orderable": true,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "enum",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Status"
        },
        {
            "allowed_chars": null,
            "allowed_choices": [
                "DC7X50",
                "NONE",
                "VSA",
                "VSG"
            ],
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "The type of the hardware service controller.",
            "exposed": true,
            "filterable": true,
            "format": null,
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "type",
            "orderable": true,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "enum",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Type"
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
            "description": "The duration the controller is unavailable (in millis).",
            "exposed": true,
            "filterable": false,
            "format": null,
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "unavailableTimestamp",
            "orderable": false,
            "read_only": false,
            "required": false,
            "subtype": "long",
            "transient": false,
            "type": "integer",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Unavailable Timestamp"
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
            "description": "A collection of VSD id(s) which are identified by this controller.",
            "exposed": true,
            "filterable": false,
            "format": null,
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "vsds",
            "orderable": false,
            "read_only": false,
            "required": false,
            "subtype": "string",
            "transient": false,
            "type": "list",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "VSDs"
        }
    ],
    "children": [
        {
            "bulk_create": false,
            "bulk_delete": false,
            "bulk_update": false,
            "create": false,
            "delete": false,
            "deprecated": false,
            "get": true,
            "relationship": "child",
            "rest_name": "alarm",
            "update": false
        },
        {
            "bulk_create": false,
            "bulk_delete": false,
            "bulk_update": false,
            "create": false,
            "delete": false,
            "deprecated": false,
            "get": true,
            "relationship": "child",
            "rest_name": "bgppeer",
            "update": false
        },
        {
            "bulk_create": false,
            "bulk_delete": false,
            "bulk_update": false,
            "create": false,
            "delete": false,
            "deprecated": null,
            "get": true,
            "relationship": "child",
            "rest_name": "controllervrslink",
            "update": false
        },
        {
            "bulk_create": false,
            "bulk_delete": false,
            "bulk_update": false,
            "create": false,
            "delete": false,
            "deprecated": false,
            "get": true,
            "relationship": "child",
            "rest_name": "eventlog",
            "update": false
        },
        {
            "bulk_create": false,
            "bulk_delete": false,
            "bulk_update": false,
            "create": true,
            "delete": false,
            "deprecated": false,
            "get": false,
            "relationship": "child",
            "rest_name": "job",
            "update": false
        },
        {
            "bulk_create": false,
            "bulk_delete": false,
            "bulk_update": false,
            "create": false,
            "delete": false,
            "deprecated": false,
            "get": true,
            "relationship": "child",
            "rest_name": "monitoringport",
            "update": false
        }
    ],
    "model": {
        "allowed_job_commands": [
            "RELOAD"
        ],
        "create": false,
        "delete": true,
        "description": "System Monitoring details for hardware service controllers.",
        "entity_name": "HSC",
        "extends": [
            "@audited",
            "@base",
            "@metadata"
        ],
        "get": true,
        "package": "sysmon",
        "resource_name": "hscs",
        "rest_name": "hsc",
        "root": false,
        "template": false,
        "update": true,
        "userlabel": "HSC"
    }
}