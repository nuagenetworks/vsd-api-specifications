{
    "attributes": [
        {
            "description": "The image type",
            "exposed": true,
            "format": "free",
            "name": "type",
            "type": "string",
            "uniqueScope": "no"
        }
    ],
    "children": [],
    "model": {
        "delete": true,
        "description": "Avatar",
        "entity_name": "Avatar",
        "extends": [
            "@audited",
            "@base",
            "@metadata"
        ],
        "get": true,
        "package": "usermgmt",
        "resource_name": "avatars",
        "rest_name": "avatar",
        "update": true,
        "userlabel": "Avatar"
    }
}