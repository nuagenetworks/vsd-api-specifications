{
    "attributes": {
        "dataCollectionFrequency": {
            "description": "How frequent to collect statistics in seconds", 
            "format": "free", 
            "filterable": true, 
            "uniqueScope": "no", 
            "required": true, 
            "exposed": true, 
            "orderable": true, 
            "type": "float"
        }, 
        "description": {
            "description": "A description of the statistics policy", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "name": {
            "description": "Name of statistics policy", 
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
        "resource_name": "statisticspolicies", 
        "description": "Defines the frequency of statistics collection associated with an object", 
        "entity_name": "StatisticsPolicy", 
        "package": "stats", 
        "get": true, 
        "update": true, 
        "rest_name": "statisticspolicy", 
        "extends": [
            "@base", 
            "@metadata"
        ], 
        "delete": true
    }
}