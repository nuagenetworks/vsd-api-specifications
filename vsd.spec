{
    "attributes": {
        "URL": {
            "description": "An optional web url for management.",
            "exposed": true,
            "format": "free",
            "max_length": 255,
            "min_length": 1,
            "type": "string",
            "uniqueScope": "no"
        },
        "address": {
            "description": "An optional IP to access this component.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 50,
            "min_length": 1,
            "type": "string",
            "uniqueScope": "no"
        },
        "alreadyMarkedForUnavailable": {
            "description": "Flag to indicate that it is already marked a unavailable.",
            "exposed": true,
            "format": "free",
            "type": "boolean",
            "uniqueScope": "no"
        },
        "averageCPUUsage": {
            "description": "Average CPU usage percentage.",
            "exposed": true,
            "format": "free",
            "subtype": "double",
            "type": "float",
            "uniqueScope": "no"
        },
        "averageMemoryUsage": {
            "description": "Average memory usage percentage.",
            "exposed": true,
            "format": "free",
            "subtype": "double",
            "type": "float",
            "uniqueScope": "no"
        },
        "currentCPUUsage": {
            "description": "Current CPU usage percentage.",
            "exposed": true,
            "format": "free",
            "subtype": "double",
            "type": "float",
            "uniqueScope": "no"
        },
        "currentMemoryUsage": {
            "description": "Current memory usage percentage.",
            "exposed": true,
            "format": "free",
            "subtype": "double",
            "type": "float",
            "uniqueScope": "no"
        },
        "description": {
            "description": "Description of the entity.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 255,
            "type": "string",
            "uniqueScope": "no"
        },
        "disks": {
            "description": "Set of disk usage details.",
            "exposed": true,
            "format": "free",
            "subtype": "object",
            "type": "list",
            "uniqueScope": "no"
        },
        "lastStateChange": {
            "description": "Last state change timestamp (in millis).",
            "exposed": true,
            "format": "free",
            "subtype": "long",
            "type": "integer",
            "uniqueScope": "no"
        },
        "location": {
            "description": "Identifies the entity to be associated with a location.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 128,
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "managementIP": {
            "description": "An optional management IP to log into this component.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 50,
            "min_length": 1,
            "type": "string",
            "uniqueScope": "no"
        },
        "messages": {
            "description": "An array of degraded messages.",
            "exposed": true,
            "format": "free",
            "subtype": "string",
            "type": "list",
            "uniqueScope": "no"
        },
        "mode": {
            "allowed_choices": [
                "CLUSTER",
                "STANDALONE"
            ],
            "description": "Standalone or cluster mode. Possible values are CLUSTER, STANDALONE, .",
            "exposed": true,
            "format": "free",
            "type": "enum",
            "uniqueScope": "no"
        },
        "name": {
            "description": "Identifies the entity with a name.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 128,
            "min_length": 1,
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "peakCPUUsage": {
            "description": "Peek CPU usage percentage.",
            "exposed": true,
            "format": "free",
            "subtype": "double",
            "type": "float",
            "uniqueScope": "no"
        },
        "peakMemoryUsage": {
            "description": "Peek memory usage percentage.",
            "exposed": true,
            "format": "free",
            "subtype": "double",
            "type": "float",
            "uniqueScope": "no"
        },
        "peerAddresses": {
            "description": "A comma separated list of peer addresses, if it is in cluster mode.",
            "exposed": true,
            "format": "free",
            "max_length": 255,
            "min_length": 1,
            "type": "string",
            "uniqueScope": "no"
        },
        "productVersion": {
            "description": "Product version supported by this entity.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 50,
            "min_length": 1,
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "status": {
            "allowed_choices": [
                "ADMIN_DOWN",
                "DOWN",
                "UP"
            ],
            "description": "Computed status of the entity. Possible values are UP, DOWN, ADMIN_DOWN, .",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "enum",
            "uniqueScope": "no"
        },
        "unavailableTimestamp": {
            "description": "The duration the controller is unavailable (in millis).",
            "exposed": true,
            "format": "free",
            "subtype": "long",
            "type": "integer",
            "uniqueScope": "no"
        }
    },
    "children": {
        "alarm": {
            "get": true,
            "relationship": "child"
        },
        "component": {
            "get": true,
            "relationship": "child"
        },
        "eventlog": {
            "get": true,
            "relationship": "child"
        },
        "job": {
            "create": true,
            "relationship": "child"
        }
    },
    "model": {
        "description": "System Monitoring details for VSD.",
        "entity_name": "VSD",
        "extends": [
            "@audited",
            "@base",
            "@metadata"
        ],
        "get": true,
        "package": "sysmon",
        "resource_name": "vsds",
        "rest_name": "vsd",
        "update": true
    }
}