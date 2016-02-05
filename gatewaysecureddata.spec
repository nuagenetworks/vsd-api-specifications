{
  "attributes" : {
    "data" : {
      "type" : "string",
      "format" : "free",
      "description" : "encrypted data",
      "exposed" : true,
      "uniqueScope" : "no"
    },
    "gatewayCertSerialNumber" : {
      "type" : "string",
      "format" : "free",
      "description" : "Serial Number of the certificate of the public key that encrypted this data",
      "filterable" : true,
      "orderable" : true,
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
    "signedData" : {
      "type" : "string",
      "format" : "free",
      "description" : "private key signed data",
      "exposed" : true,
      "uniqueScope" : "no"
    }
  },
  "children" : { },
  "model" : {
    "description" : "This object represents the secured data object under the gateway",
    "entity_name" : "GatewaySecuredData",
    "extends" : [ "@audited", "@base", "@metadata" ],
    "package" : "ipsec",
    "resource_name" : "gatewaysecureddatas",
    "rest_name" : "gatewaysecureddata",
    "get" : true,
    "delete" : true
  }
}