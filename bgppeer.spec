{
    "attributes": {
        "address": {
            "description": "IP of the BGP peer.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string",
            "min_length": 1,
            "max_length": 255,
            "uniqueScope": "no"
        },
        "lastStateChange": {
            "description": "Last state change timestamp.",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
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
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "enum",
            "uniqueScope": "no"
        }
    },
    "model": {
        "description": "Encapsulates the BGP peer information for system monitor entity.",
        "entity_name": "BGPPeer",
        "extends": [
            "@base",
            "@metadata"
        ],
        "package": "sysmon",
        "resource_name": "bgppeers",
        "rest_name": "bgppeer"
    }
}