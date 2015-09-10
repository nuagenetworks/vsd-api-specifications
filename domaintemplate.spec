{
  "apis": {
    "children": {
      "/domaintemplates/{id}/domains": {
        "RESTName": "domain", 
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
        "resourceName": "domains"
      }, 
      "/domaintemplates/{id}/egressacltemplates": {
        "RESTName": "egressacltemplate", 
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
      "/domaintemplates/{id}/eventlogs": {
        "RESTName": "eventlog", 
        "operations": [
          {
            "availability": null, 
            "method": "GET"
          }
        ], 
        "resourceName": "eventlogs"
      }, 
      "/domaintemplates/{id}/groups": {
        "RESTName": "group", 
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
      "/domaintemplates/{id}/ingressacltemplates": {
        "RESTName": "ingressacltemplate", 
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
      "/domaintemplates/{id}/ingressadvfwdtemplates": {
        "RESTName": "ingressadvfwdtemplate", 
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
      "/domaintemplates/{id}/ingressexternalservicetemplates": {
        "RESTName": "ingressexternalservicetemplate", 
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
      "/domaintemplates/{id}/jobs": {
        "RESTName": "job", 
        "operations": [
          {
            "availability": null, 
            "method": "POST"
          }
        ], 
        "resourceName": "jobs"
      }, 
      "/domaintemplates/{id}/permissions": {
        "RESTName": "permission", 
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
      "/domaintemplates/{id}/policygrouptemplates": {
        "RESTName": "policygrouptemplate", 
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
      "/domaintemplates/{id}/qos": {
        "RESTName": "qos", 
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
      "/domaintemplates/{id}/redirectiontargettemplates": {
        "RESTName": "redirectiontargettemplate", 
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
      }, 
      "/domaintemplates/{id}/subnettemplates": {
        "RESTName": "subnettemplate", 
        "operations": [
          {
            "availability": null, 
            "method": "GET"
          }
        ], 
        "resourceName": "subnettemplates"
      }, 
      "/domaintemplates/{id}/zonetemplates": {
        "RESTName": "zonetemplate", 
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
        "resourceName": "zonetemplates"
      }
    }, 
    "parents": {
      "/domains/{id}/domaintemplates": {
        "RESTName": "domain", 
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
        "resourceName": "domains"
      }, 
      "/enterprises/{id}/domaintemplates": {
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
      "/domaintemplates/{id}": {
        "RESTName": "domaintemplate", 
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
        "resourceName": "domaintemplates"
      }
    }
  }, 
  "model": {
    "RESTName": "domaintemplate", 
    "attributes": {
      "associatedMulticastChannelMapID": {
        "allowedChars": null, 
        "allowedChoices": null, 
        "autogenerated": false, 
        "availability": null, 
        "channel": null, 
        "creationOnly": false, 
        "defaultOrder": false, 
        "defaultValue": null, 
        "description": "The ID of the Multi Cast Channel Map  this domain template is associated with. This has to be set when  enableMultiCast is set to ENABLED", 
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
        "description": "Domain template description provided by the user", 
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
      "encryption": {
        "allowedChars": null, 
        "allowedChoices": [
          "ENABLED", 
          "DISABLED"
        ], 
        "autogenerated": false, 
        "availability": null, 
        "channel": null, 
        "creationOnly": false, 
        "defaultOrder": false, 
        "defaultValue": null, 
        "description": "Determines whether IPSEC is enabled. Possible values are ENABLED, DISABLED, .", 
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
        "description": "multicast is enum that indicates multicast policy on domain. Possible values are ENABLED ,DISABLED  and INHERITED Possible values are INHERITED, ENABLED, DISABLED, .", 
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
        "description": "The name of the domain template, that is unique within an enterprise. Valid characters are alphabets, numbers, space and hyphen( - ).", 
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
      "policyChangeStatus": {
        "allowedChars": null, 
        "allowedChoices": [
          "ENABLED", 
          "DISABLED"
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
    "description": "Domains in VSD are created from domain templates. This object provides the definition of the DomainTemplate", 
    "entityName": "DomainTemplate", 
    "package": "/network", 
    "resourceName": "domaintemplates"
  }
}