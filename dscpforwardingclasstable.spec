{
    "attributes": {
        "description": {
            "description": "A description of the dscp-fc mapping table.", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "name": {
            "description": "A unique name of the dscp-fc mapping table.", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "required": true, 
            "type": "string", 
            "min_length": 1,
            "max_length": 255,
            "uniqueScope": "no"
        }
    }, 
    "children": {
        "dscpforwardingclassmapping": {
            "create": true, 
            "get": true, 
            "relationship": "child"
        }
    }, 
    "model": {
        "delete": true, 
        "description": "Provides the definition of a table that holds multiple DSCP -> Forwarding class mappings. Used in QoS policies.", 
        "entity_name": "DSCPForwardingClassTable", 
        "extends": [
            "@base", 
            "@metadata"
        ], 
        "get": true, 
        "package": "policy", 
        "resource_name": "dscpforwardingclasstables", 
        "rest_name": "dscpforwardingclasstable", 
        "update": true
    }
}