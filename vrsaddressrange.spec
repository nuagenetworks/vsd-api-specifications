{
    "attributes": {
        "maxAddress": {
            "description": "Higest address in the address range", 
            "format": "free", 
            "filterable": true, 
            "uniqueScope": "no", 
            "required": true, 
            "exposed": true, 
            "orderable": true, 
            "type": "string"
        }, 
        "minAddress": {
            "description": "Lowest address in the address range", 
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
        "resource_name": "vrsaddressranges", 
        "description": "This is the definition of a Address Range associated with a VRS", 
        "entity_name": "VRSAddressRange", 
        "package": "vmware", 
        "get": true, 
        "update": true, 
        "rest_name": "vrsaddressrange", 
        "extends": [
            "@base", 
            "@metadata"
        ], 
        "delete": true
    }
}