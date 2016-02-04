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