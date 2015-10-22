{
    "attributes": {
        "BUMPeakBurstSize": {
            "description": "Peak burst size setting in kilo-bytes (kilo-octets) for Broadcast/Multicast rate limiting (BUM).", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "FIPCommittedBurstSize": {
            "description": "Committed burst size setting in kilo-bytes (kilo-octets) for FIP Shaper.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "BUMRateLimitingActive": {
            "description": "Flag the indicates whether Broadcast/Multicast rate limiting is enabled or disabled", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "boolean"
        }, 
        "trustedForwardingClass": {
            "description": "Specifies if the trusted flag is set for the QoS policy / template", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "boolean"
        }, 
        "FIPRateLimitingActive": {
            "description": "Flag the indicates whether FIP rate limiting is enabled or disabled", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "boolean"
        }, 
        "committedInformationRate": {
            "description": "Committed Information Rate :  Committed bandwidth that is allowed from each VM in Mb/s; only whole values supported.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "committedBurstSize": {
            "description": "Committed Burst Size :  Burst size associated with the rate limiter in kilo-bytes (kilo-octets); only whole values are supported.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "associatedDSCPForwardingClassTableName": {
            "description": "Name of the DSCP->Forwarding Class used by this Qos Policy", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "burst": {
            "description": "Peak Burst Size :  The maximum burst size associated with the rate limiter in kilo-bytes (kilo-octets); only whole values allowed and 'INFINITY' if rate limiting is disabled.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "FIPPeakInformationRate": {
            "description": "Peak rate setting for FIP rate limiting in Mb/s;", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "description": {
            "description": "A description of the QoS object", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "serviceClass": {
            "required": true, 
            "description": "Class of service to be used. Service classes in order of priority are A(1), B(2), C(3), D(4), E(5), F(6), G(7) and H(8) Possible values are NONE, A, B, C, D, E, F, G, H, .", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
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
            "orderable": true, 
            "type": "enum"
        }, 
        "peak": {
            "description": "Peak Information Rate :  Peak bandwidth that is allowed from each VM in Mb/s; only whole values allowed and 'INFINITY' if rate limiting is disabled.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "active": {
            "description": "If enabled, it means that this ACL or QOS entry is active", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "boolean"
        }, 
        "BUMPeakInformationRate": {
            "description": "Peak rate setting in Mb/s for Broadcast/Multicast rate limiting ", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "rewriteForwardingClass": {
            "description": "Specifies if the rewrite flag is set for the QoS policy / template", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "boolean"
        }, 
        "name": {
            "description": "A unique name of the QoS object", 
            "format": "free", 
            "filterable": true, 
            "uniqueScope": "no", 
            "required": true, 
            "exposed": true, 
            "orderable": true, 
            "type": "string"
        }, 
        "rateLimitingActive": {
            "description": "Identifies if rate limiting must be implemented", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "boolean"
        }, 
        "associatedDSCPForwardingClassTableID": {
            "description": "ID of the DSCP->Forwarding Class used by this Qos Policy", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "FIPCommittedInformationRate": {
            "description": "Committed information rate setting in Mb/s for FIP Shaper.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "assocQosId": {
            "description": "ID of object associated with this QoS object", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "FIPPeakBurstSize": {
            "description": "Peak burst size setting in kilo-bytes (kilo-octets) for FIP rate limiting.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "BUMCommittedInformationRate": {
            "description": "Committed information rate setting in Mb/s for BUM Shaper.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "BUMCommittedBurstSize": {
            "description": "Committed burst size setting in kilo-bytes (kilo-octets) for BUM Shaper.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }
    }, 
    "model": {
        "resource_name": "qos", 
        "description": "The object manipulates the QoS parameters attached to a domain, zone, or subnet", 
        "entity_name": "QOS", 
        "package": "policy/qos", 
        "get": true, 
        "update": true, 
        "rest_name": "qos", 
        "extends": [
            "@base", 
            "@metadata"
        ], 
        "delete": true
    }, 
    "children": {
        "vm": {
            "relationship": "child", 
            "get": true
        }, 
        "eventlog": {
            "relationship": "child", 
            "get": true
        }
    }
}