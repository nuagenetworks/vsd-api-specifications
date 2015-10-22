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
            "description": "The enterprise permitted to use/extend  this Gateway", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }
    }, 
    "model": {
        "resource_name": "enterprisepermissions", 
        "description": "Represents Enterprise Permission for a CSP entity", 
        "entity_name": "EnterprisePermission", 
        "package": "gateway", 
        "get": true, 
        "update": true, 
        "rest_name": "enterprisepermission", 
        "extends": [
            "@base", 
            "@metadata"
        ], 
        "delete": true
    }
}