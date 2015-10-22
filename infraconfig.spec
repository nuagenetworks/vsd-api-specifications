{
    "attributes": {
        "configStatus": {
            "description": "Status of the configuration application", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "config": {
            "description": "Infrastructure Config", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "object"
        }
    }, 
    "model": {
        "resource_name": "infraconfig", 
        "description": "Represents Infrastructure Config", 
        "entity_name": "InfrastructureConfig", 
        "package": "gateway", 
        "rest_name": "infraconfig", 
        "extends": [
            "@base", 
            "@metadata"
        ]
    }
}