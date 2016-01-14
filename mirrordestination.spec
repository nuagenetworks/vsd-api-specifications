{
    "attributes": {
        "destinationIp": {
            "description": "IP address of the destination server where you want your traffic to be mirrored.",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        },
        "name": {
            "description": "Name of the mirror destination. Valid characters are alphabets, numbers, space and hyphen( - ).",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string",
            "min_length": 1,
            "max_length": 64,
            "uniqueScope": "no"
        },
        "serviceId": {
            "description": "Service ID of the mirror destination.",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "integer",
            "subtype": "long",
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
        "description": "Represents the mirror destination entity.",
        "entity_name": "MirrorDestination",
        "extends": [
            "@base",
            "@audited",
            "@metadata"
        ],
        "get": true,
        "package": "vport",
        "resource_name": "mirrordestinations",
        "rest_name": "mirrordestination",
        "update": true
    }
}