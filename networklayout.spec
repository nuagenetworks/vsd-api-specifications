{
    "attributes": {
        "autonomousSystemNum": {
            "description": "The AS number associated with this data center", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "integer", 
            "uniqueScope": "no"
        }, 
        "routeReflectorIP": {
            "description": "The IP address of the route reflector that can be used by the VSCs", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "serviceType": {
            "allowed_choices": [
                "ROUTER_SWITCH", 
                "ROUTER_ONLY", 
                "SUBNET_ONLY"
            ], 
            "description": "Identifies whether L3 or L2 services are supported. Only L3services are supported in R1.0. Possible values are ROUTER_ONLY, ROUTER_SWITCH, SUBNET_ONLY, .", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "enum", 
            "uniqueScope": "no"
        }
    }, 
    "delete": true, 
    "description": "This API defines the AS number that should be used in the data center as well as the IP address of the route reflector", 
    "entity_name": "NetworkLayout", 
    "extends": [
        "@base", 
        "@metadata"
    ], 
    "get": true, 
    "package": "/network", 
    "resource_name": "networklayout", 
    "rest_name": "networklayout", 
    "update": true
}