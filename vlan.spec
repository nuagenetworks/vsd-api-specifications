{
    "attributes": {
        "associatedEgressQOSPolicyID": {
            "description": "ID of the Egress QOS Policy associated with this Vlan.", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "description": {
            "description": "A description of the Port", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "gatewayID": {
            "description": "The Gateway associated with this  VLAN  . This is a read only attribute", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "permittedAction": {
            "allowed_choices": [
                "EXTEND", 
                "INSTANTIATE", 
                "DEPLOY", 
                "USE", 
                "READ", 
                "ALL"
            ], 
            "description": "The permitted  action to USE/EXTEND  this Gateway Possible values are USE, READ, ALL, INSTANTIATE, EXTEND, DEPLOY, .", 
            "exposed": true, 
            "type": "enum", 
            "uniqueScope": "no"
        }, 
        "readonly": {
            "description": "Determines whether this entity is read only.  Read only objects cannot be modified or deleted.", 
            "exposed": true, 
            "type": "boolean", 
            "uniqueScope": "no"
        }, 
        "restricted": {
            "description": "Determines whether this entity can be used in associations with other properties.", 
            "exposed": true, 
            "type": "boolean", 
            "uniqueScope": "no"
        }, 
        "status": {
            "allowed_choices": [
                "ORPHAN", 
                "MISMATCH", 
                "INITIALIZED", 
                "READY"
            ], 
            "description": "Status of the VLAN. Possible values are - INITIALIZED, ORPHAN, READY, MISMATCH Possible values are INITIALIZED, ORPHAN, READY, MISMATCH, .", 
            "exposed": true, 
            "type": "enum", 
            "uniqueScope": "no"
        }, 
        "templateID": {
            "description": "The ID of the template that this Port was created from", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "useUserMnemonic": {
            "description": "determines whether to use user mnemonic of the Port", 
            "exposed": true, 
            "type": "boolean", 
            "uniqueScope": "no"
        }, 
        "userMnemonic": {
            "description": "user mnemonic of the Port", 
            "exposed": true, 
            "required": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "value": {
            "description": "value of VLAN", 
            "exposed": true, 
            "required": true, 
            "type": "integer", 
            "uniqueScope": "no"
        }, 
        "vportID": {
            "description": "The Vport associated with this  VLAN  . This is a read only attribute", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }
    }, 
    "children": {
        "alarm": {
            "get": true, 
            "relationship": "child"
        }, 
        "enterprisepermission": {
            "create": true, 
            "get": true, 
            "relationship": "child"
        }, 
        "eventlog": {
            "get": true, 
            "relationship": "child"
        }, 
        "permission": {
            "create": true, 
            "get": true, 
            "relationship": "child"
        }
    }, 
    "delete": true, 
    "description": "Represents VLAN object under a given PORT object", 
    "entity_name": "VLAN", 
    "extends": [
        "@base", 
        "@metadata"
    ], 
    "get": true, 
    "package": "/gateway", 
    "resource_name": "vlans", 
    "rest_name": "vlan", 
    "update": true
}