{
    "attributes": {
        "EVPNCommunityTag": {
            "description": "An extended community or other similar BGP attribute to the specific EVPN / IP-VPN NLRI where the VM or network macro is being advertised.", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "description": {
            "description": "Describes this policy group", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "external": {
            "description": "Indicates whether this PG is internal to VSP or not.", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
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
        "type": {
            "allowed_choices": [
                "HARDWARE", 
                "SOFTWARE"
            ], 
            "description": "Type of policy group - possible values SOFTWARE/HARDWARE Possible values are SOFTWARE, HARDWARE, .", 
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
        "eventlog": {
            "get": true, 
            "relationship": "child"
        }, 
        "job": {
            "create": true, 
            "relationship": "child"
        }
    }, 
    "delete": true, 
    "description": "PolicyGroupTemplate represents the template of a policy group object. PolicyGroup is group of vports on which a user can policies like ACL, QoS etc.", 
    "entity_name": "PolicyGroupTemplate", 
    "extends": [
        "@base", 
        "@metadata"
    ], 
    "get": true, 
    "package": "vport", 
    "resource_name": "policygrouptemplates", 
    "rest_name": "policygrouptemplate", 
    "update": true
}