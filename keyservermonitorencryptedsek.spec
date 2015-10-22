{
    "attributes": {
        "NSGCertificateSerialNumber": {
            "description": "NSG Certificate Serial Number", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "float"
        }, 
        "keyServerCertificateSerialNumber": {
            "description": "KeyServer Certificate Serial Number", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "float"
        }, 
        "gatewaySecuredDataID": {
            "description": "Gateway Secured ID record this monitor represents", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "associatedKeyServerMonitorSEKCreationTime": {
            "description": "The ID of the associated KeyServer Monitor Seed ID", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "float"
        }, 
        "associatedKeyServerMonitorSEKID": {
            "description": "The ID of the associated KeyServer Monitor SEK ID", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }
    }, 
    "model": {
        "resource_name": "keyservermonitorencryptedseks", 
        "description": "Represents a Keyserver Monitor Encrypted Seed Snapshot", 
        "entity_name": "KeyServerMonitorEncryptedSEK", 
        "package": "keyserver", 
        "get": true, 
        "rest_name": "keyservermonitorencryptedsek", 
        "extends": [
            "@base", 
            "@metadata"
        ], 
        "delete": true
    }
}