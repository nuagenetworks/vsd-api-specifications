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
        "privatePort": {
            "description": "",
            "exposed": true,
            "format": "free",
            "type": "string"
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
        "publicPort": {
            "description": null,
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string"
        },
        "type": {
            "allowed_choices": [
                "1:1_NAT",
                "1:N_PAT"
            ],
            "default_value": "1:1_NAT",
            "description": "Choose the type of address map",
            "exposed": true,
            "filterable": true,
            "format": "free",
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