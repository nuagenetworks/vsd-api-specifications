{
    "attributes": {
        "BGPEnabled": {
            "description": "Enable BGP for this enterprise profile",
            "exposed": true,
            "filterable": true,
            "orderable": false,
            "type": "boolean",
            "uniqueScope": "no"
        },
        "DHCPLeaseInterval": {
            "description": "DHCP Lease Interval (in hours) to be used by an enterprise.",
            "exposed": true,
            "filterable": false,
            "orderable": false,
            "type": "integer",
            "min_value": 12,
            "max_value": 60,
            "default_value": 12,
            "uniqueScope": "no"
        },
        "allowAdvancedQOSConfiguration": {
            "description": "Controls whether this enterprise has access to advanced QoS settings.",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "boolean",
            "uniqueScope": "no"
        },
        "allowGatewayManagement": {
            "description": "If set to true lets the enterprise admin create gateway templates and instances.",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "boolean",
            "uniqueScope": "no"
        },
        "allowTrustedForwardingClass": {
            "description": "Controls whether QoS policies and templates created under this enterprise set the trusted flag to true",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "boolean",
            "uniqueScope": "no"
        },
        "allowedForwardingClasses": {
            "allowed_choices": [
                "A",
                "B",
                "C",
                "D",
                "E",
                "F",
                "G",
                "H",
                "NONE"
            ],
            "description": "Allowed Forwarding Classes for this enterprise. Possible values are NONE, A, B, C, D, E, F, G, H, .",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "list",
            "subtype": "enum",
            "uniqueScope": "no"
        },
        "description": {
            "description": "A description of the enterprise/organisation profile.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": false,
            "type": "string",
            "min_length": 1,
            "max_length": 255,
            "uniqueScope": "no"
        },
        "encryptionManagementMode": {
            "allowed_choices": [
                "DISABLED",
                "MANAGED"
            ],
            "description": "encryption management mode for this enterprise Possible values are DISABLED, MANAGED, .",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "enum",
            "uniqueScope": "no"
        },
        "floatingIPsQuota": {
            "description": "Quota set for the number of floating IPs to be used by an enterprise.",
            "exposed": true,
            "filterable": false,
            "orderable": false,
            "type": "integer",
            "min_value": 0,
            "max_value": 250000,
            "default_value": 0,
            "uniqueScope": "no"
        },
        "name": {
            "description": "The unique name of the enterprise. Valid characters are alphabets, numbers, space and hyphen( - ).",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "required": true,
            "type": "string",
            "min_length": 1,
            "max_length": 255,
            "uniqueScope": "no"
        },
        "receiveMultiCastListID": {
            "description": "Readonly ID of the auto generated receive multicast list associated with this enterprise profile",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        },
        "sendMultiCastListID": {
            "description": "Readonly ID of the auto generated send multicast list associated with this enterprise profile",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        }
    },
    "children": {
        "enterprise": {
            "get": true,
            "relationship": "child"
        },
        "eventlog": {
            "get": true,
            "relationship": "child"
        },
        "externalservice": {
            "get": true,
            "relationship": "child",
            "update": true
        },
        "multicastlist": {
            "get": true,
            "relationship": "child"
        }
    },
    "model": {
        "delete": true,
        "description": "Enterprise profile, used to store an enterprise's policies, quota etc",
        "entity_name": "EnterpriseProfile",
        "extends": [
            "@base",
            "@audited",
            "@metadata"
        ],
        "get": true,
        "package": "usermgmt",
        "resource_name": "enterpriseprofiles",
        "rest_name": "enterpriseprofile",
        "update": true
    }
}