{
    "attributes": {
        "accountRestrictions": {
            "description": "Determines whether group is disabled or not.",
            "exposed": true,
            "format": "free",
            "type": "boolean",
            "uniqueScope": "no"
        },
        "description": {
            "description": "Description of the group",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 255,
            "type": "string",
            "uniqueScope": "no"
        },
        "managementMode": {
            "allowed_choices": [
                "CMS",
                "DEFAULT"
            ],
            "description": "Management mode of the user object - allows for override of external authorization and syncup",
            "exposed": true,
            "format": "free",
            "type": "enum",
            "uniqueScope": "no"
        },
        "name": {
            "description": "A unique name of the group",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 255,
            "min_length": 1,
            "orderable": true,
            "required": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "private": {
            "description": "A private group is visible only by the owner of the group. Public groups are visible by all users in the enterprise",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "required": true,
            "type": "boolean",
            "uniqueScope": "no"
        },
        "restrictionDate": {
            "description": "When the group was disabled.",
            "exposed": true,
            "format": "free",
            "type": "time",
            "uniqueScope": "no"
        },
        "role": {
            "allowed_choices": [
                "CMS",
                "CSPOPERATOR",
                "CSPROOT",
                "JMS",
                "ORGADMIN",
                "ORGAPPDESIGNER",
                "ORGNETWORKDESIGNER",
                "ORGUSER",
                "SYSTEM",
                "UNKNOWN",
                "USER"
            ],
            "description": "The role associated with this group - CSPROOT, CSPOPERATOR, ORGADMIN, ORGNETWORKDESIGNER, ORGUSER and USER Possible values are SYSTEM, JMS, CSPROOT, CMS, CSPOPERATOR, ORGADMIN, ORGAPPDESIGNER, ORGNETWORKDESIGNER, ORGUSER, USER, UNKNOWN, .",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "enum",
            "uniqueScope": "no"
        }
    },
    "children": {
        "eventlog": {
            "get": true,
            "relationship": "child"
        },
        "user": {
            "get": true,
            "relationship": "member",
            "update": true
        }
    },
    "model": {
        "delete": true,
        "description": "Identifies a group within an enterprise.",
        "entity_name": "Group",
        "extends": [
            "@audited",
            "@base",
            "@metadata"
        ],
        "get": true,
        "package": "usermgmt",
        "resource_name": "groups",
        "rest_name": "group",
        "update": true
    }
}