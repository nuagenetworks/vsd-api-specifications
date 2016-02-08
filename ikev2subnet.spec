{
  "attributes" : {
    "associatedIKEv2GatewayID" : {
      "type" : "string",
      "format" : "free",
      "description" : "The ID of the associated IKEv2Gateway",
      "exposed" : true,
      "uniqueScope" : "no"
    },
    "prefix" : {
      "type" : "string",
      "format" : "free",
      "description" : "The subnet prefix (eg: 10.0.0.0/24)",
      "filterable" : true,
      "orderable" : true,
      "exposed" : true,
      "uniqueScope" : "no"
    }
  },
  "children" : { },
  "model" : {
    "description" : "Represents an IKEv2 Subnet (right side)",
    "entity_name" : "IKEv2Subnet",
    "extends" : [ "@audited", "@base", "@metadata" ],
    "package" : "ikev2",
    "resource_name" : "ikev2subnets",
    "rest_name" : "ikev2subnet",
    "get" : true,
    "delete" : true,
    "update" : true
  }
}