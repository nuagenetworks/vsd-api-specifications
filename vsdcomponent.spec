{
    "attributes": {
        "address": {
            "description": "An optional IP to access this component.", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "description": {
            "description": "Description of the entity.", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "location": {
            "description": "Identifies the entity to be associated with a location.", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "managementIP": {
            "description": "An optional management IP to log into this component.", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "name": {
            "description": "Identifies the entity with a name.", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "productVersion": {
            "description": "Product version supported by this entity.", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "status": {
            "allowed_choices": [
                "DOWN", 
                "UP", 
                "ADMIN_DOWN"
            ], 
            "description": "Current status of the entity. Possible values are UP, DOWN, ADMIN_DOWN, .", 
            "exposed": true, 
            "type": "enum", 
            "uniqueScope": "no"
        }, 
        "type": {
            "allowed_choices": [
                "STATSCOLLECTOR", 
                "EJABBERD", 
                "PERCONA", 
                "MEDIATOR", 
                "STATSSERVER", 
                "TCA", 
                "JBOSS"
            ], 
            "description": "Type of the component Possible values are JBOSS, MEDIATOR, PERCONA, EJABBERD, TCA, STATSCOLLECTOR, STATSSERVER, .", 
            "exposed": true, 
            "type": "enum", 
            "uniqueScope": "no"
        }
    }, 
    "description": "System Monitoring details for components of VSD system", 
    "entity_name": "VSDComponent", 
    "extends": [
        "@base", 
        "@metadata"
    ], 
    "package": "/sysmon", 
    "resource_name": "components", 
    "rest_name": "component"
}