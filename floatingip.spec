{
    "apis": {
        "children": {
            "/floatingips/{id}/eventlogs": {
                "RESTName": "eventlog", 
                "operations": [
                    {
                        "availability": null, 
                        "method": "GET"
                    }
                ], 
                "resourceName": "eventlogs"
            }, 
            "/floatingips/{id}/vports": {
                "RESTName": "vport", 
                "operations": [
                    {
                        "availability": null, 
                        "method": "GET"
                    }
                ], 
                "resourceName": "vports"
            }
        }, 
        "parents": {
            "/domains/{id}/floatingips": {
                "RESTName": "domain", 
                "operations": [
                    {
                        "availability": null, 
                        "method": "GET"
                    }, 
                    {
                        "availability": null, 
                        "method": "POST"
                    }
                ], 
                "resourceName": "domains"
            }, 
            "/floatingips": {
                "RESTName": "floatingip", 
                "operations": [
                    {
                        "availability": null, 
                        "method": "GET"
                    }
                ], 
                "resourceName": "floatingips"
            }
        }, 
        "self": {
            "/floatingips/{id}": {
                "RESTName": "floatingip", 
                "operations": [
                    {
                        "availability": null, 
                        "method": "DELETE"
                    }, 
                    {
                        "availability": null, 
                        "method": "GET"
                    }
                ], 
                "resourceName": "floatingips"
            }
        }
    }, 
    "metadata": {
        "api_version": "3.2", 
        "author": "", 
        "comments": "", 
        "date": "05-15-2015", 
        "dev_backend": "", 
        "dev_frontend": "", 
        "dev_qd": "", 
        "plm": "", 
        "prd_url": "http://", 
        "revisions": []
    }, 
    "model": {
        "RESTName": "floatingip", 
        "attributes": {
            "address": {
                "allowedChars": null, 
                "allowedChoices": null, 
                "autogenerated": false, 
                "availability": null, 
                "creationOnly": false, 
                "defaultOrder": false, 
                "defaultValue": null, 
                "description": "Floating IP address assigned to the Domain", 
                "filterable": false, 
                "format": null, 
                "maxLength": null, 
                "maxValue": null, 
                "minLength": null, 
                "minValue": null, 
                "orderable": false, 
                "readonly": false, 
                "required": false, 
                "type": "string", 
                "uniqueItems": false
            }, 
            "assigned": {
                "allowedChars": null, 
                "allowedChoices": null, 
                "autogenerated": false, 
                "availability": null, 
                "creationOnly": false, 
                "defaultOrder": false, 
                "defaultValue": null, 
                "description": "True if this floating IP is assigned to a network interface else the value is false", 
                "filterable": false, 
                "format": null, 
                "maxLength": null, 
                "maxValue": null, 
                "minLength": null, 
                "minValue": null, 
                "orderable": false, 
                "readonly": false, 
                "required": false, 
                "type": "boolean", 
                "uniqueItems": false
            }, 
            "associatedSharedNetworkResourceID": {
                "allowedChars": null, 
                "allowedChoices": null, 
                "autogenerated": false, 
                "availability": null, 
                "creationOnly": false, 
                "defaultOrder": false, 
                "defaultValue": null, 
                "description": "Id of the shared network resource subnet which was used to get this floating IP address", 
                "filterable": false, 
                "format": null, 
                "maxLength": null, 
                "maxValue": null, 
                "minLength": null, 
                "minValue": null, 
                "orderable": false, 
                "readonly": false, 
                "required": true, 
                "type": "string", 
                "uniqueItems": false
            }
        }, 
        "description": "Floating IP that is associated to a Domain. This floating IP could be used in the VM interface for NAT functionality", 
        "entityName": "FloatingIp", 
        "package": "/network", 
        "resourceName": "floatingips"
    }
}