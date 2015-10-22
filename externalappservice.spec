{
    "attributes": {
        "sourceNATAddress": {
            "description": "Source NAT Address", 
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
        "egressType": {
            "description": "Egress type: ROUTE / REDIRECT Possible values are ROUTE, REDIRECT, .", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "allowed_choices": [
                "ROUTE", 
                "REDIRECT"
            ], 
            "orderable": true, 
            "type": "enum"
        }, 
        "associatedServiceEgressRedirectID": {
            "description": "the redirect target ID that identifies the output ports", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "destinationNATEnabled": {
            "description": "Boolean flag to indicate whether source NAT is enabled", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "boolean"
        }, 
        "destinationNATAddress": {
            "description": "Destination NAT Address", 
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
        "virtualIPRequired": {
            "description": "Boolean flag to indicate whether we require a VIP", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "boolean"
        }, 
        "associatedServiceIngressGroupID": {
            "description": "ID of service port group identifying the input ports", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "sourceNATEnabled": {
            "description": "Boolean flag to indicate whether source NAT is enabled", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "boolean"
        }, 
        "ingressType": {
            "description": "Ingress type: ROUTE / REDIRECT Possible values are ROUTE, REDIRECT, .", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "allowed_choices": [
                "ROUTE", 
                "REDIRECT"
            ], 
            "orderable": true, 
            "type": "enum"
        }, 
        "associatedServiceIngressRedirectID": {
            "description": "the redirect target ID that identifies the input ports", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "destinationNATMask": {
            "description": "netmask of the Destination NAT", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "virtualIP": {
            "description": "Virtual IP Address", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "associatedServiceEgressGroupID": {
            "description": "ID of service port group identifying the output ports", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "metadata": {
            "description": "metadata", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }
    }, 
    "model": {
        "resource_name": "externalappservices", 
        "description": "Represents an External Service in the Application Designer", 
        "entity_name": "ExternalAppService", 
        "package": "appd", 
        "get": true, 
        "update": true, 
        "rest_name": "externalappservice", 
        "extends": [
            "@base", 
            "@metadata"
        ], 
        "delete": true
    }
}