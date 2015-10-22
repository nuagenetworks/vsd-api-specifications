{
    "attributes": {
        "routeReflectorIP": {
            "description": "The IP address of the route reflector that can be used by the VSCs", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "serviceType": {
            "description": "Identifies whether L3 or L2 services are supported. Only L3services are supported in R1.0. Possible values are ROUTER_ONLY, ROUTER_SWITCH, SUBNET_ONLY, .", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "allowed_choices": [
                "ROUTER_SWITCH", 
                "ROUTER_ONLY", 
                "SUBNET_ONLY"
            ], 
            "orderable": true, 
            "type": "enum"
        }, 
        "autonomousSystemNum": {
            "description": "The AS number associated with this data center", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "integer"
        }
    }, 
    "model": {
        "resource_name": "networklayout", 
        "description": "This API defines the AS number that should be used in the data center as well as the IP address of the route reflector", 
        "entity_name": "NetworkLayout", 
        "package": "network", 
        "get": true, 
        "update": true, 
        "rest_name": "networklayout", 
        "extends": [
            "@base", 
            "@metadata"
        ], 
        "delete": true
    }
}