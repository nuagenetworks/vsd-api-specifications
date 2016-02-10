{
    "attributes": {
        "BGPEnabled": {
            "description": "Enable BGP for this enterprise profile",
            "exposed": true,
            "format": "free",
            "type": "boolean",
            "uniqueScope": "no"
        },
        "DHCPLeaseInterval": {
            "description": "DHCP Lease Interval (in hours) to be used by an enterprise.",
            "exposed": true,
            "format": "free",
            "max_value": 60,
            "min_value": 12,
            "type": "integer",
            "uniqueScope": "no"
        },
        "allowAdvancedQOSConfiguration": {
            "description": "Controls whether this enterprise has access to advanced QoS settings.",
            "exposed": true,
            "format": "free",
            "type": "boolean",
            "uniqueScope": "no"
        },
        "allowGatewayManagement": {
            "description": "If set to true lets the enterprise admin create gateway templates and instances.",
            "exposed": true,
            "format": "free",
            "type": "boolean",
            "uniqueScope": "no"
        },
        "allowTrustedForwardingClass": {
            "description": "Controls whether QoS policies and templates created under this enterprise set the trusted flag to true",
            "exposed": true,
            "format": "free",
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
            "format": "free",
            "type": "list",
            "subtype": "enum",
            "uniqueScope": "no"
        },
        "description": {
            "description": "A description of the enterprise/organisation profile.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 255,
            "min_length": 1,
            "type": "string",
            "uniqueScope": "no"
        },
        "encryptionManagementMode": {
            "allowed_choices": [
                "DISABLED",
                "MANAGED"
            ],
            "description": "encryption management mode for this enterprise Possible values are DISABLED, MANAGED, .",
            "exposed": true,
            "format": "free",
            "type": "enum",
            "uniqueScope": "no"
        },
        "floatingIPsQuota": {
            "description": "Quota set for the number of floating IPs to be used by an enterprise.",
            "exposed": true,
            "format": "free",
            "min_value": 0,
            "max_value": 250000,
            "default_value": 0,
            "type": "integer",
            "uniqueScope": "no"
        },
        "name": {
            "description": "The unique name of the enterprise. Valid characters are alphabets, numbers, space and hyphen( - ).",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 255,
            "min_length": 1,
            "orderable": true,
            "required": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "receiveMultiCastListID": {
            "description": "Readonly ID of the auto generated receive multicast list associated with this enterprise profile",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "sendMultiCastListID": {
            "description": "Readonly ID of the auto generated send multicast list associated with this enterprise profile",
            "exposed": true,
            "format": "free",
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
            "@audited",
            "@base",
            "@metadata"
        ],
        "get": true,
        "package": "usermgmt",
        "resource_name": "enterpriseprofiles",
        "rest_name": "enterpriseprofile",
        "update": true
    }
}