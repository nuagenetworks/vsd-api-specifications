{
    "attributes": {
        "networkID": {
            "description": "The destination network entity that is referenced(subnet/zone/macro)", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "protocol": {
            "description": "Protocol number that must be matched", 
            "format": "free", 
            "filterable": true, 
            "uniqueScope": "no", 
            "required": true, 
            "exposed": true, 
            "orderable": true, 
            "type": "string"
        }, 
        "etherType": {
            "description": "Ether type of the packet to be matched. etherType can be * or a valid hexadecimal value", 
            "format": "free", 
            "filterable": true, 
            "uniqueScope": "no", 
            "required": true, 
            "exposed": true, 
            "orderable": true, 
            "type": "string"
        }, 
        "policyState": {
            "description": "State of the policy.  Possible values are DRAFT, LIVE, .", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "allowed_choices": [
                "DRAFT", 
                "LIVE"
            ], 
            "orderable": true, 
            "type": "enum"
        }, 
        "statsLoggingEnabled": {
            "description": "Is stats logging enabled for this particular template", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "boolean"
        }, 
        "priority": {
            "description": "The priority of the ACL entry that determines the order of entries", 
            "format": "free", 
            "filterable": true, 
            "uniqueScope": "no", 
            "required": true, 
            "exposed": true, 
            "orderable": true, 
            "type": "integer"
        }, 
        "associatedApplicationObjectType": {
            "description": "The associated application object type Refer to API section for supported types.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "allowed_choices": [
                "FORWARD", 
                "REDIRECT", 
                "DROP"
            ], 
            "orderable": true, 
            "type": "enum"
        }, 
        "associatedApplicationObjectID": {
            "description": "The associated application object ID", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "description": {
            "description": "Description of the ACL entry", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "DSCP": {
            "description": "DSCP match condition to be set in the rule. It is either * or from 0-63", 
            "format": "free", 
            "filterable": true, 
            "uniqueScope": "no", 
            "required": true, 
            "exposed": true, 
            "orderable": true, 
            "type": "string"
        }, 
        "addressOverride": {
            "description": "Overrides the source IP for Ingress and destination IP for Egress, macentries will use this adress as the match criteria.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "associatedLiveEntityID": {
            "description": "In the draft mode, the ACL entry refers to this LiveEntity. In non-drafted mode, this is null.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "destinationPort": {
            "description": "The destination port to be matched if protocol is UDP or TCP. Value should be either * or single port number or a port range", 
            "format": "free", 
            "filterable": true, 
            "uniqueScope": "no", 
            "required": true, 
            "exposed": true, 
            "orderable": true, 
            "type": "string"
        }, 
        "sourcePort": {
            "description": "Source port to be matched if protocol is UDP or TCP. Value can be either * or single port number or a port range", 
            "format": "free", 
            "filterable": true, 
            "uniqueScope": "no", 
            "required": true, 
            "exposed": true, 
            "orderable": true, 
            "type": "string"
        }, 
        "networkType": {
            "required": true, 
            "description": "Type of the source network -  VM_SUBNET or VM_ZONE or VM_DOMAIN or SUBNET or ZONE or ENTERPRISE_NETWORK or PUBLIC_NETWORK or ANY Possible values are ENDPOINT_SUBNET, ENDPOINT_ZONE, ENDPOINT_DOMAIN, SUBNET, ZONE, ENTERPRISE_NETWORK, PUBLIC_NETWORK, POLICYGROUP, NETWORK_MACRO_GROUP, ANY, INTERNET_POLICYGROUP, .", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "allowed_choices": [
                "SUBNET", 
                "NETWORK_MACRO_GROUP", 
                "ANY", 
                "PUBLIC_NETWORK", 
                "INTERNET_POLICYGROUP", 
                "ENTERPRISE_NETWORK", 
                "POLICYGROUP", 
                "ENDPOINT_SUBNET", 
                "ENDPOINT_DOMAIN", 
                "ENDPOINT_ZONE", 
                "ZONE"
            ], 
            "orderable": true, 
            "type": "enum"
        }, 
        "associatedApplicationID": {
            "description": "The associated application ID", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "locationType": {
            "required": true, 
            "description": "Type of the location entity - ANY or SUBNET or ZONE or VPORTTAG Possible values are ANY, SUBNET, ZONE, POLICYGROUP, REDIRECTIONTARGET, VPORTTAG, .", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "allowed_choices": [
                "VPORTTAG", 
                "SUBNET", 
                "ANY", 
                "POLICYGROUP", 
                "REDIRECTIONTARGET", 
                "ZONE"
            ], 
            "orderable": true, 
            "type": "enum"
        }, 
        "locationID": {
            "description": "The ID of the location entity (Subnet/Zone/VportTag)", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "action": {
            "required": true, 
            "description": "The action of the ACL entry DROP or FORWARD or REDIRECT. Action REDIRECT is allowed only for IngressAdvancedForwardingEntry Possible values are DROP, FORWARD, REDIRECT, .", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "allowed_choices": [
                "FORWARD", 
                "REDIRECT", 
                "DROP"
            ], 
            "orderable": true, 
            "type": "enum"
        }, 
        "flowLoggingEnabled": {
            "description": "Is flow logging enabled for this particular template", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "boolean"
        }, 
        "statsID": {
            "description": "The statsID that is created in the VSD and identifies this ACL Template Entry. This is auto-generated by VSD", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "redirectExternalServiceEndPointID": {
            "description": "VPort tag to which traffic will be redirected to, when ACL entry match criteria succeeds", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }
    }, 
    "model": {
        "resource_name": "ingressexternalserviceentrytemplates", 
        "description": "Defines the template of Ingress External Service ACL entries", 
        "entity_name": "IngressExternalServiceTemplateEntry", 
        "package": "policy/acl", 
        "get": true, 
        "update": true, 
        "rest_name": "ingressexternalserviceentrytemplate", 
        "extends": [
            "@base", 
            "@metadata"
        ], 
        "delete": true
    }, 
    "children": {
        "job": {
            "create": true, 
            "relationship": "child"
        }, 
        "statistics": {
            "relationship": "child", 
            "get": true
        }
    }
}