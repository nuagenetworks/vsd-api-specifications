{
    "attributes": {
        "accountRestrictions": {
            "description": "Determines whether group is disabled or not.", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "boolean", 
            "uniqueScope": "no"
        }, 
        "description": {
            "description": "Description of the group", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
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
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
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
            "@metadata"
        ], 
        "get": true, 
        "package": "usermgmt", 
        "resource_name": "groups", 
        "rest_name": "group", 
        "update": true
    }
}