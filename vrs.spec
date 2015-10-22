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
        "managementIP": {
            "description": "The management IP of the VRS entity", 
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
        "dynamic": {
            "description": "Flag to indicate it is dynamically configured or not.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "boolean"
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
        "JSONRPCConnectionState": {
            "description": "The current JSON RPC connection status. Possible values are UP, DOWN, ADMIN_DOWN, .", 
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
        "multiNICVPortEnabled": {
            "description": "VRS is in Multi-NIC VPORT Mode", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "boolean"
        }, 
        "hypervisorName": {
            "description": "The hypervisor name associated with the VRS.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "uptime": {
            "description": "How long the VRS was up.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "float"
        }, 
        "numberOfBridgeInterfaces": {
            "description": "Number of bridge interfaces defined in this VRS.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "integer"
        }, 
        "clusterNodeRole": {
            "description": "Indicate that the controller associated is primary, secondary or unknown. Possible values are PRIMARY, SECONDARY, NONE, .", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "allowed_choices": [
                "SECONDARY", 
                "PRIMARY", 
                "NONE"
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
        "hypervisorIdentifier": {
            "description": "The hypervisor IP (or name) associated with the VRS.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "lastEventName": {
            "description": "The last event name from the hypervisor.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
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
        "numberOfHostInterfaces": {
            "description": "Number of host interfaces defined in this VRS.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "integer"
        }, 
        "role": {
            "description": "Flag to indicate that VRS-G redundancy state (active/standby/standalone).  Only applicable for gateways. Possible values are MASTER, SLAVE, NONE, .", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "allowed_choices": [
                "SLAVE", 
                "MASTER", 
                "NONE"
            ], 
            "orderable": true, 
            "type": "enum"
        }, 
        "hypervisorConnectionState": {
            "description": "The VRS connection state with the hypervisor. Possible values are UP, DOWN, ADMIN_DOWN, .", 
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
        "lastEventTimestamp": {
            "description": "The last event timestamp from the hypervisor.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "float"
        }, 
        "averageMemoryUsage": {
            "description": "Average memory usage percentage.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "float"
        }, 
        "dbSynced": {
            "description": "Flag to indicate if the ovs database is synced between the NSG pair part of a redundant group", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "boolean"
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
        "description": {
            "description": "Description of the entity.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "lastEventObject": {
            "description": "The last event object (including metadata) from the hypervisor.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
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
        "peer": {
            "description": "The redundant peer id for the current VRS.", 
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
        "numberOfVirtualMachines": {
            "description": "Number of VMs defined in this VRS.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "integer"
        }, 
        "hypervisorType": {
            "description": "The hypervisor type associated with the VRS.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "parentIDs": {
            "description": "Holds VRS controllers ids", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "list"
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
        "messages": {
            "description": "An array of degraded messages.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "list"
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
        "personality": {
            "description": "VRS personality. Possible values are VRSG, VRS, NSG, NONE, HARDWARE_VTEP, .", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "allowed_choices": [
                "VRSG", 
                "VRS", 
                "HARDWARE_VTEP", 
                "NONE", 
                "NSG"
            ], 
            "orderable": true, 
            "type": "enum"
        }
    }, 
    "model": {
        "resource_name": "vrss", 
        "description": "System Monitoring details for VRS connected to VSC or HSC", 
        "entity_name": "VRS", 
        "package": "sysmon", 
        "get": true, 
        "update": true, 
        "rest_name": "vrs", 
        "extends": [
            "@base", 
            "@metadata"
        ], 
        "delete": true
    }, 
    "children": {
        "hsc": {
            "update": true, 
            "relationship": "child"
        }, 
        "eventlog": {
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
        "vm": {
            "relationship": "child", 
            "get": true
        }, 
        "job": {
            "create": true, 
            "relationship": "child"
        }, 
        "vsc": {
            "update": true, 
            "relationship": "child"
        }, 
        "vport": {
            "relationship": "child", 
            "get": true
        }, 
        "multinicvport": {
            "relationship": "child", 
            "get": true
        }
    }
}