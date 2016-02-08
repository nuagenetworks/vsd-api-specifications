{
  "attributes" : {
    "defaultAction" : {
      "type" : "enum",
      "allowed_choices" : [ "ACCEPT", "REJECT" ],
      "description" : "type used to specify default route disposition in a policy chain",
      "exposed" : true,
      "uniqueScope" : "no"
    },
    "description" : {
      "type" : "string",
      "format" : "free",
      "description" : "A short description for this routing policy",
      "exposed" : true,
      "uniqueScope" : "no"
    },
    "name" : {
      "type" : "string",
      "format" : "free",
      "description" : "The name of Routing Policy unique within the enterprise. Valid characters are alphabets, numbers, space and hyphen( - ).",
      "min_length" : 1,
      "max_length" : 255,
      "exposed" : true,
      "uniqueScope" : "no"
    },
    "policyDefinition" : {
      "type" : "string",
      "format" : "free",
      "description" : "Data definitions for pre-defined sets of attributes used in policy match conditions: prefix lists, entries, damping profile, etc This is a generic attribute to allow the user to specify matching conditions for different routing protocols.",
      "exposed" : true,
      "uniqueScope" : "no"
    }
  },
  "children" : { },
  "model" : {
    "description" : "Model of a routing policy configuration. It is intended to be used for configuring routing protocols: BGP, OSPF, OSPFv3, ISIS, etc.",
    "entity_name" : "RoutingPolicy",
    "extends" : [ "@audited", "@base", "@metadata" ],
    "package" : "network",
    "resource_name" : "routingpolicies",
    "rest_name" : "routingpolicy",
    "get" : true,
    "update" : true,
    "delete" : true
  }
}