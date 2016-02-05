{
  "attributes" : {
    "address" : {
      "type" : "string",
      "format" : "free",
      "description" : "IKEv2 Third Party Gateway IP Address or FQDN.",
      "exposed" : true,
      "uniqueScope" : "no"
    },
    "associatedIKEv2EncryptionProfileID" : {
      "type" : "string",
      "format" : "free",
      "description" : "The ID of the associated IKEv2 Encryption Profile",
      "exposed" : true,
      "uniqueScope" : "no"
    },
    "associatedNSGatewayID" : {
      "type" : "string",
      "format" : "free",
      "description" : "The ID of the NSGateway associated with this object. This is a read only attribute",
      "exposed" : true,
      "uniqueScope" : "no"
    },
    "preSharedKey" : {
      "type" : "string",
      "format" : "free",
      "description" : "IKE preSharedKey. Min=5 chars, Max=255 chars",
      "min_length" : 5,
      "max_length" : 255,
      "exposed" : true,
      "uniqueScope" : "no"
    }
  },
  "children" : { },
  "model" : {
    "description" : "Represents an IKEv2 Gateway",
    "entity_name" : "IKEv2Gateway",
    "extends" : [ "@audited", "@base", "@metadata" ],
    "package" : "keyserver",
    "resource_name" : "ikev2gateways",
    "rest_name" : "ikev2gateway",
    "get" : true,
    "update" : true,
    "delete" : true
  }
}