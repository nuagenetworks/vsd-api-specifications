{
    "attributes": {
        "name": {
            "description": "Name of the  Permission",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
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
            "filterable": true,
            "format": "free",
            "orderable": true,
            "required": true,
            "type": "enum",
            "uniqueScope": "no"
        },
        "permittedEntityDescription": {
            "description": "Description for the permittedEntity",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "permittedEntityID": {
            "description": "The  entity ID for which this permission action is associated against Possible values are .",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "required": true,
            "type": "enum",
            "uniqueScope": "no"
        },
        "permittedEntityName": {
            "description": "Name of the entity for which we have given permission.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "permittedEntityType": {
            "description": "Type of the entity for which we have given permission.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        }
    },
    "children": {
        "eventlog": {
            "get": true,
            "relationship": "child"
        }
    },
    "delete": true,
    "description": "Represents  Permitted action on an  entity for a group",
    "entity_name": "PermittedAction",
    "extends": [
        "@base",
        "@metadata"
    ],
    "get": true,
    "package": "usermgmt",
    "resource_name": "permissions",
    "rest_name": "permission",
    "update": true
}