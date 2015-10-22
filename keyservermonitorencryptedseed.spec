{
    "attributes": {
        "SEKCreationTime": {
            "description": "SEK Creation Time", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "float"
        }, 
        "enterpriseSecuredDataID": {
            "description": "Enterprise Secured ID record this monitor represents", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "associatedKeyServerMonitorSeedID": {
            "description": "The ID of the associated KeyServer Monitor Seed ID", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
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
        "associatedKeyServerMonitorSeedCreationTime": {
            "description": "The ID of the associated KeyServer Monitor Seed ID", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "float"
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
        "resource_name": "keyservermonitorencryptedseeds", 
        "description": "Represents a Keyserver Monitor Encrypted Seed Snapshot", 
        "entity_name": "KeyServerMonitorEncryptedSeed", 
        "package": "keyserver", 
        "get": true, 
        "update": true, 
        "rest_name": "keyservermonitorencryptedseed", 
        "extends": [
            "@base", 
            "@metadata"
        ], 
        "delete": true
    }
}