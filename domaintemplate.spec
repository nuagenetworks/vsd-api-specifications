{
    "attributes": {
        "policyChangeStatus": {
            "description": "", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "allowed_choices": [
                "ENABLED", 
                "DISABLED"
            ], 
            "orderable": true, 
            "type": "enum"
        }, 
        "description": {
            "description": "Domain template description provided by the user", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "encryption": {
            "description": "Determines whether IPSEC is enabled. Possible values are ENABLED, DISABLED, .", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "allowed_choices": [
                "ENABLED", 
                "DISABLED"
            ], 
            "orderable": true, 
            "type": "enum"
        }, 
        "associatedMulticastChannelMapID": {
            "description": "The ID of the Multi Cast Channel Map  this domain template is associated with. This has to be set when  enableMultiCast is set to ENABLED", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "multicast": {
            "description": "multicast is enum that indicates multicast policy on domain. Possible values are ENABLED ,DISABLED  and INHERITED Possible values are INHERITED, ENABLED, DISABLED, .", 
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
        "name": {
            "description": "The name of the domain template, that is unique within an enterprise. Valid characters are alphabets, numbers, space and hyphen( - ).", 
            "format": "free", 
            "filterable": true, 
            "uniqueScope": "no", 
            "required": true, 
            "exposed": true, 
            "orderable": true, 
            "type": "string"
        }
    }, 
    "model": {
        "resource_name": "domaintemplates", 
        "description": "Domains in VSD are created from domain templates. This object provides the definition of the DomainTemplate", 
        "entity_name": "DomainTemplate", 
        "package": "network", 
        "get": true, 
        "update": true, 
        "rest_name": "domaintemplate", 
        "extends": [
            "@base", 
            "@metadata"
        ], 
        "delete": true
    }, 
    "children": {
        "domain": {
            "update": true, 
            "relationship": "child", 
            "get": true
        }, 
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
        "zonetemplate": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }, 
        "redirectiontargettemplate": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }, 
        "subnettemplate": {
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