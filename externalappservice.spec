{
    "attributes": {
        "associatedServiceEgressGroupID": {
            "description": "ID of service port group identifying the output ports", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "associatedServiceEgressRedirectID": {
            "description": "the redirect target ID that identifies the output ports", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "associatedServiceIngressGroupID": {
            "description": "ID of service port group identifying the input ports", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "associatedServiceIngressRedirectID": {
            "description": "the redirect target ID that identifies the input ports", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "description": {
            "description": "Description of the flow.", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "destinationNATAddress": {
            "description": "Destination NAT Address", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "destinationNATEnabled": {
            "description": "Boolean flag to indicate whether source NAT is enabled", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "boolean", 
            "uniqueScope": "no"
        }, 
        "destinationNATMask": {
            "description": "netmask of the Destination NAT", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "egressType": {
            "allowed_choices": [
                "ROUTE", 
                "REDIRECT"
            ], 
            "description": "Egress type: ROUTE / REDIRECT Possible values are ROUTE, REDIRECT, .", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "enum", 
            "uniqueScope": "no"
        }, 
        "ingressType": {
            "allowed_choices": [
                "ROUTE", 
                "REDIRECT"
            ], 
            "description": "Ingress type: ROUTE / REDIRECT Possible values are ROUTE, REDIRECT, .", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "enum", 
            "uniqueScope": "no"
        }, 
        "metadata": {
            "description": "metadata", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "name": {
            "description": "Name of the flow.", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "required": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "sourceNATAddress": {
            "description": "Source NAT Address", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "sourceNATEnabled": {
            "description": "Boolean flag to indicate whether source NAT is enabled", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "boolean", 
            "uniqueScope": "no"
        }, 
        "virtualIP": {
            "description": "Virtual IP Address", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "virtualIPRequired": {
            "description": "Boolean flag to indicate whether we require a VIP", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "boolean", 
            "uniqueScope": "no"
        }
    }, 
    "model": {
        "delete": true, 
        "description": "Represents an External Service in the Application Designer", 
        "entity_name": "ExternalAppService", 
        "extends": [
            "@base", 
            "@metadata"
        ], 
        "get": true, 
        "package": "appd", 
        "resource_name": "externalappservices", 
        "rest_name": "externalappservice", 
        "update": true
    }
}