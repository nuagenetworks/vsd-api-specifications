{
    "attributes": {
        "associatedEgressQOSPolicyID": {
            "description": "ID of the Egress QOS Policy associated with this Vlan.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "description": {
            "description": "A description of the Port", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "value": {
            "description": "value of VLAN", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "integer"
        }
    }, 
    "model": {
        "resource_name": "vlantemplates", 
        "description": "Represents VLAN Template under a PORT Template object.", 
        "entity_name": "VLANTemplate", 
        "package": "gateway", 
        "get": true, 
        "update": true, 
        "rest_name": "vlantemplate", 
        "extends": [
            "@base", 
            "@metadata"
        ], 
        "delete": true
    }
}