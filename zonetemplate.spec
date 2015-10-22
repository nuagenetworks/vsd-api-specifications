{
    "attributes": {
        "IPType": {
            "allowed_choices": [
                "IPV6", 
                "IPV4"
            ], 
            "description": "IPv4 or IPv6(only IPv4 is supported in R1.0) Possible values are IPV4, IPV6, .", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "enum", 
            "uniqueScope": "no"
        }, 
        "address": {
            "description": "IP address of the subnet defined. In case of zone, this is an optional field for and allows users to allocate an IP address range to a zone. The VSD will auto-assign IP addresses to subnets from this range if a specific IP address is not defined for the subnet", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "associatedMulticastChannelMapID": {
            "description": "The ID of the Multi Cast Channel Map  this zone/zone template is associated with. This has to be set when  enableMultiCast is set to ENABLED", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "description": {
            "description": "A description of the Zone template", 
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
                "INHERITED", 
                "DISABLED"
            ], 
            "description": "Determines whether or not IPSEC is enabled. Possible values are INHERITED, ENABLED, DISABLED, .", 
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
            "description": "multicast is enum that indicates multicast policy on zone/zone template. Possible values are ENABLED ,DISABLED  and INHERITED Possible values are INHERITED, ENABLED, DISABLED, .", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "enum", 
            "uniqueScope": "no"
        }, 
        "name": {
            "description": "Name of the current entity(Zone or zone template or subnet etc..) Valid characters are alphabets, numbers, space and hyphen( - ).", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "required": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "netmask": {
            "description": "Netmask of the subnet defined", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "numberOfHostsInSubnets": {
            "description": "Number of hosts in the subnets where IP addresses are automatically assigned from the zone IP pool", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "integer", 
            "uniqueScope": "no"
        }, 
        "publicZone": {
            "description": "Identifies if the zone is a public zone, in which case any subnets associated with this zone are actually connected to the public subnet of the data center", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "boolean", 
            "uniqueScope": "no"
        }
    }, 
    "children": {
        "eventlog": {
            "get": true, 
            "relationship": "child"
        }, 
        "qos": {
            "create": true, 
            "get": true, 
            "relationship": "child"
        }, 
        "subnettemplate": {
            "create": true, 
            "get": true, 
            "relationship": "child"
        }
    }, 
    "model": {
        "delete": true, 
        "description": "As in domains and subnets, zones are derived from templates. This object provides the definition of the template", 
        "entity_name": "ZoneTemplate", 
        "extends": [
            "@base", 
            "@metadata"
        ], 
        "get": true, 
        "package": "network", 
        "resource_name": "zonetemplates", 
        "rest_name": "zonetemplate", 
        "update": true
    }
}