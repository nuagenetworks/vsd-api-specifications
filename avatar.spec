{
    "attributes" : [ {
        "name" : "type",
        "type" : "string",
        "format" : "free",
        "description" : "The image type",
        "exposed" : true,
        "uniqueScope" : "no"
    } ],
    "children" : [ ],
    "model" : {
        "description" : "Avatar",
        "entity_name" : "Avatar",
        "extends" : [ "@audited", "@base", "@metadata" ],
        "package" : "usermgmt",
        "resource_name" : "avatars",
        "rest_name" : "avatar",
        "get" : true,
        "update" : true,
        "delete" : true
    }
}
