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
        "managementIP": {
            "description": "The management IP of the VSC/HSC entity", 
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
        "name": {
            "description": "Identifies the entity with a name.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "vsds": {
            "description": "A collection of VSD id(s) which are identified by this controller.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "list"
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
            "description": "The IP of the VRS entity", 
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
        "model": {
            "description": "The model of the hardware service controller", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "type": {
            "description": "The type of the hardware service controller Possible values are VSA, VSG, DC7X50, NONE, .", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "allowed_choices": [
                "DC7X50", 
                "VSG", 
                "VSA", 
                "NONE"
            ], 
            "orderable": true, 
            "type": "enum"
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
        "resource_name": "hscs", 
        "description": "System Monitoring details for hardware service controllers", 
        "entity_name": "HSC", 
        "package": "sysmon", 
        "get": true, 
        "update": true, 
        "rest_name": "hsc", 
        "extends": [
            "@base", 
            "@metadata"
        ], 
        "delete": true
    }, 
    "children": {
        "vrs": {
            "relationship": "child", 
            "get": true
        }, 
        "eventlog": {
            "relationship": "child", 
            "get": true
        }, 
        "bgppeer": {
            "relationship": "child", 
            "get": true
        }, 
        "monitoringport": {
            "relationship": "child", 
            "get": true
        }, 
        "alarm": {
            "relationship": "child", 
            "get": true
        }, 
        "job": {
            "create": true, 
            "relationship": "child"
        }
    }
}