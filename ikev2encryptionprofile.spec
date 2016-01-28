{
    "attributes": {
        "DPDInterval": {
            "description": null,
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "integer",
            "uniqueScope": "no"
        },
        "DPDMode": {
            "allowed_choices": [
                "PERIODIC",
                "ON_DEMAND",
                "REPLY_ONLY"
            ],
            "description": null,
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "enum",
            "uniqueScope": "no"
        },
        "DPDRetryInterval": {
            "allowed_choices": [
                "WINDOW_SIZE_0",
                "WINDOW_SIZE_32",
                "WINDOW_SIZE_64",
                "WINDOW_SIZE_128",
                "WINDOW_SIZE_256",
                "WINDOW_SIZE_512",
                "WINDOW_SIZE_1024"
            ],
            "description": null,
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "enum",
            "uniqueScope": "no"
        },
        "DPDTimeout": {
            "description": null,
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "integer",
            "uniqueScope": "no"
        },
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
                "GROUP_1_768_BIT_DH",
                "GROUP_2_1024_BIT_DH",
                "GROUP_5_1536_BIT_DH",
                "GROUP_14_2048_BIT_DH",
                "GROUP_15_3072_BIT_DH",
                "GROUP_16_4096_BIT_DH",
                "GROUP_19_256_BIT_ECDH",
                "GROUP_20_384_BIT_ECDH",
                "GROUP_24_2048_BIT_ECDH"
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