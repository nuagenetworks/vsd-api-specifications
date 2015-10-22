{
    "attributes": {
        "status": {
            "description": "Bootstrap status; can be, for example, Active, Inactive, or Notified. Possible values are INACTIVE, NOTIFICATION_APP_REQ_SENT, NOTIFICATION_APP_REQ_ACK, CERTIFICATE_SIGNED, ACTIVE, .", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "allowed_choices": [
                "CERTIFICATE_SIGNED", 
                "NOTIFICATION_APP_REQ_SENT", 
                "INACTIVE", 
                "NOTIFICATION_APP_REQ_ACK", 
                "ACTIVE"
            ], 
            "orderable": true, 
            "type": "enum"
        }, 
        "installerID": {
            "description": "The Installer ID", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }
    }, 
    "model": {
        "resource_name": "bootstraps", 
        "description": "Gateway bootstrap details", 
        "entity_name": "Bootstrap", 
        "package": "gateway", 
        "get": true, 
        "update": true, 
        "rest_name": "bootstrap", 
        "extends": [
            "@base", 
            "@metadata"
        ]
    }
}