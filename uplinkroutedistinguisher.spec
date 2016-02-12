{
    "attributes": {
        "routeDistinguisher": {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "The uplink route distinguisher value is used to identify which route packets should be flowing through with regards to having multiple network ports on the VRS/NSG.",
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
        "uplinkType": {
            "allowed_chars": null,
            "allowed_choices": [
                "RD_PRIMARY1",
                "RD_PRIMARY2",
                "RD_SECONDARY1",
                "RD_SECONDARY2"
            ],
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "Indicates the uplink type associated with the instance of Uplink Route Distinguisher.  Default value is RD Primary1 Possible values are RD_PRIMARY1, RD_PRIMARY2, RD_SECONDARY1, RD_SECONDARY2, .",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "orderable": false,
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
        "description": "Represents a network port uplink route distinguisher value.",
        "entity_name": "UplinkRD",
        "extends": [
            "@base",
            "@audited",
            "@metadata"
        ],
        "get": true,
        "package": "network",
        "resource_name": "uplinkroutedistinguishers",
        "rest_name": "uplinkroutedistinguisher",
        "root": false,
        "update": false
    }
}