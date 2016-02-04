{
    "attributes": {
        "associatedExportRoutingPolicyID": {
            "description": "export BGP policy ID",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "associatedImportRoutingPolicyID": {
            "description": "import BGP policy ID",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "dampeningHalfLife": {
            "description": "The time in minutes to wait before decrementing dampening penalty; range 1 - 45, default: 15",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string"
        },
        "dampeningMaxSuppress": {
            "description": "The maximum duration in minutes that a route will be suppressed; range: 1-720, default: 60",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string"
        },
        "dampeningName": {
            "description": "Name for the dampening profile. Unique per enterprise",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string"
        },
        "description": {
            "description": null,
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "name": {
            "creation_only": true,
            "description": "Per enterprise unique name",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "required": true,
            "type": "string",
            "uniqueScope": "no"
        }
    },
    "model": {
        "delete": true,
        "entity_name": "BGPProfile",
        "extends": [
            "@base",
            "@metadata"
        ],
        "get": true,
        "resource_name": "bgpprofiles",
        "rest_name": "bgpprofile",
        "update": true
    }
}