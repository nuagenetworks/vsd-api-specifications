{
    "attributes": {
        "associatedMulticastChannelMapID": {
            "description": "The ID of the Multi Cast Channel Map  this domain template is associated with. This has to be set when  enableMultiCast is set to ENABLED", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "description": {
            "description": "Domain template description provided by the user", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "encryption": {
            "allowed_choices": [
                "ENABLED", 
                "DISABLED"
            ], 
            "description": "Determines whether IPSEC is enabled. Possible values are ENABLED, DISABLED, .", 
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
            "description": "multicast is enum that indicates multicast policy on domain. Possible values are ENABLED ,DISABLED  and INHERITED Possible values are INHERITED, ENABLED, DISABLED, .", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "enum", 
            "uniqueScope": "no"
        }, 
        "name": {
            "description": "The name of the domain template, that is unique within an enterprise. Valid characters are alphabets, numbers, space and hyphen( - ).", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "required": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "policyChangeStatus": {
            "allowed_choices": [
                "ENABLED", 
                "DISABLED"
            ], 
            "description": "", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "enum", 
            "uniqueScope": "no"
        }
    }, 
    "children": {
        "domain": {
            "get": true, 
            "relationship": "child", 
            "update": true
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
        "policygrouptemplate": {
            "create": true, 
            "get": true, 
            "relationship": "child"
        }, 
        "qos": {
            "create": true, 
            "get": true, 
            "relationship": "child"
        }, 
        "redirectiontargettemplate": {
            "create": true, 
            "get": true, 
            "relationship": "child"
        }, 
        "subnettemplate": {
            "get": true, 
            "relationship": "child"
        }, 
        "zonetemplate": {
            "create": true, 
            "get": true, 
            "relationship": "child"
        }
    }, 
    "delete": true, 
    "description": "Domains in VSD are created from domain templates. This object provides the definition of the DomainTemplate", 
    "entity_name": "DomainTemplate", 
    "extends": [
        "@base", 
        "@metadata"
    ], 
    "get": true, 
    "package": "network", 
    "resource_name": "domaintemplates", 
    "rest_name": "domaintemplate", 
    "update": true
}