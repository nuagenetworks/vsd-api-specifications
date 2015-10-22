{
    "attributes": {
        "description": {
            "description": "A description of the Profile instance created.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "probeInterval": {
            "description": "Openflow echo timer in millisecond", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "float"
        }, 
        "enterpriseID": {
            "description": "Enterprise/Organisation associated with this Profile instance.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "secondController": {
            "description": "Second VSC Controller :  IP Address of the secondary VSC system NSG instances associated to this profile will be reaching for.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "firstController": {
            "description": "First VSC Controller :  IP Address of the first VSC system NSG instances associated to this profile will be reaching for.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "enterprise": {
            "description": "Name of the enterprise/organisation associated with this Profile instance.  This is a read only attribute", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "name": {
            "description": "Name of the Infrastructure Profile", 
            "format": "free", 
            "filterable": true, 
            "uniqueScope": "no", 
            "required": true, 
            "exposed": true, 
            "orderable": true, 
            "type": "string"
        }
    }, 
    "model": {
        "resource_name": "infrastructurevscprofiles", 
        "description": "Represents an Infrastructure VSC Profile", 
        "entity_name": "InfrastructureVscProfile", 
        "package": "infrastructure", 
        "get": true, 
        "update": true, 
        "rest_name": "infrastructurevscprofile", 
        "extends": [
            "@base", 
            "@metadata"
        ], 
        "delete": true
    }
}