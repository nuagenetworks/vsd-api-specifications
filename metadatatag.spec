{
    "attributes": {
        "associatedExternalServiceID": {
            "description": "ID of the entity to which the Metadata tag is  associated to", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "autoCreated": {
            "description": "set to true if it is the default metadata tag created as part of external service creation", 
            "exposed": true, 
            "type": "boolean", 
            "uniqueScope": "no"
        }, 
        "description": {
            "description": "Description of the Metadata tag.", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "name": {
            "description": "name of the Metadata tag.", 
            "exposed": true, 
            "required": true, 
            "type": "string", 
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
    "delete": true, 
    "description": "Metadata tag associated to a metadata", 
    "entity_name": "MetadataTag", 
    "extends": [
        "@base"
    ], 
    "get": true, 
    "package": "/common", 
    "resource_name": "metadatatags", 
    "rest_name": "metadatatag", 
    "update": true
}