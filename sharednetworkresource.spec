{
    "attributes": {
        "backHaulVNID": {
            "description": "backHaulVNID of the Shared Resource", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "float"
        }, 
        "sharedResourceParentID": {
            "description": "Parent ID of the floating IP subnet to which this FIP subnet must be attached. If empty it will be created in a new domain.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "uplinkInterfaceMAC": {
            "description": "MAC address of the host interface", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "domainRouteDistinguisher": {
            "description": "Route distinguisher configured on the shared resource", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "backHaulRouteDistinguisher": {
            "description": "backHaulRouteDistinguisher of the Shared Resource", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "underlay": {
            "description": "Indicates whether this shared subnet is in underlay or not.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "boolean"
        }, 
        "gateway": {
            "description": "Gatemask configured on the shared resource", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "uplinkGWVlanAttachmentID": {
            "description": "VLAN ID to which this vport must be attached", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "DHCPManaged": {
            "description": "true if DHCP is enabled else it is false. This value is always true for network resource of type PUBLIC or FLOATING.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "boolean"
        }, 
        "domainRouteTarget": {
            "description": "Route target configured on the shared resource", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "type": {
            "description": "Type of the shared resource. This is an enum with possible values PUBLIC/FLOATING/L2DOMAIN/UPLINK_SUBNET", 
            "format": "free", 
            "filterable": true, 
            "uniqueScope": "no", 
            "required": true, 
            "exposed": true, 
            "orderable": true, 
            "type": "enum"
        }, 
        "description": {
            "description": "Description of the shared resource", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "vnID": {
            "description": "VNID of the Shared Resource", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "float"
        }, 
        "permittedActionType": {
            "description": "Permitted action on this shared network resource", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "accessRestrictionEnabled": {
            "description": "Boolean indicates that this shared network resource is avaiable to everyone by default or not", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "boolean"
        }, 
        "netmask": {
            "description": "Netmask configured on the shared resource", 
            "format": "free", 
            "filterable": true, 
            "uniqueScope": "no", 
            "required": true, 
            "exposed": true, 
            "orderable": true, 
            "type": "string"
        }, 
        "address": {
            "description": "Address configured on the shared resource", 
            "format": "free", 
            "filterable": true, 
            "uniqueScope": "no", 
            "required": true, 
            "exposed": true, 
            "orderable": true, 
            "type": "string"
        }, 
        "uplinkVPortName": {
            "description": "Name of the uplink vport", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "backHaulRouteTarget": {
            "description": "backHaulRouteTarget of the Shared Resource", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "name": {
            "description": "Name of the shared resource. Valid characters are alphabets, numbers, space and hyphen( - ).", 
            "format": "free", 
            "filterable": true, 
            "uniqueScope": "no", 
            "required": true, 
            "exposed": true, 
            "orderable": true, 
            "type": "string"
        }, 
        "ECMPCount": {
            "description": "Domain specific Equal-cost multi-path routing count, ECMPCount = 1 means no ECMP", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "integer"
        }, 
        "uplinkInterfaceIP": {
            "description": "IP address of the host interface", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }
    }, 
    "model": {
        "resource_name": "sharednetworkresources", 
        "description": "This defines shared infrastructure resources that are created by user with CSPROOT role. These resources can be used by all the enterprises in the data center for various purposes. Examples of  shared resources are public subnet, floating subnet, public L2 domain etc.", 
        "entity_name": "SharedNetworkResource", 
        "package": "network", 
        "get": true, 
        "update": true, 
        "rest_name": "sharednetworkresource", 
        "extends": [
            "@base", 
            "@metadata"
        ], 
        "delete": true
    }, 
    "children": {
        "enterprisepermission": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }, 
        "addressrange": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }, 
        "dhcpoption": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }, 
        "vpnconnection": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }, 
        "staticroute": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }
    }
}