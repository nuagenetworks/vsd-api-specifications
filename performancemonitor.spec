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
            "description": "Description of application group probe",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 255,
            "max_value": null,
            "min_length": 0,
            "min_value": null,
            "name": "description",
            "orderable": true,
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
            "description": "List of targets for IKE performance monitor probes",
            "exposed": true,
            "filterable": false,
            "format": null,
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "destinationTargetList",
            "orderable": false,
            "read_only": false,
            "required": false,
            "subtype": "String",
            "transient": false,
            "type": "list",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Destination Target List"
        },
        {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": "900",
            "deprecated": false,
            "description": "probation Timer in seconds",
            "exposed": true,
            "filterable": false,
            "format": null,
            "max_length": null,
            "max_value": 15000,
            "min_length": null,
            "min_value": 1000,
            "name": "holdDownTimer",
            "orderable": false,
            "read_only": false,
            "required": false,
            "subtype": "integer",
            "transient": false,
            "type": "integer",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Probation Timer"
        },
        {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": "3000",
            "deprecated": false,
            "description": "interval in seconds",
            "exposed": true,
            "filterable": true,
            "format": null,
            "max_length": null,
            "max_value": 1818000,
            "min_length": null,
            "min_value": 1,
            "name": "interval",
            "orderable": true,
            "read_only": false,
            "required": true,
            "subtype": null,
            "transient": false,
            "type": "integer",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Interval"
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
            "description": "Name of the application group probe",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 255,
            "max_value": null,
            "min_length": 1,
            "min_value": null,
            "name": "name",
            "orderable": true,
            "read_only": false,
            "required": true,
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
            "default_value": "1",
            "deprecated": false,
            "description": "number of packets",
            "exposed": true,
            "filterable": true,
            "format": null,
            "max_length": null,
            "max_value": 9999,
            "min_length": null,
            "min_value": 1,
            "name": "numberOfPackets",
            "orderable": true,
            "read_only": false,
            "required": true,
            "subtype": null,
            "transient": false,
            "type": "integer",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Number Of Packets"
        },
        {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": "108",
            "deprecated": false,
            "description": "Payload size (This is a mandatory field if the networkProbeType = ONEWAY, and optional for probeType = HTTP,IPSEC_AND_VXLAN)",
            "exposed": true,
            "filterable": true,
            "format": null,
            "max_length": null,
            "max_value": 1500,
            "min_length": null,
            "min_value": 137,
            "name": "payloadSize",
            "orderable": true,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "integer",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Payload Size"
        },
        {
            "allowed_chars": null,
            "allowed_choices": [
                "HTTP",
                "IPSEC_AND_VXLAN",
                "ONEWAY"
            ],
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": "ONEWAY",
            "deprecated": false,
            "description": "Type to be assigned to this probe",
            "exposed": true,
            "filterable": true,
            "format": null,
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "probeType",
            "orderable": false,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "enum",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Probe Type"
        },
        {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": "false",
            "deprecated": false,
            "description": "Determines whether this entity is read only.  Read only objects cannot be modified or deleted.",
            "exposed": true,
            "filterable": false,
            "format": null,
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "readOnly",
            "orderable": false,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "boolean",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Read Only"
        },
        {
            "allowed_chars": null,
            "allowed_choices": [
                "A",
                "B",
                "C",
                "D",
                "E",
                "F",
                "G",
                "H"
            ],
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": "H",
            "deprecated": false,
            "description": "Class of service to be used.  Service classes in order of priority are A, B, C, D, E, F, G, and H.",
            "exposed": true,
            "filterable": true,
            "format": null,
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "serviceClass",
            "orderable": true,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "enum",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Service Class"
        },
        {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": "1000",
            "deprecated": false,
            "description": "number of milliseconds to wait until the probe is timed out",
            "exposed": true,
            "filterable": false,
            "format": null,
            "max_length": null,
            "max_value": 5000,
            "min_length": null,
            "min_value": 1000,
            "name": "timeout",
            "orderable": false,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "integer",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Timeout"
        }
    ],
    "children": [
        {
            "bulk_create": false,
            "bulk_delete": false,
            "bulk_update": false,
            "create": false,
            "delete": false,
            "deprecated": null,
            "get": true,
            "relationship": "member",
            "rest_name": "applicationperformancemanagement",
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
            "relationship": "member",
            "rest_name": "nsgateway",
            "update": true
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
            "rest_name": "tier",
            "update": false
        }
    ],
    "model": {
        "create": null,
        "delete": true,
        "description": null,
        "entity_name": "PerformanceMonitor",
        "extends": [
            "@audited",
            "@base"
        ],
        "get": true,
        "package": "perfrouting",
        "resource_name": "performancemonitors",
        "rest_name": "performancemonitor",
        "root": null,
        "update": true,
        "userlabel": "Performance Monitor"
    }
}