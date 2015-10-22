{
    "attributes": {
        "EVPNCommunityTag": {
            "description": "An extended community or other similar BGP attribute to the specific EVPN / IP-VPN NLRI where the VM or network macro is being advertised.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "type": {
            "required": true, 
            "description": "Type of policy group - possible values SOFTWARE/HARDWARE Possible values are SOFTWARE, HARDWARE, .", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "allowed_choices": [
                "HARDWARE", 
                "SOFTWARE"
            ], 
            "orderable": true, 
            "type": "enum"
        }, 
        "description": {
            "description": "Describes this policy group", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "name": {
            "description": "Name of the policy group", 
            "format": "free", 
            "filterable": true, 
            "uniqueScope": "no", 
            "required": true, 
            "exposed": true, 
            "orderable": true, 
            "type": "string"
        }, 
        "external": {
            "description": "Indicates whether this PG is internal to VSP or not.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "boolean"
        }
    }, 
    "model": {
        "resource_name": "policygrouptemplates", 
        "description": "PolicyGroupTemplate represents the template of a policy group object. PolicyGroup is group of vports on which a user can policies like ACL, QoS etc.", 
        "entity_name": "PolicyGroupTemplate", 
        "package": "vport", 
        "get": true, 
        "update": true, 
        "rest_name": "policygrouptemplate", 
        "extends": [
            "@base", 
            "@metadata"
        ], 
        "delete": true
    }, 
    "children": {
        "job": {
            "create": true, 
            "relationship": "child"
        }, 
        "eventlog": {
            "relationship": "child", 
            "get": true
        }
    }
}