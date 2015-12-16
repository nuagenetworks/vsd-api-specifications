{
    "attributes": {
        "SEKGenerationInterval": {
            "description": "Group Key SEK Generation Interval in Seconds. Min=1, Max=86400", 
            "exposed": true, 
            "filterable": true, 
            "orderable": true, 
            "type": "integer",
            "min_value": 15,
            "max_value": 86400,
            "default_value": 1200, 
            "uniqueScope": "no"
        }, 
        "SEKLifetime": {
            "description": "Group Key SEK Lifetime in Seconds. Min=1, Max=86400", 
            "exposed": true, 
            "filterable": true, 
            "orderable": true, 
            "type": "integer",
            "min_value": 60,
            "max_value": 86400,
            "default_value": 86400, 
            "uniqueScope": "no"
        }, 
        "SEKPayloadEncryptionAlgorithm": {
            "allowed_choices": [
                "RSA_1024"
            ], 
            "description": "Group Key SEK Payload Encryption Algorithm. Possible values are RSA_1024, .", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "enum", 
            "uniqueScope": "no"
        }, 
        "SEKPayloadEncryptionBCAlgorithm": {
            "description": "Group Key Sek Payload Encryption BC Algorithm (read only)", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "SEKPayloadEncryptionKeyLength": {
            "description": "Group Key Sek Payload Encryption Key Length (read only)", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "integer", 
            "uniqueScope": "no"
        }, 
        "SEKPayloadSigningAlgorithm": {
            "allowed_choices": [
                "SHA256withRSA", 
                "SHA1withRSA", 
                "SHA384withRSA", 
                "SHA224withRSA", 
                "SHA512withRSA"
            ], 
            "description": "Group Key SEK Payload Signature Algorithm. Possible values are SHA1withRSA, SHA224withRSA, SHA256withRSA, SHA384withRSA, SHA512withRSA, .", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "enum", 
            "uniqueScope": "no"
        }, 
        "description": {
            "description": "A description of the Profile instance created.", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "name": {
            "description": "Name of the Encryption Profile", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "seedGenerationInterval": {
            "description": "Group Key SEED Generation Interval in Seconds. Min=1, Max=86400", 
            "exposed": true, 
            "filterable": true, 
            "orderable": true, 
            "type": "integer",
            "min_value": 15,
            "max_value": 86400,
            "default_value": 1200, 
            "uniqueScope": "no"
        }, 
        "seedLifetime": {
            "description": "Group Key SEED Lifetime in Seconds. Min=1, Max=86400", 
            "exposed": true, 
            "filterable": true, 
            "orderable": true, 
            "type": "integer",
            "min_value": 30,
            "max_value": 86400,
            "default_value": 14400, 
            "uniqueScope": "no"
        }, 
        "seedPayloadAuthenticationAlgorithm": {
            "allowed_choices": [
                "HMAC_SHA512", 
                "HMAC_SHA1", 
                "HMAC_SHA256"
            ], 
            "description": "Group Key SEK Payload Signature Algorithm. Possible values are HMAC_SHA1, HMAC_SHA256, HMAC_SHA512, .", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "enum", 
            "uniqueScope": "no"
        }, 
        "seedPayloadAuthenticationBCAlgorithm": {
            "description": "Group Key Seed Payload Authentication Algorithm (read only)", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "seedPayloadAuthenticationKeyLength": {
            "description": "Group Key Seed Payload Authentication Key Length  (read only)", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "integer", 
            "uniqueScope": "no"
        }, 
        "seedPayloadEncryptionAlgorithm": {
            "allowed_choices": [
                "AES_128_CBC", 
                "AES_256_CBC", 
                "TRIPLE_DES_CBC"
            ], 
            "description": "Group Key SEED Payload Encryption Algorithm. Possible values are AES_128_CBC, AES_256_CBC, TRIPLE_DES_CBC, .", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "enum", 
            "uniqueScope": "no"
        }, 
        "seedPayloadEncryptionBCAlgorithm": {
            "description": "Group Key Seed Payload Encryption Algorithm (read only)", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "seedPayloadEncryptionKeyLength": {
            "description": "Group Key Seed Payload Encryption Key Length (read only)", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "integer", 
            "uniqueScope": "no"
        }, 
        "seedPayloadSigningAlgorithm": {
            "allowed_choices": [
                "SHA256withRSA", 
                "SHA1withRSA", 
                "SHA384withRSA", 
                "SHA224withRSA", 
                "SHA512withRSA"
            ], 
            "description": "Group Key Seed Payload Signature Algorithm. Possible values are SHA1withRSA, SHA224withRSA, SHA256withRSA, SHA384withRSA, SHA512withRSA, .", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "enum", 
            "uniqueScope": "no"
        }, 
        "trafficAuthenticationAlgorithm": {
            "allowed_choices": [
                "HMAC_SHA384", 
                "HMAC_SHA512", 
                "HMAC_SHA1", 
                "HMAC_MD5", 
                "HMAC_SHA256"
            ], 
            "description": "Group Key traffic Authentication Algorithm. Possible values are HMAC_SHA1, HMAC_SHA256, HMAC_SHA384, HMAC_SHA512, HMAC_MD5, .", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "enum", 
            "uniqueScope": "no"
        }, 
        "trafficEncryptionAlgorithm": {
            "allowed_choices": [
                "AES_128_CBC", 
                "AES_256_CBC", 
                "AES_192_CBC", 
                "TRIPLE_DES_CBC"
            ], 
            "description": "Group Key traffic Encryption Algorithm. Possible values are AES_128_CBC, AES_192_CBC, AES_256_CBC, TRIPLE_DES_CBC, .", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "enum", 
            "uniqueScope": "no"
        }, 
        "trafficEncryptionKeyLifetime": {
            "description": "Group Key Traffic Encryption Key Lifetime in Seconds. Min=1, Max=86400", 
            "exposed": true, 
            "filterable": true, 
            "orderable": true, 
            "type": "integer",
            "min_value": 5,
            "max_value": 86400,
            "default_value": 300, 
            "uniqueScope": "no"
        }
    }, 
    "model": {
        "description": "Represents a Group Key Profile", 
        "entity_name": "GroupKeyEncryptionProfile", 
        "extends": [
            "@base", 
            "@metadata"
        ], 
        "get": true, 
        "package": "keyserver", 
        "resource_name": "groupkeyencryptionprofiles", 
        "rest_name": "groupkeyencryptionprofile", 
        "update": true
    }
}
