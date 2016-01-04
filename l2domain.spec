{
    "attributes": {
        "DHCPManaged": {
            "description": "decides whether L2Domain / L2Domain template DHCP is managed by VSD", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "boolean", 
            "uniqueScope": "no"
        }, 
        "IPType": {
            "allowed_choices": [
                "IPV6", 
                "IPV4"
            ], 
            "description": "IPv4 or IPv6(only IPv4 is supported in R2.0) Possible values are IPV4, IPV6, .", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "enum", 
            "uniqueScope": "no"
        }, 
        "address": {
            "description": "Network address of the L2Domain / L2Domain template defined. ", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "associatedMulticastChannelMapID": {
            "description": "The ID of the Multi Cast Channel Map this L2Domain / L2Domain template template is associated with. This has to be set when  enableMultiCast is set to ENABLED", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "associatedSharedNetworkResourceID": {
            "description": "The ID of the L2 Domain  that this L2 Domain object is pointing to", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "description": {
            "description": "A description field provided by the user that identifies the L2Domain / L2Domain template.", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "gateway": {
            "description": "The IP address of the gateway of this l2 domain", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "gatewayMACAddress": {
            "description": "The MAC address of the Gateway.", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "maintenanceMode": {
            "allowed_choices": [
                "ENABLED", "DISABLED", "ENABLED_INHERITED"
            ],
            "description": "maintenanceMode is an enum that indicates if the L2Domain is accepting VM activation requests. Possible values are DISABLED, ENABLED and ENABLED_INHERITED Possible values are .",
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "enum", 
            "uniqueScope": "no"
        }, 
        "multicast": {
            "allowed_choices": [
                "ENABLED", 
                "INHERITED", 
                "DISABLED"
            ], 
            "description": "multicast is enum that indicates multicast policy on L2Domain / L2Domain template. Possible values are ENABLED and DISABLED Possible values are INHERITED, ENABLED, DISABLED, .", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "enum", 
            "uniqueScope": "no"
        }, 
        "name": {
            "description": "Name of the L2Domain / L2Domain template,has to be unique within a Enterprise. Valid characters are alphabets, numbers, space and hyphen( - ).", 
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
        "netmask": {
            "description": "Netmask of the L2Domain / L2Domain template defined", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "policyChangeStatus": {
            "description": "", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "enum", 
            "uniqueScope": "no"
        }, 
        "routeDistinguisher": {
            "description": "The Route Distinguisher value assigned by VSD for this subnet that is used by the BGP-EVPN protocol in VSC", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "routeTarget": {
            "description": "The Route Target value assigned by VSD for this subnet that is used by the BGP-EVPN protocol in VSC", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "serviceID": {
            "description": "The service ID used by the VSCs to identify this subnet", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "float", 
            "uniqueScope": "no"
        }, 
        "stretched": {
            "description": "Indicates whether this domain is streched,if so remote VM resolutions will be allowed", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "boolean", 
            "uniqueScope": "no"
        }, 
        "templateID": {
            "description": "The ID of the L2 Domain template that this L2 Domain object was derived from", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "uplinkPreference": {
            "allowed_choices": [
                "SECONDARY", 
                "SYMMETRIC", 
                "SECONDARY_PRIMARY", 
                "PRIMARY", 
                "PRIMARY_SECONDARY"
            ], 
            "description": "Indicates the preferencial path selection for network traffic in this domain - Default is Primary 1 and Secondary 2. Possible values are PRIMARY_SECONDARY, SECONDARY_PRIMARY, PRIMARY, SECONDARY, SYMMETRIC, .", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "enum", 
            "uniqueScope": "no"
        }, 
        "vnId": {
            "description": "Current Network's  globally unique  VXLAN network identifier generated by VSD", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "float", 
            "uniqueScope": "no"
        },
        "encryption": {
            "allowed_choices": [
                "ENABLED",
                "DISABLED"
            ],
            "description": "Determines whether IPSEC is enabled Possible values are ENABLED, DISABLED, .",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "enum",
            "uniqueScope": "no"
        }
    }, 
    "children": {
        "addressrange": {
            "get": true, 
            "relationship": "child"
        }, 
        "bridgeinterface": {
            "get": true, 
            "relationship": "child"
        }, 
        "dhcpoption": {
            "create": true, 
            "get": true, 
            "relationship": "child"
        }, 
        "egressaclentrytemplate": {
            "get": true, 
            "relationship": "child"
        }, 
        "egressacltemplate": {
            "create": true, 
            "get": true, 
            "relationship": "child"
        }, 
        "eventlog": {
            "get": true, 
            "relationship": "child"
        }, 
        "group": {
            "get": true, 
            "relationship": "child", 
            "update": true
        }, 
        "hostinterface": {
            "get": true, 
            "relationship": "child"
        }, 
        "ingressaclentrytemplate": {
            "get": true, 
            "relationship": "child"
        }, 
        "ingressacltemplate": {
            "create": true, 
            "get": true, 
            "relationship": "child"
        }, 
        "ingressadvfwdtemplate": {
            "create": true, 
            "get": true, 
            "relationship": "child"
        }, 
        "ingressexternalservicetemplate": {
            "create": true, 
            "get": true, 
            "relationship": "child"
        }, 
        "job": {
            "create": true, 
            "relationship": "child"
        }, 
        "permission": {
            "create": true, 
            "get": true, 
            "relationship": "child"
        }, 
        "policygroup": {
            "create": true, 
            "get": true, 
            "relationship": "child"
        }, 
        "qos": {
            "create": true, 
            "get": true, 
            "relationship": "child"
        }, 
        "redirectiontarget": {
            "create": true, 
            "get": true, 
            "relationship": "child"
        }, 
        "staticroute": {
            "create": true, 
            "get": true, 
            "relationship": "child"
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
        "uplinkroutedistinguisher": {
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
        "vpnconnection": {
            "create": true, 
            "get": true, 
            "relationship": "child"
        }, 
        "vport": {
            "create": true, 
            "get": true, 
            "relationship": "child"
        }
    }, 
    "model": {
        "delete": true, 
        "description": "This is the definition of a l2 domain associated with a Enterprise", 
        "entity_name": "L2Domain", 
        "extends": [
            "@base", 
            "@metadata"
        ], 
        "get": true, 
        "package": "network", 
        "resource_name": "l2domains", 
        "rest_name": "l2domain", 
        "update": true
    }
}