{
    "attributes": {
        "DSCP": {
            "description": "DSCP match condition to be set in the rule. It is either * or from 0-63", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "required": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "FCOverride": {
            "allowed_choices": [
                "D", 
                "E", 
                "F", 
                "G", 
                "A", 
                "B", 
                "C", 
                "H", 
                "NONE"
            ], 
            "description": "Value of the Service Class to be overridden in the packet when the match conditions are satisfied Possible values are NONE, A, B, C, D, E, F, G, H, .", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "enum", 
            "uniqueScope": "no"
        }, 
        "action": {
            "allowed_choices": [
                "FORWARD", 
                "REDIRECT", 
                "DROP"
            ], 
            "description": "The action of the ACL entry DROP or FORWARD or REDIRECT. Action REDIRECT is allowed only for IngressAdvancedForwardingEntry Possible values are DROP, FORWARD, REDIRECT, .", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "required": true, 
            "type": "enum", 
            "uniqueScope": "no"
        }, 
        "addressOverride": {
            "description": "Overrides the source IP for Ingress and destination IP for Egress, macentries will use this adress as the match criteria.", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "associatedApplicationID": {
            "description": "The associated application ID", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "associatedApplicationObjectID": {
            "description": "The associated application object ID", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "associatedApplicationObjectType": {
            "allowed_choices": [
                "FORWARD", 
                "REDIRECT", 
                "DROP"
            ], 
            "description": "The associated application object type Refer to API section for supported types.", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "enum", 
            "uniqueScope": "no"
        }, 
        "associatedLiveEntityID": {
            "description": "In the draft mode, the ACL entry refers to this LiveEntity. In non-drafted mode, this is null.", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "description": {
            "description": "Description of the ACL entry", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "destinationPort": {
            "description": "The destination port to be matched if protocol is UDP or TCP. Value should be either * or single port number or a port range", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "required": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "etherType": {
            "description": "Ether type of the packet to be matched. etherType can be * or a valid hexadecimal value", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "required": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "flowLoggingEnabled": {
            "description": "Is flow logging enabled for this particular template", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "boolean", 
            "uniqueScope": "no"
        }, 
        "locationID": {
            "description": "The ID of the location entity (Subnet/Zone/VportTag)", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "locationType": {
            "allowed_choices": [
                "VPORTTAG", 
                "SUBNET", 
                "ANY", 
                "POLICYGROUP", 
                "REDIRECTIONTARGET", 
                "ZONE"
            ], 
            "description": "Type of the location entity - ANY or SUBNET or ZONE or VPORTTAG Possible values are ANY, SUBNET, ZONE, POLICYGROUP, REDIRECTIONTARGET, VPORTTAG, .", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "required": true, 
            "type": "enum", 
            "uniqueScope": "no"
        }, 
        "networkID": {
            "description": "The destination network entity that is referenced(subnet/zone/macro)", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "networkType": {
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
            "description": "Type of the source network -  VM_SUBNET or VM_ZONE or VM_DOMAIN or SUBNET or ZONE or ENTERPRISE_NETWORK or PUBLIC_NETWORK or ANY Possible values are ENDPOINT_SUBNET, ENDPOINT_ZONE, ENDPOINT_DOMAIN, SUBNET, ZONE, ENTERPRISE_NETWORK, PUBLIC_NETWORK, POLICYGROUP, NETWORK_MACRO_GROUP, ANY, INTERNET_POLICYGROUP, .", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "required": true, 
            "type": "enum", 
            "uniqueScope": "no"
        }, 
        "policyState": {
            "allowed_choices": [
                "DRAFT", 
                "LIVE"
            ], 
            "description": "State of the policy.  Possible values are DRAFT, LIVE, .", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "enum", 
            "uniqueScope": "no"
        }, 
        "priority": {
            "description": "The priority of the ACL entry that determines the order of entries", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "required": true, 
            "type": "integer", 
            "uniqueScope": "no"
        }, 
        "protocol": {
            "description": "Protocol number that must be matched", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "required": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "redirectVPortTagID": {
            "description": "VPort tag to which traffic will be redirected to, when ACL entry match criteria succeeds", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "sourcePort": {
            "description": "Source port to be matched if protocol is UDP or TCP. Value can be either * or single port number or a port range", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "required": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "statsID": {
            "description": "The statsID that is created in the VSD and identifies this ACL Template Entry. This is auto-generated by VSD", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "statsLoggingEnabled": {
            "description": "Is stats logging enabled for this particular template", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "boolean", 
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
            "description": "Indicates the preferencial path selection for network traffic for this ACL - Default is Primary 1 and Secondary 2 when the attribute is applicable. Possible values are PRIMARY_SECONDARY, SECONDARY_PRIMARY, PRIMARY, SECONDARY, SYMMETRIC, .", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "enum", 
            "uniqueScope": "no"
        }
    }, 
    "children": {
        "job": {
            "create": true, 
            "relationship": "child"
        }, 
        "statistics": {
            "get": true, 
            "relationship": "child"
        }
    }, 
    "delete": true, 
    "description": "Defines the template of Ingress Advanced Forwarding entries", 
    "entity_name": "IngressAdvFwdEntryTemplate", 
    "extends": [
        "@base", 
        "@metadata"
    ], 
    "get": true, 
    "package": "/policy/acl", 
    "resource_name": "ingressadvfwdentrytemplates", 
    "rest_name": "ingressadvfwdentrytemplate", 
    "update": true
}