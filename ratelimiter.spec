{
    "attributes": {
        "committedInformationRate": {
            "description": "Committed Information Rate :  Committed bandwidth that is allowed in Mb/s; only whole values supported.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "description": {
            "description": "A description of the Rate Limiter object",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 255,
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "name": {
            "description": "A unique name of the Rate Limiter object",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 255,
            "min_length": 1,
            "orderable": true,
            "required": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "peakBurstSize": {
            "description": "Peak Burst Size :  The maximum burst size associated with the rate limiter in kilo-bits; only whole values are supported.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "peakInformationRate": {
            "description": "Peak Information Rate :  Peak bandwidth allowed in Mb/s; only whole values supported.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        }
    },
    "model": {
        "delete": true,
        "description": "Rate Limiter object that contains peak, burst and cir. It can be associated with Egress QOS policy objects.",
        "entity_name": "RateLimiter",
        "extends": [
            "@audited",
            "@base",
            "@metadata"
        ],
        "get": true,
        "package": "policy/qos",
        "resource_name": "ratelimiters",
        "rest_name": "ratelimiter",
        "update": true
    }
}