{
    "attributes": {
        "lastStateChange": {
            "description": "Last state change timestamp (in millis).", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "float"
        }, 
        "status": {
            "description": "Computed status of the entity. Possible values are UP, DOWN, ADMIN_DOWN, .", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "allowed_choices": [
                "DOWN", 
                "UP", 
                "ADMIN_DOWN"
            ], 
            "orderable": true, 
            "type": "enum"
        }, 
        "disks": {
            "description": "Set of disk usage details.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "list"
        }, 
        "description": {
            "description": "Description of the entity.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "alreadyMarkedForUnavailable": {
            "description": "Flag to indicate that it is already marked a unavailable.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "boolean"
        }, 
        "URL": {
            "description": "An optional web url for management.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "name": {
            "description": "Identifies the entity with a name.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "managementIP": {
            "description": "An optional management IP to log into this component.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "currentCPUUsage": {
            "description": "Current CPU usage percentage.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "float"
        }, 
        "messages": {
            "description": "An array of degraded messages.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "list"
        }, 
        "productVersion": {
            "description": "Product version supported by this entity.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "peakMemoryUsage": {
            "description": "Peek memory usage percentage.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "float"
        }, 
        "mode": {
            "description": "Standalone or cluster mode. Possible values are CLUSTER, STANDALONE, .", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "allowed_choices": [
                "CLUSTER", 
                "STANDALONE"
            ], 
            "orderable": true, 
            "type": "enum"
        }, 
        "currentMemoryUsage": {
            "description": "Current memory usage percentage.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "float"
        }, 
        "unavailableTimestamp": {
            "description": "The duration the controller is unavailable (in millis).", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "float"
        }, 
        "location": {
            "description": "Identifies the entity to be associated with a location.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "peakCPUUsage": {
            "description": "Peek CPU usage percentage.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "float"
        }, 
        "address": {
            "description": "An optional IP to access this component.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "averageCPUUsage": {
            "description": "Average CPU usage percentage.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "float"
        }, 
        "peerAddresses": {
            "description": "A comma separated list of peer addresses, if it is in cluster mode.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "averageMemoryUsage": {
            "description": "Average memory usage percentage.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "float"
        }
    }, 
    "model": {
        "resource_name": "vsds", 
        "description": "System Monitoring details for VSD", 
        "entity_name": "VSD", 
        "package": "sysmon", 
        "get": true, 
        "update": true, 
        "rest_name": "vsd", 
        "extends": [
            "@base", 
            "@metadata"
        ]
    }, 
    "children": {
        "alarm": {
            "relationship": "child", 
            "get": true
        }, 
        "component": {
            "relationship": "child", 
            "get": true
        }, 
        "job": {
            "create": true, 
            "relationship": "child"
        }, 
        "eventlog": {
            "relationship": "child", 
            "get": true
        }
    }
}