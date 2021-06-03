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
            "description": "Domain name within which the source vPort being tested resides.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 255,
            "max_value": null,
            "min_length": 1,
            "min_value": null,
            "name": "domainName",
            "orderable": true,
            "read_only": true,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "string",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Domain Name"
        }
    ],
    "children": [],
    "model": {
        "allowed_job_commands": null,
        "create": false,
        "delete": true,
        "description": "A Scheduled Test Suite Run represents the execution of a given Scheduled Test Suite within a namespace on an NSG. It groups together multiple ICMP Echo Test Runs.",
        "entity_name": "Scheduledtestsuiterun",
        "extends": [],
        "get": true,
        "package": "nsg",
        "resource_name": "scheduledtestsuiteruns",
        "rest_name": "scheduledtestsuiterun",
        "root": null,
        "template": null,
        "update": true,
        "userlabel": "Scheduled Test Suite Run"
    }
}