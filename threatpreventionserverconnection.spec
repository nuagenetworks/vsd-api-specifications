{
    "attributes": [
        {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": true,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "Threat Prevention Server FQDN or IP address",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "FQDN",
            "orderable": false,
            "read_only": true,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "string",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "FQDN"
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
            "description": "Array of the embedded resource Threat Prevention Node Info for each Threat Prevention node.",
            "exposed": true,
            "filterable": false,
            "format": null,
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "nodeInfo",
            "orderable": false,
            "read_only": true,
            "required": false,
            "subtype": "ThreatPreventionNodeInfo",
            "transient": false,
            "type": "list",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Threat Prevention Node Info"
        },
        {
            "allowed_chars": null,
            "allowed_choices": [
                "AUTHENTICATION_FAILED",
                "CONNECTED",
                "DEGRADED",
                "DISCONNECTED",
                "UNREACHABLE"
            ],
            "autogenerated": true,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "VSD instance connection status with Threat Prevention Server",
            "exposed": true,
            "filterable": true,
            "format": null,
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "status",
            "orderable": false,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "enum",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Status"
        }
    ],
    "children": [],
    "model": {
        "allowed_job_commands": null,
        "create": false,
        "delete": true,
        "description": "Represents connection between VSD instance and Threat Prevention Server",
        "entity_name": "ThreatPreventionServerConnection",
        "extends": [],
        "get": true,
        "package": null,
        "resource_name": "threatpreventionserverconnections",
        "rest_name": "threatpreventionserverconnection",
        "root": null,
        "template": null,
        "update": true,
        "userlabel": "Threat Prevention Server Connection"
    }
}