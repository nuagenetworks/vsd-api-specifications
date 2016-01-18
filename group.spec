{
    "attributes": {
        "accountRestrictions": {
            "description": "Determines whether group is disabled or not.",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "boolean",
            "uniqueScope": "no"
        },
        "description": {
            "description": "Description of the group",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": false,
            "type": "string",
            "min_length": 0,
            "max_length": 255,
            "uniqueScope": "no"
        },
        "managementMode": {
            "description": "Management mode of the user object - allows for override of external authorization and syncup",
            "exposed": true,
            "allowed_choices": [
                "CMS",
                "DEFAULT"
            ],
            "filterable": false,
            "orderable": false,
            "type": "enum",
            "uniqueScope": "no"
        },
        "name": {
            "description": "A unique name of the group",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "required": true,
            "type": "string",
            "min_length": 1,
            "max_length": 255,
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
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "time",
            "uniqueScope": "no"
        },
        "role": {
            "allowed_choices": [
                "ORGAPPDESIGNER",
                "CMS",
                "CSPROOT",
                "UNKNOWN",
                "SYSTEM",
                "ORGNETWORKDESIGNER",
                "ORGADMIN",
                "JMS",
                "CSPOPERATOR",
                "ORGUSER",
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
            "relationship": "child",
            "update": true
        }
    },
    "model": {
        "delete": true,
        "description": "Identifies a group within an enterprise",
        "entity_name": "Group",
        "extends": [
            "@base",
            "@audited",
            "@metadata"
        ],
        "get": true,
        "package": "usermgmt",
        "resource_name": "groups",
        "rest_name": "group",
        "update": true
    }
}