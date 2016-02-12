{
    "attributes": {
        "MAC": {
            "description": "The MAC address of the virtual port",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "associatedFloatingIPID": {
            "description": "Id of Floating IP address associated to this virtual ip",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "subnetID": {
            "description": "Id of subnet to which this ip address belongs",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "virtualIP": {
            "description": "Virtual IP address",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "required": true,
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
        "description": "Virtual IP address.",
        "entity_name": "VirtualIP",
        "extends": [
            "@audited",
            "@base",
            "@metadata"
        ],
        "get": true,
        "package": "vport",
        "resource_name": "virtualips",
        "rest_name": "virtualip",
        "update": true
    }
}