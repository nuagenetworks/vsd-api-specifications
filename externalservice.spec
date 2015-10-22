{
    "attributes": {
        "serviceType": {
            "required": true, 
            "description": "Type of the SERVICE -  L3,L2 Possible values are L3, L2, .", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "allowed_choices": [
                "L2", 
                "L3"
            ], 
            "orderable": true, 
            "type": "enum"
        }, 
        "direction": {
            "description": "Direction -  INGRESS Possible values are INGRESS, .", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "allowed_choices": [
                "INGRESS"
            ], 
            "orderable": true, 
            "type": "enum"
        }, 
        "stage": {
            "description": "Stage -  START,END Possible values are START, .", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "allowed_choices": [
                "START"
            ], 
            "orderable": true, 
            "type": "enum"
        }, 
        "description": {
            "description": "Description of the External Service.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "name": {
            "description": "unique name of the External Service. ", 
            "format": "free", 
            "filterable": true, 
            "uniqueScope": "no", 
            "required": true, 
            "exposed": true, 
            "orderable": true, 
            "type": "string"
        }
    }, 
    "model": {
        "resource_name": "externalservices", 
        "description": "Representation of External Service", 
        "entity_name": "ExternalService", 
        "package": "policy", 
        "get": true, 
        "update": true, 
        "rest_name": "externalservice", 
        "extends": [
            "@base", 
            "@metadata"
        ], 
        "delete": true
    }, 
    "children": {
        "metadatatag": {
            "relationship": "child", 
            "get": true
        }, 
        "endpoint": {
            "relationship": "child", 
            "get": true
        }, 
        "eventlog": {
            "relationship": "child", 
            "get": true
        }
    }
}