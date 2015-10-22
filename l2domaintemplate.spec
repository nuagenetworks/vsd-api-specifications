{
    "attributes": {
        "policyChangeStatus": {
            "description": "", 
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
        "address": {
            "description": "Network address of the L2Domain / L2Domain template defined. ", 
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
        "resource_name": "l2domaintemplates", 
        "description": "L2 Domain in VSD as derived by templates. This object describes the L2 Domain template", 
        "entity_name": "L2DomainTemplate", 
        "package": "network", 
        "get": true, 
        "update": true, 
        "rest_name": "l2domaintemplate", 
        "extends": [
            "@base", 
            "@metadata"
        ], 
        "delete": true
    }, 
    "children": {
        "group": {
            "update": true, 
            "relationship": "child", 
            "get": true
        }, 
        "eventlog": {
            "relationship": "child", 
            "get": true
        }, 
        "permission": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }, 
        "egressacltemplate": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }, 
        "l2domain": {
            "relationship": "child", 
            "get": true
        }, 
        "addressrange": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }, 
        "ingressadvfwdtemplate": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }, 
        "policygrouptemplate": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }, 
        "job": {
            "create": true, 
            "relationship": "child"
        }, 
        "redirectiontargettemplate": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }, 
        "ingressexternalservicetemplate": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }, 
        "ingressacltemplate": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }, 
        "qos": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }
    }
}