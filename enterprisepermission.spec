{
    "attributes": {
        "name": {
            "description": "Name of the  Permission",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 255,
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "permittedAction": {
            "allowed_choices": [
                "ALL",
                "DEPLOY",
                "EXTEND",
                "INSTANTIATE",
                "READ",
                "USE"
            ],
            "description": "The permitted  action to USE/EXTEND/READ/INSTANTIATE  an entity Possible values are USE, READ, ALL, INSTANTIATE, EXTEND, DEPLOY, .",
            "exposed": true,
            "format": "free",
            "required": true,
            "type": "enum",
            "uniqueScope": "no"
        },
        "permittedEntityDescription": {
            "description": "Description for the permittedEntity",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "permittedEntityID": {
            "description": "The enterprise permitted to use/extend  this Gateway",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "permittedEntityName": {
            "description": "Name of the entity for which we have given permission.",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "permittedEntityType": {
            "description": "Type of the entity for which we have given permission.",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        }
    },
    "model": {
        "delete": true,
        "description": "Represents Enterprise Permission for a CSP entity.",
        "entity_name": "EnterprisePermission",
        "extends": [
            "@audited",
            "@base",
            "@metadata"
        ],
        "get": true,
        "package": "gateway",
        "resource_name": "enterprisepermissions",
        "rest_name": "enterprisepermission",
        "update": true
    }
}