{
    "attributes": {
        "EVPNCommunityTag": {
            "description": "Assigned by VSD. An extended community or other similar BGP attribute to the specific EVPN / IP-VPN NLRI where the VM or network macro is being advertised.",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        },
        "description": {
            "description": "Describes this policy group",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        },
        "external": {
            "description": "Indicates whether this PG is internal to VSP or not.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": false,
            "type": "boolean",
            "uniqueScope": "no"
        },
        "name": {
            "description": "Name of the policy group",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "required": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "policyGroupID": {
            "description": "PG ID for the subnet. This is unique per domain and will be in the range 1-4095",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": false,
            "type": "integer",
            "subtype": "long",
            "uniqueScope": "no"
        },
        "templateID": {
            "description": "Determines which template ID this policy group belongs to.",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        },
        "type": {
            "allowed_choices": [
                "HARDWARE",
                "SOFTWARE"
            ],
            "description": "Type of policy group - possible values SOFTWARE/HARDWARE Possible values are SOFTWARE, HARDWARE, .",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": false,
            "required": true,
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
        },
        "vport": {
            "get": true,
            "relationship": "child",
            "update": true
        }
    },
    "model": {
        "delete": true,
        "description": "PolicyGroup is group of policys on which a user can policies like ACL, QoS etc.",
        "entity_name": "PolicyGroup",
        "extends": [
            "@base",
            "@audited",
            "@metadata"
        ],
        "get": true,
        "package": "vport",
        "resource_name": "policygroups",
        "rest_name": "policygroup",
        "update": true
    }
}