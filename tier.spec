{
    "attributes": {
        "address": {
            "description": "IP address of the tier defined.",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        },
        "associatedApplicationID": {
            "description": "The associated network macro ID.",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        },
        "associatedFloatingIPPoolID": {
            "description": "The associated floating IP Pool ID.",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        },
        "associatedNetworkMacroID": {
            "description": "The associated network macro ID.",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        },
        "associatedNetworkObjectID": {
            "description": "The associated network object id.",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        },
        "associatedNetworkObjectType": {
            "description": "The associated network object type. Refer to API section for supported types.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "enum",
            "uniqueScope": "no"
        },
        "description": {
            "description": "Description of the application tier.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string",
            "min_length": 0,
            "max_length": 255,
            "uniqueScope": "no"
        },
        "gateway": {
            "description": "The IP address of the gateway for this tier.",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        },
        "metadata": {
            "description": "Metadata field to store tier related data.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string",
            "min_length": 0,
            "max_length": 255,
            "uniqueScope": "no"
        },
        "name": {
            "description": "Name of the application tier.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "required": true,
            "type": "string",
            "min_length": 1,
            "max_length": 60,
            "uniqueScope": "no"
        },
        "netmask": {
            "description": "Netmask for the tier.",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        },
        "type": {
            "allowed_choices": [
                "NETWORK_MACRO",
                "APPLICATION",
                "STANDARD",
                "APPLICATION_EXTENDED_NETWORK"
            ],
            "description": "Type of the application tier. (Example: STANDARD, NETWORK_MACRO, APPLICATION or APPLICATION_EXTENDED_NETWORK Possible values are STANDARD, NETWORK_MACRO, APPLICATION, APPLICATION_EXTENDED_NETWORK, .",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "required": true,
            "type": "enum",
            "uniqueScope": "no"
        }
    },
    "children": {
        "eventlog": {
            "get": true,
            "relationship": "child"
        },
        "statistics": {
            "get": true,
            "relationship": "child"
        },
        "statisticspolicy": {
            "get": true,
            "relationship": "child"
        },
        "tca": {
            "get": true,
            "relationship": "child"
        },
        "vm": {
            "get": true,
            "relationship": "child"
        },
        "vport": {
            "get": true,
            "relationship": "child",
            "update": true
        }
    },
    "model": {
        "delete": true,
        "description": "Tier represents a portion of an application.",
        "entity_name": "Tier",
        "extends": [
            "@base",
            "@metadata"
        ],
        "get": true,
        "package": "appd",
        "resource_name": "tiers",
        "rest_name": "tier",
        "update": true
    }
}