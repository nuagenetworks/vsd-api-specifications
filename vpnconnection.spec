{
    "attributes": {
        "associatedWANServiceID": {
            "description": "Assosciated WAN Service", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "description": {
            "description": "A description of the VPNConnect", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "name": {
            "description": "Name of the VPNConnect", 
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
        "resource_name": "vpnconnections", 
        "description": "This is the definition of a VPN Connect which holds the PE service assocaition with a DOMAIN", 
        "entity_name": "VPNConnection", 
        "package": "network", 
        "get": true, 
        "update": true, 
        "rest_name": "vpnconnection", 
        "extends": [
            "@base", 
            "@metadata"
        ], 
        "delete": true
    }
}