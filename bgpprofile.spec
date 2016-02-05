{
  "attributes" : {
    "associatedExportRoutingPolicyID" : {
      "type" : "string",
      "format" : "free",
      "description" : "???",
      "filterable" : true,
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
    "dampeningHalfLife" : {
      "type" : "integer",
      "description" : "The time in minutes to wait before decrementing dampening penalty; range 1 - 45, default: 15",
      "filterable" : true,
      "orderable" : true,
      "min_value" : 1,
      "max_value" : 45,
      "default_value" : 15,
      "exposed" : true,
      "uniqueScope" : "no"
    },
    "dampeningMaxSuppress" : {
      "type" : "integer",
      "description" : "The maximum duration in minutes that a route will be suppressed; range: 1-720, default: 60",
      "filterable" : true,
      "orderable" : true,
      "min_value" : 1,
      "max_value" : 720,
      "default_value" : 60,
      "exposed" : true,
      "uniqueScope" : "no"
    },
    "dampeningName" : {
      "type" : "string",
      "format" : "free",
      "description" : "The name of the BGP Dampening object. Valid characters are alphabets, numbers, space and hyphen( - ).",
      "filterable" : true,
      "orderable" : true,
      "min_length" : 1,
      "max_length" : 255,
      "exposed" : true,
      "uniqueScope" : "no"
    },
    "dampeningReuse" : {
      "type" : "integer",
      "description" : "This value is compared with penalty to determine route reusability.If the penalty is greater than the suppress limit, the route will be suppressed; if not, it will be reused; Range: 1-20 000, default 750.",
      "filterable" : true,
      "orderable" : true,
      "min_value" : 1,
      "max_value" : 20000,
      "default_value" : 750,
      "exposed" : true,
      "uniqueScope" : "no"
    },
    "dampeningSuppress" : {
      "type" : "integer",
      "description" : "Specifies the penalty that will be used if a route is suppressed; range 1-20 000, default 3000.",
      "filterable" : true,
      "orderable" : true,
      "min_value" : 1,
      "max_value" : 20000,
      "default_value" : 3000,
      "exposed" : true,
      "uniqueScope" : "no"
    },
    "description" : {
      "type" : "string",
      "format" : "free",
      "description" : "A short description for this BGP profile",
      "exposed" : true,
      "uniqueScope" : "no"
    },
    "name" : {
      "type" : "string",
      "format" : "free",
      "description" : "The name of the BGP profile unique within the enterprise. Valid characters are alphabets, numbers, space and hyphen( - ).",
      "filterable" : true,
      "orderable" : true,
      "min_length" : 1,
      "max_length" : 255,
      "exposed" : true,
      "uniqueScope" : "no"
    }
  },
  "children" : { },
  "model" : {
    "description" : "Definition of a BGP Profile object.",
    "entity_name" : "BGPProfile",
    "extends" : [ "@audited", "@base", "@metadata" ],
    "package" : "bgp",
    "resource_name" : "bgpprofiles",
    "rest_name" : "bgpprofile",
    "get" : true,
    "update" : true,
    "delete" : true
  }
}