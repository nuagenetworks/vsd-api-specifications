{
    "attributes": {
        "UUID": {
            "description": "UUID of the VM",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "required": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "VRSID": {
            "description": "Id of the VRS that this VM is attached to.",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        },
        "appName": {
            "description": "Application name that this VM belongs to",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        },
        "deleteExpiry": {
            "description": "reflects the  VM Deletion expiry timer in secs , deleteMode needs to be non-null value for deleteExpiry to be taken in to effect. CMS created VM's will always have deleteMode set to TIMER",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "integer",
            "subtype": "long",
            "uniqueScope": "no"
        },
        "deleteMode": {
            "allowed_choices": [
                "TIMER"
            ],
            "description": "reflects the mode of VM Deletion -  TIMER  Possible values are TIMER, .",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "enum",
            "uniqueScope": "no"
        },
        "domainIDs": {
            "description": "Array of IDs of the domain that the VM is connected to",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "list",
            "subtype": "string",
            "uniqueScope": "no"
        },
        "enterpriseID": {
            "description": "ID of the enterprise that this VM belongs to",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        },
        "enterpriseName": {
            "description": "Name of the enterprise that this VM belongs to",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "hypervisorIP": {
            "description": "IP address of the hypervisor that this VM is currently running in",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "interfaces": {
            "description": "List of VM interfaces associated with the VM",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "list",
            "subtype": "object",
            "uniqueScope": "no"
        },
        "l2DomainIDs": {
            "description": "Array of IDs of the l2 domain that the VM is connected to",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "list",
            "subtype": "string",
            "uniqueScope": "no"
        },
        "name": {
            "description": "Name of the VM",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "required": true,
            "type": "string",
            "min_length": 1,
            "max_length": 255,
            "uniqueScope": "no"
        },
        "reasonType": {
            "allowed_choices": [
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
            "description": "Reason of the event associated with the VM - UNKNOWN, NOSTATE_UNKNOWN, NOSTATE_LAST, RUNNING_UNKNOWN, RUNNING_BOOTED, RUNNING_MIGRATED, RUNNING_RESTORED, RUNNING_FROM_SNAPSHOT, RUNNING_UNPAUSED, RUNNING_MIGRATION_CANCELED, RUNNING_SAVE_CANCELED, RUNNING_LAST, BLOCKED_UNKNOWN, BLOCKED_LAST, PAUSED_UNKNOWN, PAUSED_USER, PAUSED_MIGRATION, PAUSED_SAVE, PAUSED_DUMP, PAUSED_IOERROR, PAUSED_WATCHDOG, PAUSED_FROM_SNAPSHOT, PAUSED_SHUTTING_DOWN, PAUSED_LAST, SHUTDOWN_UNKNOWN, SHUTDOWN_USER, SHUTDOWN_LAST, SHUTOFF_UNKNOWN, SHUTOFF_SHUTDOWN, SHUTOFF_DESTROYED, SHUTOFF_CRASHED, SHUTOFF_MIGRATED, SHUTOFF_SAVED, SHUTOFF_FAILED,SHUTOFF_FROM_SNAPSHOT, SHUTOFF_LAST, CRASHED_UNKNOWN, CRASHED_LAST Possible values are UNKNOWN, NOSTATE_UNKNOWN, NOSTATE_LAST, RUNNING_UNKNOWN, RUNNING_BOOTED, RUNNING_MIGRATED, RUNNING_RESTORED, RUNNING_FROM_SNAPSHOT, RUNNING_UNPAUSED, RUNNING_MIGRATION_CANCELED, RUNNING_SAVE_CANCELED, RUNNING_LAST, BLOCKED_UNKNOWN, BLOCKED_LAST, PAUSED_UNKNOWN, PAUSED_USER, PAUSED_MIGRATION, PAUSED_SAVE, PAUSED_DUMP, PAUSED_IOERROR, PAUSED_WATCHDOG, PAUSED_FROM_SNAPSHOT, PAUSED_SHUTTING_DOWN, PAUSED_LAST, SHUTDOWN_UNKNOWN, SHUTDOWN_USER, SHUTDOWN_LAST, SHUTOFF_UNKNOWN, SHUTOFF_SHUTDOWN, SHUTOFF_DESTROYED, SHUTOFF_CRASHED, SHUTOFF_MIGRATED, SHUTOFF_SAVED, SHUTOFF_FAILED, SHUTOFF_FROM_SNAPSHOT, SHUTOFF_LAST, CRASHED_UNKNOWN, CRASHED_LAST, .",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "enum",
            "uniqueScope": "no"
        },
        "resyncInfo": {
            "description": "Information of the status of the resync operation of a VM",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "object",
            "uniqueScope": "no"
        },
        "siteIdentifier": {
            "description": "This property specifies the site the VM belongs to, for Geo-redundancy.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "status": {
            "allowed_choices": [
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
            "description": "Status of the VM - UNKNOWN, NOSTATE, RUNNING, BLOCKED, PAUSED, SHUTDOWN, SHUTOFF, CRASHED, LAST, UNREACHABLE, INIT, DELETE_PENDING Possible values are UNKNOWN, NOSTATE, RUNNING, BLOCKED, PAUSED, SHUTDOWN, SHUTOFF, CRASHED, LAST, UNREACHABLE, INIT, DELETE_PENDING, .",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "enum",
            "uniqueScope": "no"
        },
        "subnetIDs": {
            "description": "Array of IDs of the subnets that the VM is connected to",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "list",
            "subtype": "string",
            "uniqueScope": "no"
        },
        "userID": {
            "description": "ID of the user that created this VM",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        },
        "userName": {
            "description": "Username of the user that created this VM",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "zoneIDs": {
            "description": "Array of IDs of the zone that this VM is attached to",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "list",
            "subtype": "string",
            "uniqueScope": "no"
        }
    },
    "children": {
        "alarm": {
            "get": true,
            "relationship": "child"
        },
        "eventlog": {
            "get": true,
            "relationship": "child"
        },
        "resync": {
            "create": true,
            "get": true,
            "relationship": "child"
        },
        "vminterface": {
            "create": true,
            "get": true,
            "relationship": "child"
        },
        "vrs": {
            "get": true,
            "relationship": "child"
        }
    },
    "model": {
        "description": "Read only API that can retrieve the VMs associated with a domain, zone or subnet for mediation created VM's for REST created  VM's you need to set the additional proxy user header in http request : X-Nuage-ProxyUservalue of the header has to be either :1) enterpriseName@UserName (example : Alcatel Lucent@bob), or 2) external ID of user in VSD, typically is UUID generally decided by the CMS tool in questionUser needs to have CMS privileges to use proxy user header",
        "entity_name": "VM",
        "extends": [
            "@base",
            "@audited",
            "@metadata"
        ],
        "get": true,
        "delete": true,
        "package": "vm",
        "resource_name": "vms",
        "rest_name": "vm",
        "update": true
    }
}