{
    "attributes": [
        {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "Entity with which this job is associated Refer to API section for supported types.",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "assocEntityType",
            "orderable": false,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "string",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Assoc Entity Type"
        },
        {
            "allowed_chars": null,
            "allowed_choices": [
                "APPLICATION_SIGNATURE_IMPORT",
                "APPLY_POLICY_CHANGES",
                "ASSIGN_SELF_REBOOTSTRAP_REQ",
                "BATCH_CRUD_REQUEST",
                "BEGIN_POLICY_CHANGES",
                "CERTIFICATE_NSG_RENEW",
                "CERTIFICATE_NSG_REVOKE",
                "CLEAR_IPSEC_DATA",
                "CLEAR_MAC_MOVE_ALARMS",
                "CLOUD_FORCE_CONFIG",
                "CLOUD_SYNC",
                "DEPLOY",
                "DISCARD_POLICY_CHANGES",
                "EXPORT",
                "FORCE_KEYSERVER_UPDATE",
                "FORCE_KEYSERVER_UPDATE_ACK",
                "FORCE_KEYSERVER_VSD_RESYNC",
                "GATEWAY_AUDIT",
                "GET_ZFB_INFO",
                "IMPORT",
                "KEYSERVER_NOTIFICATION_TEST",
                "NETCONF_FORCE_DEPLOY",
                "NETCONF_SYNC",
                "NOTIFY_NSG_REGISTRATION",
                "NOTIFY_NSG_REGISTRATION_ACK",
                "NOTIFY_NSG_REGISTRATION_TEST",
                "NSG_LIFT_QUARANTINE",
                "NSG_NOTIFICATION_TEST",
                "NSG_QUARANTINE",
                "NSG_REGISTRATION_INFO",
                "PUBSUBNODE_AUDIT",
                "RECOVER_NSG",
                "REDEPLOY",
                "REJECT_ZFB_REQUEST",
                "RELOAD",
                "RELOAD_GEO_REDUNDANT_INFO",
                "RELOAD_NSG_CONFIG",
                "RESTART",
                "RETRIEVE_ACTIVE_NSGS",
                "SAAS_APPLICATION_TYPE",
                "START",
                "STATUS",
                "STOP",
                "SYNC",
                "UNDEPLOY",
                "VCENTER_ADD_COMPUTERESOURCE_INSCOPE",
                "VCENTER_DELETE_AGENCY",
                "VCENTER_MARK_AGENT_VM_AVAILABLE",
                "VCENTER_RECONNECT",
                "VCENTER_RELOAD",
                "VCENTER_REMOVE_COMPUTERESOURCE_INSCOPE",
                "VCENTER_SCRIPT_UPGRADE_VRS",
                "VCENTER_SYNC",
                "VCENTER_UPGRADE_VRS"
            ],
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": true,
            "default_value": null,
            "deprecated": false,
            "description": "Name of the command.",
            "exposed": true,
            "filterable": true,
            "format": null,
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "command",
            "orderable": true,
            "read_only": false,
            "required": true,
            "subtype": null,
            "transient": false,
            "type": "enum",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Command"
        },
        {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "Additional arguments required for the specific command. Differs based on types of command.",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "parameters",
            "orderable": false,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "object",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Parameters"
        },
        {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "Indicates the progress of the job as a faction. eg : 0.5 means 50% done.",
            "exposed": true,
            "filterable": false,
            "format": null,
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "progress",
            "orderable": false,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "float",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Progress"
        },
        {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "Results from the execution of the job",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "result",
            "orderable": false,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "object",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Result"
        },
        {
            "allowed_chars": null,
            "allowed_choices": [
                "FAILED",
                "RUNNING",
                "SUCCESS"
            ],
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "Current status of the job. Possible values are RUNNING, FAILED, SUCCESS, .",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "status",
            "orderable": false,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "enum",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Status"
        }
    ],
    "children": [],
    "model": {
        "allowed_job_commands": null,
        "create": false,
        "delete": true,
        "description": "Represents JOB entity. The job API accepts a command and parameters and executes the job and returns the results. Jobs API are typically used for long running tasks.",
        "entity_name": "Job",
        "extends": [
            "@audited",
            "@base",
            "@metadata"
        ],
        "get": true,
        "package": "job",
        "resource_name": "jobs",
        "rest_name": "job",
        "root": false,
        "template": false,
        "update": true,
        "userlabel": "Job"
    }
}