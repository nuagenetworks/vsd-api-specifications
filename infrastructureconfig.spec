{
    "attributes": {
        "config": {
            "description": "Infrastructure Config", 
            "exposed": true, 
            "type": "object", 
            "uniqueScope": "no"
        }, 
        "configStatus": {
            "description": "Status of the configuration application", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }
    }, 
    "description": "Represents Infrastructure Config", 
    "entity_name": "InfrastructureConfig", 
    "extends": [
        "@base", 
        "@metadata"
    ], 
    "package": "/gateway", 
    "resource_name": "infraconfig", 
    "rest_name": "infraconfig"
}