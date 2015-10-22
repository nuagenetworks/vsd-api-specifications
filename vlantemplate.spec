{
    "attributes": {
        "associatedEgressQOSPolicyID": {
            "description": "ID of the Egress QOS Policy associated with this Vlan.", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "description": {
            "description": "A description of the Port", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "value": {
            "description": "value of VLAN", 
            "exposed": true, 
            "type": "integer", 
            "uniqueScope": "no"
        }
    }, 
    "delete": true, 
    "description": "Represents VLAN Template under a PORT Template object.", 
    "entity_name": "VLANTemplate", 
    "extends": [
        "@base", 
        "@metadata"
    ], 
    "get": true, 
    "package": "/gateway", 
    "resource_name": "vlantemplates", 
    "rest_name": "vlantemplate", 
    "update": true
}