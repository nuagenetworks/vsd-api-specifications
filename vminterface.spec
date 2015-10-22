{
    "attributes": {
        "tierID": {
            "description": "ID of the tier that the interface is attached to.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "VPortName": {
            "description": "Name of the vport that the VM is attached to", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "name": {
            "description": "Device name associated with this interface", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "zoneName": {
            "description": "Name of the zone that the VM is attached to", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "domainName": {
            "description": "Name of the domain that the VM is attached to", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "networkName": {
            "description": "Name of the network that the VM is attached to", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "netmask": {
            "description": "Netmask of the subnet that the VM is attached to", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "associatedFloatingIPAddress": {
            "description": "Floating Ip Address of this network interface eg: 10.1.2.1", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "zoneID": {
            "description": "ID of the zone that the interface is attached to", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "MAC": {
            "description": "MAC address of the  interface", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "domainID": {
            "description": "ID of the domain that the VM is attached to", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "attachedNetworkID": {
            "description": "ID of the l2 domain or Subnet that the VM is attached to", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "attachedNetworkType": {
            "description": "l2 domain or Subnet that the interface is attached to", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "multiNICVPortName": {
            "description": "Name of the Multi NIC VPort associated with this VM Interface", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "VMUUID": {
            "description": "UUID of the associated virtual machine", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "policyDecisionID": {
            "description": "The policy decision ID for this particular  interface", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "IPAddress": {
            "description": "IP address of the  interface", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "gateway": {
            "description": "Gateway of the subnet that the VM is connected to", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "VPortID": {
            "description": "ID of the vport that the interface is attached to", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }
    }, 
    "model": {
        "resource_name": "vminterfaces", 
        "description": "Read only API that can retrieve the VM interface associated with a domain, zone or subnet for mediation created VM's for REST created  VM interfaces you need to set the additional proxy header in http request : X-Nuage-ProxyUservalue of the header has to be either :1) enterpriseName@UserName (example :bob@Alcatel Lucent), or 2) external ID of user in VSD, typically is UUID generally decided by the CMS tool in questionUser needs to have CMS privileges to use proxy user header", 
        "entity_name": "VMInterface", 
        "package": "vm", 
        "get": true, 
        "update": true, 
        "rest_name": "vminterface", 
        "extends": [
            "@base", 
            "@metadata"
        ], 
        "delete": true
    }, 
    "children": {
        "statistics": {
            "relationship": "child", 
            "get": true
        }, 
        "redirectiontarget": {
            "relationship": "child", 
            "get": true
        }, 
        "eventlog": {
            "relationship": "child", 
            "get": true
        }, 
        "dhcpoption": {
            "relationship": "child", 
            "get": true
        }, 
        "staticroute": {
            "relationship": "child", 
            "get": true
        }, 
        "multicastchannelmap": {
            "relationship": "child", 
            "get": true
        }, 
        "policygroup": {
            "relationship": "child", 
            "get": true
        }, 
        "policydecision": {
            "relationship": "child", 
            "get": true
        }, 
        "tca": {
            "relationship": "child", 
            "get": true
        }
    }
}