{
    "attributes": {
        "IPAddress": {
            "description": "Its own IPAddress.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string"
        },
        "IPType": {
            "allowed_choices": [
                "DUALSTACK",
                "IPV4",
                "IPV6"
            ],
            "description": "IPv4 or IPv6 (only IPv4 supported in R1.0)",
            "exposed": true,
            "filterable": true,
            "orderable": true,
            "type": "enum"
        },
        "PATCentralized": {
            "description": "This flag will determine whether we can expect anchor point or not.",
            "exposed": true,
            "filterable": true,
            "orderable": true,
            "type": "boolean"
        },
        "associatedDomainID": {
            "description": "The ID of the associated l3-domain.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string"
        },
        "hypervisorID": {
            "description": "The ID of the PatMapper entity to which this domain is associated to.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string"
        }
    },
    "model": {
        "delete": true,
        "entity_name": "PATIPEntry",
        "get": true,
        "resource_name": "patipentries",
        "rest_name": "patipentry",
        "update": true
    }
}