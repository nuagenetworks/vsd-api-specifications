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
            "description": "change revision number for the gateway security data",
            "exposed": true,
            "uniqueScope": "no"
        }
    },
    "children": {
        "gatewaysecureddata": {
            "get": true,
            "create": true,
            "relationship": "child"
        }
    },
    "model": {
        "description": "This object represents the gateway security object",
        "entity_name": "GatewaySecurity",
        "extends": [ "@audited", "@base", "@metadata" ],
        "package": "ipsec",
        "resource_name": "gatewaysecurities",
        "rest_name": "gatewaysecurity",
        "get": true
    }
}