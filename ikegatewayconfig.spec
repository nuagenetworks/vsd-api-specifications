{
    "attributes": [
        {
            "name": "config",
            "type": "object",
            "description": "Configuration Object",
            "filterable": true,
            "orderable": true,
            "exposed": true,
            "uniqueScope": "no"
        }
    ],
    "children": [
        
    ],
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
        "rest_name": "ikegatewayconfig"
    }
}