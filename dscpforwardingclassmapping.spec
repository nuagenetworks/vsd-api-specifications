{
    "attributes": {
        "DSCP": {
            "description": "DSCP value range from enumeration of 65 values :  *, 0, 1, ..., 63",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "forwardingClass": {
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
            "description": "Class of service to be used.  Service classes in order of priority are A, B, C, D, E, F, G, and H.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "enum",
            "uniqueScope": "no"
        }
    },
    "model": {
        "delete": true,
        "description": "Provides the definition of a single DSCP to a Forwarding class mapping that is part of a Table used in QoS policies.",
        "entity_name": "DSCPForwardingClassMapping",
        "extends": [
            "@audited",
            "@base",
            "@metadata"
        ],
        "get": true,
        "package": "policy",
        "resource_name": "dscpforwardingclassmappings",
        "rest_name": "dscpforwardingclassmapping",
        "update": true
    }
}