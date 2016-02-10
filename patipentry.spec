{
    "attributes": {
        "associatedPATMapperID": {
            "description": null,
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string"
        },
        "hypervisorID": {
            "description": null,
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string"
        },
        "ipAddress": {
            "description": null,
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string"
        },
        "ipType": {
            "description": null,
            "exposed": true,
            "filterable": true,
            "orderable": true,
            "type": "object"
        }
    },
    "model": {
        "delete": true,
        "entity_name": "PATIpEntry",
        "get": true,
        "resource_name": "patipentries",
        "rest_name": "patipentry",
        "update": true
    }
}