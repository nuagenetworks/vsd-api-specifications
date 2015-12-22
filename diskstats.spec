{
    "attributes": {
        "available": {
            "description": "Available disk space.",
            "type": "double",
            "required": false
        },
        "name": {
            "description": "Name of the disk.",
            "type": "string",
            "min_length": 1,
            "max_length": 255,
            "required": false
        },
        "size": {
            "description": "Total disk space.",
            "type": "double",
            "required": false
        },
        "unit": {
            "description": "Storage unit type (example: bytes, KB, MB, etc.,).",
            "type": "enum",
            "allowed_choices": [
                "Bytes", "PB", "MB", "KB", "ZB", "YB", "GB", "EB", "TB"
            ],
            "required": false
        },
        "used": {
            "description": "Disk space used.",
            "type": "double",
            "required": false
        }
    },
    "model": {
        "description": "Encapsulates the disk usage metrics for system monitor entity.",
        "create": false,
        "get": false,
        "update": false,
        "delete": false,
        "package": "vm",
        "resource_name": "diskstats",
        "rest_name": "diskstat"
    }
}
