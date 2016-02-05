{
  "attributes" : {
    "active" : {
      "type" : "boolean",
      "description" : "If enabled, it means that this ACL or QOS entry is active",
      "filterable" : true,
      "orderable" : true,
      "exposed" : true,
      "uniqueScope" : "no"
    },
    "associatedLiveEntityID" : {
      "type" : "string",
      "format" : "free",
      "description" : "???",
      "filterable" : true,
      "exposed" : true,
      "uniqueScope" : "no"
    },
    "defaultAllowIP" : {
      "type" : "boolean",
      "description" : "If enabled a default ACL of Allow All is added as the last entry in the list of ACL entries",
      "filterable" : true,
      "orderable" : true,
      "exposed" : true,
      "uniqueScope" : "no"
    },
    "defaultAllowNonIP" : {
      "type" : "boolean",
      "description" : "If enabled, non ip traffic will be dropped",
      "filterable" : true,
      "orderable" : true,
      "exposed" : true,
      "uniqueScope" : "no"
    },
    "description" : {
      "type" : "string",
      "format" : "free",
      "description" : "A description of the entity",
      "filterable" : true,
      "min_length" : 0,
      "max_length" : 255,
      "exposed" : true,
      "uniqueScope" : "no"
    },
    "name" : {
      "type" : "string",
      "format" : "free",
      "description" : "The name of the entity",
      "filterable" : true,
      "orderable" : true,
      "min_length" : 1,
      "max_length" : 255,
      "exposed" : true,
      "uniqueScope" : "no"
    },
    "policyState" : {
      "type" : "enum",
      "allowed_choices" : [ "DRAFT", "LIVE" ],
      "description" : "???",
      "filterable" : true,
      "orderable" : true,
      "exposed" : true,
      "uniqueScope" : "no"
    },
    "priority" : {
      "type" : "integer",
      "description" : "The priority of the ACL entry that determines the order of entries",
      "filterable" : true,
      "orderable" : true,
      "exposed" : true,
      "uniqueScope" : "no"
    },
    "priorityType" : {
      "type" : "enum",
      "allowed_choices" : [ "TOP", "BOTTOM", "NONE" ],
      "description" : "???",
      "filterable" : true,
      "orderable" : true,
      "exposed" : true,
      "uniqueScope" : "no"
    }
  },
  "children" : {
    "egressfloatingipaclentrytemplate" : {
      "get" : true,
      "create" : true,
      "relationship" : "child"
    }
  },
  "model" : {
    "description" : "Defines the template for an Floating IP ACL",
    "entity_name" : "FloatingIPACLTemplate",
    "extends" : [ "@audited", "@base", "@metadata" ],
    "package" : "policy",
    "resource_name" : "egressfloatingipacltemplates",
    "rest_name" : "egressfloatingipacltemplate",
    "create" : true,
    "get" : true,
    "update" : true,
    "delete" : true
  }
}