{
    "attributes": {
        "assocVCenterId": {
            "description": "The ID of the vcenter to which this host is attached",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string"
        },
        "managedObjectID": {
            "description": "VCenter Managed Object ID of the Datacenter",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string"
        },
        "name": {
            "description": "Name of the shared resource. Valid characters are alphabets, numbers, space and hyphen( - ).",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string"
        }
    },
    "model": {
        "delete": true,
        "entity_name": "Autodiscovereddatacenter",
        "get": true,
        "resource_name": "autodiscovereddatacenters",
        "rest_name": "autodiscovereddatacenter",
        "update": true
    }
}