{
    "attributes": {
        "seedTrafficEncryptionAlgorithm": {
            "description": "Seed traffic Encryption Algorithm. Possible values are AES_128_CBC, AES_192_CBC, AES_256_CBC, TRIPLE_DES_CBC, .", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "allowed_choices": [
                "AES_128_CBC", 
                "AES_256_CBC", 
                "AES_192_CBC", 
                "TRIPLE_DES_CBC"
            ], 
            "orderable": true, 
            "type": "enum"
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
        "startTime": {
            "description": "The time this entry  was activated (milliseconds since epoch)", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "float"
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
        "seedTrafficEncryptionKeyLifetime": {
            "description": "Seed Traffic Encryption Key Lifetime in Seconds", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "integer"
        }, 
        "seedTrafficAuthenticationAlgorithm": {
            "description": "Seed traffic Authentication Algorithm. Possible values are HMAC_SHA1, HMAC_SHA256, HMAC_SHA384, HMAC_SHA512, HMAC_MD5, .", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "allowed_choices": [
                "HMAC_SHA384", 
                "HMAC_SHA512", 
                "HMAC_SHA1", 
                "HMAC_MD5", 
                "HMAC_SHA256"
            ], 
            "orderable": true, 
            "type": "enum"
        }
    }, 
    "model": {
        "resource_name": "keyservermonitorseeds", 
        "description": "Represents a Keyserver Monitor Seed Snapshot", 
        "entity_name": "KeyServerMonitorSeed", 
        "package": "keyserver", 
        "get": true, 
        "update": true, 
        "rest_name": "keyservermonitorseed", 
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
        }
    }
}