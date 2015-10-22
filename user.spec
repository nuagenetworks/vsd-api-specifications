{
    "attributes": {
        "userName": {
            "description": "Unique Username of the user. Valid characters are alphabets, numbers and hyphen( - ).", 
            "format": "free", 
            "filterable": true, 
            "uniqueScope": "no", 
            "required": true, 
            "exposed": true, 
            "orderable": true, 
            "type": "string"
        }, 
        "mobileNumber": {
            "description": "Mobile Number of the user", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "firstName": {
            "description": "First name of the user", 
            "format": "free", 
            "filterable": true, 
            "uniqueScope": "no", 
            "required": true, 
            "exposed": true, 
            "orderable": true, 
            "type": "string"
        }, 
        "avatarData": {
            "description": "URL to the avatar data associated with the enterprise. If the avatarType is URL then value of avatarData should an URL of the image. If the avatarType BASE64 then avatarData should be BASE64 encoded value of the image", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "disabled": {
            "description": "Status of the user account; true=disabled, false=not disabled; default value = false", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "boolean"
        }, 
        "avatarType": {
            "description": "Avatar type - URL or BASE64 Possible values are URL, BASE64, COMPUTEDURL, .", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "allowed_choices": [
                "COMPUTEDURL", 
                "BASE64", 
                "URL"
            ], 
            "orderable": true, 
            "type": "enum"
        }, 
        "lastName": {
            "description": "Last name of the user", 
            "format": "free", 
            "filterable": true, 
            "uniqueScope": "no", 
            "required": true, 
            "exposed": true, 
            "orderable": true, 
            "type": "string"
        }, 
        "password": {
            "description": "User password stored as a hash (SHA-1 encrpted)", 
            "format": "free", 
            "filterable": true, 
            "uniqueScope": "no", 
            "required": true, 
            "exposed": true, 
            "orderable": true, 
            "type": "string"
        }, 
        "email": {
            "description": "Email address of the user", 
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
        "resource_name": "users", 
        "description": "Object that identifies the user functions", 
        "entity_name": "User", 
        "package": "usermgmt", 
        "get": true, 
        "update": true, 
        "rest_name": "user", 
        "extends": [
            "@base", 
            "@metadata"
        ], 
        "delete": true
    }, 
    "children": {
        "group": {
            "relationship": "child", 
            "get": true
        }, 
        "vm": {
            "relationship": "child", 
            "get": true
        }, 
        "eventlog": {
            "relationship": "child", 
            "get": true
        }
    }
}