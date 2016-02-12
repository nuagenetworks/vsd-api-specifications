{
    "attributes": {
        "description": {
            "description": "Description of this redirection target template",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "endPointType": {
            "allowed_choices": [
                "L3",
                "NONE",
                "VIRTUAL_WIRE"
            ],
            "description": "VPortTagEndPointType is an enum. It defines the type of header rewrite and forwarding performed by VRS when the endpoint is used as a PBR destination. Possible values are NONE, L3, VIRTUAL_WIRE.",
            "exposed": true,
            "format": "free",
            "required": true,
            "type": "enum",
            "uniqueScope": "no"
        },
        "name": {
            "description": "Name of this redirection target template",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "required": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "redundancyEnabled": {
            "description": "Allow/Disallow redundant appliances and VIP",
            "exposed": true,
            "format": "free",
            "required": true,
            "type": "boolean",
            "uniqueScope": "no"
        },
        "triggerType": {
            "allowed_choices": [
                "GARP",
                "NONE"
            ],
            "description": "Trigger type, could be NONE/GARP - THIS IS READONLY",
            "exposed": true,
            "format": "free",
            "type": "enum",
            "uniqueScope": "no"
        }
    },
    "children": {
        "eventlog": {
            "get": true,
            "relationship": "child"
        },
        "job": {
            "create": true,
            "relationship": "child"
        }
    },
    "model": {
        "delete": true,
        "description": "Template for a vporttag. It can be created only at the template level and available for all instances.",
        "entity_name": "RedirectionTargetTemplate",
        "extends": [
            "@audited",
            "@base",
            "@metadata"
        ],
        "get": true,
        "package": "vport",
        "resource_name": "redirectiontargettemplates",
        "rest_name": "redirectiontargettemplate",
        "update": true
    }
}