{
    "attributes": {
        "domainID": {
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
            "allowed_choices": [
                "IPV6",
                "IPV4"
            ],
            "description": null,
            "exposed": true,
            "filterable": true,
            "orderable": true,
            "type": "enum"
        },
        "isPATCentralized": {
            "description": null,
            "exposed": true,
            "filterable": true,
            "orderable": true,
            "type": "boolean"
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