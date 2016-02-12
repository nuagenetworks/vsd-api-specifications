{
    "attributes": {
        "description": {
            "description": "A description of the Gateway",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 255,
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "enterpriseID": {
            "description": "The enterprise associated with this Gateway. This is a read only attribute",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "name": {
            "description": "Name of the Gateway",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 255,
            "min_length": 1,
            "orderable": true,
            "required": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "personality": {
            "allowed_choices": [
                "DC7X50",
                "HARDWARE_VTEP",
                "NSG",
                "OTHER",
                "VRSG",
                "VSA",
                "VSG"
            ],
            "description": "Personality of the Gateway - VSG,VRSG,NSG,NONE,OTHER, cannot be changed after creation. Possible values are VSG, VSA, VRSG, DC7X50, NSG, HARDWARE_VTEP, OTHER, .",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "required": true,
            "type": "enum",
            "uniqueScope": "no"
        }
    },
    "children": {
        "porttemplate": {
            "create": true,
            "get": true,
            "relationship": "child"
        }
    },
    "model": {
        "delete": true,
        "description": "Represents Gateway Template object.",
        "entity_name": "GatewayTemplate",
        "extends": [
            "@audited",
            "@base",
            "@metadata"
        ],
        "get": true,
        "package": "gateway",
        "resource_name": "gatewaytemplates",
        "rest_name": "gatewaytemplate",
        "update": true
    }
}