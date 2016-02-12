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
        "infrastructureProfileID": {
            "description": "The ID of the infrastructure gateway profile this instance of a Gateway is associated with.",
            "exposed": true,
            "format": "free",
            "required": true,
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
        }
    },
    "children": {
        "nsporttemplate": {
            "create": true,
            "get": true,
            "relationship": "child"
        }
    },
    "model": {
        "delete": true,
        "description": "Represents a Network Service Gateway Template.",
        "entity_name": "NSGatewayTemplate",
        "extends": [
            "@audited",
            "@base",
            "@metadata"
        ],
        "get": true,
        "package": "nsg",
        "resource_name": "nsgatewaytemplates",
        "rest_name": "nsgatewaytemplate",
        "update": true
    }
}