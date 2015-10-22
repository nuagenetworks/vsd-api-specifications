{
    "attributes": {
        "infrastructureProfileID": {
            "description": "The ID of the infrastructure profile this instance is associated with.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "status": {
            "description": "Status of the port. Possible values are - INITIALIZED, ORPHAN, READY, MISMATCH Possible values are INITIALIZED, ORPHAN, READY, MISMATCH, .", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "allowed_choices": [
                "ORPHAN", 
                "MISMATCH", 
                "INITIALIZED", 
                "READY"
            ], 
            "orderable": true, 
            "type": "enum"
        }, 
        "description": {
            "description": "A description of the Port", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "portPeer2ID": {
            "description": "The slave gateway peer port id.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "useUserMnemonic": {
            "description": "determines whether to use user mnemonic of the Port", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "boolean"
        }, 
        "physicalName": {
            "description": "Identifier of the Port", 
            "format": "free", 
            "filterable": true, 
            "uniqueScope": "no", 
            "required": true, 
            "exposed": true, 
            "orderable": true, 
            "type": "string"
        }, 
        "useUntaggedHeartbeatVlan": {
            "description": "A flag to indicate if for this redundant port an untagged heartbeat VLAN is to be used. If this is not set then will use the heartbeat VLAN set by the NS redundant group", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "boolean"
        }, 
        "userMnemonic": {
            "description": "user mnemonic of the Port", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "permittedAction": {
            "description": "The permitted  action to USE/EXTEND  this Gateway Possible values are USE, READ, ALL, INSTANTIATE, EXTEND, DEPLOY, .", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "allowed_choices": [
                "EXTEND", 
                "INSTANTIATE", 
                "DEPLOY", 
                "USE", 
                "READ", 
                "ALL"
            ], 
            "orderable": true, 
            "type": "enum"
        }, 
        "VLANRange": {
            "description": "VLAN Range of the Port.  Format must conform to a-b,c,d-f where a,b,c,d,f are integers between 0 and 4095.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "associatedEgressQOSPolicyID": {
            "description": "ID of the Egress QOS Policy associated with this Vlan.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "portType": {
            "required": true, 
            "description": "Type of the Port - NETWORK, ACCESS Possible values are ACCESS, NETWORK, .", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "allowed_choices": [
                "ACCESS", 
                "NETWORK"
            ], 
            "orderable": true, 
            "type": "enum"
        }, 
        "portPeer1ID": {
            "description": "The master gateway peer port id.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "name": {
            "description": "Name of the Port", 
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
        "resource_name": "nsredundantports", 
        "description": "Represents Port under a particular gateway object or redundant group object.", 
        "entity_name": "RedundantPort", 
        "package": "gateway", 
        "get": true, 
        "update": true, 
        "rest_name": "nsredundantport", 
        "extends": [
            "@base", 
            "@metadata"
        ], 
        "delete": true
    }, 
    "children": {
        "nsport": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }, 
        "vlan": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }
    }
}