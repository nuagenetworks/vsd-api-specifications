{
  "attributes" : {
    "data" : {
      "type" : "string",
      "format" : "free",
      "description" : "encrypted data",
      "exposed" : true,
      "uniqueScope" : "no"
    },
    "hash" : {
      "type" : "string",
      "format" : "free",
      "description" : "authentication hash",
      "exposed" : true,
      "uniqueScope" : "no"
    },
    "keyserverCertSerialNumber" : {
      "type" : "string",
      "format" : "free",
      "description" : "Serial Number of the certificate needed to verify the encrypted data",
      "filterable" : true,
      "orderable" : true,
      "exposed" : true,
      "uniqueScope" : "no"
    },
    "sekId" : {
      "type" : "integer",
      "subtype" : "long",
      "description" : "Seed Encryption Key id that encrypted this data",
      "filterable" : true,
      "orderable" : true,
      "exposed" : true,
      "uniqueScope" : "no"
    },
    "signedHash" : {
      "type" : "string",
      "format" : "free",
      "description" : "private key signed hash",
      "exposed" : true,
      "uniqueScope" : "no"
    }
  },
  "children" : { },
  "model" : {
    "description" : "This object represents the secured data object under the enterprise",
    "entity_name" : "EnterpriseSecuredData",
    "extends" : [ "@audited", "@base", "@metadata" ],
    "package" : "ipsec",
    "resource_name" : "enterprisesecureddatas",
    "rest_name" : "enterprisesecureddata",
    "get" : true,
    "delete" : true
  }
}