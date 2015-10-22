{
    "attributes": {
        "originTierID": {
            "description": "Flow origin tier id.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "destinationTierID": {
            "description": "Flow destination tier id.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "description": {
            "description": "Description of the flow.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "name": {
            "description": "Name of the flow.", 
            "format": "free", 
            "filterable": true, 
            "uniqueScope": "no", 
            "required": true, 
            "exposed": true, 
            "orderable": true, 
            "type": "string"
        }, 
        "metadata": {
            "description": "Metadata field to store flow related data.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }
    }, 
    "model": {
        "resource_name": "flows", 
        "description": "Flow represents the traffic between two different tiers.", 
        "entity_name": "Flow", 
        "package": "appd", 
        "get": true, 
        "update": true, 
        "rest_name": "flow", 
        "extends": [
            "@base", 
            "@metadata"
        ], 
        "delete": true
    }, 
    "children": {
        "flowsecuritypolicy": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }, 
        "flowforwardingpolicy": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }, 
        "eventlog": {
            "relationship": "child", 
            "get": true
        }
    }
}