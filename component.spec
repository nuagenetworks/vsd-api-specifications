{
    "attributes": {
        "status": {
            "description": "Current status of the entity. Possible values are UP, DOWN, ADMIN_DOWN, .", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "allowed_choices": [
                "DOWN", 
                "UP", 
                "ADMIN_DOWN"
            ], 
            "orderable": true, 
            "type": "enum"
        }, 
        "description": {
            "description": "Description of the entity.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "managementIP": {
            "description": "An optional management IP to log into this component.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "name": {
            "description": "Identifies the entity with a name.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "productVersion": {
            "description": "Product version supported by this entity.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "address": {
            "description": "An optional IP to access this component.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "type": {
            "description": "Type of the component Possible values are JBOSS, MEDIATOR, PERCONA, EJABBERD, TCA, STATSCOLLECTOR, STATSSERVER, .", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "allowed_choices": [
                "STATSCOLLECTOR", 
                "EJABBERD", 
                "PERCONA", 
                "MEDIATOR", 
                "STATSSERVER", 
                "TCA", 
                "JBOSS"
            ], 
            "orderable": true, 
            "type": "enum"
        }, 
        "location": {
            "description": "Identifies the entity to be associated with a location.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }
    }, 
    "model": {
        "resource_name": "components", 
        "description": "System Monitoring details for components of VSD system", 
        "entity_name": "VSDComponent", 
        "package": "sysmon", 
        "rest_name": "component", 
        "extends": [
            "@base", 
            "@metadata"
        ]
    }
}