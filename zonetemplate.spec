{
    "attributes": {
        "publicZone": {
            "description": "Identifies if the zone is a public zone, in which case any subnets associated with this zone are actually connected to the public subnet of the data center", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "boolean"
        }, 
        "description": {
            "description": "A description of the Zone template", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "encryption": {
            "description": "Determines whether or not IPSEC is enabled. Possible values are INHERITED, ENABLED, DISABLED, .", 
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
            "description": "Name of the current entity(Zone or zone template or subnet etc..) Valid characters are alphabets, numbers, space and hyphen( - ).", 
            "format": "free", 
            "filterable": true, 
            "uniqueScope": "no", 
            "required": true, 
            "exposed": true, 
            "orderable": true, 
            "type": "string"
        }, 
        "associatedMulticastChannelMapID": {
            "description": "The ID of the Multi Cast Channel Map  this zone/zone template is associated with. This has to be set when  enableMultiCast is set to ENABLED", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "netmask": {
            "description": "Netmask of the subnet defined", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "multicast": {
            "description": "multicast is enum that indicates multicast policy on zone/zone template. Possible values are ENABLED ,DISABLED  and INHERITED Possible values are INHERITED, ENABLED, DISABLED, .", 
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
            "description": "IP address of the subnet defined. In case of zone, this is an optional field for and allows users to allocate an IP address range to a zone. The VSD will auto-assign IP addresses to subnets from this range if a specific IP address is not defined for the subnet", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "numberOfHostsInSubnets": {
            "description": "Number of hosts in the subnets where IP addresses are automatically assigned from the zone IP pool", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "integer"
        }, 
        "IPType": {
            "description": "IPv4 or IPv6(only IPv4 is supported in R1.0) Possible values are IPV4, IPV6, .", 
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
        "resource_name": "zonetemplates", 
        "description": "As in domains and subnets, zones are derived from templates. This object provides the definition of the template", 
        "entity_name": "ZoneTemplate", 
        "package": "network", 
        "get": true, 
        "update": true, 
        "rest_name": "zonetemplate", 
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
        "eventlog": {
            "relationship": "child", 
            "get": true
        }, 
        "subnettemplate": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }
    }
}