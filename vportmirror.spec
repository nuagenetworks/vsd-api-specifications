{
    "attributes": {
        "VPortName": {
            "description": "Name of the vport to which the mirror destination is associated with.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "mirrorDestinationID": {
            "description": "Destination ID of the mirror destination object.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "domainName": {
            "description": "Domain name of the vport associated with the mirror destination", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "mirrorDirection": {
            "description": "Describes what type of traffic needs to be mirrors - ingress/egress/both Possible values are BOTH, INGRESS, EGRESS, .", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "allowed_choices": [
                "BOTH", 
                "EGRESS", 
                "INGRESS"
            ], 
            "orderable": true, 
            "type": "enum"
        }, 
        "mirrorDestinationName": {
            "description": "Name of the mirror destination", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "attachedNetworkType": {
            "description": "Type of the network attached - L2/L3", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "enterpiseName": {
            "description": "Enterprise to which the vport associated with the mirror destination belongs to.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "networkName": {
            "description": "Name of the network to which the vport belongs to", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "vportId": {
            "description": "Id of the vport to which the mirror destination is associated with.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }
    }, 
    "model": {
        "resource_name": "vportmirrors", 
        "description": "VPort Mirror Object represents the relationship between a vport and a mirror destination.", 
        "entity_name": "VPortMirror", 
        "package": "vport", 
        "get": true, 
        "update": true, 
        "rest_name": "vportmirror", 
        "extends": [
            "@base", 
            "@metadata"
        ], 
        "delete": true
    }
}