{
    "attributes": {
        "associatedWANServiceID": {
            "description": "Assosciated WAN Service", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "description": {
            "description": "A description of the VPNConnect", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "name": {
            "description": "Name of the VPNConnect", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "required": true, 
            "type": "string", 
            "uniqueScope": "no"
        }
    }, 
    "delete": true, 
    "description": "This is the definition of a VPN Connect which holds the PE service assocaition with a DOMAIN", 
    "entity_name": "VPNConnection", 
    "extends": [
        "@base", 
        "@metadata"
    ], 
    "get": true, 
    "package": "network", 
    "resource_name": "vpnconnections", 
    "rest_name": "vpnconnection", 
    "update": true
}