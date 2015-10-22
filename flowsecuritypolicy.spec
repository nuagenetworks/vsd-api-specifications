{
    "attributes": {
        "associatedNetworkObjectType": {
            "description": "The associated network object type. Refer to API section for supported types.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "enum"
        }, 
        "associatedApplicationServiceID": {
            "description": "The associated service id.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "associatedNetworkObjectID": {
            "description": "The associated network object id.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "priority": {
            "description": "The priority of the flow security policy that determines the order of entries.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "integer"
        }, 
        "flowID": {
            "description": "The associated service id.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "action": {
            "description": "The flow action. The action can be either FORWARD or DROP.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "destinationAddressOverwrite": {
            "description": "The destination address overwrite. Needs to be in CIDR format x.x.x.x/n", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "sourceAddressOverwrite": {
            "description": "The source address overwrite. Needs to be in CIDR format x.x.x.x/n", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }
    }, 
    "model": {
        "resource_name": "flowsecuritypolicies", 
        "description": "The security policy on the flow.", 
        "entity_name": "FlowSecurityPolicy", 
        "package": "appd", 
        "get": true, 
        "update": true, 
        "rest_name": "flowsecuritypolicy", 
        "extends": [
            "@base", 
            "@metadata"
        ], 
        "delete": true
    }, 
    "children": {
        "eventlog": {
            "relationship": "child", 
            "get": true
        }
    }
}