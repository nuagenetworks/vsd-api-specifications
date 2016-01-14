{
    "attributes": {
        "address": {
            "description": "Floating IP address assigned to the Domain",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "assigned": {
            "description": "True if this floating IP is assigned to a network interface else the value is false",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": false,
            "type": "boolean",
            "uniqueScope": "no"
        },
        "assignedToObjectType": {
            "description": "The object type to which this floating ip is assigned. Eg. vport or virtualip",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "associatedSharedNetworkResourceID": {
            "description": "Id of the shared network resource subnet which was used to get this floating IP address",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "required": true,
            "type": "string",
            "uniqueScope": "no"
        }
    },
    "children": {
        "eventlog": {
            "get": true,
            "relationship": "child"
        },
        "vport": {
            "get": true,
            "relationship": "child"
        }
    },
    "model": {
        "delete": true,
        "description": "Floating IP that is associated to a Domain. This floating IP could be used in the VM interface for NAT functionality",
        "entity_name": "FloatingIp",
        "extends": [
            "@base",
            "@audited",
            "@metadata"
        ],
        "get": true,
        "package": "network",
        "resource_name": "floatingips",
        "rest_name": "floatingip",
        "update": true
    }
}