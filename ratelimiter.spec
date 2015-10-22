{
    "attributes": {
        "committedInformationRate": {
            "description": "Committed Information Rate :  Committed bandwidth that is allowed in Mb/s; only whole values supported.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "peakBurstSize": {
            "description": "Peak Burst Size :  The maximum burst size associated with the rate limiter in kilo-bits; only whole values are supported.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "peakInformationRate": {
            "description": "Peak Information Rate :  Peak bandwidth allowed in Mb/s; only whole values supported.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "description": {
            "description": "A description of the Rate Limiter object", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "name": {
            "description": "A unique name of the Rate Limiter object", 
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
        "resource_name": "ratelimiters", 
        "description": "Rate Limiter object that contains peak, burst and cir. Can be associated with Egress QOS policy objects.", 
        "entity_name": "RateLimiter", 
        "package": "policy/qos", 
        "get": true, 
        "update": true, 
        "rest_name": "ratelimiter", 
        "extends": [
            "@base", 
            "@metadata"
        ], 
        "delete": true
    }
}