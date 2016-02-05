{
  "attributes" : {
    "description" : {
      "type" : "string",
      "format" : "free",
      "description" : "Description of this redirection target template",
      "exposed" : true,
      "uniqueScope" : "no"
    },
    "endPointType" : {
      "type" : "enum",
      "allowed_choices" : [ "NONE", "L3", "VIRTUAL_WIRE" ],
      "description" : "VPortTagEndPointType is an enum. It defines the type of header rewrite and forwarding performed by VRS when the endpoint is used as a PBR destination. Possible values are NONE, L3, VIRTUAL_WIRE.",
      "default_value" : "NONE",
      "exposed" : true,
      "uniqueScope" : "no"
    },
    "name" : {
      "type" : "string",
      "format" : "free",
      "description" : "Name of this redirection target template",
      "filterable" : true,
      "orderable" : true,
      "exposed" : true,
      "uniqueScope" : "no"
    },
    "redundancyEnabled" : {
      "type" : "boolean",
      "description" : "Allow/Disallow redundant appliances and VIP",
      "exposed" : true,
      "uniqueScope" : "no"
    },
    "triggerType" : {
      "type" : "enum",
      "allowed_choices" : [ "NONE", "GARP" ],
      "description" : "Trigger type, could be NONE/GARP - THIS IS READONLY",
      "exposed" : true,
      "uniqueScope" : "no"
    }
  },
  "children" : {
    "job" : {
      "create" : true,
      "relationship" : "child"
    },
    "eventlog" : {
      "get" : true,
      "relationship" : "child"
    }
  },
  "model" : {
    "description" : "Template for a vporttag. Can be created only at the template level and available for all instances.",
    "entity_name" : "VPortTagTemplate",
    "extends" : [ "@audited", "@base", "@metadata" ],
    "package" : "vport",
    "resource_name" : "vporttagtemplates",
    "rest_name" : "vporttagtemplate",
    "get" : true,
    "update" : true,
    "delete" : true
  }
}