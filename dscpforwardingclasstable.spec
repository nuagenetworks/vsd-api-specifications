{
    "attributes": {
        "description": {
            "description": "A description of the dscp-fc mapping table.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "name": {
            "description": "A unique name of the dscp-fc mapping table.", 
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
        "resource_name": "dscpforwardingclasstables", 
        "description": "Provides the definition of a table that holds multiple DSCP -> Forwarding class mappings. Used in QoS policies.", 
        "entity_name": "DSCPForwardingClassTable", 
        "package": "policy", 
        "get": true, 
        "update": true, 
        "rest_name": "dscpforwardingclasstable", 
        "extends": [
            "@base", 
            "@metadata"
        ], 
        "delete": true
    }, 
    "children": {
        "dscpforwardingclassmapping": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }
    }
}