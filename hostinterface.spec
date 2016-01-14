{
    "attributes": {
        "IPAddress": {
            "description": "IP address of the  interface",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "MAC": {
            "description": "MAC address of the  interface, cannot be modified after creation.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "required": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "VPortID": {
            "description": "ID of the vport that the interface is attached to",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        },
        "VPortName": {
            "description": "Name of the vport that the VM is attached to",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        },
        "associatedFloatingIPAddress": {
            "description": "Floating Ip Address of this network interface eg: 10.1.2.1",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        },
        "attachedNetworkID": {
            "description": "ID of the l2 domain or Subnet that the VM is attached to",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        },
        "attachedNetworkType": {
            "description": "l2 domain or Subnet that the interface is attached to",
            "allowed_choices": [
                "L2DOMAIN", "SUBNET"
            ],
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "enum",
            "uniqueScope": "no"
        },
        "domainID": {
            "description": "ID of the domain that the VM is attached to",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        },
        "domainName": {
            "description": "Name of the domain that the VM is attached to",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        },
        "gateway": {
            "description": "Gateway of the subnet that the VM is connected to",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        },
        "name": {
            "description": "Device name associated with this interface",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "netmask": {
            "description": "Netmask of the subnet that the VM is attached to",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        },
        "networkName": {
            "description": "Name of the network that the VM is attached to",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        },
        "policyDecisionID": {
            "description": "The policy decision ID for this particular  interface",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        },
        "tierID": {
            "description": "ID of the tier that the interface is attached to.",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        },
        "zoneID": {
            "description": "ID of the zone that the interface is attached to",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        },
        "zoneName": {
            "description": "Name of the zone that the VM is attached to",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        }
    },
    "children": {
        "dhcpoption": {
            "get": true,
            "relationship": "child"
        },
        "eventlog": {
            "get": true,
            "relationship": "child"
        },
        "multicastchannelmap": {
            "get": true,
            "relationship": "child"
        },
        "policydecision": {
            "get": true,
            "relationship": "child"
        },
        "policygroup": {
            "get": true,
            "relationship": "child"
        },
        "qos": {
            "create": true,
            "get": true,
            "relationship": "child"
        },
        "redirectiontarget": {
            "get": true,
            "relationship": "child"
        },
        "staticroute": {
            "get": true,
            "relationship": "child"
        },
        "statistics": {
            "get": true,
            "relationship": "child"
        },
        "tca": {
            "get": true,
            "relationship": "child"
        }
    },
    "model": {
        "delete": true,
        "description": "Provides information for each host interface",
        "entity_name": "HostInterface",
        "extends": [
            "@base",
            "@audited",
            "@metadata"
        ],
        "get": true,
        "package": "vport",
        "resource_name": "hostinterfaces",
        "rest_name": "hostinterface",
        "update": true
    }
}