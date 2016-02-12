{
    "attributes": {
        "associatedEgressQOSPolicyID": {
            "description": "ID of the Egress QOS Policy associated with this Vlan.",
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
        "value": {
            "description": "value of VLAN",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_value": 4096,
            "orderable": true,
            "type": "integer",
            "uniqueScope": "no"
        }
    },
    "model": {
        "delete": true,
        "description": "Represents VLAN Template under a Port Template object.",
        "entity_name": "VLANTemplate",
        "extends": [
            "@audited",
            "@base",
            "@metadata"
        ],
        "get": true,
        "package": "gateway",
        "resource_name": "vlantemplates",
        "rest_name": "vlantemplate",
        "update": true
    }
}