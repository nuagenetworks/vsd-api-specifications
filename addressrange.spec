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
        "DHCPPoolType": {
            "description": "DHCPPoolType is an enum that indicates if the DHCP Pool is for HOST/BRIDGE. Possible values are HOST, BRIDGE Possible values are HOST, BRIDGE, .", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "allowed_choices": [
                "HOST", 
                "BRIDGE"
            ], 
            "orderable": true, 
            "type": "enum"
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
        "resource_name": "addressranges", 
        "description": "This is the definition of a Address Range associated with a Network", 
        "entity_name": "AddressRange", 
        "package": "network", 
        "get": true, 
        "update": true, 
        "rest_name": "addressrange", 
        "extends": [
            "@base", 
            "@metadata"
        ], 
        "delete": true
    }, 
    "children": {
        "eventlog": {
            "relationship": "child", 
            "get": true
        }
    }
}