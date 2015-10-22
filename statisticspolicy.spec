{
    "attributes": {
        "dataCollectionFrequency": {
            "description": "How frequent to collect statistics in seconds", 
            "exposed": true, 
            "required": true, 
            "type": "float", 
            "uniqueScope": "no"
        }, 
        "description": {
            "description": "A description of the statistics policy", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "name": {
            "description": "Name of statistics policy", 
            "exposed": true, 
            "required": true, 
            "type": "string", 
            "uniqueScope": "no"
        }
    }, 
    "delete": true, 
    "description": "Defines the frequency of statistics collection associated with an object", 
    "entity_name": "StatisticsPolicy", 
    "extends": [
        "@base", 
        "@metadata"
    ], 
    "get": true, 
    "package": "/stats", 
    "resource_name": "statisticspolicies", 
    "rest_name": "statisticspolicy", 
    "update": true
}