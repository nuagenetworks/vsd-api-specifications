{
    "attributes": {
        "associatedPATNATPoolID": {
            "description": "Read Only - Indicates which PATNATPool this entry belongs to",
            "exposed": true,
            "format": "free",
            "required": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "privateIP": {
            "description": "Private IP address of the interface",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "required": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "publicIP": {
            "description": "Public IP address of the interface",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "required": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "type": {
            "allowed_choices": [
                "1:1 PAT"
            ],
            "description": "Choose the type of address map",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "enum"
        }
    },
    "model": {
        "delete": true,
        "description": "Defines a MAP between the private ip and public ip",
        "entity_name": "NATMapEntry",
        "extends": [
            "@audited",
            "@base",
            "@metadata"
        ],
        "get": true,
        "package": "gateway",
        "resource_name": "natmapentries",
        "rest_name": "natmapentry"
    }
}