{
  "apis": {
    "children": {
      "/vports/{id}/aggregatemetadatas": {
        "RESTName": "aggregatemetadata", 
        "entityName": "AggregateMetadata", 
        "operations": [
          {
            "availability": null, 
            "method": "GET"
          }
        ], 
        "resourceName": "aggregatemetadatas"
      }, 
      "/vports/{id}/alarms": {
        "RESTName": "alarm", 
        "entityName": "Alarm", 
        "operations": [
          {
            "availability": null, 
            "method": "GET"
          }
        ], 
        "resourceName": "alarms"
      }, 
      "/vports/{id}/bridgeinterfaces": {
        "RESTName": "bridgeinterface", 
        "entityName": "BridgeInterface", 
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
        "resourceName": "bridgeinterfaces"
      }, 
      "/vports/{id}/dhcpoptions": {
        "RESTName": "dhcpoption", 
        "entityName": "DHCPOption", 
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
        "resourceName": "dhcpoptions"
      }, 
      "/vports/{id}/eventlogs": {
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
      "/vports/{id}/hostinterfaces": {
        "RESTName": "hostinterface", 
        "entityName": "HostInterface", 
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
        "resourceName": "hostinterfaces"
      }, 
      "/vports/{id}/policygroups": {
        "RESTName": "policygroup", 
        "entityName": "PolicyGroup", 
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
        "resourceName": "policygroups"
      }, 
      "/vports/{id}/qos": {
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
      "/vports/{id}/redirectiontargets": {
        "RESTName": "redirectiontarget", 
        "entityName": "RedirectionTarget", 
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
        "resourceName": "redirectiontargets"
      }, 
      "/vports/{id}/statistics": {
        "RESTName": "statistics", 
        "entityName": "Statistics", 
        "operations": [
          {
            "availability": null, 
            "method": "GET"
          }
        ], 
        "resourceName": "statistics"
      }, 
      "/vports/{id}/statisticspolicies": {
        "RESTName": "statisticspolicy", 
        "entityName": "StatisticsPolicy", 
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
        "resourceName": "statisticspolicies"
      }, 
      "/vports/{id}/tcas": {
        "RESTName": "tca", 
        "entityName": "TCA", 
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
        "resourceName": "tcas"
      }, 
      "/vports/{id}/virtualips": {
        "RESTName": "virtualip", 
        "entityName": "VirtualIP", 
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
        "resourceName": "virtualips"
      }, 
      "/vports/{id}/vminterfaces": {
        "RESTName": "vminterface", 
        "entityName": "VMInterface", 
        "operations": [
          {
            "availability": null, 
            "method": "GET"
          }
        ], 
        "resourceName": "vminterfaces"
      }, 
      "/vports/{id}/vms": {
        "RESTName": "vm", 
        "entityName": "VM", 
        "operations": [
          {
            "availability": null, 
            "method": "GET"
          }
        ], 
        "resourceName": "vms"
      }, 
      "/vports/{id}/vportmirrors": {
        "RESTName": "vportmirror", 
        "entityName": "VPortMirror", 
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
        "resourceName": "vportmirrors"
      }, 
      "/vports/{id}/vrss": {
        "RESTName": "vrs", 
        "entityName": "VRS", 
        "operations": [
          {
            "availability": null, 
            "method": "GET"
          }
        ], 
        "resourceName": "vrss"
      }
    }, 
    "parents": {
      "/domains/{id}/vports": {
        "RESTName": "domain", 
        "operations": [
          {
            "availability": null, 
            "method": "GET"
          }
        ], 
        "resourceName": "domains"
      }, 
      "/floatingips/{id}/vports": {
        "RESTName": "floatingip", 
        "operations": [
          {
            "availability": null, 
            "method": "GET"
          }
        ], 
        "resourceName": "floatingips"
      }, 
      "/l2domains/{id}/vports": {
        "RESTName": "l2domain", 
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
        "resourceName": "l2domains"
      }, 
      "/multinicvports/{id}/vports": {
        "RESTName": "multinicvport", 
        "operations": [
          {
            "availability": null, 
            "method": "GET"
          }
        ], 
        "resourceName": "multinicvports"
      }, 
      "/policygroups/{id}/vports": {
        "RESTName": "policygroup", 
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
        "resourceName": "policygroups"
      }, 
      "/redirectiontargets/{id}/vports": {
        "RESTName": "redirectiontarget", 
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
        "resourceName": "redirectiontargets"
      }, 
      "/subnets/{id}/vports": {
        "RESTName": "subnet", 
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
        "resourceName": "subnets"
      }, 
      "/tiers/{id}/vports": {
        "RESTName": "tier", 
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
        "resourceName": "tiers"
      }, 
      "/vrss/{id}/vports": {
        "RESTName": "vrs", 
        "operations": [
          {
            "availability": null, 
            "method": "GET"
          }
        ], 
        "resourceName": "vrss"
      }
    }, 
    "self": {
      "/vports/{id}": {
        "RESTName": "vport", 
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
        "resourceName": "vports"
      }
    }
  }, 
  "model": {
    "RESTName": "vport", 
    "attributes": {
      "VLANID": {
        "allowedChars": null, 
        "allowedChoices": null, 
        "autogenerated": false, 
        "availability": null, 
        "channel": null, 
        "creationOnly": false, 
        "defaultOrder": false, 
        "defaultValue": null, 
        "description": "associated Vlan of this vport - applicable for type host/bridge", 
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
      "active": {
        "allowedChars": null, 
        "allowedChoices": null, 
        "autogenerated": false, 
        "availability": null, 
        "channel": null, 
        "creationOnly": false, 
        "defaultOrder": false, 
        "defaultValue": null, 
        "description": "Indicates if this vport is up or down", 
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
        "type": "boolean", 
        "unique": false
      }, 
      "addressSpoofing": {
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
        "description": "Indicates if address spoofing is ENABLED/DISABLED/INHERITED for this vport Possible values are INHERITED, ENABLED, DISABLED, .", 
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
        "type": "enum", 
        "unique": false
      }, 
      "associatedFloatingIPID": {
        "allowedChars": null, 
        "allowedChoices": null, 
        "autogenerated": false, 
        "availability": null, 
        "channel": null, 
        "creationOnly": false, 
        "defaultOrder": false, 
        "defaultValue": null, 
        "description": "Id of Floating IP address associated to this vport", 
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
        "description": "The ID of the receive Multicast Channel Map this Vport is associated with. This has to be set when enableMultiCast is set to ENABLED", 
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
      "associatedSendMulticastChannelMapID": {
        "allowedChars": null, 
        "allowedChoices": null, 
        "autogenerated": false, 
        "availability": null, 
        "channel": null, 
        "creationOnly": false, 
        "defaultOrder": false, 
        "defaultValue": null, 
        "description": "The ID of the send Multicast Channel Map this Vport is associated with. This has to be set when enableMultiCast is set to ENABLED", 
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
        "description": "Description for this vport", 
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
      "domainID": {
        "allowedChars": null, 
        "allowedChoices": null, 
        "autogenerated": false, 
        "availability": null, 
        "channel": null, 
        "creationOnly": false, 
        "defaultOrder": false, 
        "defaultValue": null, 
        "description": "ID the Domain associated with the VPort", 
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
      "hasAttachedInterfaces": {
        "allowedChars": null, 
        "allowedChoices": null, 
        "autogenerated": false, 
        "availability": null, 
        "channel": null, 
        "creationOnly": false, 
        "defaultOrder": false, 
        "defaultValue": null, 
        "description": "Indicates that this vport has attached interfaces", 
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
      "multiNICVPortID": {
        "allowedChars": null, 
        "allowedChoices": null, 
        "autogenerated": false, 
        "availability": null, 
        "channel": null, 
        "creationOnly": false, 
        "defaultOrder": false, 
        "defaultValue": null, 
        "description": "ID of the Multi NIC VPort associated with the VPort", 
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
        "description": "multicast is enum that indicates multicast policy on Vport. Possible values are ENABLED ,DISABLED  and INHERITED Possible values are INHERITED, ENABLED, DISABLED, .", 
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
        "description": "Name of the vport. Valid characters are alphabets, numbers, space and hyphen( - ).", 
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
      "operationalState": {
        "allowedChars": null, 
        "allowedChoices": [
          "DOWN", 
          "UP", 
          "INIT"
        ], 
        "autogenerated": false, 
        "availability": null, 
        "channel": null, 
        "creationOnly": false, 
        "defaultOrder": false, 
        "defaultValue": null, 
        "description": "Operational State of the VPort - RUNNING/SHUTDOWN Possible values are INIT, UP, DOWN, .", 
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
      "systemType": {
        "allowedChars": null, 
        "allowedChoices": [
          "HARDWARE", 
          "NUAGE_VRSG", 
          "NUAGE_2", 
          "NUAGE_1", 
          "HARDWARE_VTEP", 
          "SOFTWARE"
        ], 
        "autogenerated": false, 
        "availability": null, 
        "channel": null, 
        "creationOnly": false, 
        "defaultOrder": false, 
        "defaultValue": null, 
        "description": "Indicates what system it is - SOFTWARE/HARDWARE_VTEP/HARDWARE/ (possible values)  Possible values are HARDWARE, SOFTWARE, HARDWARE_VTEP, NUAGE_1, NUAGE_2, NUAGE_VRSG, .", 
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
      "type": {
        "allowedChars": null, 
        "allowedChoices": [
          "HOST", 
          "BRIDGE", 
          "VM"
        ], 
        "autogenerated": false, 
        "availability": null, 
        "channel": null, 
        "creationOnly": false, 
        "defaultOrder": false, 
        "defaultValue": null, 
        "description": "Type of vport - possible values VM/HOST/BRIDGE Possible values are VM, HOST, BRIDGE, .", 
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
        "type": "enum", 
        "unique": false
      }, 
      "zoneID": {
        "allowedChars": null, 
        "allowedChoices": null, 
        "autogenerated": false, 
        "availability": null, 
        "channel": null, 
        "creationOnly": false, 
        "defaultOrder": false, 
        "defaultValue": null, 
        "description": "ID the Zone associated with the VPort", 
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
      }
    }, 
    "description": "VPorts are a new level in the domain hierarchy, intended to provide more granular configuration than at subnet, and also support a split workflow, where the vPort is configured and associated with a VM port (or gateway port) before the port exists on the hypervisor or gateway", 
    "entityName": "VPort", 
    "package": "/vport", 
    "resourceName": "vports"
  }
}