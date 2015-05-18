{
    "apis": {
        "children": {}, 
        "parents": {
            "/bridgeinterfaces/{id}/statistics": {
                "RESTName": "bridgeinterface", 
                "operations": [
                    {
                        "availability": null, 
                        "method": "GET"
                    }
                ], 
                "resourceName": "bridgeinterfaces"
            }, 
            "/domains/{id}/statistics": {
                "RESTName": "domain", 
                "operations": [
                    {
                        "availability": null, 
                        "method": "GET"
                    }
                ], 
                "resourceName": "domains"
            }, 
            "/egressaclentrytemplates/{id}/statistics": {
                "RESTName": "egressaclentrytemplate", 
                "operations": [
                    {
                        "availability": null, 
                        "method": "GET"
                    }
                ], 
                "resourceName": "egressaclentrytemplates"
            }, 
            "/hostinterfaces/{id}/statistics": {
                "RESTName": "hostinterface", 
                "operations": [
                    {
                        "availability": null, 
                        "method": "GET"
                    }
                ], 
                "resourceName": "hostinterfaces"
            }, 
            "/ingressaclentrytemplates/{id}/statistics": {
                "RESTName": "ingressaclentrytemplate", 
                "operations": [
                    {
                        "availability": null, 
                        "method": "GET"
                    }
                ], 
                "resourceName": "ingressaclentrytemplates"
            }, 
            "/ingressadvfwdentrytemplates/{id}/statistics": {
                "RESTName": "ingressadvfwdentrytemplate", 
                "operations": [
                    {
                        "availability": null, 
                        "method": "GET"
                    }
                ], 
                "resourceName": "ingressadvfwdentrytemplates"
            }, 
            "/ingressexternalserviceentrytemplates/{id}/statistics": {
                "RESTName": "ingressexternalserviceentrytemplate", 
                "operations": [
                    {
                        "availability": null, 
                        "method": "GET"
                    }
                ], 
                "resourceName": "ingressexternalserviceentrytemplates"
            }, 
            "/l2domains/{id}/statistics": {
                "RESTName": "l2domain", 
                "operations": [
                    {
                        "availability": null, 
                        "method": "GET"
                    }
                ], 
                "resourceName": "l2domains"
            }, 
            "/subnets/{id}/statistics": {
                "RESTName": "subnet", 
                "operations": [
                    {
                        "availability": null, 
                        "method": "GET"
                    }
                ], 
                "resourceName": "subnets"
            }, 
            "/tiers/{id}/statistics": {
                "RESTName": "tier", 
                "operations": [
                    {
                        "availability": null, 
                        "method": "GET"
                    }
                ], 
                "resourceName": "tiers"
            }, 
            "/vminterfaces/{id}/statistics": {
                "RESTName": "vminterface", 
                "operations": [
                    {
                        "availability": null, 
                        "method": "GET"
                    }
                ], 
                "resourceName": "vminterfaces"
            }, 
            "/vports/{id}/statistics": {
                "RESTName": "vport", 
                "operations": [
                    {
                        "availability": null, 
                        "method": "GET"
                    }
                ], 
                "resourceName": "vports"
            }, 
            "/zones/{id}/statistics": {
                "RESTName": "zone", 
                "operations": [
                    {
                        "availability": null, 
                        "method": "GET"
                    }
                ], 
                "resourceName": "zones"
            }
        }, 
        "self": {}
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
        "RESTName": "statistics", 
        "attributes": {
            "endTime": {
                "allowedChars": null, 
                "allowedChoices": null, 
                "autogenerated": false, 
                "availability": null, 
                "creationOnly": false, 
                "defaultOrder": false, 
                "defaultValue": null, 
                "description": "End time for the statistics to be retrieved", 
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
            "numberOfDataPoints": {
                "allowedChars": null, 
                "allowedChoices": null, 
                "autogenerated": false, 
                "availability": null, 
                "creationOnly": false, 
                "defaultOrder": false, 
                "defaultValue": null, 
                "description": "Number of data points between start time and end time", 
                "filterable": false, 
                "format": null, 
                "maxLength": null, 
                "maxValue": null, 
                "minLength": null, 
                "minValue": null, 
                "orderable": false, 
                "readOnly": false, 
                "required": false, 
                "type": "int", 
                "unique": false, 
                "uniqueItems": false
            }, 
            "startTime": {
                "allowedChars": null, 
                "allowedChoices": null, 
                "autogenerated": false, 
                "availability": null, 
                "creationOnly": false, 
                "defaultOrder": false, 
                "defaultValue": null, 
                "description": "Start time for the statistics to be retrieved", 
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
            "statsData": {
                "allowedChars": null, 
                "allowedChoices": null, 
                "autogenerated": false, 
                "availability": null, 
                "creationOnly": false, 
                "defaultOrder": false, 
                "defaultValue": null, 
                "description": "Map&lt;TCAMetric, Long[]&gt; TCAMetric is an Enum. Possible values are packets_in, bytes_in, packets_in_dropped, packets_in_errors, packets_out, bytes_out, packets_out_dropped, packets_out_errors, packets_dropped_rate_limit", 
                "filterable": false, 
                "format": null, 
                "maxLength": null, 
                "maxValue": null, 
                "minLength": null, 
                "minValue": null, 
                "orderable": false, 
                "readOnly": false, 
                "required": false, 
                "type": "Map", 
                "unique": false, 
                "uniqueItems": false
            }, 
            "version": {
                "allowedChars": null, 
                "allowedChoices": null, 
                "autogenerated": false, 
                "availability": null, 
                "creationOnly": false, 
                "defaultOrder": false, 
                "defaultValue": null, 
                "description": "Version of this Sequence number.", 
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
            }
        }, 
        "description": "Retrieves the statistics for a particular domain, zone, subnet, or VM", 
        "entityName": "Statistics", 
        "package": "/stats", 
        "resourceName": "statistics"
    }
}