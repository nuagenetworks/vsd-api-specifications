{
    "attributes": {
        "name": {
            "description": "Name of the  Permission", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "permittedEntityType": {
            "description": "Type of the entity for which we have given permission.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "permittedEntityDescription": {
            "description": "Description for the permittedEntity", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "permittedAction": {
            "required": true, 
            "description": "The permitted  action to USE/EXTEND/READ/INSTANTIATE  an entity Possible values are USE, READ, ALL, INSTANTIATE, EXTEND, DEPLOY, .", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "allowed_choices": [
                "EXTEND", 
                "INSTANTIATE", 
                "DEPLOY", 
                "USE", 
                "READ", 
                "ALL"
            ], 
            "orderable": true, 
            "type": "enum"
        }, 
        "permittedEntityName": {
            "description": "Name of the entity for which we have given permission.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "permittedEntityID": {
            "description": "The  entity ID for which this permission action is associated against Possible values are .", 
            "format": "free", 
            "filterable": true, 
            "uniqueScope": "no", 
            "required": true, 
            "exposed": true, 
            "orderable": true, 
            "type": "enum"
        }
    }, 
    "model": {
        "resource_name": "permissions", 
        "description": "Represents  Permitted action on an  entity for a group", 
        "entity_name": "PermittedAction", 
        "package": "usermgmt", 
        "get": true, 
        "update": true, 
        "rest_name": "permission", 
        "extends": [
            "@base", 
            "@metadata"
        ], 
        "delete": true
    }, 
    "children": {
        "eventlog": {
            "relationship": "child", 
            "get": true
        }
    }
}