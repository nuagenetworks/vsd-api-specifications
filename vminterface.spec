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
            "description": "MAC address of the  interface",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "VMUUID": {
            "description": "UUID of the associated virtual machine",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
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
                "L2DOMAIN",
                "SUBNET"
            ],
            "exposed": true,
            "filterable": false,
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
        "multiNICVPortName": {
            "description": "Name of the Multi NIC VPort associated with this VM Interface",
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
        "description": "Read only API that can retrieve the VM interface associated with a domain, zone or subnet for mediation created VM's for REST created  VM interfaces you need to set the additional proxy header in http request : X-Nuage-ProxyUservalue of the header has to be either :1) enterpriseName@UserName (example :bob@Alcatel Lucent), or 2) external ID of user in VSD, typically is UUID generally decided by the CMS tool in questionUser needs to have CMS privileges to use proxy user header",
        "entity_name": "VMInterface",
        "extends": [
            "@base",
            "@audited",
            "@metadata"
        ],
        "get": true,
        "package": "vm",
        "resource_name": "vminterfaces",
        "rest_name": "vminterface",
        "update": true
    }
}