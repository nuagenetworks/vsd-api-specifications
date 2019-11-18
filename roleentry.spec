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
            "filterable": false,
            "format": null,
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "associatedEntityType",
            "orderable": false,
            "read_only": false,
            "required": true,
            "subtype": null,
            "transient": false,
            "type": "enum",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Associated Entity Type"
        },
        {
            "allowed_chars": null,
            "allowed_choices": [
                "CREATE",
                "CUD_CHILDREN",
                "DELETE",
                "MODIFY",
                "NO_ACCESS",
                "NO_ACCESS_CHILDREN",
                "READ",
                "READ_CHILDREN"
            ],
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "List of Access like READ, READ_CHILDREN, CREATE, MODIFY, DELETE, CUD_CHILDREN, NO_ACCESS, NO_ACCESS_CHILDREN",
            "exposed": true,
            "filterable": false,
            "format": null,
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "roleAccessTypeList",
            "orderable": false,
            "read_only": false,
            "required": true,
            "subtype": "enum",
            "transient": false,
            "type": "list",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Role Access"
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