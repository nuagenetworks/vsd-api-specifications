{
    "attributes": {
        "address": {
            "description": "The IP of the VRS entity", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "alreadyMarkedForUnavailable": {
            "description": "Flag to indicate that it is already marked a unavailable.", 
            "exposed": true, 
            "type": "boolean", 
            "uniqueScope": "no"
        }, 
        "averageCPUUsage": {
            "description": "Average CPU usage percentage.", 
            "exposed": true, 
            "type": "float", 
            "uniqueScope": "no"
        }, 
        "averageMemoryUsage": {
            "description": "Average memory usage percentage.", 
            "exposed": true, 
            "type": "float", 
            "uniqueScope": "no"
        }, 
        "currentCPUUsage": {
            "description": "Current CPU usage percentage.", 
            "exposed": true, 
            "type": "float", 
            "uniqueScope": "no"
        }, 
        "currentMemoryUsage": {
            "description": "Current memory usage percentage.", 
            "exposed": true, 
            "type": "float", 
            "uniqueScope": "no"
        }, 
        "description": {
            "description": "Description of the entity.", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "disks": {
            "description": "Set of disk usage details.", 
            "exposed": true, 
            "type": "list", 
            "uniqueScope": "no"
        }, 
        "lastStateChange": {
            "description": "Last state change timestamp (in millis).", 
            "exposed": true, 
            "type": "float", 
            "uniqueScope": "no"
        }, 
        "location": {
            "description": "Identifies the entity to be associated with a location.", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "managementIP": {
            "description": "The management IP of the VSC/HSC entity", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "messages": {
            "description": "An array of degraded messages.", 
            "exposed": true, 
            "type": "list", 
            "uniqueScope": "no"
        }, 
        "name": {
            "description": "Identifies the entity with a name.", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "peakCPUUsage": {
            "description": "Peek CPU usage percentage.", 
            "exposed": true, 
            "type": "float", 
            "uniqueScope": "no"
        }, 
        "peakMemoryUsage": {
            "description": "Peek memory usage percentage.", 
            "exposed": true, 
            "type": "float", 
            "uniqueScope": "no"
        }, 
        "productVersion": {
            "description": "Product version supported by this entity.", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "status": {
            "allowed_choices": [
                "DOWN", 
                "UP", 
                "ADMIN_DOWN"
            ], 
            "description": "Computed status of the entity. Possible values are UP, DOWN, ADMIN_DOWN, .", 
            "exposed": true, 
            "type": "enum", 
            "uniqueScope": "no"
        }, 
        "unavailableTimestamp": {
            "description": "The duration the controller is unavailable (in millis).", 
            "exposed": true, 
            "type": "float", 
            "uniqueScope": "no"
        }, 
        "vsds": {
            "description": "A collection of VSD id(s) which are identified by this controller.", 
            "exposed": true, 
            "type": "list", 
            "uniqueScope": "no"
        }
    }, 
    "children": {
        "alarm": {
            "get": true, 
            "relationship": "child"
        }, 
        "bgppeer": {
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
        }, 
        "monitoringport": {
            "get": true, 
            "relationship": "child"
        }, 
        "vrs": {
            "get": true, 
            "relationship": "child"
        }
    }, 
    "delete": true, 
    "description": "System Monitoring details for VSC", 
    "entity_name": "VSC", 
    "extends": [
        "@base", 
        "@metadata"
    ], 
    "get": true, 
    "package": "/sysmon", 
    "resource_name": "vscs", 
    "rest_name": "vsc", 
    "update": true
}