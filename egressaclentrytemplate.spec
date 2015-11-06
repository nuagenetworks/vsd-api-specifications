{
    "attributes": {
        "mirrorDestinationID": {
            "description": "Destination ID of the mirror destination object.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        },
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
        "reflexive": {
            "description": "true means that this ACL entry is reflexive, so there will be a corresponding egress rule that will be created by OVS in the network. false means that there is no corresponding egress rule created by OVS in the network", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "boolean", 
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
    "model": {
        "delete": true, 
        "description": "Defines the template of Egress ACL Template entries", 
        "entity_name": "EgressACLEntryTemplate", 
        "extends": [
            "@base", 
            "@metadata"
        ], 
        "get": true, 
        "package": "policy/acl", 
        "resource_name": "egressaclentrytemplates", 
        "rest_name": "egressaclentrytemplate", 
        "update": true
    }
}
