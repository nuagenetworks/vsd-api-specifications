{
    "attributes": {
        "status": {
            "description": "Status of the resync - IN_PROGRESS, SUCCESS Possible values are IN_PROGRESS, SUCCESS, .", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "allowed_choices": [
                "SUCCESS", 
                "IN_PROGRESS"
            ], 
            "orderable": true, 
            "type": "enum"
        }, 
        "lastRequestTimestamp": {
            "description": "Time of the last timestamp received", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "float"
        }, 
        "lastTimeResyncInitiated": {
            "description": "Time that the resync was initiated", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "float"
        }
    }, 
    "model": {
        "resource_name": "resync", 
        "description": "Provide information about the state of a VM resync request", 
        "entity_name": "VMResync", 
        "package": "vm", 
        "rest_name": "resync", 
        "extends": [
            "@base", 
            "@metadata"
        ]
    }
}