{
    "attributes": {
        "IPAddress": {
            "description": "Static IP Address", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "required": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "MAC": {
            "description": "MAC Address", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "required": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "dynamicAllocationEnabled": {
            "description": "Binding is static or dynamic", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "boolean", 
            "uniqueScope": "no"
        }
    }, 
    "children": {
        "eventlog": {
            "get": true, 
            "relationship": "child"
        }
    }, 
    "delete": true, 
    "description": "This is the definition of a IP Bindings associated with in a Network", 
    "entity_name": "IPReservation", 
    "extends": [
        "@base", 
        "@metadata"
    ], 
    "get": true, 
    "package": "/network", 
    "resource_name": "ipreservations", 
    "rest_name": "ipreservation", 
    "update": true
}