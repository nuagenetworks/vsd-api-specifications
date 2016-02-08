{
  "attributes" : {
    "associatedEnterpriseID" : {
      "type" : "string",
      "format" : "free",
      "description" : "The ID of the associated Enterprise",
      "exposed" : true,
      "uniqueScope" : "no"
    },
    "autoCreated" : {
      "type" : "boolean",
      "description" : "Was this object autocreated from the connection",
      "filterable" : true,
      "orderable" : true,
      "exposed" : true,
      "uniqueScope" : "no"
    },
    "description" : {
      "type" : "string",
      "format" : "free",
      "description" : "Description of the IKEv2 Authentication",
      "filterable" : true,
      "orderable" : true,
      "exposed" : true,
      "uniqueScope" : "no"
    },
    "encryptedPSK" : {
      "type" : "string",
      "format" : "free",
      "description" : "Base64 Encoded Encrypted PSK",
      "filterable" : true,
      "orderable" : true,
      "exposed" : true,
      "uniqueScope" : "no"
    },
    "encryptingCertificateSerialNumber" : {
      "type" : "integer",
      "subtype" : "long",
      "description" : "Serial Number of the certificate of the public key that encrypted this data",
      "filterable" : true,
      "orderable" : true,
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
    "signature" : {
      "type" : "string",
      "format" : "free",
      "description" : "Base64 Encoded private key signature",
      "filterable" : true,
      "orderable" : true,
      "exposed" : true,
      "uniqueScope" : "no"
    },
    "signingCertificateSerialNumber" : {
      "type" : "integer",
      "subtype" : "long",
      "description" : "Serial Number of the certificate needed to verify the encrypted data",
      "filterable" : true,
      "orderable" : true,
      "exposed" : true,
      "uniqueScope" : "no"
    },
    "unencryptedPSK" : {
      "type" : "string",
      "format" : "free",
      "description" : "Unencrypted PSK",
      "exposed" : true,
      "uniqueScope" : "no"
    }
  },
  "children" : { },
  "model" : {
    "description" : "Represents an IKEv2 Pre Shared Key",
    "entity_name" : "IKEv2PSK",
    "extends" : [ "@audited", "@base", "@metadata" ],
    "package" : "ikev2",
    "resource_name" : "ikev2psks",
    "rest_name" : "ikev2psk",
    "get" : true,
    "delete" : true,
    "update" : true
  }
}