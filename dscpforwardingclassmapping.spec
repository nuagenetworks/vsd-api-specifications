{
    "attributes": {
        "DSCP": {
            "description": "DSCP value range from enumeration of 65 values :  *, 0, 1, ..., 63", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "forwardingClass": {
            "description": "Class of service to be used.  Service classes in order of priority are A, B, C, D, E, F, G, and H.", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "enum", 
            "uniqueScope": "no"
        }
    }, 
    "delete": true, 
    "description": "Provides the definition of a single DSCP -> Forwarding class mapping that is part of a Table used in QoS policies.", 
    "entity_name": "DSCPForwardingClassMapping", 
    "extends": [
        "@base", 
        "@metadata"
    ], 
    "get": true, 
    "package": "/policy", 
    "resource_name": "dscpforwardingclassmappings", 
    "rest_name": "dscpforwardingclassmapping", 
    "update": true
}