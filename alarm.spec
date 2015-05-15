{
    "apis": {
        "children": {}, 
        "parents": {
            "/enterprises/{id}/alarms": {
                "RESTName": "enterprise", 
                "operations": [
                    {
                        "availability": null, 
                        "method": "GET"
                    }
                ], 
                "resourceName": "enterprises"
            }, 
            "/enterprises/{id}/allalarms": {
                "RESTName": "enterprise", 
                "operations": [
                    {
                        "availability": null, 
                        "method": "GET"
                    }
                ], 
                "resourceName": "enterprises"
            }, 
            "/gateways/{id}/alarms": {
                "RESTName": "gateway", 
                "operations": [
                    {
                        "availability": null, 
                        "method": "GET"
                    }
                ], 
                "resourceName": "gateways"
            }, 
            "/hscs/{id}/alarms": {
                "RESTName": "hsc", 
                "operations": [
                    {
                        "availability": null, 
                        "method": "GET"
                    }
                ], 
                "resourceName": "hscs"
            }, 
            "/nsgateways/{id}/alarms": {
                "RESTName": "nsgateway", 
                "operations": [
                    {
                        "availability": null, 
                        "method": "GET"
                    }
                ], 
                "resourceName": "nsgateways"
            }, 
            "/nsgredundancygroups/{id}/alarms": {
                "RESTName": "nsgredundancygroup", 
                "operations": [
                    {
                        "availability": null, 
                        "method": "GET"
                    }
                ], 
                "resourceName": "nsgredundancygroups"
            }, 
            "/ports/{id}/alarms": {
                "RESTName": "port", 
                "operations": [
                    {
                        "availability": null, 
                        "method": "GET"
                    }
                ], 
                "resourceName": "ports"
            }, 
            "/redundancygroups/{id}/alarms": {
                "RESTName": "redundancygroup", 
                "operations": [
                    {
                        "availability": null, 
                        "method": "GET"
                    }
                ], 
                "resourceName": "redundancygroups"
            }, 
            "/services/{id}/alarms": {
                "RESTName": "service", 
                "operations": [
                    {
                        "availability": null, 
                        "method": "GET"
                    }
                ], 
                "resourceName": "services"
            }, 
            "/tcas/{id}/alarms": {
                "RESTName": "tca", 
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
                "resourceName": "tcas"
            }, 
            "/vlans/{id}/alarms": {
                "RESTName": "vlan", 
                "operations": [
                    {
                        "availability": null, 
                        "method": "GET"
                    }
                ], 
                "resourceName": "vlans"
            }, 
            "/vms/{id}/alarms": {
                "RESTName": "vm", 
                "operations": [
                    {
                        "availability": null, 
                        "method": "GET"
                    }
                ], 
                "resourceName": "vms"
            }, 
            "/vports/{id}/alarms": {
                "RESTName": "vport", 
                "operations": [
                    {
                        "availability": null, 
                        "method": "GET"
                    }
                ], 
                "resourceName": "vports"
            }, 
            "/vrss/{id}/alarms": {
                "RESTName": "vrs", 
                "operations": [
                    {
                        "availability": null, 
                        "method": "GET"
                    }
                ], 
                "resourceName": "vrss"
            }, 
            "/vscs/{id}/alarms": {
                "RESTName": "vsc", 
                "operations": [
                    {
                        "availability": null, 
                        "method": "GET"
                    }
                ], 
                "resourceName": "vscs"
            }, 
            "/vsds/{id}/alarms": {
                "RESTName": "vsd", 
                "operations": [
                    {
                        "availability": null, 
                        "method": "GET"
                    }
                ], 
                "resourceName": "vsds"
            }
        }, 
        "self": {
            "/alarms/{id}": {
                "RESTName": "alarm", 
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
                "resourceName": "alarms"
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
        "RESTName": "alarm", 
        "attributes": {
            "acknowledged": {
                "allowedChars": null, 
                "allowedChoices": null, 
                "autogenerated": false, 
                "availability": null, 
                "creationOnly": false, 
                "defaultOrder": false, 
                "defaultValue": null, 
                "description": "Flag to indicate that is already acknowledge or not", 
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
            "description": {
                "allowedChars": null, 
                "allowedChoices": null, 
                "autogenerated": false, 
                "availability": null, 
                "creationOnly": false, 
                "defaultOrder": false, 
                "defaultValue": null, 
                "description": "Description of the alarm", 
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
                "description": "Enterprise that this alarm belongs to", 
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
            "errorCondition": {
                "allowedChars": null, 
                "allowedChoices": null, 
                "autogenerated": false, 
                "availability": null, 
                "creationOnly": false, 
                "defaultOrder": false, 
                "defaultValue": null, 
                "description": "Identifies the error condition", 
                "filterable": false, 
                "format": null, 
                "maxLength": null, 
                "maxValue": null, 
                "minLength": null, 
                "minValue": null, 
                "orderable": false, 
                "readonly": false, 
                "required": false, 
                "type": "int", 
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
                "description": "The alarm name.  Each type of alarm will generate its own name", 
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
            "numberOfOccurances": {
                "allowedChars": null, 
                "allowedChoices": null, 
                "autogenerated": false, 
                "availability": null, 
                "creationOnly": false, 
                "defaultOrder": false, 
                "defaultValue": null, 
                "description": "Number of times that the alarm was triggered", 
                "filterable": false, 
                "format": null, 
                "maxLength": null, 
                "maxValue": null, 
                "minLength": null, 
                "minValue": null, 
                "orderable": false, 
                "readonly": false, 
                "required": false, 
                "type": "int", 
                "uniqueItems": false
            }, 
            "reason": {
                "allowedChars": null, 
                "allowedChoices": null, 
                "autogenerated": false, 
                "availability": null, 
                "creationOnly": false, 
                "defaultOrder": false, 
                "defaultValue": null, 
                "description": "Provides a description of the alarm", 
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
            "severity": {
                "allowedChars": null, 
                "allowedChoices": [
                    "MINOR", 
                    "MAJOR", 
                    "WARNING", 
                    "CRITICAL", 
                    "INFO"
                ], 
                "autogenerated": false, 
                "availability": null, 
                "creationOnly": false, 
                "defaultOrder": false, 
                "defaultValue": null, 
                "description": "Severity of the alarm. - MAJOR, MINOR, CRITICAL, INFO, WARNING. Possible values are MAJOR, MINOR, CRITICAL, INFO, WARNING, .", 
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
            "targetObject": {
                "allowedChars": null, 
                "allowedChoices": null, 
                "autogenerated": false, 
                "availability": null, 
                "creationOnly": false, 
                "defaultOrder": false, 
                "defaultValue": null, 
                "description": "Identifies affected Entity.  Example: Alarm generated by TCA for Domain domain1(Packets towards a VM, Breach)", 
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
            "timestamp": {
                "allowedChars": null, 
                "allowedChoices": null, 
                "autogenerated": false, 
                "availability": null, 
                "creationOnly": false, 
                "defaultOrder": false, 
                "defaultValue": null, 
                "description": "Indicates the time that the alarm was triggered", 
                "filterable": false, 
                "format": null, 
                "maxLength": null, 
                "maxValue": null, 
                "minLength": null, 
                "minValue": null, 
                "orderable": false, 
                "readonly": false, 
                "required": false, 
                "type": "long", 
                "uniqueItems": false
            }
        }, 
        "description": "The alarm API allows the management of system alarms", 
        "entityName": "Alarm", 
        "package": "/alarm", 
        "resourceName": "alarms"
    }
}