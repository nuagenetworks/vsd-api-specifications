{
    "attributes" : {
        "DPDInterval" : {
          "type" : "integer",
          "description" : "ISAKMP Keep Alive Interval.",
          "exposed" : true,
          "uniqueScope" : "no"
        },
        "DPDMode" : {
          "type" : "enum",
          "allowed_choices" : [ "ON_DEMAND", "PERIODIC", "REPLY_ONLY" ],
          "description" : "DPD Mode.",
          "default_value" : "REPLY_ONLY",
          "exposed" : true,
          "uniqueScope" : "no"
        },
        "DPDRetryInterval" : {
          "type" : "integer",
          "description" : "DPD Retry Interval.",
          "exposed" : true,
          "uniqueScope" : "no"
        },
        "DPDTimeout" : {
          "type" : "integer",
          "description" : "DPD Timeout.",
          "exposed" : true,
          "uniqueScope" : "no"
        },
        "IPSecAuthenticationAlgorithm" : {
          "type" : "enum",
          "allowed_choices" : [ "HMAC_SHA1", "HMAC_SHA256", "HMAC_SHA512" ],
          "description" : "IPSec Authentication Algorithm.",
          "default_value" : "HMAC_SHA256",
          "exposed" : true,
          "uniqueScope" : "no"
        },
        "IPSecDontFragment" : {
          "type" : "boolean",
          "description" : "IPSec Don't Fragment",
          "exposed" : true,
          "uniqueScope" : "no"
        },
        "IPSecEnablePFS" : {
          "type" : "boolean",
          "description" : "IPSec Enable PFS",
          "exposed" : true,
          "uniqueScope" : "no"
        },
        "IPSecEncryptionAlgorithm" : {
          "type" : "enum",
          "allowed_choices" : [ "TRIPLE_DES", "AES128", "AES192", "AES256" ],
          "description" : "IPSec Encryption Algorithm.",
          "default_value" : "AES256",
          "exposed" : true,
          "uniqueScope" : "no"
        },
        "IPSecPreFragment" : {
          "type" : "boolean",
          "description" : "IPSec PreFragment",
          "exposed" : true,
          "uniqueScope" : "no"
        },
        "IPSecSALifetime" : {
          "type" : "integer",
          "description" : "IPSec SA Lifetime in Seconds.",
          "default_value" : 3600,
          "exposed" : true,
          "uniqueScope" : "no"
        },
        "IPSecSAReplayWindowSize" : {
          "type" : "enum",
          "allowed_choices" : [ "WINDOW_SIZE_0", "WINDOW_SIZE_32", "WINDOW_SIZE_64", "WINDOW_SIZE_128", "WINDOW_SIZE_256", "WINDOW_SIZE_512", "WINDOW_SIZE_1024" ],
          "description" : "IPSec Replay Window Size in Packets.",
          "default_value" : "WINDOW_SIZE_32",
          "exposed" : true,
          "uniqueScope" : "no"
        },
        "ISAKMPAuthenticationMode" : {
          "type" : "enum",
          "allowed_choices" : [ "RSA_SIGNATURE", "PRE_SHARED_KEY" ],
          "description" : "ISAKMP Authentication Algorithm.",
          "default_value" : "PRE_SHARED_KEY",
          "exposed" : true,
          "uniqueScope" : "no"
        },
        "ISAKMPDiffieHelmanGroupIdentifier" : {
          "type" : "enum",
          "allowed_choices" : [ "GROUP_1_768_BIT_DH", "GROUP_2_1024_BIT_DH", "GROUP_5_1536_BIT_DH", "GROUP_14_2048_BIT_DH", "GROUP_15_3072_BIT_DH", "GROUP_16_4096_BIT_DH", "GROUP_19_256_BIT_ECDH", "GROUP_20_384_BIT_ECDH", "GROUP_24_2048_BIT_ECDH" ],
          "description" : "ISAKMP Diffie-Helman Group Identifier.",
          "default_value" : "GROUP_5_1536_BIT_DH",
          "exposed" : true,
          "uniqueScope" : "no"
        },
        "ISAKMPEncryptionAlgorithm" : {
          "type" : "enum",
          "allowed_choices" : [ "TRIPLE_DES", "AES128", "AES192", "AES256" ],
          "description" : "ISAKMP Encryption Algorithm.",
          "default_value" : "AES256",
          "exposed" : true,
          "uniqueScope" : "no"
        },
        "ISAKMPEncryptionKeyLifetime" : {
          "type" : "integer",
          "description" : "ISAKMP Encryption Key Lifetime in Seconds",
          "default_value" : 1200,
          "exposed" : true,
          "uniqueScope" : "no"
        },
        "ISAKMPHashAlgorithm" : {
          "type" : "enum",
          "allowed_choices" : [ "MD5", "SHA1", "SHA256" ],
          "description" : "ISAKMP Hash Algorithm.",
          "default_value" : "SHA256",
          "exposed" : true,
          "uniqueScope" : "no"
        },
        "associatedEnterpriseID" : {
          "type" : "string",
          "format" : "free",
          "description" : "The ID of the associated Enterprise",
          "exposed" : true,
          "uniqueScope" : "no"
        },
        "description" : {
          "type" : "string",
          "format" : "free",
          "description" : "A description of the Profile instance created.",
          "filterable" : true,
          "orderable" : true,
          "min_length" : 0,
          "max_length" : 255,
          "exposed" : true,
          "uniqueScope" : "no"
        },
        "name" : {
          "type" : "string",
          "format" : "free",
          "description" : "Name of the Encryption Profile",
          "filterable" : true,
          "orderable" : true,
          "min_length" : 1,
          "max_length" : 255,
          "exposed" : true,
          "uniqueScope" : "no"
        },
        "sequence": {
            "type" : "integer",
            "subtype" : "long",
            "description" : "",
            "exposed" : true,
            "uniqueScope" : "no"
        }
    },
    "children" : { },
    "model" : {
        "description" : "Represents an IKEv2 Profile",
        "entity_name" : "IKEv2EncryptionProfile",
        "extends" : [ "@audited", "@base", "@metadata" ],
        "package" : "keyserver",
        "resource_name" : "ikev2encryptionprofiles",
        "rest_name" : "ikev2encryptionprofile",
        "get" : true,
        "update" : true,
        "delete" : true
    }
}