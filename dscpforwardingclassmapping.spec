{
    "attributes": {
        "DSCP": {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "DSCP value range from enumeration of 65 values :  *, 0, 1, ..., 63",
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
            "type": "string",
            "unique": false,
            "uniqueScope": "no"
        },
        "forwardingClass": {
            "allowed_chars": null,
            "allowed_choices": [
                "A",
                "B",
                "C",
                "D",
                "E",
                "F",
                "G",
                "H",
                "NONE"
            ],
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "Class of service to be used.  Service classes in order of priority are A, B, C, D, E, F, G, and H.",
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
        "delete": true,
        "description": "Provides the definition of a single DSCP -> Forwarding class mapping that is part of a Table used in QoS policies.",
        "entity_name": "DSCPForwardingClassMapping",
        "extends": [
            "@base",
            "@metadata",
            "@audited"
        ],
        "get": true,
        "package": "policy",
        "resource_name": "dscpforwardingclassmappings",
        "rest_name": "dscpforwardingclassmapping",
        "root": false,
        "update": true
    }
}