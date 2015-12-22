{
    "attributes": {
        "DHCPBehavior": {
            "allowed_choices": [
                "CONSUME", 
                "FLOOD", 
                "RELAY"
            ], 
            "description": "DHCPBehaviorType is an enum that indicates DHCP Behavior of VRS having VM's under this domain. Possible values are FLOOD, CONSUME ,RELAY Possible values are CONSUME, FLOOD, RELAY, .", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "enum", 
            "uniqueScope": "no"
        }, 
        "DHCPServerAddress": {
            "description": "when DHCPBehaviorType is RELAY, then DHCP Server IP Address needs to be set", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "ECMPCount": {
            "description": "Domain specific Equal-cost multi-path routing count, ECMPCount = 1 means no ECMP", 
            "exposed": true, 
            "filterable": true, 
            "orderable": true,
            "type": "integer", 
            "min_value": 1,
            "max_value": 8,
            "default_value": 8,
            "uniqueScope": "no"
        }, 
        "PATEnabled": {
            "allowed_choices": [
                "ENABLED", 
                "INHERITED", 
                "DISABLED"
            ], 
            "description": "Indicates whether PAT is enabled for the subnets in this domain - ENABLED/DISABLED Possible values are INHERITED, ENABLED, DISABLED, .", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "enum", 
            "uniqueScope": "no"
        }, 
        "applicationDeploymentPolicy": {
            "allowed_choices": [
                "ZONE", 
                "NONE"
            ], 
            "description": "Application deployment policy. Possible values are NONE, ZONE, .", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "enum", 
            "uniqueScope": "no"
        }, 
        "associatedMulticastChannelMapID": {
            "description": "The ID of the Multi Cast Channel Map  this domain is associated with. This has to be set when  enableMultiCast is set to ENABLED", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "backHaulRouteDistinguisher": {
            "description": "Route distinguisher associated with the BackHaul Service in dVRS. If not provided during creation, System generates this identifier automatically", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "backHaulRouteTarget": {
            "description": "Route target associated with the BackHaul Service in dVRS. If not provided during creation, System generates this identifier automatically", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "backHaulVNID": {
            "description": "Current BackHaul Network's globally unique  VXLAN network identifier generated by VSD", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "float", 
            "uniqueScope": "no"
        }, 
        "customerID": {
            "description": "The customerID that is created in the VSC and identifies this dVRS. This is auto-generated by VSD", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "float", 
            "uniqueScope": "no"
        }, 
        "description": {
            "description": "A description string of the domain that is provided by the user", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "min_length": 0,
            "max_length": 255,
            "uniqueScope": "no"
        }, 
        "dhcpServerAddresses": {
            "description": "when DHCPBehaviorType is RELAY, then DHCP Server IP Address needs to be set", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "list", 
            "subtype": "string",
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
        }, 
        "exportRouteTarget": {
            "description": "Route target associated with the dVRS. It is an optional parameterthat can be provided by the user or auto-managed by VSDSystem generates this identifier automatically, if not provided", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "globalRoutingEnabled": {
            "description": "Indicates if this domain is a globally routable domain or not - boolean true/false", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "boolean", 
            "uniqueScope": "no"
        }, 
        "importRouteTarget": {
            "description": "Route distinguisher associated with the dVRS. It is an optional parameter that can be provided by the user or auto-managed by VSD. System generates this identifier automatically, if not provided", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "labelID": {
            "description": "The label associated with the dVRS. This is a read only attribute", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "float", 
            "uniqueScope": "no"
        }, 
        "leakingEnabled": {
            "description": "Indicates if this domain is a leakable domain or not - boolean true/false", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "boolean", 
            "uniqueScope": "no"
        }, 
        "maintenanceMode": {
            "description": "maintenanceMode is an enum that indicates if the Domain is accepting VM activation requests. Possible values are DISABLED, ENABLED and ENABLED_INHERITED Possible values are .", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "enum",
            "allowed_choices": [
                "ENABLED", "DISABLED", "ENABLED_INHERITED"
            ],
            "uniqueScope": "no"
        }, 
        "multicast": {
            "allowed_choices": [
                "ENABLED", 
                "INHERITED", 
                "DISABLED"
            ], 
            "description": "multicast is enum that indicates multicast policy on domain. Possible values are ENABLED ,DISABLED  and INHERITED Possible values are INHERITED, ENABLED, DISABLED, .", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "enum", 
            "uniqueScope": "no"
        }, 
        "name": {
            "description": "The name of the domain. Valid characters are  alphabets, numbers, space and hyphen( - ).", 
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
        "permittedAction": {
            "allowed_choices": [
                "EXTEND", 
                "INSTANTIATE", 
                "DEPLOY", 
                "USE", 
                "READ", 
                "ALL"
            ], 
            "description": "The permitted  action to USE/DEPLOY for the Domain Possible values are USE, READ, ALL, INSTANTIATE, EXTEND, DEPLOY, .", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "enum", 
            "uniqueScope": "no"
        }, 
        "policyChangeStatus": {
            "allowed_choices": [
                "EXTEND", 
                "INSTANTIATE", 
                "DEPLOY", 
                "USE", 
                "READ", 
                "ALL"
            ], 
            "description": "", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "enum", 
            "uniqueScope": "no"
        }, 
        "routeDistinguisher": {
            "description": "Route distinguisher associated with the dVRS. It is an optional parameter that can be provided by the user or auto-managed by VSD. System generates this identifier automatically, if not provided", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "routeTarget": {
            "description": "Route target associated with the dVRS. It is an optional parameterthat can be provided by the user or auto-managed by VSDSystem generates this identifier automatically, if not provided", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "secondaryDHCPServerAddress": {
            "description": "when DHCPBehaviorType is RELAY, then DHCP Server IP Address needs to be set", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "serviceID": {
            "description": "The serviceID of the Virtual Router created in VSC and is associated with this object. This is auto-generated by VSD", 
            "exposed": true, 
            "filterable": true, 
            "orderable": true,
            "format": "long",
            "type": "integer",
            "min_value": 1,
            "autogenerated": true,
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
            "description": "The ID of the template that this domain was created from. This should be set when instantiating a domain", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "required": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "tunnelType": {
            "allowed_choices": [
                "DC_DEFAULT", 
                "VXLAN", 
                "GRE"
            ], 
            "description": "Default Domain Tunnel Type .Possible values are VXLAN,GRE Possible values are DC_DEFAULT, GRE, VXLAN, .", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "enum", 
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
        }
    }, 
    "children": {
        "bridgeinterface": {
            "get": true, 
            "relationship": "child"
        }, 
        "dhcpoption": {
            "create": true, 
            "get": true, 
            "relationship": "child"
        }, 
        "domain": {
            "get": true, 
            "relationship": "child", 
            "update": true
        }, 
        "domaintemplate": {
            "get": true, 
            "relationship": "child", 
            "update": true
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
        "externalappservice": {
            "create": true, 
            "get": true, 
            "relationship": "child"
        }, 
        "floatingip": {
            "create": true, 
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
        "subnet": {
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
            "get": true, 
            "relationship": "child"
        }, 
        "zone": {
            "create": true, 
            "get": true, 
            "relationship": "child"
        }
    }, 
    "model": {
        "delete": true, 
        "description": "This object is used to manipulate domain state. A domain corresponds to a distributed Virtual Router and Switch (dVRS)", 
        "entity_name": "Domain", 
        "extends": [
            "@base", 
            "@metadata"
        ], 
        "get": true, 
        "package": "network", 
        "resource_name": "domains", 
        "rest_name": "domain", 
        "update": true
    }
}