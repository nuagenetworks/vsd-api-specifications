{
    "attributes": {
        "installerID": {
            "description": "The Installer ID",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "status": {
            "allowed_choices": [
                "ACTIVE",
                "CERTIFICATE_SIGNED",
                "INACTIVE",
                "NOTIFICATION_APP_REQ_ACK",
                "NOTIFICATION_APP_REQ_SENT"
            ],
            "description": "Bootstrap status; can be, for example, Active, Inactive, or Notified. Possible values are INACTIVE, NOTIFICATION_APP_REQ_SENT, NOTIFICATION_APP_REQ_ACK, CERTIFICATE_SIGNED, ACTIVE, .",
            "exposed": true,
            "format": "free",
            "type": "enum",
            "uniqueScope": "no"
        }
    },
    "model": {
        "description": "Gateway bootstrap details.",
        "entity_name": "Bootstrap",
        "extends": [
            "@audited",
            "@base",
            "@metadata"
        ],
        "get": true,
        "package": "gateway",
        "resource_name": "bootstraps",
        "rest_name": "bootstrap",
        "update": true
    }
}