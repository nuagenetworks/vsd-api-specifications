{
  "apis": {
    "children": {
      "/vminterfaces/id/metadatas": {
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
      "/vminterfaces/{id}/dhcpoptions": {
        "RESTName": "dhcpoption",
        "entityName": "DHCPOption",
        "operations": [
          {
            "availability": null,
            "method": "GET"
          }
        ],
        "resourceName": "dhcpoptions"
      },
      "/vminterfaces/{id}/eventlogs": {
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
      "/vminterfaces/{id}/multicastchannelmaps": {
        "RESTName": "multicastchannelmap",
        "entityName": "MultiCastChannelMap",
        "operations": [
          {
            "availability": null,
            "method": "GET"
          }
        ],
        "resourceName": "multicastchannelmaps"
      },
      "/vminterfaces/{id}/policydecisions": {
        "RESTName": "policydecision",
        "entityName": "PolicyDecision",
        "operations": [
          {
            "availability": null,
            "method": "GET"
          }
        ],
        "resourceName": "policydecisions"
      },
      "/vminterfaces/{id}/policygroups": {
        "RESTName": "policygroup",
        "entityName": "PolicyGroup",
        "operations": [
          {
            "availability": null,
            "method": "GET"
          }
        ],
        "resourceName": "policygroups"
      },
      "/vminterfaces/{id}/redirectiontargets": {
        "RESTName": "redirectiontarget",
        "entityName": "RedirectionTarget",
        "operations": [
          {
            "availability": null,
            "method": "GET"
          }
        ],
        "resourceName": "redirectiontargets"
      },
      "/vminterfaces/{id}/staticroutes": {
        "RESTName": "staticroute",
        "entityName": "StaticRoute",
        "operations": [
          {
            "availability": null,
            "method": "GET"
          }
        ],
        "resourceName": "staticroutes"
      },
      "/vminterfaces/{id}/statistics": {
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
      "/vminterfaces/{id}/tcas": {
        "RESTName": "tca",
        "entityName": "TCA",
        "operations": [
          {
            "availability": null,
            "method": "GET"
          }
        ],
        "resourceName": "tcas"
      }
    },
    "parents": {
      "/domains/{id}/vminterfaces": {
        "RESTName": "domain",
        "operations": [
          {
            "availability": null,
            "method": "GET"
          }
        ],
        "resourceName": "domains"
      },
      "/l2domains/{id}/vminterfaces": {
        "RESTName": "l2domain",
        "operations": [
          {
            "availability": null,
            "method": "GET"
          }
        ],
        "resourceName": "l2domains"
      },
      "/subnets/{id}/vminterfaces": {
        "RESTName": "subnet",
        "operations": [
          {
            "availability": null,
            "method": "GET"
          }
        ],
        "resourceName": "subnets"
      },
      "/vminterfaces": {
        "RESTName": "vminterface",
        "operations": [
          {
            "availability": null,
            "method": "GET"
          }
        ],
        "resourceName": "vminterfaces"
      },
      "/vms/{id}/vminterfaces": {
        "RESTName": "vm",
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
        "resourceName": "vms"
      },
      "/vports/{id}/vminterfaces": {
        "RESTName": "vport",
        "operations": [
          {
            "availability": null,
            "method": "GET"
          }
        ],
        "resourceName": "vports"
      },
      "/zones/{id}/vminterfaces": {
        "RESTName": "zone",
        "operations": [
          {
            "availability": null,
            "method": "GET"
          }
        ],
        "resourceName": "zones"
      }
    },
    "self": {
      "/vminterfaces/{id}": {
        "RESTName": "vminterface",
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
        "resourceName": "vminterfaces"
      }
    }
  },
  "model": {
    "RESTName": "vminterface",
    "attributes": {
      "IPAddress": {
        "allowedChars": null,
        "allowedChoices": null,
        "autogenerated": false,
        "availability": null,
        "channel": null,
        "creationOnly": false,
        "defaultOrder": false,
        "defaultValue": null,
        "description": "IP address of the  interface",
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
      "MAC": {
        "allowedChars": null,
        "allowedChoices": null,
        "autogenerated": false,
        "availability": null,
        "channel": null,
        "creationOnly": false,
        "defaultOrder": false,
        "defaultValue": null,
        "description": "MAC address of the  interface",
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
      "VMUUID": {
        "allowedChars": null,
        "allowedChoices": null,
        "autogenerated": false,
        "availability": null,
        "channel": null,
        "creationOnly": false,
        "defaultOrder": false,
        "defaultValue": null,
        "description": "UUID of the associated virtual machine",
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
      "VPortID": {
        "allowedChars": null,
        "allowedChoices": null,
        "autogenerated": false,
        "availability": null,
        "channel": null,
        "creationOnly": false,
        "defaultOrder": false,
        "defaultValue": null,
        "description": "ID of the vport that the interface is attached to",
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
      "VPortName": {
        "allowedChars": null,
        "allowedChoices": null,
        "autogenerated": false,
        "availability": null,
        "channel": null,
        "creationOnly": false,
        "defaultOrder": false,
        "defaultValue": null,
        "description": "Name of the vport that the VM is attached to",
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
      "associatedFloatingIPAddress": {
        "allowedChars": null,
        "allowedChoices": null,
        "autogenerated": false,
        "availability": null,
        "channel": null,
        "creationOnly": false,
        "defaultOrder": false,
        "defaultValue": null,
        "description": "Floating Ip Address of this network interface eg: 10.1.2.1",
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
      "attachedNetworkID": {
        "allowedChars": null,
        "allowedChoices": null,
        "autogenerated": false,
        "availability": null,
        "channel": null,
        "creationOnly": false,
        "defaultOrder": false,
        "defaultValue": null,
        "description": "ID of the l2 domain or Subnet that the VM is attached to",
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
      "attachedNetworkType": {
        "allowedChars": null,
        "allowedChoices": null,
        "autogenerated": false,
        "availability": null,
        "channel": null,
        "creationOnly": false,
        "defaultOrder": false,
        "defaultValue": null,
        "description": "l2 domain or Subnet that the interface is attached to",
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
        "type": "ManagedObjectType",
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
        "description": "ID of the domain that the VM is attached to",
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
      "domainName": {
        "allowedChars": null,
        "allowedChoices": null,
        "autogenerated": false,
        "availability": null,
        "channel": null,
        "creationOnly": false,
        "defaultOrder": false,
        "defaultValue": null,
        "description": "Name of the domain that the VM is attached to",
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
        "description": "Gateway of the subnet that the VM is connected to",
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
      "multiNICVPortName": {
        "allowedChars": null,
        "allowedChoices": null,
        "autogenerated": false,
        "availability": null,
        "channel": null,
        "creationOnly": false,
        "defaultOrder": false,
        "defaultValue": null,
        "description": "Name of the Multi NIC VPort associated with this VM Interface",
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
      "name": {
        "allowedChars": null,
        "allowedChoices": null,
        "autogenerated": false,
        "availability": null,
        "channel": null,
        "creationOnly": false,
        "defaultOrder": false,
        "defaultValue": null,
        "description": "Device name associated with this interface",
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
      "netmask": {
        "allowedChars": null,
        "allowedChoices": null,
        "autogenerated": false,
        "availability": null,
        "channel": null,
        "creationOnly": false,
        "defaultOrder": false,
        "defaultValue": null,
        "description": "Netmask of the subnet that the VM is attached to",
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
      "networkName": {
        "allowedChars": null,
        "allowedChoices": null,
        "autogenerated": false,
        "availability": null,
        "channel": null,
        "creationOnly": false,
        "defaultOrder": false,
        "defaultValue": null,
        "description": "Name of the network that the VM is attached to",
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
      "policyDecisionID": {
        "allowedChars": null,
        "allowedChoices": null,
        "autogenerated": false,
        "availability": null,
        "channel": null,
        "creationOnly": false,
        "defaultOrder": false,
        "defaultValue": null,
        "description": "The policy decision ID for this particular  interface",
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
      "tierID": {
        "allowedChars": null,
        "allowedChoices": null,
        "autogenerated": false,
        "availability": null,
        "channel": null,
        "creationOnly": false,
        "defaultOrder": false,
        "defaultValue": null,
        "description": "ID of the tier that the interface is attached to.",
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
      "zoneID": {
        "allowedChars": null,
        "allowedChoices": null,
        "autogenerated": false,
        "availability": null,
        "channel": null,
        "creationOnly": false,
        "defaultOrder": false,
        "defaultValue": null,
        "description": "ID of the zone that the interface is attached to",
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
      "zoneName": {
        "allowedChars": null,
        "allowedChoices": null,
        "autogenerated": false,
        "availability": null,
        "channel": null,
        "creationOnly": false,
        "defaultOrder": false,
        "defaultValue": null,
        "description": "Name of the zone that the VM is attached to",
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
    "description": "Read only API that can retrieve the VM interface associated with a domain, zone or subnet for mediation created VM's for REST created  VM interfaces you need to set the additional proxy header in http request : X-Nuage-ProxyUservalue of the header has to be either :1) enterpriseName@UserName (example :bob@Alcatel Lucent), or 2) external ID of user in VSD, typically is UUID generally decided by the CMS tool in questionUser needs to have CMS privileges to use proxy user header",
    "entityName": "VMInterface",
    "package": "/vm",
    "resourceName": "vminterfaces"
  }
}