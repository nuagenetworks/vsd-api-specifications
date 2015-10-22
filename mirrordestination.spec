{
    "attributes": {
        "destinationIp": {
            "description": "IP address of the destination server where you want your traffic to be mirrored.", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "name": {
            "description": "Name of the mirror destination. Valid characters are alphabets, numbers, space and hyphen( - ).", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "serviceId": {
            "description": "Service ID of the mirror destination.", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "float", 
            "uniqueScope": "no"
        }
    }, 
    "children": {
        "vportmirror": {
            "get": true, 
            "relationship": "child"
        }
    }, 
    "delete": true, 
    "description": "Represents the mirror destination entity.", 
    "entity_name": "MirrorDestination", 
    "extends": [
        "@base", 
        "@metadata"
    ], 
    "get": true, 
    "package": "vport", 
    "resource_name": "mirrordestinations", 
    "rest_name": "mirrordestination", 
    "update": true
}