{
    "attributes": [
        {
            "allowed_chars": null,
            "allowed_choices": [
                "IKE",
                "PAT",
                "UNDERLAY_ROUTE"
            ],
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "Type of forwarding action associated with this entry.",
            "exposed": true,
            "filterable": true,
            "format": null,
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "forwardingAction",
            "orderable": true,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "enum",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Forwarding Action"
        }
    ],
    "children": [],
    "model": {
        "create": null,
        "delete": true,
        "description": "Forwarding path list entry to be associated with forwarding path list for l4 based policy to PAT / IKE to underlay.",
        "entity_name": "ForwardingPathListEntry",
        "extends": [],
        "get": true,
        "package": null,
        "resource_name": "forwardingpathlistentries",
        "rest_name": "forwardingpathlistentry",
        "root": null,
        "update": true,
        "userlabel": "Forwarding Path List Entry"
    }
}