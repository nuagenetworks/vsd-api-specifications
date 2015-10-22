{
    "attributes": {
        "seedPayloadSigningAlgorithm": {
            "description": "Group Key Seed Payload Signature Algorithm. Possible values are SHA1withRSA, SHA224withRSA, SHA256withRSA, SHA384withRSA, SHA512withRSA, .", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "allowed_choices": [
                "SHA256withRSA", 
                "SHA1withRSA", 
                "SHA384withRSA", 
                "SHA224withRSA", 
                "SHA512withRSA"
            ], 
            "orderable": true, 
            "type": "enum"
        }, 
        "trafficAuthenticationAlgorithm": {
            "description": "Group Key traffic Authentication Algorithm. Possible values are HMAC_SHA1, HMAC_SHA256, HMAC_SHA384, HMAC_SHA512, HMAC_MD5, .", 
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
        }, 
        "trafficEncryptionAlgorithm": {
            "description": "Group Key traffic Encryption Algorithm. Possible values are AES_128_CBC, AES_192_CBC, AES_256_CBC, TRIPLE_DES_CBC, .", 
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
        "SEKPayloadEncryptionKeyLength": {
            "description": "Group Key Sek Payload Encryption Key Length (read only)", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "integer"
        }, 
        "description": {
            "description": "A description of the Profile instance created.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "name": {
            "description": "Name of the Encryption Profile", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "SEKLifetime": {
            "description": "Group Key SEK Lifetime in Seconds. Min=1, Max=86400", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "integer"
        }, 
        "seedLifetime": {
            "description": "Group Key SEED Lifetime in Seconds. Min=1, Max=86400", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "integer"
        }, 
        "seedPayloadEncryptionAlgorithm": {
            "description": "Group Key SEED Payload Encryption Algorithm. Possible values are AES_128_CBC, AES_256_CBC, TRIPLE_DES_CBC, .", 
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
        "SEKPayloadEncryptionBCAlgorithm": {
            "description": "Group Key Sek Payload Encryption BC Algorithm (read only)", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "seedPayloadAuthenticationAlgorithm": {
            "description": "Group Key SEK Payload Signature Algorithm. Possible values are HMAC_SHA1, HMAC_SHA256, HMAC_SHA512, .", 
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
        "trafficEncryptionKeyLifetime": {
            "description": "Group Key Traffic Encryption Key Lifetime in Seconds. Min=1, Max=86400", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "integer"
        }, 
        "SEKPayloadEncryptionAlgorithm": {
            "description": "Group Key SEK Payload Encryption Algorithm. Possible values are RSA_1024, .", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "allowed_choices": [
                "RSA_1024"
            ], 
            "orderable": true, 
            "type": "enum"
        }, 
        "SEKPayloadSigningAlgorithm": {
            "description": "Group Key SEK Payload Signature Algorithm. Possible values are SHA1withRSA, SHA224withRSA, SHA256withRSA, SHA384withRSA, SHA512withRSA, .", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "allowed_choices": [
                "SHA256withRSA", 
                "SHA1withRSA", 
                "SHA384withRSA", 
                "SHA224withRSA", 
                "SHA512withRSA"
            ], 
            "orderable": true, 
            "type": "enum"
        }, 
        "seedPayloadEncryptionBCAlgorithm": {
            "description": "Group Key Seed Payload Encryption Algorithm (read only)", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "seedGenerationInterval": {
            "description": "Group Key SEED Generation Interval in Seconds. Min=1, Max=86400", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "integer"
        }, 
        "seedPayloadEncryptionKeyLength": {
            "description": "Group Key Seed Payload Encryption Key Length (read only)", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "integer"
        }, 
        "seedPayloadAuthenticationBCAlgorithm": {
            "description": "Group Key Seed Payload Authentication Algorithm (read only)", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "seedPayloadAuthenticationKeyLength": {
            "description": "Group Key Seed Payload Authentication Key Length  (read only)", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "integer"
        }, 
        "SEKGenerationInterval": {
            "description": "Group Key SEK Generation Interval in Seconds. Min=1, Max=86400", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "integer"
        }
    }, 
    "model": {
        "resource_name": "groupkeyencryptionprofiles", 
        "description": "Represents a Group Key Profile", 
        "entity_name": "GroupKeyEncryptionProfile", 
        "package": "keyserver", 
        "get": true, 
        "update": true, 
        "rest_name": "groupkeyencryptionprofile", 
        "extends": [
            "@base", 
            "@metadata"
        ]
    }
}