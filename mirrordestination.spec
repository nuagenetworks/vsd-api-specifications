{
    "attributes": {
        "serviceId": {
            "description": "Service ID of the mirror destination.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "float"
        }, 
        "name": {
            "description": "Name of the mirror destination. Valid characters are alphabets, numbers, space and hyphen( - ).", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "destinationIp": {
            "description": "IP address of the destination server where you want your traffic to be mirrored.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }
    }, 
    "model": {
        "resource_name": "mirrordestinations", 
        "description": "Represents the mirror destination entity.", 
        "entity_name": "MirrorDestination", 
        "package": "vport", 
        "get": true, 
        "update": true, 
        "rest_name": "mirrordestination", 
        "extends": [
            "@base", 
            "@metadata"
        ], 
        "delete": true
    }, 
    "children": {
        "vportmirror": {
            "relationship": "child", 
            "get": true
        }
    }
}