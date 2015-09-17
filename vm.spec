{
  "apis": {
    "children": {
      "/vms/{id}/alarms": {
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
      "/vms/{id}/eventlogs": {
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
      "/vms/{id}/resync": {
        "RESTName": "resync", 
        "entityName": "VMResync", 
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
        "resourceName": "resync"
      }, 
      "/vms/{id}/vminterfaces": {
        "RESTName": "vminterface", 
        "entityName": "VMInterface", 
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
        "resourceName": "vminterfaces"
      }, 
      "/vms/{id}/vrss": {
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
      "/domains/{id}/vms": {
        "RESTName": "domain", 
        "operations": [
          {
            "availability": null, 
            "method": "GET"
          }
        ], 
        "resourceName": "domains"
      }, 
      "/egressacltemplates/{id}/vms": {
        "RESTName": "egressacltemplate", 
        "operations": [
          {
            "availability": null, 
            "method": "GET"
          }
        ], 
        "resourceName": "egressacltemplates"
      }, 
      "/enterprises/{id}/vms": {
        "RESTName": "enterprise", 
        "operations": [
          {
            "availability": null, 
            "method": "GET"
          }
        ], 
        "resourceName": "enterprises"
      }, 
      "/ingressacltemplates/{id}/vms": {
        "RESTName": "ingressacltemplate", 
        "operations": [
          {
            "availability": null, 
            "method": "GET"
          }
        ], 
        "resourceName": "ingressacltemplates"
      }, 
      "/l2domains/{id}/vms": {
        "RESTName": "l2domain", 
        "operations": [
          {
            "availability": null, 
            "method": "GET"
          }
        ], 
        "resourceName": "l2domains"
      }, 
      "/qos/{id}/vms": {
        "RESTName": "qos", 
        "operations": [
          {
            "availability": null, 
            "method": "GET"
          }
        ], 
        "resourceName": "qos"
      }, 
      "/subnets/{id}/vms": {
        "RESTName": "subnet", 
        "operations": [
          {
            "availability": null, 
            "method": "GET"
          }
        ], 
        "resourceName": "subnets"
      }, 
      "/tiers/{id}/vms": {
        "RESTName": "tier", 
        "operations": [
          {
            "availability": null, 
            "method": "GET"
          }
        ], 
        "resourceName": "tiers"
      }, 
      "/users/{id}/vms": {
        "RESTName": "user", 
        "operations": [
          {
            "availability": null, 
            "method": "GET"
          }
        ], 
        "resourceName": "users"
      }, 
      "/vms": {
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
      "/vports/{id}/vms": {
        "RESTName": "vport", 
        "operations": [
          {
            "availability": null, 
            "method": "GET"
          }
        ], 
        "resourceName": "vports"
      }, 
      "/vrss/{id}/vms": {
        "RESTName": "vrs", 
        "operations": [
          {
            "availability": null, 
            "method": "GET"
          }
        ], 
        "resourceName": "vrss"
      }, 
      "/zones/{id}/vms": {
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
      "/vms/{id}": {
        "RESTName": "vm", 
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
        "resourceName": "vms"
      }
    }
  }, 
  "model": {
    "RESTName": "vm", 
    "attributes": {
      "UUID": {
        "allowedChars": null, 
        "allowedChoices": null, 
        "autogenerated": false, 
        "availability": null, 
        "channel": null, 
        "creationOnly": false, 
        "defaultOrder": false, 
        "defaultValue": null, 
        "description": "UUID of the VM", 
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
      "VRSID": {
        "allowedChars": null, 
        "allowedChoices": null, 
        "autogenerated": false, 
        "availability": null, 
        "channel": null, 
        "creationOnly": false, 
        "defaultOrder": false, 
        "defaultValue": null, 
        "description": "Id of the VRS that this VM is attached to.", 
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
      "appName": {
        "allowedChars": null, 
        "allowedChoices": null, 
        "autogenerated": false, 
        "availability": null, 
        "channel": null, 
        "creationOnly": false, 
        "defaultOrder": false, 
        "defaultValue": null, 
        "description": "Application name that this VM belongs to", 
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
      "deleteExpiry": {
        "allowedChars": null, 
        "allowedChoices": null, 
        "autogenerated": false, 
        "availability": null, 
        "channel": null, 
        "creationOnly": false, 
        "defaultOrder": false, 
        "defaultValue": null, 
        "description": "reflects the  VM Deletion expiry timer in secs , deleteMode needs to be non-null value for deleteExpiry to be taken in to effect. CMS created VM's will always have deleteMode set to TIMER", 
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
        "type": "long", 
        "unique": false
      }, 
      "deleteMode": {
        "allowedChars": null, 
        "allowedChoices": [
          "TIMER"
        ], 
        "autogenerated": false, 
        "availability": null, 
        "channel": null, 
        "creationOnly": false, 
        "defaultOrder": false, 
        "defaultValue": null, 
        "description": "reflects the mode of VM Deletion -  TIMER  Possible values are TIMER, .", 
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
      "domainIDs": {
        "allowedChars": null, 
        "allowedChoices": null, 
        "autogenerated": false, 
        "availability": null, 
        "channel": null, 
        "creationOnly": false, 
        "defaultOrder": false, 
        "defaultValue": null, 
        "description": "Array of IDs of the domain that the VM is connected to", 
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
        "type": "Array[String]", 
        "unique": false
      }, 
      "enterpriseID": {
        "allowedChars": null, 
        "allowedChoices": null, 
        "autogenerated": false, 
        "availability": null, 
        "channel": null, 
        "creationOnly": false, 
        "defaultOrder": false, 
        "defaultValue": null, 
        "description": "ID of the enterprise that this VM belongs to", 
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
      "enterpriseName": {
        "allowedChars": null, 
        "allowedChoices": null, 
        "autogenerated": false, 
        "availability": null, 
        "channel": null, 
        "creationOnly": false, 
        "defaultOrder": false, 
        "defaultValue": null, 
        "description": "Name of the enterprise that this VM belongs to", 
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
      "hypervisorIP": {
        "allowedChars": null, 
        "allowedChoices": null, 
        "autogenerated": false, 
        "availability": null, 
        "channel": null, 
        "creationOnly": false, 
        "defaultOrder": false, 
        "defaultValue": null, 
        "description": "IP address of the hypervisor that this VM is currently running in", 
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
      "interfaces": {
        "allowedChars": null, 
        "allowedChoices": null, 
        "autogenerated": false, 
        "availability": null, 
        "channel": null, 
        "creationOnly": false, 
        "defaultOrder": false, 
        "defaultValue": null, 
        "description": "List of VM interfaces associated with the VM", 
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
        "type": "Array[VMInterface]", 
        "unique": false
      }, 
      "l2DomainIDs": {
        "allowedChars": null, 
        "allowedChoices": null, 
        "autogenerated": false, 
        "availability": null, 
        "channel": null, 
        "creationOnly": false, 
        "defaultOrder": false, 
        "defaultValue": null, 
        "description": "Array of IDs of the l2 domain that the VM is connected to", 
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
        "type": "Array[String]", 
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
        "description": "Name of the VM", 
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
      "reasonType": {
        "allowedChars": null, 
        "allowedChoices": [
          "RUNNING_MIGRATION_CANCELED", 
          "NOSTATE_UNKNOWN", 
          "PAUSED_FROM_SNAPSHOT", 
          "SHUTDOWN_UNKNOWN", 
          "PAUSED_UNKNOWN", 
          "PAUSED_WATCHDOG", 
          "SHUTOFF_MIGRATED", 
          "RUNNING_UNKNOWN", 
          "PAUSED_SAVE", 
          "SHUTOFF_FAILED", 
          "NOSTATE_LAST", 
          "RUNNING_BOOTED", 
          "PAUSED_SHUTTING_DOWN", 
          "SHUTOFF_FROM_SNAPSHOT", 
          "CRASHED_UNKNOWN", 
          "SHUTOFF_DESTROYED", 
          "PAUSED_DUMP", 
          "SHUTOFF_SAVED", 
          "SHUTOFF_SHUTDOWN", 
          "SHUTOFF_UNKNOWN", 
          "RUNNING_UNPAUSED", 
          "RUNNING_FROM_SNAPSHOT", 
          "UNKNOWN", 
          "RUNNING_LAST", 
          "SHUTDOWN_LAST", 
          "SHUTDOWN_USER", 
          "BLOCKED_LAST", 
          "RUNNING_SAVE_CANCELED", 
          "PAUSED_USER", 
          "RUNNING_MIGRATED", 
          "RUNNING_RESTORED", 
          "BLOCKED_UNKNOWN", 
          "CRASHED_LAST", 
          "SHUTOFF_CRASHED", 
          "PAUSED_MIGRATION", 
          "PAUSED_LAST", 
          "SHUTOFF_LAST", 
          "PAUSED_IOERROR"
        ], 
        "autogenerated": false, 
        "availability": null, 
        "channel": null, 
        "creationOnly": false, 
        "defaultOrder": false, 
        "defaultValue": null, 
        "description": "Reason of the event associated with the VM - UNKNOWN, NOSTATE_UNKNOWN, NOSTATE_LAST, RUNNING_UNKNOWN, RUNNING_BOOTED, RUNNING_MIGRATED, RUNNING_RESTORED, RUNNING_FROM_SNAPSHOT, RUNNING_UNPAUSED, RUNNING_MIGRATION_CANCELED, RUNNING_SAVE_CANCELED, RUNNING_LAST, BLOCKED_UNKNOWN, BLOCKED_LAST, PAUSED_UNKNOWN, PAUSED_USER, PAUSED_MIGRATION, PAUSED_SAVE, PAUSED_DUMP, PAUSED_IOERROR, PAUSED_WATCHDOG, PAUSED_FROM_SNAPSHOT, PAUSED_SHUTTING_DOWN, PAUSED_LAST, SHUTDOWN_UNKNOWN, SHUTDOWN_USER, SHUTDOWN_LAST, SHUTOFF_UNKNOWN, SHUTOFF_SHUTDOWN, SHUTOFF_DESTROYED, SHUTOFF_CRASHED, SHUTOFF_MIGRATED, SHUTOFF_SAVED, SHUTOFF_FAILED,SHUTOFF_FROM_SNAPSHOT, SHUTOFF_LAST, CRASHED_UNKNOWN, CRASHED_LAST Possible values are UNKNOWN, NOSTATE_UNKNOWN, NOSTATE_LAST, RUNNING_UNKNOWN, RUNNING_BOOTED, RUNNING_MIGRATED, RUNNING_RESTORED, RUNNING_FROM_SNAPSHOT, RUNNING_UNPAUSED, RUNNING_MIGRATION_CANCELED, RUNNING_SAVE_CANCELED, RUNNING_LAST, BLOCKED_UNKNOWN, BLOCKED_LAST, PAUSED_UNKNOWN, PAUSED_USER, PAUSED_MIGRATION, PAUSED_SAVE, PAUSED_DUMP, PAUSED_IOERROR, PAUSED_WATCHDOG, PAUSED_FROM_SNAPSHOT, PAUSED_SHUTTING_DOWN, PAUSED_LAST, SHUTDOWN_UNKNOWN, SHUTDOWN_USER, SHUTDOWN_LAST, SHUTOFF_UNKNOWN, SHUTOFF_SHUTDOWN, SHUTOFF_DESTROYED, SHUTOFF_CRASHED, SHUTOFF_MIGRATED, SHUTOFF_SAVED, SHUTOFF_FAILED, SHUTOFF_FROM_SNAPSHOT, SHUTOFF_LAST, CRASHED_UNKNOWN, CRASHED_LAST, .", 
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
      "resyncInfo": {
        "allowedChars": null, 
        "allowedChoices": null, 
        "autogenerated": false, 
        "availability": null, 
        "channel": null, 
        "creationOnly": false, 
        "defaultOrder": false, 
        "defaultValue": null, 
        "description": "Information of the status of the resync operation of a VM", 
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
        "type": "VMResync", 
        "unique": false
      }, 
      "siteIdentifier": {
        "allowedChars": null, 
        "allowedChoices": null, 
        "autogenerated": false, 
        "availability": null, 
        "channel": null, 
        "creationOnly": false, 
        "defaultOrder": false, 
        "defaultValue": null, 
        "description": "This property specifies the site the VM belongs to, for Geo-redundancy.", 
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
      "status": {
        "allowedChars": null, 
        "allowedChoices": [
          "UNREACHABLE", 
          "SHUTDOWN", 
          "RUNNING", 
          "NOSTATE", 
          "LAST", 
          "CRASHED", 
          "SHUTOFF", 
          "UNKNOWN", 
          "PAUSED", 
          "INIT", 
          "DELETE_PENDING", 
          "BLOCKED"
        ], 
        "autogenerated": false, 
        "availability": null, 
        "channel": null, 
        "creationOnly": false, 
        "defaultOrder": false, 
        "defaultValue": null, 
        "description": "Status of the VM - UNKNOWN, NOSTATE, RUNNING, BLOCKED, PAUSED, SHUTDOWN, SHUTOFF, CRASHED, LAST, UNREACHABLE, INIT, DELETE_PENDING Possible values are UNKNOWN, NOSTATE, RUNNING, BLOCKED, PAUSED, SHUTDOWN, SHUTOFF, CRASHED, LAST, UNREACHABLE, INIT, DELETE_PENDING, .", 
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
      "subnetIDs": {
        "allowedChars": null, 
        "allowedChoices": null, 
        "autogenerated": false, 
        "availability": null, 
        "channel": null, 
        "creationOnly": false, 
        "defaultOrder": false, 
        "defaultValue": null, 
        "description": "Array of IDs of the subnets that the VM is connected to", 
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
        "type": "Array[String]", 
        "unique": false
      }, 
      "userID": {
        "allowedChars": null, 
        "allowedChoices": null, 
        "autogenerated": false, 
        "availability": null, 
        "channel": null, 
        "creationOnly": false, 
        "defaultOrder": false, 
        "defaultValue": null, 
        "description": "ID of the user that created this VM", 
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
      "userName": {
        "allowedChars": null, 
        "allowedChoices": null, 
        "autogenerated": false, 
        "availability": null, 
        "channel": null, 
        "creationOnly": false, 
        "defaultOrder": false, 
        "defaultValue": null, 
        "description": "Username of the user that created this VM", 
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
      "zoneIDs": {
        "allowedChars": null, 
        "allowedChoices": null, 
        "autogenerated": false, 
        "availability": null, 
        "channel": null, 
        "creationOnly": false, 
        "defaultOrder": false, 
        "defaultValue": null, 
        "description": "Array of IDs of the zone that this VM is attached to", 
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
        "type": "Array[String]", 
        "unique": false
      }
    }, 
    "description": "Read only API that can retrieve the VMs associated with a domain, zone or subnet for mediation created VM's for REST created  VM's you need to set the additional proxy user header in http request : X-Nuage-ProxyUservalue of the header has to be either :1) enterpriseName@UserName (example : Alcatel Lucent@bob), or 2) external ID of user in VSD, typically is UUID generally decided by the CMS tool in questionUser needs to have CMS privileges to use proxy user header", 
    "entityName": "VM", 
    "package": "/vm", 
    "resourceName": "vms"
  }
}