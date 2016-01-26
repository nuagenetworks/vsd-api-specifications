{
    "attributes": {
        "installerID": {
            "description": "The Installer ID",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        },
        "status": {
            "allowed_choices": [
                "CERTIFICATE_SIGNED",
                "NOTIFICATION_APP_REQ_SENT",
                "INACTIVE",
                "NOTIFICATION_APP_REQ_ACK",
                "ACTIVE"
            ],
            "description": "Bootstrap status; can be, for example, Active, Inactive, or Notified. Possible values are INACTIVE, NOTIFICATION_APP_REQ_SENT, NOTIFICATION_APP_REQ_ACK, CERTIFICATE_SIGNED, ACTIVE, .",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "enum",
            "uniqueScope": "no"
        }
    },
    "model": {
        "description": "Gateway bootstrap details",
        "entity_name": "Bootstrap",
        "extends": [
            "@base",
            "@audited",
            "@metadata"
        ],
        "get": true,
        "package": "gateway",
        "resource_name": "bootstraps",
        "rest_name": "bootstrap",
        "update": true
    }
}