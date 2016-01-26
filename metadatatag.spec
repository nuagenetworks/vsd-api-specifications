{
    "attributes": {
        "associatedExternalServiceID": {
            "description": "ID of the entity to which the Metadata tag is  associated to", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "autoCreated": {
            "description": "set to true if it is the default metadata tag created as part of external service creation", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "boolean", 
            "uniqueScope": "no"
        }, 
        "description": {
            "description": "Description of the Metadata tag.", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "min_length": 0,
            "max_length": 255,
            "uniqueScope": "no"
        }, 
        "name": {
            "description": "name of the Metadata tag.", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "required": true, 
            "type": "string", 
            "min_length": 1,
            "max_length": 255,
            "uniqueScope": "no"
        }
    }, 
    "children": {
        "eventlog": {
            "get": true, 
            "relationship": "child"
        }, 
        "globalmetadata": {
            "get": true, 
            "relationship": "child", 
            "update": true
        }, 
        "metadata": {
            "get": true, 
            "relationship": "child", 
            "update": true
        }
    }, 
    "model": {
        "delete": true, 
        "description": "Metadata tag associated to a metadata", 
        "entity_name": "MetadataTag", 
        "extends": [
            "@base",
            "@audited"
        ],
        "get": true, 
        "package": "common", 
        "resource_name": "metadatatags", 
        "rest_name": "metadatatag", 
        "update": true
    }
}