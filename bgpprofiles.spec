{
    "attributes": {
        "associatedExportPolicyID": {
            "description": "export BGP policy ID", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "integer"
        }, 
        "associatedImportPolicyID": {
            "description": "import BGP policy ID", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "integer"
        }, 
        "description": {
            "description": null, 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string"
        }, 
        "name": {
            "creation_only": true, 
            "description": "Per enterprise unique name", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "required": true, 
            "type": "string"
        }
    }, 
    "model": {
        "delete": true, 
        "entity_name": "BgpProfile", 
        "get": true, 
        "resource_name": "bgpprofiles", 
        "rest_name": "bgpprofiles", 
        "update": true
    }
}