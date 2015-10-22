{
    "attributes": {
        "JSONRPCConnectionState": {
            "allowed_choices": [
                "DOWN", 
                "UP", 
                "ADMIN_DOWN"
            ], 
            "description": "The current JSON RPC connection status. Possible values are UP, DOWN, ADMIN_DOWN, .", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "enum", 
            "uniqueScope": "no"
        }, 
        "address": {
            "description": "The IP of the VRS entity", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "averageCPUUsage": {
            "description": "Average CPU usage percentage.", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "float", 
            "uniqueScope": "no"
        }, 
        "averageMemoryUsage": {
            "description": "Average memory usage percentage.", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "float", 
            "uniqueScope": "no"
        }, 
        "clusterNodeRole": {
            "allowed_choices": [
                "SECONDARY", 
                "PRIMARY", 
                "NONE"
            ], 
            "description": "Indicate that the controller associated is primary, secondary or unknown. Possible values are PRIMARY, SECONDARY, NONE, .", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "enum", 
            "uniqueScope": "no"
        }, 
        "currentCPUUsage": {
            "description": "Current CPU usage percentage.", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "float", 
            "uniqueScope": "no"
        }, 
        "currentMemoryUsage": {
            "description": "Current memory usage percentage.", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "float", 
            "uniqueScope": "no"
        }, 
        "dbSynced": {
            "description": "Flag to indicate if the ovs database is synced between the NSG pair part of a redundant group", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "boolean", 
            "uniqueScope": "no"
        }, 
        "description": {
            "description": "Description of the entity.", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "disks": {
            "description": "Set of disk usage details.", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "list", 
            "uniqueScope": "no"
        }, 
        "dynamic": {
            "description": "Flag to indicate it is dynamically configured or not.", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "boolean", 
            "uniqueScope": "no"
        }, 
        "hypervisorConnectionState": {
            "allowed_choices": [
                "DOWN", 
                "UP", 
                "ADMIN_DOWN"
            ], 
            "description": "The VRS connection state with the hypervisor. Possible values are UP, DOWN, ADMIN_DOWN, .", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "enum", 
            "uniqueScope": "no"
        }, 
        "hypervisorIdentifier": {
            "description": "The hypervisor IP (or name) associated with the VRS.", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "hypervisorName": {
            "description": "The hypervisor name associated with the VRS.", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "hypervisorType": {
            "description": "The hypervisor type associated with the VRS.", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "lastEventName": {
            "description": "The last event name from the hypervisor.", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "lastEventObject": {
            "description": "The last event object (including metadata) from the hypervisor.", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "lastEventTimestamp": {
            "description": "The last event timestamp from the hypervisor.", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "float", 
            "uniqueScope": "no"
        }, 
        "lastStateChange": {
            "description": "Last state change timestamp (in millis).", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "float", 
            "uniqueScope": "no"
        }, 
        "location": {
            "description": "Identifies the entity to be associated with a location.", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "managementIP": {
            "description": "The management IP of the VRS entity", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "messages": {
            "description": "An array of degraded messages.", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "list", 
            "uniqueScope": "no"
        }, 
        "multiNICVPortEnabled": {
            "description": "VRS is in Multi-NIC VPORT Mode", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "boolean", 
            "uniqueScope": "no"
        }, 
        "name": {
            "description": "Identifies the entity with a name.", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "numberOfBridgeInterfaces": {
            "description": "Number of bridge interfaces defined in this VRS.", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "integer", 
            "uniqueScope": "no"
        }, 
        "numberOfHostInterfaces": {
            "description": "Number of host interfaces defined in this VRS.", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "integer", 
            "uniqueScope": "no"
        }, 
        "numberOfVirtualMachines": {
            "description": "Number of VMs defined in this VRS.", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "integer", 
            "uniqueScope": "no"
        }, 
        "parentIDs": {
            "description": "Holds VRS controllers ids", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "list", 
            "uniqueScope": "no"
        }, 
        "peakCPUUsage": {
            "description": "Peek CPU usage percentage.", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "float", 
            "uniqueScope": "no"
        }, 
        "peakMemoryUsage": {
            "description": "Peek memory usage percentage.", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "float", 
            "uniqueScope": "no"
        }, 
        "peer": {
            "description": "The redundant peer id for the current VRS.", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "personality": {
            "allowed_choices": [
                "VRSG", 
                "VRS", 
                "HARDWARE_VTEP", 
                "NONE", 
                "NSG"
            ], 
            "description": "VRS personality. Possible values are VRSG, VRS, NSG, NONE, HARDWARE_VTEP, .", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "enum", 
            "uniqueScope": "no"
        }, 
        "productVersion": {
            "description": "Product version supported by this entity.", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "role": {
            "allowed_choices": [
                "SLAVE", 
                "MASTER", 
                "NONE"
            ], 
            "description": "Flag to indicate that VRS-G redundancy state (active/standby/standalone).  Only applicable for gateways. Possible values are MASTER, SLAVE, NONE, .", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "enum", 
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
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "enum", 
            "uniqueScope": "no"
        }, 
        "uptime": {
            "description": "How long the VRS was up.", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "float", 
            "uniqueScope": "no"
        }
    }, 
    "children": {
        "alarm": {
            "get": true, 
            "relationship": "child"
        }, 
        "eventlog": {
            "get": true, 
            "relationship": "child"
        }, 
        "hsc": {
            "relationship": "child", 
            "update": true
        }, 
        "job": {
            "create": true, 
            "relationship": "child"
        }, 
        "monitoringport": {
            "get": true, 
            "relationship": "child"
        }, 
        "multinicvport": {
            "get": true, 
            "relationship": "child"
        }, 
        "vm": {
            "get": true, 
            "relationship": "child"
        }, 
        "vport": {
            "get": true, 
            "relationship": "child"
        }, 
        "vsc": {
            "relationship": "child", 
            "update": true
        }
    }, 
    "model": {
        "delete": true, 
        "description": "System Monitoring details for VRS connected to VSC or HSC", 
        "entity_name": "VRS", 
        "extends": [
            "@base", 
            "@metadata"
        ], 
        "get": true, 
        "package": "sysmon", 
        "resource_name": "vrss", 
        "rest_name": "vrs", 
        "update": true
    }
}