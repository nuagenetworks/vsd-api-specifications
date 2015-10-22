{
    "attributes": {
        "associatedApplicationID": {
            "description": "The associated application ID.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "publicZone": {
            "description": "If a zone is marked as public, then it is lined to the public network associated with this data center", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "boolean"
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
        "policyGroupID": {
            "description": "PG ID for the subnet. This is unique per domain and will be in the range 1-4095", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "float"
        }, 
        "templateID": {
            "description": "The ID of the template that this zone was derived from", 
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
        "associatedApplicationObjectType": {
            "description": "The associated application object type. Refer to API section for supported types.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "enum"
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
        "maintenanceMode": {
            "description": "maintenanceMode is an enum that indicates if the Zone is accepting VM activation requests. Possible values are DISABLED, ENABLED and ENABLED_INHERITED Possible values are .", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "enum"
        }, 
        "associatedApplicationObjectID": {
            "description": "The associated application object ID.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "numberOfHostsInSubnets": {
            "description": "Number of hosts in each of the subnets that can be created under a zone and are auto-assigned IP addresses", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "integer"
        }, 
        "description": {
            "description": "A description of the zone", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }
    }, 
    "model": {
        "resource_name": "zones", 
        "description": "The zone is a collection of subnets attached to a domain. The zone concept enables the definition of policies for collections of subnets", 
        "entity_name": "Zone", 
        "package": "network", 
        "get": true, 
        "update": true, 
        "rest_name": "zone", 
        "extends": [
            "@base", 
            "@metadata"
        ], 
        "delete": true
    }, 
    "children": {
        "subnet": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }, 
        "statistics": {
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
        "dhcpoption": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }, 
        "vm": {
            "relationship": "child", 
            "get": true
        }, 
        "vminterface": {
            "relationship": "child", 
            "get": true
        }, 
        "qos": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }, 
        "tca": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }, 
        "statisticspolicy": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }
    }
}