{
  "apis": {
    "children": {
      "/l2domaintemplates/id/metadatas": {
        "RESTName": "metadata", 
        "entityName": "Metadata", 
        "operations": [
          {
            "availability": null, 
            "method": "GET"
          }, 
          {
            "availability": null, 
            "method": "POST"
          }
        ], 
        "resourceName": "metadatas"
      }, 
      "/l2domaintemplates/{id}/addressranges": {
        "RESTName": "addressrange", 
        "entityName": "AddressRange", 
        "operations": [
          {
            "availability": null, 
            "method": "GET"
          }, 
          {
            "availability": null, 
            "method": "POST"
          }
        ], 
        "resourceName": "addressranges"
      }, 
      "/l2domaintemplates/{id}/egressacltemplates": {
        "RESTName": "egressacltemplate", 
        "entityName": "EgressACLTemplate", 
        "operations": [
          {
            "availability": null, 
            "method": "GET"
          }, 
          {
            "availability": null, 
            "method": "POST"
          }
        ], 
        "resourceName": "egressacltemplates"
      }, 
      "/l2domaintemplates/{id}/eventlogs": {
        "RESTName": "eventlog", 
        "entityName": "EventLog", 
        "operations": [
          {
            "availability": null, 
            "method": "GET"
          }
        ], 
        "resourceName": "eventlogs"
      }, 
      "/l2domaintemplates/{id}/groups": {
        "RESTName": "group", 
        "entityName": "Group", 
        "operations": [
          {
            "availability": null, 
            "method": "GET"
          }, 
          {
            "availability": null, 
            "method": "PUT"
          }
        ], 
        "resourceName": "groups"
      }, 
      "/l2domaintemplates/{id}/ingressacltemplates": {
        "RESTName": "ingressacltemplate", 
        "entityName": "IngressACLTemplate", 
        "operations": [
          {
            "availability": null, 
            "method": "GET"
          }, 
          {
            "availability": null, 
            "method": "POST"
          }
        ], 
        "resourceName": "ingressacltemplates"
      }, 
      "/l2domaintemplates/{id}/ingressadvfwdtemplates": {
        "RESTName": "ingressadvfwdtemplate", 
        "entityName": "IngressAdvFwdTemplate", 
        "operations": [
          {
            "availability": null, 
            "method": "GET"
          }, 
          {
            "availability": null, 
            "method": "POST"
          }
        ], 
        "resourceName": "ingressadvfwdtemplates"
      }, 
      "/l2domaintemplates/{id}/ingressexternalservicetemplates": {
        "RESTName": "ingressexternalservicetemplate", 
        "entityName": "IngressExternalServiceTemplate", 
        "operations": [
          {
            "availability": null, 
            "method": "GET"
          }, 
          {
            "availability": null, 
            "method": "POST"
          }
        ], 
        "resourceName": "ingressexternalservicetemplates"
      }, 
      "/l2domaintemplates/{id}/jobs": {
        "RESTName": "job", 
        "entityName": "Job", 
        "operations": [
          {
            "availability": null, 
            "method": "POST"
          }
        ], 
        "resourceName": "jobs"
      }, 
      "/l2domaintemplates/{id}/l2domains": {
        "RESTName": "l2domain", 
        "entityName": "L2Domain", 
        "operations": [
          {
            "availability": null, 
            "method": "GET"
          }
        ], 
        "resourceName": "l2domains"
      }, 
      "/l2domaintemplates/{id}/permissions": {
        "RESTName": "permission", 
        "entityName": "PermittedAction", 
        "operations": [
          {
            "availability": null, 
            "method": "GET"
          }, 
          {
            "availability": null, 
            "method": "POST"
          }
        ], 
        "resourceName": "permissions"
      }, 
      "/l2domaintemplates/{id}/policygrouptemplates": {
        "RESTName": "policygrouptemplate", 
        "entityName": "PolicyGroupTemplate", 
        "operations": [
          {
            "availability": null, 
            "method": "GET"
          }, 
          {
            "availability": null, 
            "method": "POST"
          }
        ], 
        "resourceName": "policygrouptemplates"
      }, 
      "/l2domaintemplates/{id}/qos": {
        "RESTName": "qos", 
        "entityName": "QOS", 
        "operations": [
          {
            "availability": null, 
            "method": "GET"
          }, 
          {
            "availability": null, 
            "method": "POST"
          }
        ], 
        "resourceName": "qos"
      }, 
      "/l2domaintemplates/{id}/redirectiontargettemplates": {
        "RESTName": "redirectiontargettemplate", 
        "entityName": "RedirectionTargetTemplate", 
        "operations": [
          {
            "availability": null, 
            "method": "GET"
          }, 
          {
            "availability": null, 
            "method": "POST"
          }
        ], 
        "resourceName": "redirectiontargettemplates"
      }
    }, 
    "parents": {
      "/enterprises/{id}/l2domaintemplates": {
        "RESTName": "enterprise", 
        "operations": [
          {
            "availability": null, 
            "method": "GET"
          }, 
          {
            "availability": null, 
            "method": "POST"
          }
        ], 
        "resourceName": "enterprises"
      }
    }, 
    "self": {
      "/l2domaintemplates/{id}": {
        "RESTName": "l2domaintemplate", 
        "operations": [
          {
            "availability": null, 
            "method": "PUT"
          }, 
          {
            "availability": null, 
            "method": "DELETE"
          }, 
          {
            "availability": null, 
            "method": "GET"
          }
        ], 
        "resourceName": "l2domaintemplates"
      }
    }
  }, 
  "model": {
    "RESTName": "l2domaintemplate", 
    "attributes": {
      "DHCPManaged": {
        "allowedChars": null, 
        "allowedChoices": null, 
        "autogenerated": false, 
        "availability": null, 
        "channel": null, 
        "creationOnly": false, 
        "defaultOrder": false, 
        "defaultValue": null, 
        "description": "decides whether L2Domain / L2Domain template DHCP is managed by VSD", 
        "exposed": true, 
        "filterable": false, 
        "format": null, 
        "maxLength": null, 
        "maxValue": null, 
        "minLength": null, 
        "minValue": null, 
        "orderable": false, 
        "readOnly": false, 
        "required": false, 
        "transient": false, 
        "type": "boolean", 
        "unique": false
      }, 
      "IPType": {
        "allowedChars": null, 
        "allowedChoices": [
          "IPV6", 
          "IPV4"
        ], 
        "autogenerated": false, 
        "availability": null, 
        "channel": null, 
        "creationOnly": false, 
        "defaultOrder": false, 
        "defaultValue": null, 
        "description": "IPv4 or IPv6(only IPv4 is supported in R2.0) Possible values are IPV4, IPV6, .", 
        "exposed": true, 
        "filterable": false, 
        "format": null, 
        "maxLength": null, 
        "maxValue": null, 
        "minLength": null, 
        "minValue": null, 
        "orderable": false, 
        "readOnly": false, 
        "required": false, 
        "transient": false, 
        "type": "enum", 
        "unique": false
      }, 
      "address": {
        "allowedChars": null, 
        "allowedChoices": null, 
        "autogenerated": false, 
        "availability": null, 
        "channel": null, 
        "creationOnly": false, 
        "defaultOrder": false, 
        "defaultValue": null, 
        "description": "Network address of the L2Domain / L2Domain template defined. ", 
        "exposed": true, 
        "filterable": false, 
        "format": null, 
        "maxLength": null, 
        "maxValue": null, 
        "minLength": null, 
        "minValue": null, 
        "orderable": false, 
        "readOnly": false, 
        "required": false, 
        "transient": false, 
        "type": "string", 
        "unique": false
      }, 
      "associatedMulticastChannelMapID": {
        "allowedChars": null, 
        "allowedChoices": null, 
        "autogenerated": false, 
        "availability": null, 
        "channel": null, 
        "creationOnly": false, 
        "defaultOrder": false, 
        "defaultValue": null, 
        "description": "The ID of the Multi Cast Channel Map this L2Domain / L2Domain template template is associated with. This has to be set when  enableMultiCast is set to ENABLED", 
        "exposed": true, 
        "filterable": false, 
        "format": null, 
        "maxLength": null, 
        "maxValue": null, 
        "minLength": null, 
        "minValue": null, 
        "orderable": false, 
        "readOnly": false, 
        "required": false, 
        "transient": false, 
        "type": "string", 
        "unique": false
      }, 
      "description": {
        "allowedChars": null, 
        "allowedChoices": null, 
        "autogenerated": false, 
        "availability": null, 
        "channel": null, 
        "creationOnly": false, 
        "defaultOrder": false, 
        "defaultValue": null, 
        "description": "A description field provided by the user that identifies the L2Domain / L2Domain template.", 
        "exposed": true, 
        "filterable": false, 
        "format": null, 
        "maxLength": null, 
        "maxValue": null, 
        "minLength": null, 
        "minValue": null, 
        "orderable": false, 
        "readOnly": false, 
        "required": false, 
        "transient": false, 
        "type": "string", 
        "unique": false
      }, 
      "entityScope": {
        "allowedChars": null, 
        "allowedChoices": null, 
        "autogenerated": false, 
        "availability": null, 
        "channel": null, 
        "creationOnly": false, 
        "defaultOrder": false, 
        "defaultValue": null, 
        "description": "Specify if scope of entity is Data center or Enterprise level", 
        "exposed": true, 
        "filterable": false, 
        "format": null, 
        "maxLength": null, 
        "maxValue": null, 
        "minLength": null, 
        "minValue": null, 
        "orderable": false, 
        "readOnly": false, 
        "required": false, 
        "transient": false, 
        "type": "EntityScope", 
        "unique": false
      }, 
      "gateway": {
        "allowedChars": null, 
        "allowedChoices": null, 
        "autogenerated": false, 
        "availability": null, 
        "channel": null, 
        "creationOnly": false, 
        "defaultOrder": false, 
        "defaultValue": null, 
        "description": "The IP address of the gateway of this l2 domain", 
        "exposed": true, 
        "filterable": false, 
        "format": null, 
        "maxLength": null, 
        "maxValue": null, 
        "minLength": null, 
        "minValue": null, 
        "orderable": false, 
        "readOnly": false, 
        "required": false, 
        "transient": false, 
        "type": "string", 
        "unique": false
      }, 
      "multicast": {
        "allowedChars": null, 
        "allowedChoices": [
          "ENABLED", 
          "INHERITED", 
          "DISABLED"
        ], 
        "autogenerated": false, 
        "availability": null, 
        "channel": null, 
        "creationOnly": false, 
        "defaultOrder": false, 
        "defaultValue": null, 
        "description": "multicast is enum that indicates multicast policy on L2Domain / L2Domain template. Possible values are ENABLED and DISABLED Possible values are INHERITED, ENABLED, DISABLED, .", 
        "exposed": true, 
        "filterable": false, 
        "format": null, 
        "maxLength": null, 
        "maxValue": null, 
        "minLength": null, 
        "minValue": null, 
        "orderable": false, 
        "readOnly": false, 
        "required": false, 
        "transient": false, 
        "type": "enum", 
        "unique": false
      }, 
      "name": {
        "allowedChars": null, 
        "allowedChoices": null, 
        "autogenerated": false, 
        "availability": null, 
        "channel": null, 
        "creationOnly": false, 
        "defaultOrder": false, 
        "defaultValue": null, 
        "description": "Name of the L2Domain / L2Domain template,has to be unique within a Enterprise. Valid characters are alphabets, numbers, space and hyphen( - ).", 
        "exposed": true, 
        "filterable": false, 
        "format": null, 
        "maxLength": null, 
        "maxValue": null, 
        "minLength": null, 
        "minValue": null, 
        "orderable": false, 
        "readOnly": false, 
        "required": true, 
        "transient": false, 
        "type": "string", 
        "unique": false
      }, 
      "netmask": {
        "allowedChars": null, 
        "allowedChoices": null, 
        "autogenerated": false, 
        "availability": null, 
        "channel": null, 
        "creationOnly": false, 
        "defaultOrder": false, 
        "defaultValue": null, 
        "description": "Netmask of the L2Domain / L2Domain template defined", 
        "exposed": true, 
        "filterable": false, 
        "format": null, 
        "maxLength": null, 
        "maxValue": null, 
        "minLength": null, 
        "minValue": null, 
        "orderable": false, 
        "readOnly": false, 
        "required": false, 
        "transient": false, 
        "type": "string", 
        "unique": false
      }, 
      "policyChangeStatus": {
        "allowedChars": null, 
        "allowedChoices": [
          "IPV6", 
          "IPV4"
        ], 
        "autogenerated": false, 
        "availability": null, 
        "channel": null, 
        "creationOnly": false, 
        "defaultOrder": false, 
        "defaultValue": null, 
        "description": "", 
        "exposed": true, 
        "filterable": false, 
        "format": null, 
        "maxLength": null, 
        "maxValue": null, 
        "minLength": null, 
        "minValue": null, 
        "orderable": false, 
        "readOnly": false, 
        "required": false, 
        "transient": false, 
        "type": "enum", 
        "unique": false
      }
    }, 
    "description": "L2 Domain in VSD as derived by templates. This object describes the L2 Domain template", 
    "entityName": "L2DomainTemplate", 
    "package": "/network", 
    "resourceName": "l2domaintemplates"
  }
}