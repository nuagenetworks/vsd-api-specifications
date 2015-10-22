{
    "attributes": {
        "redundancyEnabled": {
            "description": "Allow/Disallow redundant appliances and VIP", 
            "format": "free", 
            "filterable": true, 
            "uniqueScope": "no", 
            "required": true, 
            "exposed": true, 
            "orderable": true, 
            "type": "boolean"
        }, 
        "triggerType": {
            "description": "Trigger type, could be NONE/GARP - THIS IS READONNLY", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "description": {
            "description": "Description of this redirection target template", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "name": {
            "description": "Name of this redirection target template", 
            "format": "free", 
            "filterable": true, 
            "uniqueScope": "no", 
            "required": true, 
            "exposed": true, 
            "orderable": true, 
            "type": "string"
        }, 
        "endPointType": {
            "description": "VPortTagEndPointType is an enum. It defines the type of header rewrite and forwarding performed by VRS when the endpoint is used as a PBR destination. Possible values are NONE, L3, VIRTUAL_WIRE.", 
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
        "resource_name": "redirectiontargettemplates", 
        "description": "Template for a vporttag. Can be created only at the template level and available for all instances.", 
        "entity_name": "RedirectionTargetTemplate", 
        "package": "vport", 
        "get": true, 
        "update": true, 
        "rest_name": "redirectiontargettemplate", 
        "extends": [
            "@base", 
            "@metadata"
        ], 
        "delete": true
    }, 
    "children": {
        "job": {
            "create": true, 
            "relationship": "child"
        }, 
        "eventlog": {
            "relationship": "child", 
            "get": true
        }
    }
}