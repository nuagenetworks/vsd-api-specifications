{
    "attributes": {
        "name": {
            "description": "Name for the Multi NIC VPort.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 255,
            "min_length": 1,
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        }
    },
    "children": {
        "vport": {
            "get": true,
            "relationship": "child"
        }
    },
    "model": {
        "description": "Encapsulates the Multi NIC VPort information for system monitoring entity.",
        "entity_name": "MultiNICVPort",
        "extends": [
            "@audited",
            "@base",
            "@metadata"
        ],
        "get": true,
        "package": "sysmon",
        "resource_name": "multinicvports",
        "rest_name": "multinicvport"
    }
}