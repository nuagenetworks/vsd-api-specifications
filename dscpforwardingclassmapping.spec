{
    "attributes": {
        "forwardingClass": {
            "description": "Class of service to be used.  Service classes in order of priority are A, B, C, D, E, F, G, and H.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "enum"
        }, 
        "DSCP": {
            "description": "DSCP value range from enumeration of 65 values :  *, 0, 1, ..., 63", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }
    }, 
    "model": {
        "resource_name": "dscpforwardingclassmappings", 
        "description": "Provides the definition of a single DSCP -> Forwarding class mapping that is part of a Table used in QoS policies.", 
        "entity_name": "DSCPForwardingClassMapping", 
        "package": "policy", 
        "get": true, 
        "update": true, 
        "rest_name": "dscpforwardingclassmapping", 
        "extends": [
            "@base", 
            "@metadata"
        ], 
        "delete": true
    }
}