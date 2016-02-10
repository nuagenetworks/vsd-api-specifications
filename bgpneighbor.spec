{
    "attributes": {
        "associatedExportRoutingPolicyID": {
            "description": "export policy ID",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        },
        "associatedImportRoutingPolicyID": {
            "description": "import routing policy ID",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        },
        "dampeningEnabled": {
            "description": null,
            "exposed": true,
            "filterable": true,
            "orderable": true,
            "type": "boolean",
            "uniqueScope": "no"
        },
        "description": {
            "description": "Short description for this peer",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string"
        },
        "name": {
            "description": "Name of the peer",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "min_length": 1,
            "max_length": 255,
            "type": "string"
        },
        "peerAS": {
            "description": "neighbor's autonomous system",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "required": true,
            "type": "integer",
            "subtype": "long",
            "min_value": 1,
            "max_value": 65535,
            "uniqueScope": "no"
        },
        "peerIP": {
            "description": "IP Address of the neighbor. If the neighbor is attached to a host vPort this is optional or must be the same as the host's IP. For uplink or bridge vPort neighbors the IP address must be specified ",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string",
            "max_length": 255,
            "uniqueScope": "no"
        },
        "session": {
            "description": "neighbor session yang blob",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        }
    },
    "model": {
        "delete": true,
        "entity_name": "BGPNeighbor",
        "extends": [
            "@base",
            "@metadata"
        ],
        "get": true,
        "resource_name": "bgpneighbors",
        "rest_name": "bgpneighbor",
        "update": true
    }
}