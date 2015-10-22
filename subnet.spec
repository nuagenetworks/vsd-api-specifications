{
    "attributes": {
        "templateID": {
            "description": "The ID of the subnet template that this subnet object was derived from", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "gatewayMACAddress": {
            "description": "", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "proxyARP": {
            "description": " when set VRS will act as  ARP Proxy", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "boolean"
        }, 
        "splitSubnet": {
            "description": "Need to add correct description", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "boolean"
        }, 
        "gateway": {
            "description": "The IP address of the gateway of this subnet", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "maintenanceMode": {
            "description": "maintenanceMode is an enum that indicates if the SubNetwork is accepting VM activation requests. Possible values are DISABLED, ENABLED and ENABLED_INHERITED Possible values are .", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "enum"
        }, 
        "IPType": {
            "description": "IPv4 or IPv6(only IPv4 is supported in R1.0) Possible values are IPV4, IPV6, .", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "allowed_choices": [
                "IPV6", 
                "IPV4"
            ], 
            "orderable": true, 
            "type": "enum"
        }, 
        "encryption": {
            "description": "Determines whether or not IPSEC is enabled. Possible values are INHERITED, ENABLED, DISABLED, .", 
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
        "defaultAction": {
            "description": "If PAT is disabled then this flag indicates what to do if routes don't exist in overlay, will default to drop | possible values USE_UNDERLAY, DROP_TRAFFIC Possible values are USE_UNDERLAY, DROP_TRAFFIC, .", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "allowed_choices": [
                "DROP_TRAFFIC", 
                "USE_UNDERLAY"
            ], 
            "orderable": true, 
            "type": "enum"
        }, 
        "associatedApplicationObjectType": {
            "description": "The associated application object type. Refer to API section for supported types.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "enum"
        }, 
        "serviceID": {
            "description": "The service ID used by the VSCs to identify this subnet", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "float"
        }, 
        "routeTarget": {
            "description": "The Route Target value assigned by VSD for this subnet that is used by the BGP-EVPN protocol in VSC", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "public": {
            "description": "when set to true means public subnet under a public zone", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "boolean"
        }, 
        "associatedApplicationID": {
            "description": "The associated application ID.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "description": {
            "description": "A description field provided by the user that identifies the subnet", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "routeDistinguisher": {
            "description": "The Route Distinguisher value assigned by VSD for this subnet that is used by the BGP-EVPN protocol in VSC", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "netmask": {
            "description": "Netmask of the subnet defined", 
            "format": "free", 
            "filterable": true, 
            "uniqueScope": "no", 
            "required": true, 
            "exposed": true, 
            "orderable": true, 
            "type": "string"
        }, 
        "address": {
            "description": "IP address of the subnet defined. In case of zone, this is an optional field for and allows users to allocate an IP address range to a zone. The VSD will auto-assign IP addresses to subnets from this range if a specific IP address is not defined for the subnet", 
            "format": "free", 
            "filterable": true, 
            "uniqueScope": "no", 
            "required": true, 
            "exposed": true, 
            "orderable": true, 
            "type": "string"
        }, 
        "name": {
            "description": "Name of the current entity(Zone or zone template or subnet etc..) Valid characters are alphabets, numbers, space and hyphen( - ).", 
            "format": "free", 
            "filterable": true, 
            "uniqueScope": "no", 
            "required": true, 
            "exposed": true, 
            "orderable": true, 
            "type": "string"
        }, 
        "PATEnabled": {
            "description": "", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "enum"
        }, 
        "associatedApplicationObjectID": {
            "description": "The associated application object ID.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "policyGroupID": {
            "description": "PG ID for the subnet. This is unique per domain and will be in the range 1-4095", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "float"
        }, 
        "associatedMulticastChannelMapID": {
            "description": "The ID of the Multi Cast Channel Map  this Subnet/Subnet Template is associated with. This has to be set when  enableMultiCast is set to ENABLED", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "vnId": {
            "description": "Current Network's  globally unique  VXLAN network identifier generated by VSD", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "float"
        }, 
        "multicast": {
            "description": "multicast is enum that indicates multicast policy on Subnet/Subnet Template. Possible values are ENABLED,DISABLED and INHERITED Possible values are INHERITED, ENABLED, DISABLED, .", 
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
        "associatedSharedNetworkResourceID": {
            "description": "The ID of public subnet that is associated with this subnet", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }
    }, 
    "model": {
        "resource_name": "subnets", 
        "description": "This is the definition of a subnet associated with a zone", 
        "entity_name": "Subnet", 
        "package": "network", 
        "get": true, 
        "update": true, 
        "rest_name": "subnet", 
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
        "qos": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }, 
        "eventlog": {
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
        "vm": {
            "relationship": "child", 
            "get": true
        }, 
        "virtualip": {
            "relationship": "child", 
            "get": true
        }, 
        "ipreservation": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }, 
        "vminterface": {
            "relationship": "child", 
            "get": true
        }, 
        "resync": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }, 
        "vport": {
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