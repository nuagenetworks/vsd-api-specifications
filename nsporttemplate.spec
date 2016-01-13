{
    "attributes": {
        "VLANRange": {
            "description": "VLAN Range of the Port.  Format must conform to a-b,c,d-f where a,b,c,d,f are integers between 0 and 4095.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": false,
            "type": "string",
            "min_length": 0,
            "max_length": 255,
            "uniqueScope": "no"
        },
        "associatedEgressQOSPolicyID": {
            "description": "ID of the Egress QOS Policy associated with this Vlan.",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        },
        "associatedVSCProfileID": {
            "description": "The ID of the infrastructure VSC profile this is associated with this instance of a port or port template.",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        },
        "description": {
            "description": "A description of the Port",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string",
            "min_length": 0,
            "max_length": 255,
            "uniqueScope": "no"
        },
        "infrastructureProfileID": {
            "description": "The ID of the infrastructure profile this instance is associated with.",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        },
        "name": {
            "description": "Name of the Port",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "required": true,
            "type": "string",
            "min_length": 1,
            "max_length": 255,
            "uniqueScope": "no"
        },
        "physicalName": {
            "description": "Identifier of the Port",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "required": true,
            "type": "string",
            "min_length": 1,
            "max_length": 255,
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
        "description": "Represents Port Template object under a given gateway template object",
        "entity_name": "NSPortTemplate",
        "extends": [
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