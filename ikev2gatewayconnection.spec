{
    "attributes": {
        "NSGIdentifier": {
            "description": null, 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string"
        }, 
        "NSGIdentifierType": {
            "description": null, 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string"
        }, 
        "associatedIKEv2AuthenticationID": {
            "description": null, 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string"
        }, 
        "associatedIKEv2AuthenticationType": {
            "allowed_choices": [
                "ikev2psk", 
                "ikev2certificate"
            ], 
            "description": null, 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "enum"
        }, 
        "associatedIKEv2EncryptionProfileID": {
            "description": null, 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string"
        }, 
        "associatedIKEv2GatewayProfileID": {
            "description": null, 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string"
        }, 
        "associatedVlanID": {
            "description": null, 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string"
        }, 
        "name": {
            "description": null, 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string"
        }, 
        "portVlanName": {
            "description": null, 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string"
        }, 
        "priority": {
            "description": null, 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string"
        }, 
        "unencryptedPSK": {
            "description": null, 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string"
        }
    }, 
    "model": {
        "delete": true, 
        "entity_name": "IKEv2GatewayConnection", 
        "extends": [
            "@base", 
            "@metadata"
        ], 
        "get": true, 
        "resource_name": "ikev2gatewayconnections", 
        "rest_name": "ikev2gatewayconnection", 
        "update": true
    }
}