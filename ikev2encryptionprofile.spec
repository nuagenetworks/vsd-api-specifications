{
    "attributes": {
        "IPSECAuthenticationAlgorithm": {
            "allowed_choices": [
                "HMAC_SHA1", 
                "HMAC_SHA256", 
                "HMAC_SHA512"
            ], 
            "default_value": "HMAC_SHA256", 
            "description": null, 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "enum"
        }, 
        "IPSECDontFragment": {
            "default_value": "false", 
            "description": null, 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "boolean"
        }, 
        "IPSECEnablePFS": {
            "default_value": "false", 
            "description": null, 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "boolean"
        }, 
        "IPSECEncryptionAlgorithm": {
            "allowed_choices": [
                "TRIPLE_DES", 
                "AES128", 
                "AES192", 
                "AES256"
            ], 
            "default_value": "AES256", 
            "description": null, 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "enum"
        }, 
        "IPSECPreFragment": {
            "default_value": "false", 
            "description": null, 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "boolean"
        }, 
        "IPSECSALifetime": {
            "default_value": "3600", 
            "description": null, 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "integer"
        }, 
        "IPSECSAReplayWindowSize": {
            "default_value": "3600", 
            "description": null, 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "integer"
        }, 
        "ISAKMPAuthenticationMode": {
            "allowed_choices": [
                "PRE_SHARED_KEY", 
                "RSA_SIGNATURE"
            ], 
            "default_value": "PRE_SHARED_KEY", 
            "description": null, 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "enum"
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
            "type": "enum"
        }, 
        "ISAKMPEncryptionAlgorithm": {
            "allowed_choices": [
                "AES256", 
                "AES192", 
                "AES128", 
                "TRIPLE_DES"
            ], 
            "default_value": "AES256", 
            "description": null, 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "enum"
        }, 
        "ISAKMPEncryptionKeyLifetime": {
            "default_value": "1200", 
            "description": null, 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "integer"
        }, 
        "ISAKMPHashAlgorithm": {
            "allowed_choices": [
                "SHA256", 
                "SHA1", 
                "MD5"
            ], 
            "default_value": "SHA256", 
            "description": null, 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "enum"
        }, 
        "ISAKMPKeepAliveInterval": {
            "description": null, 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string"
        }, 
        "ISAKMPKeepAliveMode": {
            "description": null, 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string"
        }, 
        "ISAKMPKeepAliveRetryInterval": {
            "description": null, 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string"
        }, 
        "associatedEnterpriseID": {
            "description": null, 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string"
        }, 
        "description": {
            "description": null, 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string"
        }, 
        "name": {
            "description": null, 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string"
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