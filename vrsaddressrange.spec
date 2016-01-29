{
    "attributes": {
        "maxAddress": {
            "description": "Higest address in the address range",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "required": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "minAddress": {
            "description": "Lowest address in the address range",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "required": true,
            "type": "string",
            "uniqueScope": "no"
        }
    },
    "model": {
        "delete": true,
        "description": "This is the definition of a Address Range associated with a VRS",
        "entity_name": "VRSAddressRange",
        "extends": [
            "@base",
            "@audited",
            "@metadata"
        ],
        "get": true,
        "package": "vmware",
        "resource_name": "vrsaddressranges",
        "rest_name": "vrsaddressrange",
        "update": true
    }
}