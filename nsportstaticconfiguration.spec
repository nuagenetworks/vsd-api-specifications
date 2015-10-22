{
    "attributes": {
        "DNSAddress": {
            "description": "DNS Address for Network NSPort.", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "address": {
            "description": "IP address of the Network NSPort.", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "enabled": {
            "description": "Boolean value that states if the NSG Port static configuration needs to be applied.", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "boolean", 
            "uniqueScope": "no"
        }, 
        "gateway": {
            "description": "IP address of the gateway bound to the Network NSPort.", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "netmask": {
            "description": "IP address netmask of the Network NSPort.", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }
    }, 
    "delete": true, 
    "description": "Represents a network port static configuration in the context of an NSG.", 
    "entity_name": "NSPortStaticConfiguration", 
    "extends": [
        "@base", 
        "@metadata"
    ], 
    "get": true, 
    "package": "/nsg", 
    "resource_name": "nsportstaticconfigurations", 
    "rest_name": "nsportstaticconfiguration", 
    "update": true
}