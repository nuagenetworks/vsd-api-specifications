{
    "attributes": {
        "VLANRange": {
            "description": "VLAN Range of the Port.  Format must conform to a-b,c,d-f where a,b,c,d,f are integers between 0 and 4095.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 255,
            "type": "string",
            "uniqueScope": "no"
        },
        "associatedEgressQOSPolicyID": {
            "description": "ID of the Egress QOS Policy associated with this Vlan.",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "associatedVSCProfileID": {
            "description": "The ID of the infrastructure VSC profile this is associated with this instance of a port or port template.",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "description": {
            "description": "A description of the Port",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 255,
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "infrastructureProfileID": {
            "description": "The ID of the infrastructure profile this instance is associated with.",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "name": {
            "description": "Name of the Port",
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
        "physicalName": {
            "description": "Identifier of the Port",
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
        "portType": {
            "allowed_choices": [
                "ACCESS",
                "NETWORK"
            ],
            "description": "Type of the Port - NETWORK, ACCESS Possible values are ACCESS, NETWORK, .",
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
        "vlantemplate": {
            "create": true,
            "get": true,
            "relationship": "child"
        }
    },
    "model": {
        "delete": true,
        "description": "Represents Port Template object under a given gateway template object.",
        "entity_name": "NSPortTemplate",
        "extends": [
            "@audited",
            "@base",
            "@metadata"
        ],
        "get": true,
        "package": "nsg",
        "resource_name": "nsporttemplates",
        "rest_name": "nsporttemplate",
        "update": true
    }
}