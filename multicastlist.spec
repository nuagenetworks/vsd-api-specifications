{
    "attributes": [
        {
            "allowed_chars": null,
            "allowed_choices": [
                "RECEIVE",
                "SEND"
            ],
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "Type of multicast list.",
            "exposed": true,
            "filterable": true,
            "format": null,
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "mcastType",
            "orderable": true,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "enum",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Multicast Type"
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
            "relationship": "member",
            "rest_name": "multicastchannelmap",
            "update": true
        }
    ],
    "model": {
        "create": false,
        "delete": false,
        "description": "This is the definition of a MultiCast Channel List.",
        "entity_name": "MultiCastList",
        "extends": [
            "@audited",
            "@base",
            "@metadata",
            "@permission"
        ],
        "get": true,
        "package": "network",
        "resource_name": "multicastlists",
        "rest_name": "multicastlist",
        "root": false,
        "update": false,
        "userlabel": "Multicast List"
    }
}