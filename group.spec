{
    "attributes": {
        "restrictionDate": {
            "description": "When the group was disabled.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "time"
        }, 
        "description": {
            "description": "Description of the group", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "private": {
            "description": "A private group is visible only by the owner of the group. Public groups are visible by all users in the enterprise", 
            "format": "free", 
            "filterable": true, 
            "uniqueScope": "no", 
            "required": true, 
            "exposed": true, 
            "orderable": true, 
            "type": "boolean"
        }, 
        "accountRestrictions": {
            "description": "Determines whether group is disabled or not.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "boolean"
        }, 
        "role": {
            "description": "The role associated with this group - CSPROOT, CSPOPERATOR, ORGADMIN, ORGNETWORKDESIGNER, ORGUSER and USER Possible values are SYSTEM, JMS, CSPROOT, CMS, CSPOPERATOR, ORGADMIN, ORGAPPDESIGNER, ORGNETWORKDESIGNER, ORGUSER, USER, UNKNOWN, .", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
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
            "orderable": true, 
            "type": "enum"
        }, 
        "name": {
            "description": "A unique name of the group", 
            "format": "free", 
            "filterable": true, 
            "uniqueScope": "no", 
            "required": true, 
            "exposed": true, 
            "orderable": true, 
            "type": "string"
        }
    }, 
    "model": {
        "resource_name": "groups", 
        "description": "Identifies a group within an enterprise", 
        "entity_name": "Group", 
        "package": "usermgmt", 
        "get": true, 
        "update": true, 
        "rest_name": "group", 
        "extends": [
            "@base", 
            "@metadata"
        ], 
        "delete": true
    }, 
    "children": {
        "user": {
            "update": true, 
            "relationship": "child", 
            "get": true
        }, 
        "eventlog": {
            "relationship": "child", 
            "get": true
        }
    }
}