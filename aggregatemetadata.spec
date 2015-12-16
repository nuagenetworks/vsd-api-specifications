{
    "attributes": {
        "blob": {
            "description": "Metadata that describes about the entity attached to it.", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "required": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "description": {
            "description": "Description of the Metadata.", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "global": {
            "description": "specifies metadata is global or local", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "boolean", 
            "uniqueScope": "no"
        }, 
        "metadataTagIDs": {
            "description": "metadata tag IDs associated with this metadata you can filter metadata based on this attribute for example  X-Nuage-Filter: '2d6fb627-603b-421c-b63a-eb0a6d712761' IN metadataTagIDs ", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "list",
            "subtype": "string",
            "uniqueScope": "no"
        }, 
        "name": {
            "description": "name of the Metadata.", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "networkNotificationDisabled": {
            "description": "specifies metadata changes need to be notified to controller,by default it is notified", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "boolean", 
            "uniqueScope": "no"
        }
    }, 
    "model": {
        "description": "Metadata associated to a entity", 
        "entity_name": "AggregateMetadata", 
        "extends": [
            "@base"
        ], 
        "package": "common", 
        "resource_name": "aggregatemetadatas", 
        "rest_name": "aggregatemetadata"
    }
}