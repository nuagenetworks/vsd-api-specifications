{
    "attributes": {
        "NSGCertificateSerialNumber": {
            "description": "NSG Certificate Serial Number", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "float", 
            "uniqueScope": "no"
        }, 
        "associatedKeyServerMonitorSEKCreationTime": {
            "description": "The ID of the associated KeyServer Monitor Seed ID", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "float", 
            "uniqueScope": "no"
        }, 
        "associatedKeyServerMonitorSEKID": {
            "description": "The ID of the associated KeyServer Monitor SEK ID", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "gatewaySecuredDataID": {
            "description": "Gateway Secured ID record this monitor represents", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "keyServerCertificateSerialNumber": {
            "description": "KeyServer Certificate Serial Number", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "float", 
            "uniqueScope": "no"
        }
    }, 
    "delete": true, 
    "description": "Represents a Keyserver Monitor Encrypted Seed Snapshot", 
    "entity_name": "KeyServerMonitorEncryptedSEK", 
    "extends": [
        "@base", 
        "@metadata"
    ], 
    "get": true, 
    "package": "keyserver", 
    "resource_name": "keyservermonitorencryptedseks", 
    "rest_name": "keyservermonitorencryptedsek"
}