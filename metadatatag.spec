{
    "attributes": {
        "autoCreated": {
            "description": "set to true if it is the default metadata tag created as part of external service creation", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "boolean"
        }, 
        "associatedExternalServiceID": {
            "description": "ID of the entity to which the Metadata tag is  associated to", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "description": {
            "description": "Description of the Metadata tag.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "name": {
            "description": "name of the Metadata tag.", 
            "format": "free", 
            "filterable": true, 
            "uniqueScope": "no", 
            "required": true, 
            "exposed": true, 
            "orderable": true, 
            "type": "string"
        }
    }, 
    "model": {
        "resource_name": "metadatatags", 
        "description": "Metadata tag associated to a metadata", 
        "entity_name": "MetadataTag", 
        "package": "common", 
        "get": true, 
        "update": true, 
        "rest_name": "metadatatag", 
        "extends": [
            "@base"
        ], 
        "delete": true
    }, 
    "children": {
        "globalmetadata": {
            "update": true, 
            "relationship": "child", 
            "get": true
        }, 
        "eventlog": {
            "relationship": "child", 
            "get": true
        }, 
        "metadata": {
            "update": true, 
            "relationship": "child", 
            "get": true
        }
    }
}