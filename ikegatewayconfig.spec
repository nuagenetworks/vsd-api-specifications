{
    "attributes": [
        {
            "description": "Configuration Object",
            "exposed": true,
            "filterable": true,
            "name": "config",
            "orderable": true,
            "type": "object",
            "uniqueScope": "no"
        }
    ],
    "children": [],
    "model": {
        "description": "Represents an IKE Gateway Configuration Object",
        "entity_name": "IKEGatewayConfig",
        "extends": [
            "@audited",
            "@base",
            "@metadata"
        ],
        "package": "ike",
        "resource_name": "ikegatewayconfig",
        "rest_name": "ikegatewayconfig",
        "userlabel": "IKE Gateway Configuration"
    }
}
