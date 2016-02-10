{
    "attributes": {
        "associatedPATIpEntryID": {
            "description": "The ID of the associated PATIPENTRY.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string"
        },
        "privateIP": {
            "description": "VM's ip-address",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string"
        },
        "privatePort": {
            "description": "The vport's port-number.",
            "exposed": true,
            "filterable": true,
            "orderable": true,
            "type": "integer"
        },
        "publicIP": {
            "description": null,
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string"
        },
        "publicPort": {
            "description": null,
            "exposed": true,
            "filterable": true,
            "orderable": true,
            "type": "integer"
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