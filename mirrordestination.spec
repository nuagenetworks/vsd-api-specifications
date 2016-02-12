{
    "attributes": {
        "destinationIp": {
            "description": "IP address of the destination server where you want your traffic to be mirrored.",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "name": {
            "description": "Name of the mirror destination. Valid characters are alphabets, numbers, space and hyphen( - ).",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 64,
            "min_length": 1,
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "serviceId": {
            "description": "Service ID of the mirror destination.",
            "exposed": true,
            "format": "free",
            "subtype": "long",
            "type": "integer",
            "uniqueScope": "no"
        }
    },
    "children": {
        "vportmirror": {
            "get": true,
            "relationship": "child"
        }
    },
    "model": {
        "delete": true,
        "description": "Represents a mirror destination.",
        "entity_name": "MirrorDestination",
        "extends": [
            "@audited",
            "@base",
            "@metadata"
        ],
        "get": true,
        "package": "vport",
        "resource_name": "mirrordestinations",
        "rest_name": "mirrordestination",
        "update": true
    }
}