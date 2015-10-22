{
    "attributes": {
        "VLANRange": {
            "description": "VLAN Range of the Port.  Format must conform to a-b,c,d-f where a,b,c,d,f are integers between 0 and 4095.", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
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
        "infrastructureProfileID": {
            "description": "The ID of the infrastructure profile this instance is associated with.", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "name": {
            "description": "Name of the Port", 
            "exposed": true, 
            "required": true, 
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
        "physicalName": {
            "description": "Identifier of the Port", 
            "exposed": true, 
            "required": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "portPeer1ID": {
            "description": "The master gateway peer port id.", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "portPeer2ID": {
            "description": "The slave gateway peer port id.", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "portType": {
            "allowed_choices": [
                "ACCESS", 
                "NETWORK"
            ], 
            "description": "Type of the Port - NETWORK, ACCESS Possible values are ACCESS, NETWORK, .", 
            "exposed": true, 
            "required": true, 
            "type": "enum", 
            "uniqueScope": "no"
        }, 
        "status": {
            "allowed_choices": [
                "ORPHAN", 
                "MISMATCH", 
                "INITIALIZED", 
                "READY"
            ], 
            "description": "Status of the port. Possible values are - INITIALIZED, ORPHAN, READY, MISMATCH Possible values are INITIALIZED, ORPHAN, READY, MISMATCH, .", 
            "exposed": true, 
            "type": "enum", 
            "uniqueScope": "no"
        }, 
        "useUntaggedHeartbeatVlan": {
            "description": "A flag to indicate if for this redundant port an untagged heartbeat VLAN is to be used. If this is not set then will use the heartbeat VLAN set by the NS redundant group", 
            "exposed": true, 
            "type": "boolean", 
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
            "type": "string", 
            "uniqueScope": "no"
        }
    }, 
    "children": {
        "nsport": {
            "create": true, 
            "get": true, 
            "relationship": "child"
        }, 
        "vlan": {
            "create": true, 
            "get": true, 
            "relationship": "child"
        }
    }, 
    "delete": true, 
    "description": "Represents Port under a particular gateway object or redundant group object.", 
    "entity_name": "RedundantPort", 
    "extends": [
        "@base", 
        "@metadata"
    ], 
    "get": true, 
    "package": "/gateway", 
    "resource_name": "nsredundantports", 
    "rest_name": "nsredundantport", 
    "update": true
}