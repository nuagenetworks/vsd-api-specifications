{
    "attributes": {
        "avatarData": {
            "description": "URL to the avatar data associated with the enterprise. If the avatarType is URL then value of avatarData should an URL of the image. If the avatarType BASE64 then avatarData should be BASE64 encoded value of the image", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "avatarType": {
            "allowed_choices": [
                "COMPUTEDURL", 
                "BASE64", 
                "URL"
            ], 
            "description": "Avatar type - URL or BASE64 Possible values are URL, BASE64, COMPUTEDURL, .", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "enum", 
            "uniqueScope": "no"
        }, 
        "disabled": {
            "description": "Status of the user account; true=disabled, false=not disabled; default value = false", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "boolean", 
            "uniqueScope": "no"
        }, 
        "email": {
            "description": "Email address of the user", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "required": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "firstName": {
            "description": "First name of the user", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "required": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "lastName": {
            "description": "Last name of the user", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "required": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "mobileNumber": {
            "description": "Mobile Number of the user", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "password": {
            "description": "User password stored as a hash (SHA-1 encrpted)", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "required": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "userName": {
            "description": "Unique Username of the user. Valid characters are alphabets, numbers and hyphen( - ).", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "required": true, 
            "type": "string", 
            "uniqueScope": "no"
        }
    }, 
    "children": {
        "eventlog": {
            "get": true, 
            "relationship": "child"
        }, 
        "group": {
            "get": true, 
            "relationship": "child"
        }, 
        "vm": {
            "get": true, 
            "relationship": "child"
        }
    }, 
    "delete": true, 
    "description": "Object that identifies the user functions", 
    "entity_name": "User", 
    "extends": [
        "@base", 
        "@metadata"
    ], 
    "get": true, 
    "package": "/usermgmt", 
    "resource_name": "users", 
    "rest_name": "user", 
    "update": true
}