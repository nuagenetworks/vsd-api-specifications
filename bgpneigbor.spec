{
  "attributes" : {
    "externalID" : {
      "type" : "string",
      "format" : "free",
      "description" : "This attribute is set when an external management system is managing this object. When set, the VSD will issue a warning if the user tries to modify this object directly through the UI or the API. For example, if VMware vCloud or Openstack create a network, then this network cannot be deleted directly by a user without requiring extra confirmation. This allows integrations to separate between managed objects by external entities and directly managed objects.",
      "filterable" : true,
      "orderable" : true,
      "exposed" : true,
      "uniqueScope" : "no"
    },
    "peerAS" : {
      "type" : "integer",
      "subtype" : "long",
      "description" : "Local autonomous system to be used when establishing a session with the remote peer if it is different from the global BGP router autonomous system number",
      "filterable" : true,
      "orderable" : true,
      "exposed" : true,
      "uniqueScope" : "no"
    },
    "peerIP" : {
      "type" : "string",
      "format" : "free",
      "description" : "Local IP Address",
      "filterable" : true,
      "orderable" : true,
      "exposed" : true,
      "uniqueScope" : "no"
    },
    "dampeningEnabled" : {
      "type" : "integer",
      "description" : "Enable/disable route flap damping.",
      "filterable" : true,
      "orderable" : true,
      "exposed" : true,
      "uniqueScope" : "no"
    },
    "session" : {
      "type" : "string",
      "format" : "free",
      "description" : "BGP Neighbor session information",
      "exposed" : true,
      "uniqueScope" : "no"
    },
    "associatedImportRoutingPolicyID" : {
      "type" : "string",
      "format" : "free",
      "description" : "???",
      "filterable" : true,
      "exposed" : true,
      "uniqueScope" : "no"
    },
    "associatedExportRoutingPolicyID" : {
      "type" : "string",
      "format" : "free",
      "description" : "???",
      "filterable" : true,
      "exposed" : true,
      "uniqueScope" : "no"
    },
    "name" : {
      "type" : "string",
      "format" : "free",
      "description" : "The name of the BGP Neighbor. Valid characters are alphabets, numbers, space and hyphen( - ).",
      "filterable" : true,
      "orderable" : true,
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
    "rest_name" : "bgpneighbor"
  }
}
