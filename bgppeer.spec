{
    "attributes": {
        "address": {
            "description": "IP of the BGP peer.", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "lastStateChange": {
            "description": "Last state change timestamp.", 
            "exposed": true, 
            "type": "float", 
            "uniqueScope": "no"
        }, 
        "status": {
            "allowed_choices": [
                "DOWN", 
                "UP", 
                "ADMIN_DOWN"
            ], 
            "description": "Current connection status of the BGP peer. Possible values are UP, DOWN, ADMIN_DOWN, .", 
            "exposed": true, 
            "type": "enum", 
            "uniqueScope": "no"
        }
    }, 
    "description": "Encapsulates the BGP peer information for system monitor entity.", 
    "entity_name": "BGPPeer", 
    "extends": [
        "@base", 
        "@metadata"
    ], 
    "package": "/sysmon", 
    "resource_name": "bgppeers", 
    "rest_name": "bgppeer"
}