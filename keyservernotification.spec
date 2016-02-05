{
  "attributes" : {
    "base64JSONString" : {
      "type" : "string",
      "format" : "free",
      "description" : "The base 64 encoded JSON String of the message object",
      "exposed" : true,
      "uniqueScope" : "no"
    },
    "message" : {
      "type" : "object",
      "description" : "The message to send",
      "exposed" : true,
      "uniqueScope" : "no"
    },
    "notificationType" : {
      "type" : "enum",
      "allowed_choices" : [ "REKEY", "ENCRYPTION_ENABLED", "ENCRYPTION_DISABLED", "TEST", "CONFIG_UPDATE" ],
      "description" : "The notification type to trigger",
      "filterable" : true,
      "orderable" : true,
      "exposed" : true,
      "uniqueScope" : "no"
    }
  },
  "children" : { },
  "model" : {
    "description" : "KeyServer Notification - Create one of these transient objects to push an event to the KeyServer",
    "entity_name" : "KeyServerNotification",
    "extends" : [ "@base", "@metadata" ],
    "package" : "keyserver",
    "resource_name" : "keyservernotifications",
    "rest_name" : "keyservernotification"
  }
}