{
    "attributes": {
        "action": {
            "description": "The flow action. The action can be either FORWARD or DROP.", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "associatedApplicationServiceID": {
            "description": "The associated service id.", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "associatedNetworkObjectID": {
            "description": "The associated network object id.", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "associatedNetworkObjectType": {
            "description": "The associated network object type. Refer to API section for supported types.", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "enum", 
            "uniqueScope": "no"
        }, 
        "destinationAddressOverwrite": {
            "description": "The destination address overwrite. Needs to be in CIDR format x.x.x.x/n", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "flowID": {
            "description": "The associated service id.", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "priority": {
            "description": "The priority of the flow security policy that determines the order of entries.", 
            "exposed": true, 
            "filterable": true, 
            "orderable": true,
            "type": "integer",
            "min_value": 0, 
            "uniqueScope": "no"
        }, 
        "sourceAddressOverwrite": {
            "description": "The source address overwrite. Needs to be in CIDR format x.x.x.x/n", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }
    }, 
    "children": {
        "eventlog": {
            "get": true, 
            "relationship": "child"
        }
    }, 
    "model": {
        "delete": true, 
        "description": "The security policy on the flow.", 
        "entity_name": "FlowSecurityPolicy", 
        "extends": [
            "@base", 
            "@metadata"
        ], 
        "get": true, 
        "package": "appd", 
        "resource_name": "flowsecuritypolicies", 
        "rest_name": "flowsecuritypolicy", 
        "update": true
    }
}
