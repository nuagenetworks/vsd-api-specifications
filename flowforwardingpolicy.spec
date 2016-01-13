{
    "attributes": {
        "associatedApplicationServiceID": {
            "description": "The associated service id.",
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
        "destinationAddressOverwrite": {
            "description": "The destination address overwrite. Needs to be in CIDR format x.x.x.x/n",
            "exposed": true,
            "filterable": true,
            "format": "CIDR",
            "orderable": true,
            "type": "string",
            "min_length": 1,
            "max_length": 50,
            "uniqueScope": "no"
        },
        "flowID": {
            "description": "The associated service id.",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        },
        "redirectTargetID": {
            "description": "The associated service id.",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        },
        "sourceAddressOverwrite": {
            "description": "The source address overwrite. Needs to be in CIDR format x.x.x.x/n",
            "exposed": true,
            "filterable": true,
            "format": "CIDR",
            "orderable": true,
            "type": "string",
            "min_length": 1,
            "max_length": 50,
            "uniqueScope": "no"
        },
        "type": {
            "description": "The redirect type.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        }
    },
    "children": {
        "eventlog": {
            "get": true,
            "relationship": "child"
        }
    },
    "model": {
        "delete": true,
        "description": "The redirect policy on the flow.",
        "entity_name": "FlowForwardingPolicy",
        "extends": [
            "@base",
            "@metadata"
        ],
        "get": true,
        "package": "appd",
        "resource_name": "flowforwardingpolicies",
        "rest_name": "flowforwardingpolicy",
        "update": true
    }
}