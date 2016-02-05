{
  "attributes" : {
    "associatedExportRoutingPolicyID" : {
      "type" : "string",
      "format" : "free",
      "description" : "ID of the associated export routing policy",
      "filterable" : true,
      "exposed" : true,
      "uniqueScope" : "no"
    },
    "associatedImportRoutingPolicyID" : {
      "type" : "string",
      "format" : "free",
      "description" : "ID of the associated import routing policy",
      "filterable" : true,
      "exposed" : true,
      "uniqueScope" : "no"
    },
    "dampeningEnabled" : {
      "type" : "boolean",
      "description" : "Enable/disable route flap damping.",
      "filterable" : true,
      "orderable" : true,
      "exposed" : true,
      "uniqueScope" : "no"
    },
    "description" : {
      "type" : "string",
      "format" : "free",
      "description" : "A short description for this neighbor",
      "exposed" : true,
      "uniqueScope" : "no"
    },
    "name" : {
      "type" : "string",
      "format" : "free",
      "description" : "The name of the BGP Neighbor. Valid characters are alphabets, numbers, space and hyphen( - ).",
      "filterable" : true,
      "orderable" : true,
      "min_length" : 1,
      "max_length" : 255,
      "exposed" : true,
      "uniqueScope" : "no"
    },
    "peerAS" : {
      "type" : "integer",
      "subtype" : "long",
      "description" : "Local autonomous system to be used when establishing a session with the remote peer if it is different from the global BGP router autonomous system number",
      "filterable" : true,
      "orderable" : true,
      "min_value" : 1,
      "max_value" : 65535,
      "exposed" : true,
      "uniqueScope" : "no"
    },
    "peerIP" : {
      "type" : "string",
      "format" : "free",
      "description" : "Local IP Address",
      "filterable" : true,
      "orderable" : true,
      "min_length" : 0,
      "max_length" : 255,
      "exposed" : true,
      "uniqueScope" : "no"
    },
    "session" : {
      "type" : "string",
      "format" : "free",
      "description" : "BGP Neighbor session information",
      "exposed" : true,
      "uniqueScope" : "no"
    }
  },
  "children" : { },
  "model" : {
    "description" : "Model of a BGP Neighbor configuration",
    "entity_name" : "BGPNeighbor",
    "extends" : [ "@audited", "@base", "@metadata" ],
    "package" : "bgp",
    "resource_name" : "bgpneighbors",
    "rest_name" : "bgpneighbor",
    "get" : true,
    "update" : true,
    "delete" : true
  }
}