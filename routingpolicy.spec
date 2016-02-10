{
    "attributes": {
        "defaultAction": {
            "allowed_choices": [
                "REJECT",
                "ACCEPT"
            ],
            "description": "accept/reject",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "required": true,
            "type": "enum"
        },
        "description": {
            "description": null,
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string"
        },
        "name": {
            "creation_only": true,
            "description": "policy name, unique within an enterprise",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "min_length": 1,
            "max_length": 255,
            "orderable": false,
            "required": true,
            "type": "string"
        },
        "policyDefinition": {
            "description": "String blob",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string"
        }
    },
    "model": {
        "delete": true,
        "entity_name": "RoutingPolicy",
        "extends": [
            "@base",
            "@metadata"
        ],
        "get": true,
        "resource_name": "routingpolicies",
        "rest_name": "routingpolicy",
        "update": true
    }
}