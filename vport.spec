{
    "attributes": {
        "hasAttachedInterfaces": {
            "description": "Indicates that this vport has attached interfaces", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "boolean"
        }, 
        "domainID": {
            "description": "ID the Domain associated with the VPort", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "zoneID": {
            "description": "ID the Zone associated with the VPort", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "description": {
            "description": "Description for this vport", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "systemType": {
            "description": "Indicates what system it is - SOFTWARE/HARDWARE_VTEP/HARDWARE/ (possible values)  Possible values are HARDWARE, SOFTWARE, HARDWARE_VTEP, NUAGE_1, NUAGE_2, NUAGE_VRSG, .", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "allowed_choices": [
                "HARDWARE", 
                "NUAGE_VRSG", 
                "NUAGE_2", 
                "NUAGE_1", 
                "HARDWARE_VTEP", 
                "SOFTWARE"
            ], 
            "orderable": true, 
            "type": "enum"
        }, 
        "associatedFloatingIPID": {
            "description": "Id of Floating IP address associated to this vport", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "addressSpoofing": {
            "required": true, 
            "description": "Indicates if address spoofing is ENABLED/DISABLED/INHERITED for this vport Possible values are INHERITED, ENABLED, DISABLED, .", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "allowed_choices": [
                "ENABLED", 
                "INHERITED", 
                "DISABLED"
            ], 
            "orderable": true, 
            "type": "enum"
        }, 
        "operationalState": {
            "description": "Operational State of the VPort - RUNNING/SHUTDOWN Possible values are INIT, UP, DOWN, .", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "allowed_choices": [
                "DOWN", 
                "UP", 
                "INIT"
            ], 
            "orderable": true, 
            "type": "enum"
        }, 
        "associatedMulticastChannelMapID": {
            "description": "The ID of the receive Multicast Channel Map this Vport is associated with. This has to be set when enableMultiCast is set to ENABLED", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "multicast": {
            "description": "multicast is enum that indicates multicast policy on Vport. Possible values are ENABLED ,DISABLED  and INHERITED Possible values are INHERITED, ENABLED, DISABLED, .", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "allowed_choices": [
                "ENABLED", 
                "INHERITED", 
                "DISABLED"
            ], 
            "orderable": true, 
            "type": "enum"
        }, 
        "VLANID": {
            "description": "associated Vlan of this vport - applicable for type host/bridge", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "multiNICVPortID": {
            "description": "ID of the Multi NIC VPort associated with the VPort", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "active": {
            "description": "Indicates if this vport is up or down", 
            "format": "free", 
            "filterable": true, 
            "uniqueScope": "no", 
            "required": true, 
            "exposed": true, 
            "orderable": true, 
            "type": "boolean"
        }, 
        "associatedSendMulticastChannelMapID": {
            "description": "The ID of the send Multicast Channel Map this Vport is associated with. This has to be set when enableMultiCast is set to ENABLED", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "type": {
            "required": true, 
            "description": "Type of vport - possible values VM/HOST/BRIDGE Possible values are VM, HOST, BRIDGE, .", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "allowed_choices": [
                "HOST", 
                "BRIDGE", 
                "VM"
            ], 
            "orderable": true, 
            "type": "enum"
        }, 
        "name": {
            "description": "Name of the vport. Valid characters are alphabets, numbers, space and hyphen( - ).", 
            "format": "free", 
            "filterable": true, 
            "uniqueScope": "no", 
            "required": true, 
            "exposed": true, 
            "orderable": true, 
            "type": "string"
        }
    }, 
    "model": {
        "resource_name": "vports", 
        "description": "VPorts are a new level in the domain hierarchy, intended to provide more granular configuration than at subnet, and also support a split workflow, where the vPort is configured and associated with a VM port (or gateway port) before the port exists on the hypervisor or gateway", 
        "entity_name": "VPort", 
        "package": "vport", 
        "get": true, 
        "update": true, 
        "rest_name": "vport", 
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
        "redirectiontarget": {
            "update": true, 
            "relationship": "child", 
            "get": true
        }, 
        "statistics": {
            "relationship": "child", 
            "get": true
        }, 
        "policygroup": {
            "update": true, 
            "relationship": "child", 
            "get": true
        }, 
        "eventlog": {
            "relationship": "child", 
            "get": true
        }, 
        "alarm": {
            "relationship": "child", 
            "get": true
        }, 
        "aggregatemetadata": {
            "relationship": "child", 
            "get": true
        }, 
        "dhcpoption": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }, 
        "vm": {
            "relationship": "child", 
            "get": true
        }, 
        "hostinterface": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }, 
        "bridgeinterface": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }, 
        "vminterface": {
            "relationship": "child", 
            "get": true
        }, 
        "vportmirror": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }, 
        "virtualip": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }, 
        "qos": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }, 
        "tca": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }, 
        "statisticspolicy": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }
    }
}