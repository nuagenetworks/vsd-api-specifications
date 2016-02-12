{
    "attributes": {
        "defaultAction": {
            "allowed_choices": [
                "ACCEPT",
                "REJECT"
            ],
            "description": "accept/reject",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "required": true,
            "type": "enum",
            "uniqueScope": "no"
        },
        "description": {
            "description": null,
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "name": {
            "creation_only": true,
            "description": "policy name, unique within an enterprise",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "required": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "policyDefinition": {
            "description": "String blob",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        }
    },
    "model": {
        "delete": true,
        "description": "missing documentation.",
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