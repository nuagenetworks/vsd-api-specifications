{
    "attributes": {
        "publicIP": {
            "description": "Public IP address of the interface", 
            "format": "free", 
            "filterable": true, 
            "uniqueScope": "no", 
            "required": true, 
            "exposed": true, 
            "orderable": true, 
            "type": "string"
        }, 
        "associatedPATNATPoolID": {
            "description": "Read Only - Indicates which PATNATPool this entry belongs to", 
            "format": "free", 
            "filterable": true, 
            "uniqueScope": "no", 
            "required": true, 
            "exposed": true, 
            "orderable": true, 
            "type": "string"
        }, 
        "privateIP": {
            "description": "Private IP address of the interface", 
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
        "resource_name": "natmapentries", 
        "description": "Defines a MAP between the private ip and public ip", 
        "entity_name": "NATMapEntry", 
        "package": "gateway", 
        "get": true, 
        "rest_name": "natmapentry", 
        "extends": [
            "@base", 
            "@metadata"
        ], 
        "delete": true
    }
}