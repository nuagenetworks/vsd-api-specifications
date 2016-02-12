{
    "attributes": {
        "name": {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "Name of the cloud management system",
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
        }
    },
    "children": {},
    "model": {
        "create": false,
        "delete": true,
        "description": "Object that identifies a cloud management system",
        "entity_name": "CloudMgmtSystem",
        "extends": [
            "@base",
            "@audited",
            "@metadata"
        ],
        "get": true,
        "package": "cms",
        "resource_name": "cms",
        "rest_name": "cms",
        "root": false,
        "update": false
    }
}