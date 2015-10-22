{
    "attributes": {
        "associatedApplicationID": {
            "description": "The associated network macro ID.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "associatedNetworkMacroID": {
            "description": "The associated network macro ID.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "associatedFloatingIPPoolID": {
            "description": "The associated floating IP Pool ID.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "description": {
            "description": "Description of the application tier.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "associatedNetworkObjectType": {
            "description": "The associated network object type. Refer to API section for supported types.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "enum"
        }, 
        "name": {
            "description": "Name of the application tier.", 
            "format": "free", 
            "filterable": true, 
            "uniqueScope": "no", 
            "required": true, 
            "exposed": true, 
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
        "netmask": {
            "description": "Netmask for the tier.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "address": {
            "description": "IP address of the tier defined.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "type": {
            "required": true, 
            "description": "Type of the application tier. (Example: STANDARD, NETWORK_MACRO, APPLICATION or APPLICATION_EXTENDED_NETWORK Possible values are STANDARD, NETWORK_MACRO, APPLICATION, APPLICATION_EXTENDED_NETWORK, .", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "allowed_choices": [
                "NETWORK_MACRO", 
                "APPLICATION", 
                "STANDARD", 
                "APPLICATION_EXTENDED_NETWORK"
            ], 
            "orderable": true, 
            "type": "enum"
        }, 
        "gateway": {
            "description": "The IP address of the gateway for this tier.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "metadata": {
            "description": "Metadata field to store tier related data.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }
    }, 
    "model": {
        "resource_name": "tiers", 
        "description": "Tier represents a portion of an application.", 
        "entity_name": "Tier", 
        "package": "appd", 
        "get": true, 
        "update": true, 
        "rest_name": "tier", 
        "extends": [
            "@base", 
            "@metadata"
        ], 
        "delete": true
    }, 
    "children": {
        "statistics": {
            "relationship": "child", 
            "get": true
        }, 
        "eventlog": {
            "relationship": "child", 
            "get": true
        }, 
        "vm": {
            "relationship": "child", 
            "get": true
        }, 
        "vport": {
            "update": true, 
            "relationship": "child", 
            "get": true
        }, 
        "statisticspolicy": {
            "relationship": "child", 
            "get": true
        }, 
        "tca": {
            "relationship": "child", 
            "get": true
        }
    }
}