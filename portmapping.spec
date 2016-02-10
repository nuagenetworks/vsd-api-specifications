{
    "attributes": {
        "associatedPATIPEntryID": {
            "description": "The ID of the associated PATIPENTRY.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "privateIP": {
            "description": "VM's ip-address",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "privatePort": {
            "description": "The vport's port-number.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "integer",
            "uniqueScope": "no"
        },
        "publicIP": {
            "description": "This is the PATIPENTRY value, for the traffic to go out of VM.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "publicPort": {
            "description": "The public port used for Static PAT.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "integer",
            "uniqueScope": "no"
        }
    },
    "model": {
        "delete": true,
        "entity_name": "PortMapping",
        "get": true,
        "resource_name": "portmappings",
        "rest_name": "portmapping",
        "update": true
    }
}