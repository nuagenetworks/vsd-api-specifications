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
            "description": "The ID of the vcenter to which this host is attached",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "associatedVCenterID",
            "orderable": false,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "string",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "VCenter"
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
            "description": "VCenter Managed Object ID of the Datacenter",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 64,
            "max_value": null,
            "min_length": 1,
            "min_value": null,
            "name": "managedObjectID",
            "orderable": true,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "string",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "VCenter Managed Object"
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
            "description": "Name of the shared resource. Valid characters are alphabets, numbers, space and hyphen( - ).",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 64,
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
        }
    ],
    "children": [],
    "model": {
        "create": false,
        "delete": false,
        "description": null,
        "entity_name": "Autodiscovereddatacenter",
        "extends": [
            "@audited",
            "@base"
        ],
        "get": false,
        "package": "vmware",
        "resource_name": "autodiscovereddatacenters",
        "rest_name": "autodiscovereddatacenter",
        "root": false,
        "update": false,
        "userlabel": "Auto Discovered Data Center"
    }
}