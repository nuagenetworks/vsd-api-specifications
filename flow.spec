{
    "attributes": {
        "description": {
            "description": "Description of the flow.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 255,
            "min_length": 1,
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "destinationTierID": {
            "description": "Flow destination tier id.",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "metadata": {
            "description": "Metadata field to store flow related data.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 255,
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "name": {
            "description": "Name of the flow.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 60,
            "min_length": 1,
            "orderable": true,
            "required": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "originTierID": {
            "description": "Flow origin tier id.",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        }
    },
    "children": {
        "eventlog": {
            "get": true,
            "relationship": "child"
        },
        "flowforwardingpolicy": {
            "create": true,
            "get": true,
            "relationship": "child"
        },
        "flowsecuritypolicy": {
            "create": true,
            "get": true,
            "relationship": "child"
        }
    },
    "model": {
        "delete": true,
        "description": "Flow represents the traffic between two different application tiers.",
        "entity_name": "Flow",
        "extends": [
            "@audited",
            "@base",
            "@metadata"
        ],
        "get": true,
        "package": "appd",
        "resource_name": "flows",
        "rest_name": "flow",
        "update": true
    }
}