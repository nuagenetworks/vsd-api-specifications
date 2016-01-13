{
    "attributes": {
        "dataCollectionFrequency": {
            "description": "How frequent to collect statistics in seconds",
            "exposed": true,
            "filterable": true,
            "orderable": true,
            "required": true,
            "type": "integer",
            "subtype": "long",
            "min_value": 1,
            "uniqueScope": "no"
        },
        "description": {
            "description": "A description of the statistics policy",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": false,
            "type": "string",
            "min_length": 1,
            "max_length": 255,
            "uniqueScope": "no"
        },
        "name": {
            "description": "Name of statistics policy",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "required": true,
            "type": "string",
            "min_length": 1,
            "max_length": 255,
            "uniqueScope": "no"
        }
    },
    "model": {
        "delete": true,
        "description": "Defines the frequency of statistics collection associated with an object",
        "entity_name": "StatisticsPolicy",
        "extends": [
            "@base",
            "@metadata"
        ],
        "get": true,
        "package": "stats",
        "resource_name": "statisticspolicies",
        "rest_name": "statisticspolicy",
        "update": true
    }
}