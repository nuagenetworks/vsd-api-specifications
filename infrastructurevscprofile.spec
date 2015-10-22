{
    "attributes": {
        "description": {
            "description": "A description of the Profile instance created.", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "enterprise": {
            "description": "Name of the enterprise/organisation associated with this Profile instance.  This is a read only attribute", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "enterpriseID": {
            "description": "Enterprise/Organisation associated with this Profile instance.", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "firstController": {
            "description": "First VSC Controller :  IP Address of the first VSC system NSG instances associated to this profile will be reaching for.", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "name": {
            "description": "Name of the Infrastructure Profile", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "required": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "probeInterval": {
            "description": "Openflow echo timer in millisecond", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "float", 
            "uniqueScope": "no"
        }, 
        "secondController": {
            "description": "Second VSC Controller :  IP Address of the secondary VSC system NSG instances associated to this profile will be reaching for.", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }
    }, 
    "delete": true, 
    "description": "Represents an Infrastructure VSC Profile", 
    "entity_name": "InfrastructureVscProfile", 
    "extends": [
        "@base", 
        "@metadata"
    ], 
    "get": true, 
    "package": "infrastructure", 
    "resource_name": "infrastructurevscprofiles", 
    "rest_name": "infrastructurevscprofile", 
    "update": true
}