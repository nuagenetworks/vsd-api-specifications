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
            "description": "Managed Object Type or end point",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "associatedManagedObjectType",
            "orderable": true,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "string",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Associated Managed Object Type"
        },
        {
            "allowed_chars": null,
            "allowed_choices": [
                "CREATE",
                "DELETE\n",
                "MODIFY",
                "READ",
                "READ_CHILDREN"
            ],
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "List of Access.",
            "exposed": true,
            "filterable": true,
            "format": null,
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "roleAccessTypeList",
            "orderable": true,
            "read_only": false,
            "required": false,
            "subtype": "enum",
            "transient": false,
            "type": "list",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Role Access Type List"
        }
    ],
    "children": [],
    "model": {
        "allowed_job_commands": null,
        "create": false,
        "delete": false,
        "description": "Entry for each end point with assoicatiated permissions.",
        "entity_name": "Roleentry",
        "extends": [],
        "get": true,
        "package": null,
        "resource_name": "roleentries",
        "rest_name": "roleentry",
        "root": null,
        "template": null,
        "update": false,
        "userlabel": "Role Entry"
    }
}