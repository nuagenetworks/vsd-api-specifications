{
    "attributes": {
        "assigned": {
            "description": "True if this floating IP is assigned to a network interface else the value is false", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "boolean"
        }, 
        "associatedSharedNetworkResourceID": {
            "description": "Id of the shared network resource subnet which was used to get this floating IP address", 
            "format": "free", 
            "filterable": true, 
            "uniqueScope": "no", 
            "required": true, 
            "exposed": true, 
            "orderable": true, 
            "type": "string"
        }, 
        "assignedToObjectType": {
            "description": "The object type to which this floating ip is assigned. Eg. vport or virtualip", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "address": {
            "description": "Floating IP address assigned to the Domain", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }
    }, 
    "model": {
        "resource_name": "floatingips", 
        "description": "Floating IP that is associated to a Domain. This floating IP could be used in the VM interface for NAT functionality", 
        "entity_name": "FloatingIp", 
        "package": "network", 
        "get": true, 
        "update": true, 
        "rest_name": "floatingip", 
        "extends": [
            "@base", 
            "@metadata"
        ], 
        "delete": true
    }, 
    "children": {
        "vport": {
            "relationship": "child", 
            "get": true
        }, 
        "eventlog": {
            "relationship": "child", 
            "get": true
        }
    }
}