{
  "attributes" : {
    "authenticationMethod" : {
      "type" : "enum",
      "allowed_choices" : [ "RSA_SIGNATURE", "RSA_NONCE", "PRE_SHARED_KEY" ],
      "description" : "IKEv2 Authentication Method.",
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
    "diffieHelmanGroupIdentifier" : {
      "type" : "enum",
      "allowed_choices" : [ "GROUP_1_768_BIT_DH", "GROUP_2_1024_BIT_DH", "GROUP_5_1024_BIT_DH", "GROUP_14_2048_BIT_DH", "GROUP_15_3072_BIT_DH", "GROUP_16_4096_BIT_DH", "GROUP_19_256_BIT_ECDH", "GROUP_20_384_BIT_ECDH", "GROUP_24_2048_BIT_ECDH" ],
      "description" : "IKEv2 Diffie-Helman Group Identifier.",
      "exposed" : true,
      "uniqueScope" : "no"
    },
    "encryptionAlgorithm" : {
      "type" : "enum",
      "allowed_choices" : [ "DES", "TDES", "AES128", "AES192", "AES256" ],
      "description" : "IKEv2 Encryption Algorithm.",
      "exposed" : true,
      "uniqueScope" : "no"
    },
    "encryptionKeyLifetime" : {
      "type" : "integer",
      "description" : "IKEv2 Encryption Key Lifetime in Seconds. Min=60, Max=86400",
      "min_value" : 60,
      "max_value" : 86400,
      "exposed" : true,
      "uniqueScope" : "no"
    },
    "hashAlgorithm" : {
      "type" : "enum",
      "allowed_choices" : [ "MD5", "SHA1", "SHA256" ],
      "description" : "IKEv2 Hash Algorithm.",
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
    "securityAssociationLifetime" : {
      "type" : "integer",
      "description" : "IKE Security Association Lifetime in Seconds. Min=60, Max=86400",
      "min_value" : 60,
      "max_value" : 86400,
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