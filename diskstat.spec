{
    "attributes": {
        "available": {
            "description": "Available disk space.",
            "format": "free",
            "type": "float",
            "uniqueScope": "no"
        },
        "name": {
            "description": "Name of the disk.",
            "filterable": true,
            "format": "free",
            "max_length": 255,
            "min_length": 1,
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "size": {
            "description": "Total disk space.",
            "format": "free",
            "type": "float",
            "uniqueScope": "no"
        },
        "unit": {
            "allowed_choices": [
                "Bytes",
                "EB",
                "GB",
                "KB",
                "MB",
                "PB",
                "TB",
                "YB",
                "ZB"
            ],
            "description": "Storage unit type (example: bytes, KB, MB, etc.,).",
            "format": "free",
            "type": "enum",
            "uniqueScope": "no"
        },
        "used": {
            "description": "Disk space used.",
            "format": "free",
            "type": "float",
            "uniqueScope": "no"
        }
    },
    "model": {
        "description": "Encapsulates the disk usage metrics for system monitor entity.",
        "entity_name": "DiskStat",
        "extends": [
            "@base"
        ],
        "package": "vm",
        "resource_name": "diskstats",
        "rest_name": "diskstat"
    }
}