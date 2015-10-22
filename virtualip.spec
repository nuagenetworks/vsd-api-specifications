{
    "attributes": {
        "subnetID": {
            "description": "Id of subnet to which this ip address belongs", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "MAC": {
            "description": "The MAC address of the virtual port", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "associatedFloatingIPID": {
            "description": "Id of Floating IP address associated to this virtual ip", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "virtualIP": {
            "description": "Virtual IP address", 
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
        "resource_name": "virtualips", 
        "description": "Virtual IP address", 
        "entity_name": "VirtualIP", 
        "package": "vport", 
        "get": true, 
        "update": true, 
        "rest_name": "virtualip", 
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