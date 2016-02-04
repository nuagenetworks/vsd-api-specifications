{
  "attributes" : {
    "description" : {
      "type" : "string",
      "format" : "free",
      "description" : "A description of the Profile instance created.",
      "filterable" : true,
      "orderable" : true,
      "exposed" : "true",
      "uniqueScope" : "no"
    },
    "externalID" : {
      "type" : "string",
      "format" : "free",
      "description" : "This attribute is set when an external management system is managing this object. When set, the VSD will issue a warning if the user tries to modify this object directly through the UI or the API. For example, if VMware vCloud or Openstack create a network, then this network cannot be deleted directly by a user without requiring extra confirmation. This allows integrations to separate between managed objects by external entities and directly managed objects.",
      "filterable" : true,
      "orderable" : true,
      "exposed" : "true",
      "uniqueScope" : "no"
    },
    "name" : {
      "type" : "string",
      "format" : "free",
      "description" : "Name of the Encryption Profile",
      "filterable" : true,
      "orderable" : true,
      "exposed" : "true",
      "uniqueScope" : "no"
    }
  },
  "children" : { },
  "model" : {
    "description" : "Represents an IKEv2 Profile",
    "entity_name" : "IKEv2EncryptionProfile",
    "extends" : [ "@audited", "@base", "@metadata" ],
    "package" : "keyserver",
    "resource_name" : "ikev2encryptionprofiles",
    "rest_name" : "ikev2encryptionprofile"
  }
}