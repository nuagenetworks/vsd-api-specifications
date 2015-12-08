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
            "description": null, 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "boolean"
        }, 
        "IPSECEncryptionAlgorithm": {
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
            "type": "enum"
        }, 
        "IPSECPreFragment": {
            "description": null, 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "boolean"
        }, 
        "IPSECSALifetime": {
            "description": null, 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "integer"
        }, 
        "IPSECSAReplayWindowSize": {
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
            "description": null, 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string"
        }, 
        "ISAKMPEncryptionAlgorithm": {
            "description": null, 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string"
        }, 
        "ISAKMPEncryptionKeyLifetime": {
            "description": null, 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string"
        }, 
        "ISAKMPHashAlgorithm": {
            "description": null, 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string"
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