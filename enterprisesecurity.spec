{
  "attributes" : {
    "enterpriseID" : {
      "type" : "string",
      "format" : "free",
      "description" : "The enterprise associated with this object. This is a read only attribute",
      "exposed" : true,
      "uniqueScope" : "no"
    },
    "gatewaySecurityRevision" : {
      "type" : "integer",
      "subtype" : "long",
      "description" : "change revision number for the gateway security data",
      "exposed" : true,
      "uniqueScope" : "no"
    },
    "revision" : {
      "type" : "integer",
      "subtype" : "long",
      "description" : "revision number for the enterprise security data",
      "exposed" : true,
      "uniqueScope" : "no"
    }
  },
  "children" : {
    "enterprisesecureddata" : {
      "get" : true,
      "create" : true,
      "relationship" : "child"
    }
  },
  "model" : {
    "description" : "This object represents the enterprise security",
    "entity_name" : "EnterpriseSecurity",
    "extends" : [ "@audited", "@base", "@metadata" ],
    "package" : "ipsec",
    "resource_name" : "enterprisesecurities",
    "rest_name" : "enterprisesecurity",
    "get" : true,
    "update" : true
  }
}