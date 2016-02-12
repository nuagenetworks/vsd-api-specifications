{
    "attributes": {
        "address": {
            "description": "IP of the BGP peer.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 255,
            "min_length": 1,
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "lastStateChange": {
            "description": "Last state change timestamp.",
            "exposed": true,
            "format": "free",
            "subtype": "long",
            "type": "integer",
            "uniqueScope": "no"
        },
        "status": {
            "allowed_choices": [
                "ADMIN_DOWN",
                "DOWN",
                "UP"
            ],
            "description": "Current connection status of the BGP peer. Possible values are UP, DOWN, ADMIN_DOWN, .",
            "exposed": true,
            "format": "free",
            "type": "enum",
            "uniqueScope": "no"
        }
    },
    "model": {
        "description": "Encapsulates the BGP peer information for system monitor entity",
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