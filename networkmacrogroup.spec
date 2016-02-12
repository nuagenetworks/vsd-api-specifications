{
    "attributes": {
        "description": {
            "description": "Description of the macro group",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 255,
            "type": "string",
            "uniqueScope": "no"
        },
        "name": {
            "description": "Name of the macro group",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 64,
            "min_length": 1,
            "orderable": true,
            "required": true,
            "type": "string",
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
        "description": "Administrators of an enterprise can define macros that are set of IP addresses that identify enterprise networks. These macros can be used in the ACL definitions by network designers and other users to identify access restrictions towards specific enterprise networks.",
        "entity_name": "NetworkMacroGroup",
        "extends": [
            "@audited",
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