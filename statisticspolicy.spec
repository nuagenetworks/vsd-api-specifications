{
    "attributes": {
        "dataCollectionFrequency": {
            "description": "How frequent to collect statistics in seconds",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "min_value": 1,
            "orderable": true,
            "required": true,
            "subtype": "long",
            "type": "integer",
            "uniqueScope": "no"
        },
        "description": {
            "description": "A description of the statistics policy",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 255,
            "min_length": 1,
            "type": "string",
            "uniqueScope": "no"
        },
        "name": {
            "description": "Name of statistics policy",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 255,
            "min_length": 1,
            "orderable": true,
            "required": true,
            "type": "string",
            "uniqueScope": "no"
        }
    },
    "model": {
        "delete": true,
        "description": "Defines the frequency of statistics collection associated with an object.",
        "entity_name": "StatisticsPolicy",
        "extends": [
            "@audited",
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