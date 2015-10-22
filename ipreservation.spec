{
    "attributes": {
        "dynamicAllocationEnabled": {
            "description": "Binding is static or dynamic", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "boolean"
        }, 
        "MAC": {
            "description": "MAC Address", 
            "format": "free", 
            "filterable": true, 
            "uniqueScope": "no", 
            "required": true, 
            "exposed": true, 
            "orderable": true, 
            "type": "string"
        }, 
        "IPAddress": {
            "description": "Static IP Address", 
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
        "resource_name": "ipreservations", 
        "description": "This is the definition of a IP Bindings associated with in a Network", 
        "entity_name": "IPReservation", 
        "package": "network", 
        "get": true, 
        "update": true, 
        "rest_name": "ipreservation", 
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