{
    "attributes": {
        "VLANID": {
            "description": "associated Vlan of this vport - applicable for type host/bridge",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "active": {
            "description": "Indicates if this vport is up or down",
            "exposed": true,
            "format": "free",
            "required": true,
            "type": "boolean",
            "uniqueScope": "no"
        },
        "addressSpoofing": {
            "allowed_choices": [
                "DISABLED",
                "ENABLED",
                "INHERITED"
            ],
            "description": "Indicates if address spoofing is ENABLED/DISABLED/INHERITED for this vport Possible values are INHERITED, ENABLED, DISABLED, .",
            "exposed": true,
            "format": "free",
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
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "associatedMulticastChannelMapID": {
            "description": "The ID of the receive Multicast Channel Map this Vport is associated with. This has to be set when enableMultiCast is set to ENABLED",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "associatedSendMulticastChannelMapID": {
            "description": "The ID of the send Multicast Channel Map this Vport is associated with. This has to be set when enableMultiCast is set to ENABLED",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "description": {
            "description": "Description for this vport",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "domainID": {
            "description": "ID the Domain associated with the VPort",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "hasAttachedInterfaces": {
            "description": "Indicates that this vport has attached interfaces",
            "exposed": true,
            "format": "free",
            "type": "boolean",
            "uniqueScope": "no"
        },
        "multiNICVPortID": {
            "description": "ID of the Multi NIC VPort associated with the VPort",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "multicast": {
            "allowed_choices": [
                "DISABLED",
                "ENABLED",
                "INHERITED"
            ],
            "description": "multicast is enum that indicates multicast policy on Vport. Possible values are ENABLED ,DISABLED  and INHERITED Possible values are INHERITED, ENABLED, DISABLED, .",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "type": "enum",
            "uniqueScope": "no"
        },
        "name": {
            "description": "Name of the vport. Valid characters are alphabets, numbers, space and hyphen( - ).",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 64,
            "min_length": 1,
            "orderable": true,
            "required": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "operationalState": {
            "allowed_choices": [
                "DOWN",
                "INIT",
                "UP"
            ],
            "description": "Operational State of the VPort - RUNNING/SHUTDOWN Possible values are INIT, UP, DOWN, .",
            "exposed": true,
            "format": "free",
            "type": "enum",
            "uniqueScope": "no"
        },
        "systemType": {
            "allowed_choices": [
                "HARDWARE",
                "HARDWARE_VTEP",
                "NUAGE_1",
                "NUAGE_2",
                "NUAGE_VRSG",
                "SOFTWARE"
            ],
            "description": "Indicates what system it is - SOFTWARE/HARDWARE_VTEP/HARDWARE/ (possible values)  Possible values are HARDWARE, SOFTWARE, HARDWARE_VTEP, NUAGE_1, NUAGE_2, NUAGE_VRSG, .",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "type": "enum",
            "uniqueScope": "no"
        },
        "type": {
            "allowed_choices": [
                "BRIDGE",
                "HOST",
                "VM"
            ],
            "description": "Type of vport - possible values VM/HOST/BRIDGE Possible values are VM, HOST, BRIDGE, .",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "required": true,
            "type": "enum",
            "uniqueScope": "no"
        },
        "zoneID": {
            "description": "ID the Zone associated with the VPort",
            "exposed": true,
            "format": "free",
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
        "bgpneighbor": {
            "create": true,
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
        "description": "VPorts are a new level in the domain hierarchy, intended to provide more granular configuration than at subnet, and also support a split workflow, where the vPort is configured and associated with a VM port (or gateway port) before the port exists on the hypervisor or gateway.",
        "entity_name": "VPort",
        "extends": [
            "@audited",
            "@base",
            "@metadata"
        ],
        "get": true,
        "package": "vport",
        "resource_name": "vports",
        "rest_name": "vport",
        "update": true
    }
}