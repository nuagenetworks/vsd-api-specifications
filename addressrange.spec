{
<<<<<<< HEAD
    "attributes": {
        "IPType": {
            "allowed_choices": [
                "IPV6",
                "IPV4",
                "DUALSTACK"
            ],
            "description": "IPv4 or IPv6(only IPv4 is supported in R1.0) Possible values are IPV4, IPV6, DUALSTACK.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "enum",
            "uniqueScope": "no"
        },
        "DHCPPoolType": {
            "allowed_choices": [
                "HOST",
                "BRIDGE"
            ],
            "description": "DHCPPoolType is an enum that indicates if the DHCP Pool is for HOST/BRIDGE. Possible values are HOST, BRIDGE Possible values are HOST, BRIDGE, .",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "enum",
            "uniqueScope": "no"
        },
        "maxAddress": {
            "description": "Higest address in the address range",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "required": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "minAddress": {
            "description": "Lowest address in the address range",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "required": true,
            "type": "string",
            "uniqueScope": "no"
        }
    },
    "children": {
        "eventlog": {
            "get": true,
            "relationship": "child"
        }
    },
    "model": {
        "delete": true,
        "description": "This is the definition of a Address Range associated with a Network",
        "entity_name": "AddressRange",
=======
    "apis": {
        "children": {
            "/addressranges/{id}/eventlogs": {
                "RESTName": "eventlog",
                "entityName": "EventLog",
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
            "/l2domains/{id}/addressranges": {
                "RESTName": "l2domain",
                "operations": [
                    {
                        "availability": null,
                        "method": "GET"
                    }
                ],
                "resourceName": "l2domains"
            },
            "/l2domaintemplates/{id}/addressranges": {
                "RESTName": "l2domaintemplate",
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
                "resourceName": "l2domaintemplates"
            },
            "/sharednetworkresources/{id}/addressranges": {
                "RESTName": "sharednetworkresource",
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
                "resourceName": "sharednetworkresources"
            },
            "/subnets/{id}/addressranges": {
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
            "/subnettemplates/{id}/addressranges": {
                "RESTName": "subnettemplate",
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
                "resourceName": "subnettemplates"
            }
        },
        "self": {
            "/addressranges/{id}": {
                "RESTName": "addressrange",
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
                "resourceName": "addressranges"
            }
        }
    },
    "model": {
        "RESTName": "addressrange",
        "attributes": {
            "DHCPPoolType": {
                "allowedChars": null,
                "allowedChoices": [
                    "HOST",
                    "BRIDGE"
                ],
                "autogenerated": false,
                "availability": null,
                "channel": null,
                "creationOnly": false,
                "defaultOrder": false,
                "defaultValue": null,
                "description": "DHCPPoolType is an enum that indicates if the DHCP Pool is for HOST/BRIDGE. Possible values are HOST, BRIDGE Possible values are HOST, BRIDGE, .",
                "exposed": true,
                "filterable": false,
                "format": null,
                "maxLength": null,
                "maxValue": null,
                "minLength": null,
                "minValue": null,
                "orderable": false,
                "readOnly": false,
                "required": false,
                "transient": false,
                "type": "enum",
                "unique": false
            },
            "maxAddress": {
                "allowedChars": null,
                "allowedChoices": null,
                "autogenerated": false,
                "availability": null,
                "channel": null,
                "creationOnly": false,
                "defaultOrder": false,
                "defaultValue": null,
                "description": "Higest address in the address range",
                "exposed": true,
                "filterable": false,
                "format": null,
                "maxLength": null,
                "maxValue": null,
                "minLength": null,
                "minValue": null,
                "orderable": false,
                "readOnly": false,
                "required": true,
                "transient": false,
                "type": "string",
                "unique": false
            },
            "minAddress": {
                "allowedChars": null,
                "allowedChoices": null,
                "autogenerated": false,
                "availability": null,
                "channel": null,
                "creationOnly": false,
                "defaultOrder": false,
                "defaultValue": null,
                "description": "Lowest address in the address range",
                "exposed": true,
                "filterable": false,
                "format": null,
                "maxLength": null,
                "maxValue": null,
                "minLength": null,
                "minValue": null,
                "orderable": false,
                "readOnly": false,
                "required": true,
                "transient": false,
                "type": "string",
                "unique": false
            },
            "IPType": {
              "allowedChars": null,
              "allowedChoices": [
                "DUALSTACK",
                "IPV4",
                "IPV6"
              ],
              "autogenerated": false,
              "availability": null,
              "channel": null,
              "creationOnly": false,
              "defaultOrder": false,
              "defaultValue": "IPV4",
              "description": "IPv4 or IPv6(only IPv4 is supported in R1.0) Possible values are IPV4, IPV6, .",
              "exposed": true,
              "filterable": true,
              "format": null,
              "maxLength": null,
              "maxValue": null,
              "minLength": null,
              "minValue": null,
              "orderable": true,
              "readOnly": true,
              "required": true,
              "transient": false,
              "type": "enum",
              "unique": false
            }
        },
        "description": "This is the definition of a Address Range associated with a Network",
        "entityName": "AddressRange",
>>>>>>> edc8a1057eda55ded4ee32335293010fd5742f6f
        "extends": [
            "@base",
            "@metadata"
        ],
<<<<<<< HEAD
        "get": true,
        "package": "network",
        "resource_name": "addressranges",
        "rest_name": "addressrange",
        "update": true
=======
        "package": "/network",
        "resourceName": "addressranges"
>>>>>>> edc8a1057eda55ded4ee32335293010fd5742f6f
    }
}