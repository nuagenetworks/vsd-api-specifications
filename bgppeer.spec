{
    "attributes": {
        "lastStateChange": {
            "description": "Last state change timestamp.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "float"
        }, 
        "status": {
            "description": "Current connection status of the BGP peer. Possible values are UP, DOWN, ADMIN_DOWN, .", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "allowed_choices": [
                "DOWN", 
                "UP", 
                "ADMIN_DOWN"
            ], 
            "orderable": true, 
            "type": "enum"
        }, 
        "address": {
            "description": "IP of the BGP peer.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }
    }, 
    "model": {
        "resource_name": "bgppeers", 
        "description": "Encapsulates the BGP peer information for system monitor entity.", 
        "entity_name": "BGPPeer", 
        "package": "sysmon", 
        "rest_name": "bgppeer", 
        "extends": [
            "@base", 
            "@metadata"
        ]
    }
}