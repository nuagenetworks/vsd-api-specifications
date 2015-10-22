{
    "attributes": {
        "netmask": {
            "description": "IP address netmask of the Network NSPort.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "gateway": {
            "description": "IP address of the gateway bound to the Network NSPort.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "enabled": {
            "description": "Boolean value that states if the NSG Port static configuration needs to be applied.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "boolean"
        }, 
        "DNSAddress": {
            "description": "DNS Address for Network NSPort.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "address": {
            "description": "IP address of the Network NSPort.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }
    }, 
    "model": {
        "resource_name": "nsportstaticconfigurations", 
        "description": "Represents a network port static configuration in the context of an NSG.", 
        "entity_name": "NSPortStaticConfiguration", 
        "package": "nsg", 
        "get": true, 
        "update": true, 
        "rest_name": "nsportstaticconfiguration", 
        "extends": [
            "@base", 
            "@metadata"
        ], 
        "delete": true
    }
}