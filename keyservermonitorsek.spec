{
    "attributes": {
        "creationTime": {
            "description": "The time this entry was created (milliseconds since epoch)", 
            "exposed": true, 
            "type": "float", 
            "uniqueScope": "no"
        }, 
        "lifetime": {
            "description": "The lifetime of this entry (seconds)", 
            "exposed": true, 
            "type": "integer", 
            "uniqueScope": "no"
        }, 
        "seedPayloadAuthenticationAlgorithm": {
            "allowed_choices": [
                "HMAC_SHA512", 
                "HMAC_SHA1", 
                "HMAC_SHA256"
            ], 
            "description": "SEK Payload Signature Algorithm Possible values are HMAC_SHA1, HMAC_SHA256, HMAC_SHA512, .", 
            "exposed": true, 
            "type": "enum", 
            "uniqueScope": "no"
        }, 
        "seedPayloadEncryptionAlgorithm": {
            "allowed_choices": [
                "AES_128_CBC", 
                "AES_256_CBC", 
                "TRIPLE_DES_CBC"
            ], 
            "description": "SEK Payload Encryption Algorithm Possible values are AES_128_CBC, AES_256_CBC, TRIPLE_DES_CBC, .", 
            "exposed": true, 
            "type": "enum", 
            "uniqueScope": "no"
        }, 
        "startTime": {
            "description": "The time this entry  was activated (milliseconds since epoch)", 
            "exposed": true, 
            "type": "float", 
            "uniqueScope": "no"
        }
    }, 
    "children": {
        "keyservermonitorencryptedseed": {
            "get": true, 
            "relationship": "child"
        }, 
        "keyservermonitorencryptedsek": {
            "get": true, 
            "relationship": "child"
        }
    }, 
    "delete": true, 
    "description": "Represents a Keyserver Monitor SEK Snapshot", 
    "entity_name": "KeyServerMonitorSEK", 
    "extends": [
        "@base", 
        "@metadata"
    ], 
    "get": true, 
    "package": "/keyserver", 
    "resource_name": "keyservermonitorseks", 
    "rest_name": "keyservermonitorsek", 
    "update": true
}