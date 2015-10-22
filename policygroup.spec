{
    "attributes": {
        "EVPNCommunityTag": {
            "description": "Assigned by VSD. An extended community or other similar BGP attribute to the specific EVPN / IP-VPN NLRI where the VM or network macro is being advertised.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "policyGroupID": {
            "description": "PG ID for the subnet. This is unique per domain and will be in the range 1-4095", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "float"
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
        }, 
        "templateID": {
            "description": "Determines which template ID this policy group belongs to.", 
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
        }
    }, 
    "model": {
        "resource_name": "policygroups", 
        "description": "PolicyGroup is group of policys on which a user can policies like ACL, QoS etc.", 
        "entity_name": "PolicyGroup", 
        "package": "vport", 
        "get": true, 
        "update": true, 
        "rest_name": "policygroup", 
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
        "vport": {
            "update": true, 
            "relationship": "child", 
            "get": true
        }, 
        "eventlog": {
            "relationship": "child", 
            "get": true
        }
    }
}