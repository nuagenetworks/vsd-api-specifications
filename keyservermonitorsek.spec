{
    "attributes": {
        "seedPayloadAuthenticationAlgorithm": {
            "description": "SEK Payload Signature Algorithm Possible values are HMAC_SHA1, HMAC_SHA256, HMAC_SHA512, .", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "allowed_choices": [
                "HMAC_SHA512", 
                "HMAC_SHA1", 
                "HMAC_SHA256"
            ], 
            "orderable": true, 
            "type": "enum"
        }, 
        "lifetime": {
            "description": "The lifetime of this entry (seconds)", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "integer"
        }, 
        "creationTime": {
            "description": "The time this entry was created (milliseconds since epoch)", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "float"
        }, 
        "seedPayloadEncryptionAlgorithm": {
            "description": "SEK Payload Encryption Algorithm Possible values are AES_128_CBC, AES_256_CBC, TRIPLE_DES_CBC, .", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "allowed_choices": [
                "AES_128_CBC", 
                "AES_256_CBC", 
                "TRIPLE_DES_CBC"
            ], 
            "orderable": true, 
            "type": "enum"
        }, 
        "startTime": {
            "description": "The time this entry  was activated (milliseconds since epoch)", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "float"
        }
    }, 
    "model": {
        "resource_name": "keyservermonitorseks", 
        "description": "Represents a Keyserver Monitor SEK Snapshot", 
        "entity_name": "KeyServerMonitorSEK", 
        "package": "keyserver", 
        "get": true, 
        "update": true, 
        "rest_name": "keyservermonitorsek", 
        "extends": [
            "@base", 
            "@metadata"
        ], 
        "delete": true
    }, 
    "children": {
        "keyservermonitorencryptedseed": {
            "relationship": "child", 
            "get": true
        }, 
        "keyservermonitorencryptedsek": {
            "relationship": "child", 
            "get": true
        }
    }
}