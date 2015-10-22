{
    "attributes": {
        "name": {
            "description": "Name of the  Permission", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "permittedAction": {
            "allowed_choices": [
                "EXTEND", 
                "INSTANTIATE", 
                "DEPLOY", 
                "USE", 
                "READ", 
                "ALL"
            ], 
            "description": "The permitted  action to USE/EXTEND/READ/INSTANTIATE  an entity Possible values are USE, READ, ALL, INSTANTIATE, EXTEND, DEPLOY, .", 
            "exposed": true, 
            "required": true, 
            "type": "enum", 
            "uniqueScope": "no"
        }, 
        "permittedEntityDescription": {
            "description": "Description for the permittedEntity", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "permittedEntityID": {
            "description": "The enterprise permitted to use/extend  this Gateway", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "permittedEntityName": {
            "description": "Name of the entity for which we have given permission.", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "permittedEntityType": {
            "description": "Type of the entity for which we have given permission.", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }
    }, 
    "delete": true, 
    "description": "Represents Enterprise Permission for a CSP entity", 
    "entity_name": "EnterprisePermission", 
    "extends": [
        "@base", 
        "@metadata"
    ], 
    "get": true, 
    "package": "/gateway", 
    "resource_name": "enterprisepermissions", 
    "rest_name": "enterprisepermission", 
    "update": true
}