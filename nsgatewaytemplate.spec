{
    "attributes": {
        "description": {
            "description": "A description of the Gateway",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string",
            "min_length": 0,
            "max_length": 255,
            "uniqueScope": "no"
        },
        "enterpriseID": {
            "description": "The enterprise associated with this Gateway. This is a read only attribute",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        },
        "infrastructureProfileID": {
            "description": "The ID of the infrastructure gateway profile this instance of a Gateway is associated with.",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "required": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "name": {
            "description": "Name of the Gateway",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "required": true,
            "type": "string",
            "min_length": 1,
            "max_length": 255,
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
        "description": "Represents Network Service Gateway Template object",
        "entity_name": "NSGatewayTemplate",
        "extends": [
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