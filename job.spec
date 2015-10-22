{
    "attributes": {
        "assocEntityType": {
            "description": "Entity with which this job is associated Refer to API section for supported types.", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "enum", 
            "uniqueScope": "no"
        }, 
        "command": {
            "allowed_choices": [
                "NSG_NOTIFICATION_TEST", 
                "DISCARD_POLICY_CHANGES", 
                "VCENTER_RELOAD", 
                "IMPORT", 
                "NOTIFY_NSG_REGISTRATION_TEST", 
                "GATEWAY_AUDIT", 
                "CERTIFICATE_NSG_RENEW", 
                "APPLY_POLICY_CHANGES", 
                "NOTIFY_NSG_REGISTRATION", 
                "NSG_REGISTRATION_INFO", 
                "FORCE_KEYSERVER_UPDATE_ACK", 
                "BATCH_CRUD_REQUEST", 
                "NOTIFY_NSG_REGISTRATION_ACK", 
                "RELOAD_GEO_REDUNDANT_INFO", 
                "FORCE_KEYSERVER_VSD_RESYNC", 
                "RELOAD_NSG_CONFIG", 
                "EXPORT", 
                "FORCE_KEYSERVER_UPDATE", 
                "CERTIFICATE_NSG_REVOKE", 
                "RELOAD", 
                "KEYSERVER_NOTIFICATION_TEST", 
                "BEGIN_POLICY_CHANGES"
            ], 
            "description": "Name of the command. Possible values are GATEWAY_AUDIT, NOTIFY_NSG_REGISTRATION, NOTIFY_NSG_REGISTRATION_ACK, CERTIFICATE_NSG_REVOKE, CERTIFICATE_NSG_RENEW, RELOAD_NSG_CONFIG, RELOAD, EXPORT, IMPORT, BEGIN_POLICY_CHANGES, DISCARD_POLICY_CHANGES, APPLY_POLICY_CHANGES, RELOAD_GEO_REDUNDANT_INFO, FORCE_KEYSERVER_UPDATE, FORCE_KEYSERVER_UPDATE_ACK, FORCE_KEYSERVER_VSD_RESYNC, NSG_NOTIFICATION_TEST, KEYSERVER_NOTIFICATION_TEST, NOTIFY_NSG_REGISTRATION_TEST, BATCH_CRUD_REQUEST, VCENTER_RELOAD, NSG_REGISTRATION_INFO, .", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "required": true, 
            "type": "enum", 
            "uniqueScope": "no"
        }, 
        "parameters": {
            "description": "Additional arguments required for the specific command. Differs based on types of command.", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "object", 
            "uniqueScope": "no"
        }, 
        "progress": {
            "description": "Indicates the progress of the job as a faction. eg : 0.5 means 50% done.", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "float", 
            "uniqueScope": "no"
        }, 
        "result": {
            "description": "Results from the execution of the job", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "object", 
            "uniqueScope": "no"
        }, 
        "status": {
            "allowed_choices": [
                "SUCCESS", 
                "RUNNING", 
                "FAILED"
            ], 
            "description": "Current status of the job. Possible values are RUNNING, FAILED, SUCCESS, .", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "enum", 
            "uniqueScope": "no"
        }
    }, 
    "model": {
        "delete": true, 
        "description": "Represents JOB entity. The job API accepts a command and parameters and executes the job and returns the results. Jobs API are typically used for long running tasks.", 
        "entity_name": "Job", 
        "extends": [
            "@base", 
            "@metadata"
        ], 
        "get": true, 
        "package": "job", 
        "resource_name": "jobs", 
        "rest_name": "job", 
        "update": true
    }
}