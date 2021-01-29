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
            "description": "Supplemental infrastructure configuration object having supplemental information required by NSG e.g. blockedPageText, avatar, avatarType etc.",
            "exposed": true,
            "filterable": false,
            "format": null,
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "supplementalConfig",
            "orderable": false,
            "read_only": false,
            "required": false,
            "subtype": "JSON",
            "transient": false,
            "type": "object",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Supplemental Config"
        }
    ],
    "children": [],
    "model": {
        "allowed_job_commands": null,
        "create": false,
        "delete": false,
        "description": "Supplemental infrastructure configuration which includes information in addition to the existing infrastructure configuration. Encapsulates properties with large data or those properties for which the existing infraconfig work-flow is not to be disturbed.",
        "entity_name": "SupplementalInfraConfig",
        "extends": [],
        "get": true,
        "package": null,
        "resource_name": "supplementalinfraconfig",
        "rest_name": "supplementalinfraconfig",
        "root": null,
        "template": null,
        "update": false,
        "userlabel": "Supplemental Infra Config"
    }
}
