{
    "attributes": {
        "description": {
            "description": "Description of the macro group", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "name": {
            "description": "Name of the macro group", 
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
        "resource_name": "networkmacrogroups", 
        "description": "Administrators of an enterprise can define macros that are set of IP addresses that identify enterprise networks. These macros can be used in the ACL definitions by network designers and other users to identify access restrictions towards specific enterprise networks", 
        "entity_name": "NetworkMacroGroup", 
        "package": "network", 
        "get": true, 
        "update": true, 
        "rest_name": "networkmacrogroup", 
        "extends": [
            "@base", 
            "@metadata"
        ], 
        "delete": true
    }, 
    "children": {
        "enterprisenetwork": {
            "update": true, 
            "relationship": "child", 
            "get": true
        }
    }
}