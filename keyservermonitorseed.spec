{
    "attributes": {
        "creationTime": {
            "description": "The time this entry was created (milliseconds since epoch)", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "float", 
            "uniqueScope": "no"
        }, 
        "lifetime": {
            "description": "The lifetime of this entry (seconds)", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "integer", 
            "uniqueScope": "no"
        }, 
        "seedTrafficAuthenticationAlgorithm": {
            "allowed_choices": [
                "HMAC_SHA384", 
                "HMAC_SHA512", 
                "HMAC_SHA1", 
                "HMAC_MD5", 
                "HMAC_SHA256"
            ], 
            "description": "Seed traffic Authentication Algorithm. Possible values are HMAC_SHA1, HMAC_SHA256, HMAC_SHA384, HMAC_SHA512, HMAC_MD5, .", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "enum", 
            "uniqueScope": "no"
        }, 
        "seedTrafficEncryptionAlgorithm": {
            "allowed_choices": [
                "AES_128_CBC", 
                "AES_256_CBC", 
                "AES_192_CBC", 
                "TRIPLE_DES_CBC"
            ], 
            "description": "Seed traffic Encryption Algorithm. Possible values are AES_128_CBC, AES_192_CBC, AES_256_CBC, TRIPLE_DES_CBC, .", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "enum", 
            "uniqueScope": "no"
        }, 
        "seedTrafficEncryptionKeyLifetime": {
            "description": "Seed Traffic Encryption Key Lifetime in Seconds", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "integer", 
            "uniqueScope": "no"
        }, 
        "startTime": {
            "description": "The time this entry  was activated (milliseconds since epoch)", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "float", 
            "uniqueScope": "no"
        }
    }, 
    "children": {
        "keyservermonitorencryptedseed": {
            "get": true, 
            "relationship": "child"
        }
    }, 
    "model": {
        "delete": true, 
        "description": "Represents a Keyserver Monitor Seed Snapshot", 
        "entity_name": "KeyServerMonitorSeed", 
        "extends": [
            "@base", 
            "@metadata"
        ], 
        "get": true, 
        "package": "keyserver", 
        "resource_name": "keyservermonitorseeds", 
        "rest_name": "keyservermonitorseed", 
        "update": true
    }
}