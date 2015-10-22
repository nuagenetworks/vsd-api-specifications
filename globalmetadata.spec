{
    "attributes": {
        "metadataTagIDs": {
            "description": "metadata tag IDs associated with this metadata you can filter metadata based on this attribute for example  X-Nuage-Filter: '2d6fb627-603b-421c-b63a-eb0a6d712761' IN metadataTagIDs ", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "list"
        }, 
        "networkNotificationDisabled": {
            "description": "specifies metadata changes need to be notified to controller,by default it is notified", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "boolean"
        }, 
        "name": {
            "description": "name of the Metadata.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "global": {
            "description": "specifies metadata is global or local", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "boolean"
        }, 
        "blob": {
            "description": "Metadata that describes about the entity attached to it.", 
            "format": "free", 
            "filterable": true, 
            "uniqueScope": "no", 
            "required": true, 
            "exposed": true, 
            "orderable": true, 
            "type": "string"
        }, 
        "description": {
            "description": "Description of the Metadata.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }
    }, 
    "model": {
        "resource_name": "globalmetadatas", 
        "description": "Metadata associated to a entity", 
        "entity_name": "GlobalMetadata", 
        "package": "common", 
        "get": true, 
        "update": true, 
        "rest_name": "globalmetadata", 
        "extends": [
            "@base", 
            "@metadata"
        ], 
        "delete": true
    }, 
    "children": {
        "metadatatag": {
            "update": true, 
            "relationship": "child", 
            "get": true
        }
    }
}