{
    "attributes": {
        "gatewayID": {
            "type": "string",
            "format": "free",
            "description": "The gateway associated with this object. This is a read only attribute",
            "exposed": true,
            "uniqueScope": "no"
        },
        "revision": {
            "type": "integer",
            "subtype": "long",
            "description": "revision number for the gateway security profile data",
            "exposed": true,
            "uniqueScope": "no"
        }
    },
    "children": {
    },
    "model": {
        "description": "This object represents the gateway security object",
        "entity_name": "GatewaySecurityProfile",
        "extends": [ "@audited", "@base", "@metadata" ],
        "package": "ipsec",
        "resource_name": "gatewaysecurityprofiles",
        "rest_name": "gatewaysecurityprofile"
    }
}