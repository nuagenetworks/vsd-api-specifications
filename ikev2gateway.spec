{
  "attributes" : {
    "IPAddress" : {
      "type" : "string",
      "format" : "free",
      "description" : "IP Address of the IKEv2 Gateway",
      "filterable" : true,
      "orderable" : true,
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
      "description" : "Description of the IKEv2 Gateway",
      "filterable" : true,
      "orderable" : true,
      "exposed" : true,
      "uniqueScope" : "no"
    },
    "name" : {
      "type" : "string",
      "format" : "free",
      "description" : "Name of the IKEv2 Gateway",
      "filterable" : true,
      "orderable" : true,
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