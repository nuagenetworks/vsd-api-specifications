{
    "attributes": {
        "IPSECAuthenticationAlgorithm": {
            "allowed_choices": [
                "HMAC_SHA1", 
                "HMAC_SHA256", 
                "HMAC_SHA512"
            ], 
            "description": null, 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "enum", 
            "uniqueScope": "no"
        }, 
        "IPSECDontFragment": {
            "description": null, 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "boolean", 
            "uniqueScope": "no"
        }, 
        "IPSECEnablePFS": {
            "description": null, 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "boolean", 
            "uniqueScope": "no"
        }, 
        "IPSECEncryptionAlgorithm": {
            "allowed_choices": [
                "TRIPLE_DES", 
                "AES128", 
                "AES192", 
                "AES256"
            ], 
            "description": null, 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "enum", 
            "uniqueScope": "no"
        }, 
        "IPSECPreFragment": {
            "description": null, 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "boolean", 
            "uniqueScope": "no"
        }, 
        "IPSECSALifetime": {
            "description": null, 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "integer", 
            "uniqueScope": "no"
        }, 
        "IPSECSAReplayWindowSize": {
            "description": null, 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "integer", 
            "uniqueScope": "no"
        }, 
        "ISAKMPAuthenticationMode": {
            "allowed_choices": [
                "PRE_SHARED_KEY", 
                "RSA_SIGNATURE"
            ], 
            "description": null, 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "enum", 
            "uniqueScope": "no"
        }, 
        "ISAKMPDiffieHelmanGroupIdentifier": {
            "allowed_choices": [
                "GROUP_24_2048_BIT_ECDH", 
                "GROUP_20_384_BIT_ECDH", 
                "GROUP_19_256_BIT_ECDH", 
                "GROUP_16_4096_BIT_DH", 
                "GROUP_15_3072_BIT_DH", 
                "GROUP_14_2048_BIT_DH", 
                "GROUP_5_1024_BIT_DH", 
                "GROUP_2_1024_BIT_DH", 
                "GROUP_1_768_BIT_DH"
            ], 
            "description": null, 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "enum", 
            "uniqueScope": "no"
        }, 
        "ISAKMPEncryptionAlgorithm": {
            "allowed_choices": [
                "AES256", 
                "AES192", 
                "AES128", 
                "TRIPLE_DES"
            ], 
            "description": null, 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "enum", 
            "uniqueScope": "no"
        }, 
        "ISAKMPEncryptionKeyLifetime": {
            "description": null, 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "integer", 
            "uniqueScope": "no"
        }, 
        "ISAKMPHashAlgorithm": {
            "allowed_choices": [
                "SHA256", 
                "SHA1", 
                "MD5"
            ], 
            "description": null, 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "enum", 
            "uniqueScope": "no"
        }, 
        "ISAKMPKeepAliveInterval": {
            "description": null, 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "integer", 
            "uniqueScope": "no"
        }, 
        "ISAKMPKeepAliveMode": {
            "allowed_choices": [
                "PERIODIC", 
                "ON_DEMAND"
            ], 
            "description": null, 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "enum", 
            "uniqueScope": "no"
        }, 
        "ISAKMPKeepAliveRetryInterval": {
            "description": null, 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "integer", 
            "uniqueScope": "no"
        }, 
        "ISAKMPKeepAliveTimeout": {
            "default_value": "150", 
            "description": null, 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "integer"
        }, 
        "associatedEnterpriseID": {
            "description": null, 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "description": {
            "description": null, 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "name": {
            "description": null, 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }
    }, 
    "model": {
        "delete": true, 
        "entity_name": "IKEv2EncryptionProfile", 
        "extends": [
            "@base", 
            "@metadata"
        ], 
        "get": true, 
        "resource_name": "ikev2encryptionprofiles", 
        "rest_name": "ikev2encryptionprofile", 
        "update": true
    }
}