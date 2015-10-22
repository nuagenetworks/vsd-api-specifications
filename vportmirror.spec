{
    "attributes": {
        "VPortName": {
            "description": "Name of the vport to which the mirror destination is associated with.", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "attachedNetworkType": {
            "description": "Type of the network attached - L2/L3", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "domainName": {
            "description": "Domain name of the vport associated with the mirror destination", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "enterpiseName": {
            "description": "Enterprise to which the vport associated with the mirror destination belongs to.", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "mirrorDestinationID": {
            "description": "Destination ID of the mirror destination object.", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "mirrorDestinationName": {
            "description": "Name of the mirror destination", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "mirrorDirection": {
            "allowed_choices": [
                "BOTH", 
                "EGRESS", 
                "INGRESS"
            ], 
            "description": "Describes what type of traffic needs to be mirrors - ingress/egress/both Possible values are BOTH, INGRESS, EGRESS, .", 
            "exposed": true, 
            "type": "enum", 
            "uniqueScope": "no"
        }, 
        "networkName": {
            "description": "Name of the network to which the vport belongs to", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "vportId": {
            "description": "Id of the vport to which the mirror destination is associated with.", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }
    }, 
    "delete": true, 
    "description": "VPort Mirror Object represents the relationship between a vport and a mirror destination.", 
    "entity_name": "VPortMirror", 
    "extends": [
        "@base", 
        "@metadata"
    ], 
    "get": true, 
    "package": "/vport", 
    "resource_name": "vportmirrors", 
    "rest_name": "vportmirror", 
    "update": true
}