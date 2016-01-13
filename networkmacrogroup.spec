{
    "attributes": {
        "description": {
            "description": "Description of the macro group",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": false,
            "type": "string",
            "min_length": 0,
            "max_length": 255,
            "uniqueScope": "no"
        },
        "name": {
            "description": "Name of the macro group",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "required": true,
            "type": "string",
            "min_length": 1,
            "max_length": 64,
            "uniqueScope": "no"
        }
    },
    "children": {
        "enterprisenetwork": {
            "get": true,
            "relationship": "child",
            "update": true
        }
    },
    "model": {
        "delete": true,
        "description": "Administrators of an enterprise can define macros that are set of IP addresses that identify enterprise networks. These macros can be used in the ACL definitions by network designers and other users to identify access restrictions towards specific enterprise networks",
        "entity_name": "NetworkMacroGroup",
        "extends": [
            "@base",
            "@metadata"
        ],
        "get": true,
        "package": "network",
        "resource_name": "networkmacrogroups",
        "rest_name": "networkmacrogroup",
        "update": true
    }
}