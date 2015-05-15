{
    "apis": {
        "children": {
            "/gateways/{id}/alarms": {
                "RESTName": "alarm", 
                "operations": [
                    {
                        "availability": null, 
                        "method": "GET"
                    }
                ], 
                "resourceName": "alarms"
            }, 
            "/gateways/{id}/enterprisepermissions": {
                "RESTName": "enterprisepermission", 
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
                "resourceName": "enterprisepermissions"
            }, 
            "/gateways/{id}/eventlogs": {
                "RESTName": "eventlog", 
                "operations": [
                    {
                        "availability": null, 
                        "method": "GET"
                    }
                ], 
                "resourceName": "eventlogs"
            }, 
            "/gateways/{id}/jobs": {
                "RESTName": "job", 
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
                "resourceName": "jobs"
            }, 
            "/gateways/{id}/patnatpools": {
                "RESTName": "patnatpool", 
                "operations": [
                    {
                        "availability": null, 
                        "method": "GET"
                    }, 
                    {
                        "availability": null, 
                        "method": "PUT"
                    }
                ], 
                "resourceName": "patnatpools"
            }, 
            "/gateways/{id}/permissions": {
                "RESTName": "permission", 
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
                "resourceName": "permissions"
            }, 
            "/gateways/{id}/ports": {
                "RESTName": "port", 
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
                "resourceName": "ports"
            }, 
            "/gateways/{id}/services": {
                "RESTName": "service", 
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
                "resourceName": "services"
            }
        }, 
        "parents": {
            "/enterprises/{id}/gateways": {
                "RESTName": "enterprise", 
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
                "resourceName": "enterprises"
            }, 
            "/gateways": {
                "RESTName": "gateway", 
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
                "resourceName": "gateways"
            }, 
            "/redundancygroups/{id}/gateways": {
                "RESTName": "redundancygroup", 
                "operations": [
                    {
                        "availability": null, 
                        "method": "GET"
                    }, 
                    {
                        "availability": null, 
                        "method": "PUT"
                    }
                ], 
                "resourceName": "redundancygroups"
            }
        }, 
        "self": {
            "/gateways/{id}": {
                "RESTName": "gateway", 
                "operations": [
                    {
                        "availability": null, 
                        "method": "PUT"
                    }, 
                    {
                        "availability": null, 
                        "method": "DELETE"
                    }, 
                    {
                        "availability": null, 
                        "method": "GET"
                    }
                ], 
                "resourceName": "gateways"
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
        "RESTName": "gateway", 
        "attributes": {
            "autoDiscGatewayID": {
                "allowedChars": null, 
                "allowedChoices": null, 
                "autogenerated": false, 
                "availability": null, 
                "creationOnly": false, 
                "defaultOrder": false, 
                "defaultValue": null, 
                "description": "The Auto Discovered Gateway associated with this Gateway Instance", 
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
            "description": {
                "allowedChars": null, 
                "allowedChoices": null, 
                "autogenerated": false, 
                "availability": null, 
                "creationOnly": false, 
                "defaultOrder": false, 
                "defaultValue": null, 
                "description": "A description of the Gateway", 
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
            "enterpriseID": {
                "allowedChars": null, 
                "allowedChoices": null, 
                "autogenerated": false, 
                "availability": null, 
                "creationOnly": false, 
                "defaultOrder": false, 
                "defaultValue": null, 
                "description": "The enterprise associated with this Gateway. This is a read only attribute", 
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
            "name": {
                "allowedChars": null, 
                "allowedChoices": null, 
                "autogenerated": false, 
                "availability": null, 
                "creationOnly": false, 
                "defaultOrder": false, 
                "defaultValue": null, 
                "description": "Name of the Gateway", 
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
            "pending": {
                "allowedChars": null, 
                "allowedChoices": null, 
                "autogenerated": false, 
                "availability": null, 
                "creationOnly": false, 
                "defaultOrder": false, 
                "defaultValue": null, 
                "description": "Indicates that this gateway is pending state or state. When in pending state it cannot be modified from REST.", 
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
            "permittedAction": {
                "allowedChars": null, 
                "allowedChoices": [
                    "EXTEND", 
                    "INSTANTIATE", 
                    "USE", 
                    "READ", 
                    "ALL"
                ], 
                "autogenerated": false, 
                "availability": null, 
                "creationOnly": false, 
                "defaultOrder": false, 
                "defaultValue": null, 
                "description": "The permitted  action to USE/EXTEND  this Gateway Possible values are USE, READ, ALL, INSTANTIATE, EXTEND, .", 
                "filterable": false, 
                "format": null, 
                "maxLength": null, 
                "maxValue": null, 
                "minLength": null, 
                "minValue": null, 
                "orderable": false, 
                "readonly": false, 
                "required": false, 
                "type": "enum", 
                "uniqueItems": false
            }, 
            "personality": {
                "allowedChars": null, 
                "allowedChoices": [
                    "DC7X50", 
                    "OTHER", 
                    "VRSG", 
                    "VSG", 
                    "VSA", 
                    "HARDWARE_VTEP", 
                    "NSG"
                ], 
                "autogenerated": false, 
                "availability": null, 
                "creationOnly": false, 
                "defaultOrder": false, 
                "defaultValue": null, 
                "description": "Personality of the Gateway - VSG,VRSG,NSG,NONE,OTHER, cannot be changed after creation. Possible values are VSG, VSA, VRSG, DC7X50, NSG, HARDWARE_VTEP, OTHER, .", 
                "filterable": false, 
                "format": null, 
                "maxLength": null, 
                "maxValue": null, 
                "minLength": null, 
                "minValue": null, 
                "orderable": false, 
                "readonly": false, 
                "required": false, 
                "type": "enum", 
                "uniqueItems": false
            }, 
            "redundancyGroupID": {
                "allowedChars": null, 
                "allowedChoices": null, 
                "autogenerated": false, 
                "availability": null, 
                "creationOnly": false, 
                "defaultOrder": false, 
                "defaultValue": null, 
                "description": "The Redundancy Gateway Group associated with this Gateway Instance. This is a read only attribute", 
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
            "systemID": {
                "allowedChars": null, 
                "allowedChoices": null, 
                "autogenerated": false, 
                "availability": null, 
                "creationOnly": false, 
                "defaultOrder": false, 
                "defaultValue": null, 
                "description": "Identifier of the Gateway, cannot be modified after creation", 
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
            "templateID": {
                "allowedChars": null, 
                "allowedChoices": null, 
                "autogenerated": false, 
                "availability": null, 
                "creationOnly": false, 
                "defaultOrder": false, 
                "defaultValue": null, 
                "description": "The ID of the template that this Gateway was created from. This should be set when instantiating a Gateway", 
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
            }
        }, 
        "description": "Represents Gateway object.", 
        "entityName": "Gateway", 
        "package": "/gateway", 
        "resourceName": "gateways"
    }
}