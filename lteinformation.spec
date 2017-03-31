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
            "description": "This attribute holds all the information about the LTE dongle plugged in to NSG. This is in JSON format and has information like - Modem Manufacturer, Model Number, Subscriber Number,  Operator etc.",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "lteConnectionInfo",
            "orderable": false,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "string",
            "unique": false,
            "uniqueScope": null
        }
    ],
    "children": [],
    "model": {
        "create": null,
        "delete": false,
        "description": "Contains information about the LTE dongle plugged in USB port on NSG. This would have information like - Modem Manufacturer, Model Number, Subscriber Number, Operator etc. could vary from vendor to vendor.",
        "entity_name": "LTEInformation",
        "extends": [],
        "get": true,
        "package": "nsg",
        "resource_name": "lteinformations",
        "rest_name": "lteinformation",
        "root": null,
        "update": false
    }
}