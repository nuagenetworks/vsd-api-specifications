{
    "attributes": {
        "routeDistinguisher": {
            "description": "The Route Distinguisher value assigned by VSD for this subnet that is used by the BGP-EVPN protocol in VSC", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "policyChangeStatus": {
            "description": "", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "enum"
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
        "description": {
            "description": "A description field provided by the user that identifies the L2Domain / L2Domain template.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "DHCPManaged": {
            "description": "decides whether L2Domain / L2Domain template DHCP is managed by VSD", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "boolean"
        }, 
        "uplinkPreference": {
            "description": "Indicates the preferencial path selection for network traffic in this domain - Default is Primary 1 and Secondary 2. Possible values are PRIMARY_SECONDARY, SECONDARY_PRIMARY, PRIMARY, SECONDARY, SYMMETRIC, .", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "allowed_choices": [
                "SECONDARY", 
                "SYMMETRIC", 
                "SECONDARY_PRIMARY", 
                "PRIMARY", 
                "PRIMARY_SECONDARY"
            ], 
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
        "templateID": {
            "description": "The ID of the L2 Domain template that this L2 Domain object was derived from", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "name": {
            "description": "Name of the L2Domain / L2Domain template,has to be unique within a Enterprise. Valid characters are alphabets, numbers, space and hyphen( - ).", 
            "format": "free", 
            "filterable": true, 
            "uniqueScope": "no", 
            "required": true, 
            "exposed": true, 
            "orderable": true, 
            "type": "string"
        }, 
        "associatedMulticastChannelMapID": {
            "description": "The ID of the Multi Cast Channel Map this L2Domain / L2Domain template template is associated with. This has to be set when  enableMultiCast is set to ENABLED", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "netmask": {
            "description": "Netmask of the L2Domain / L2Domain template defined", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "multicast": {
            "description": "multicast is enum that indicates multicast policy on L2Domain / L2Domain template. Possible values are ENABLED and DISABLED Possible values are INHERITED, ENABLED, DISABLED, .", 
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
        "gatewayMACAddress": {
            "description": "The MAC address of the Gateway.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "stretched": {
            "description": "Indicates whether this domain is streched,if so remote VM resolutions will be allowed", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "boolean"
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
        "address": {
            "description": "Network address of the L2Domain / L2Domain template defined. ", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "maintenanceMode": {
            "description": "maintenanceMode is an enum that indicates if the L2Domain is accepting VM activation requests. Possible values are DISABLED, ENABLED and ENABLED_INHERITED Possible values are .", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "enum"
        }, 
        "associatedSharedNetworkResourceID": {
            "description": "The ID of the L2 Domain  that this L2 Domain object is pointing to", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "gateway": {
            "description": "The IP address of the gateway of this l2 domain", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "IPType": {
            "description": "IPv4 or IPv6(only IPv4 is supported in R2.0) Possible values are IPV4, IPV6, .", 
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
        }
    }, 
    "model": {
        "resource_name": "l2domains", 
        "description": "This is the definition of a l2 domain associated with a Enterprise", 
        "entity_name": "L2Domain", 
        "package": "network", 
        "get": true, 
        "update": true, 
        "rest_name": "l2domain", 
        "extends": [
            "@base", 
            "@metadata"
        ], 
        "delete": true
    }, 
    "children": {
        "qos": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }, 
        "addressrange": {
            "relationship": "child", 
            "get": true
        }, 
        "vm": {
            "relationship": "child", 
            "get": true
        }, 
        "ingressexternalservicetemplate": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }, 
        "vport": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }, 
        "vpnconnection": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }, 
        "tca": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }, 
        "statistics": {
            "relationship": "child", 
            "get": true
        }, 
        "policygroup": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }, 
        "eventlog": {
            "relationship": "child", 
            "get": true
        }, 
        "egressacltemplate": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }, 
        "statisticspolicy": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }, 
        "ingressaclentrytemplate": {
            "relationship": "child", 
            "get": true
        }, 
        "permission": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }, 
        "ingressadvfwdtemplate": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }, 
        "hostinterface": {
            "relationship": "child", 
            "get": true
        }, 
        "job": {
            "create": true, 
            "relationship": "child"
        }, 
        "vminterface": {
            "relationship": "child", 
            "get": true
        }, 
        "staticroute": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }, 
        "group": {
            "update": true, 
            "relationship": "child", 
            "get": true
        }, 
        "redirectiontarget": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }, 
        "dhcpoption": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }, 
        "egressaclentrytemplate": {
            "relationship": "child", 
            "get": true
        }, 
        "bridgeinterface": {
            "relationship": "child", 
            "get": true
        }, 
        "uplinkroutedistinguisher": {
            "relationship": "child", 
            "get": true
        }, 
        "ingressacltemplate": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }
    }
}