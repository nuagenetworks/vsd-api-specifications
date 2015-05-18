{
    "apis": {
        "children": {
            "/tcas/{id}/alarms": {
                "RESTName": "alarm", 
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
                "resourceName": "alarms"
            }, 
            "/tcas/{id}/eventlogs": {
                "RESTName": "eventlog", 
                "operations": [
                    {
                        "availability": null, 
                        "method": "GET"
                    }
                ], 
                "resourceName": "eventlogs"
            }
        }, 
        "parents": {
            "/bridgeinterfaces/{id}/tcas": {
                "RESTName": "bridgeinterface", 
                "operations": [
                    {
                        "availability": null, 
                        "method": "GET"
                    }
                ], 
                "resourceName": "bridgeinterfaces"
            }, 
            "/domains/{id}/tcas": {
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
            "/hostinterfaces/{id}/tcas": {
                "RESTName": "hostinterface", 
                "operations": [
                    {
                        "availability": null, 
                        "method": "GET"
                    }
                ], 
                "resourceName": "hostinterfaces"
            }, 
            "/l2domains/{id}/tcas": {
                "RESTName": "l2domain", 
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
                "resourceName": "l2domains"
            }, 
            "/subnets/{id}/tcas": {
                "RESTName": "subnet", 
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
                "resourceName": "subnets"
            }, 
            "/tcas": {
                "RESTName": "tca", 
                "operations": [
                    {
                        "availability": null, 
                        "method": "GET"
                    }
                ], 
                "resourceName": "tcas"
            }, 
            "/tiers/{id}/tcas": {
                "RESTName": "tier", 
                "operations": [
                    {
                        "availability": null, 
                        "method": "GET"
                    }
                ], 
                "resourceName": "tiers"
            }, 
            "/vminterfaces/{id}/tcas": {
                "RESTName": "vminterface", 
                "operations": [
                    {
                        "availability": null, 
                        "method": "GET"
                    }
                ], 
                "resourceName": "vminterfaces"
            }, 
            "/vports/{id}/tcas": {
                "RESTName": "vport", 
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
                "resourceName": "vports"
            }, 
            "/zones/{id}/tcas": {
                "RESTName": "zone", 
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
                "resourceName": "zones"
            }
        }, 
        "self": {
            "/tcas/{id}": {
                "RESTName": "tca", 
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
                "resourceName": "tcas"
            }
        }
    }, 
    "metadata": {
        "api_version": "3.2", 
        "author": "", 
        "comments": "", 
        "date": "05-18-2015", 
        "dev_backend": "", 
        "dev_frontend": "", 
        "dev_qd": "", 
        "plm": "", 
        "prd_url": "http://", 
        "revisions": []
    }, 
    "model": {
        "RESTName": "tca", 
        "attributes": {
            "URLEndPoint": {
                "allowedChars": null, 
                "allowedChoices": null, 
                "autogenerated": false, 
                "availability": null, 
                "creationOnly": false, 
                "defaultOrder": false, 
                "defaultValue": null, 
                "description": "URL endpoint to post Alarm data to when TCA is triggered", 
                "filterable": false, 
                "format": null, 
                "maxLength": null, 
                "maxValue": null, 
                "minLength": null, 
                "minValue": null, 
                "orderable": false, 
                "readOnly": false, 
                "required": false, 
                "type": "string", 
                "unique": false, 
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
                "description": "Desription of the TCA", 
                "filterable": false, 
                "format": null, 
                "maxLength": null, 
                "maxValue": null, 
                "minLength": null, 
                "minValue": null, 
                "orderable": false, 
                "readOnly": false, 
                "required": false, 
                "type": "string", 
                "unique": false, 
                "uniqueItems": false
            }, 
            "metric": {
                "allowedChars": null, 
                "allowedChoices": [
                    "BYTES_IN", 
                    "EGRESS_BYTE_COUNT", 
                    "PACKETS_IN_ERROR", 
                    "PACKETS_OUT_DROPPED", 
                    "BYTES_OUT", 
                    "PACKETS_IN_DROPPED", 
                    "INGRESS_BYTE_COUNT", 
                    "PACKETS_IN", 
                    "PACKETS_OUT_ERROR", 
                    "PACKETS_DROPPED_BY_RATE_LIMIT", 
                    "INGRESS_PACKET_COUNT", 
                    "PACKETS_OUT", 
                    "EGRESS_PACKET_COUNT"
                ], 
                "autogenerated": false, 
                "availability": null, 
                "creationOnly": false, 
                "defaultOrder": false, 
                "defaultValue": null, 
                "description": "The metric associated with the TCA - PACKETS_IN, BYTES_IN, PACKETS_IN_DROPPED, PACKETS_IN_ERROR, PACKETS_OUT, BYTES_OUT PACKETS_OUT_DROPPED, PACKETS_OUT_ERROR and PACKETS_DROPPED_BY_RATE_LIMIT Possible values are PACKETS_IN, BYTES_IN, PACKETS_IN_DROPPED, PACKETS_IN_ERROR, PACKETS_OUT, BYTES_OUT, PACKETS_OUT_DROPPED, PACKETS_OUT_ERROR, PACKETS_DROPPED_BY_RATE_LIMIT, INGRESS_BYTE_COUNT, INGRESS_PACKET_COUNT, EGRESS_BYTE_COUNT, EGRESS_PACKET_COUNT, .", 
                "filterable": false, 
                "format": null, 
                "maxLength": null, 
                "maxValue": null, 
                "minLength": null, 
                "minValue": null, 
                "orderable": false, 
                "readOnly": false, 
                "required": false, 
                "type": "enum", 
                "unique": false, 
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
                "description": "The name of the TCA", 
                "filterable": false, 
                "format": null, 
                "maxLength": null, 
                "maxValue": null, 
                "minLength": null, 
                "minValue": null, 
                "orderable": false, 
                "readOnly": false, 
                "required": false, 
                "type": "string", 
                "unique": false, 
                "uniqueItems": false
            }, 
            "period": {
                "allowedChars": null, 
                "allowedChoices": null, 
                "autogenerated": false, 
                "availability": null, 
                "creationOnly": false, 
                "defaultOrder": false, 
                "defaultValue": null, 
                "description": "The averaging period", 
                "filterable": false, 
                "format": null, 
                "maxLength": null, 
                "maxValue": null, 
                "minLength": null, 
                "minValue": null, 
                "orderable": false, 
                "readOnly": false, 
                "required": false, 
                "type": "long", 
                "unique": false, 
                "uniqueItems": false
            }, 
            "scope": {
                "allowedChars": null, 
                "allowedChoices": [
                    "LOCAL", 
                    "GLOBAL"
                ], 
                "autogenerated": false, 
                "availability": null, 
                "creationOnly": false, 
                "defaultOrder": false, 
                "defaultValue": null, 
                "description": "GLOBAL or LOCAL scope. Global refers to aggregate values across subnets, zones or domains. Local refers to traffic from/to individual VMs Possible values are GLOBAL, LOCAL, .", 
                "filterable": false, 
                "format": null, 
                "maxLength": null, 
                "maxValue": null, 
                "minLength": null, 
                "minValue": null, 
                "orderable": false, 
                "readOnly": false, 
                "required": false, 
                "type": "enum", 
                "unique": false, 
                "uniqueItems": false
            }, 
            "threshold": {
                "allowedChars": null, 
                "allowedChoices": null, 
                "autogenerated": false, 
                "availability": null, 
                "creationOnly": false, 
                "defaultOrder": false, 
                "defaultValue": null, 
                "description": "The threshold that must be exceeded before an alarm is issued", 
                "filterable": false, 
                "format": null, 
                "maxLength": null, 
                "maxValue": null, 
                "minLength": null, 
                "minValue": null, 
                "orderable": false, 
                "readOnly": false, 
                "required": false, 
                "type": "long", 
                "unique": false, 
                "uniqueItems": false
            }, 
            "type": {
                "allowedChars": null, 
                "allowedChoices": [
                    "ROLLING_AVERAGE", 
                    "BREACH"
                ], 
                "autogenerated": false, 
                "availability": null, 
                "creationOnly": false, 
                "defaultOrder": false, 
                "defaultValue": null, 
                "description": "Rolling average or sequence of samples over the averaging period - ROLLING_AVERAGE or BREACH Possible values are ROLLING_AVERAGE, BREACH, .", 
                "filterable": false, 
                "format": null, 
                "maxLength": null, 
                "maxValue": null, 
                "minLength": null, 
                "minValue": null, 
                "orderable": false, 
                "readOnly": false, 
                "required": false, 
                "type": "enum", 
                "unique": false, 
                "uniqueItems": false
            }
        }, 
        "description": "Provides the definition of the Threshold Control Alarms", 
        "entityName": "TCA", 
        "package": "/stats", 
        "resourceName": "tcas"
    }
}