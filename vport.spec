{
    "attributes": {
        "VLANID": {
            "description": "associated Vlan of this vport - applicable for type host/bridge",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        },
        "active": {
            "description": "Indicates if this vport is up or down",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "required": true,
            "type": "boolean",
            "uniqueScope": "no"
        },
        "addressSpoofing": {
            "allowed_choices": [
                "ENABLED",
                "INHERITED",
                "DISABLED"
            ],
            "description": "Indicates if address spoofing is ENABLED/DISABLED/INHERITED for this vport Possible values are INHERITED, ENABLED, DISABLED, .",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "required": true,
            "type": "enum",
            "uniqueScope": "no"
        },
        "associatedBGPProfileID": {
            "description": "The ID of the associated BGP profile",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "associatedFloatingIPID": {
            "description": "Id of Floating IP address associated to this vport",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        },
        "associatedMulticastChannelMapID": {
            "description": "The ID of the receive Multicast Channel Map this Vport is associated with. This has to be set when enableMultiCast is set to ENABLED",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        },
        "associatedSendMulticastChannelMapID": {
            "description": "The ID of the send Multicast Channel Map this Vport is associated with. This has to be set when enableMultiCast is set to ENABLED",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        },
        "description": {
            "description": "Description for this vport",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        },
        "domainID": {
            "description": "ID the Domain associated with the VPort",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        },
        "hasAttachedInterfaces": {
            "description": "Indicates that this vport has attached interfaces",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "boolean",
            "uniqueScope": "no"
        },
        "multiNICVPortID": {
            "description": "ID of the Multi NIC VPort associated with the VPort",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        },
        "multicast": {
            "allowed_choices": [
                "ENABLED",
                "INHERITED",
                "DISABLED"
            ],
            "description": "multicast is enum that indicates multicast policy on Vport. Possible values are ENABLED ,DISABLED  and INHERITED Possible values are INHERITED, ENABLED, DISABLED, .",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": false,
            "type": "enum",
            "uniqueScope": "no"
        },
        "name": {
            "description": "Name of the vport. Valid characters are alphabets, numbers, space and hyphen( - ).",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "required": true,
            "type": "string",
            "min_length": 1,
            "max_length": 64,
            "uniqueScope": "no"
        },
        "operationalState": {
            "allowed_choices": [
                "DOWN",
                "UP",
                "INIT"
            ],
            "description": "Operational State of the VPort - RUNNING/SHUTDOWN Possible values are INIT, UP, DOWN, .",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "enum",
            "uniqueScope": "no"
        },
        "systemType": {
            "allowed_choices": [
                "HARDWARE",
                "NUAGE_VRSG",
                "NUAGE_2",
                "NUAGE_1",
                "HARDWARE_VTEP",
                "SOFTWARE"
            ],
            "description": "Indicates what system it is - SOFTWARE/HARDWARE_VTEP/HARDWARE/ (possible values)  Possible values are HARDWARE, SOFTWARE, HARDWARE_VTEP, NUAGE_1, NUAGE_2, NUAGE_VRSG, .",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": false,
            "type": "enum",
            "uniqueScope": "no"
        },
        "type": {
            "allowed_choices": [
                "HOST",
                "BRIDGE",
                "VM"
            ],
            "description": "Type of vport - possible values VM/HOST/BRIDGE Possible values are VM, HOST, BRIDGE, .",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": false,
            "required": true,
            "type": "enum",
            "uniqueScope": "no"
        },
        "zoneID": {
            "description": "ID the Zone associated with the VPort",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        }
    },
    "children": {
        "aggregatemetadata": {
            "get": true,
            "relationship": "child"
        },
        "alarm": {
            "get": true,
            "relationship": "child"
        },
        "bridgeinterface": {
            "create": true,
            "get": true,
            "relationship": "child"
        },
        "dhcpoption": {
            "create": true,
            "get": true,
            "relationship": "child"
        },
        "eventlog": {
            "get": true,
            "relationship": "child"
        },
        "hostinterface": {
            "create": true,
            "get": true,
            "relationship": "child"
        },
        "policygroup": {
            "get": true,
            "relationship": "child",
            "update": true
        },
        "qos": {
            "create": true,
            "get": true,
            "relationship": "child"
        },
        "redirectiontarget": {
            "get": true,
            "relationship": "child",
            "update": true
        },
        "statistics": {
            "get": true,
            "relationship": "child"
        },
        "statisticspolicy": {
            "create": true,
            "get": true,
            "relationship": "child"
        },
        "tca": {
            "create": true,
            "get": true,
            "relationship": "child"
        },
        "virtualip": {
            "create": true,
            "get": true,
            "relationship": "child"
        },
        "vm": {
            "get": true,
            "relationship": "child"
        },
        "vminterface": {
            "get": true,
            "relationship": "child"
        },
        "vportmirror": {
            "create": true,
            "get": true,
            "relationship": "child"
        },
        "vrs": {
            "get": true,
            "relationship": "child"
        }
    },
    "model": {
        "delete": true,
        "description": "VPorts are a new level in the domain hierarchy, intended to provide more granular configuration than at subnet, and also support a split workflow, where the vPort is configured and associated with a VM port (or gateway port) before the port exists on the hypervisor or gateway",
        "entity_name": "VPort",
        "extends": [
            "@base",
            "@audited",
            "@metadata"
        ],
        "get": true,
        "package": "vport",
        "resource_name": "vports",
        "rest_name": "vport",
        "update": true
    }
}