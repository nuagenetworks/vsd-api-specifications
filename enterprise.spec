{
    "attributes": {
        "BGPEnabled": {
            "description": "Read only flag to display if BGP is enabled for this enterprise",
            "exposed": true,
            "filterable": true,
            "orderable": false,
            "type": "boolean",
            "uniqueScope": "no"
        },
        "DHCPLeaseInterval": {
            "description": "DHCP Lease Interval (in hrs) to be used by an enterprise.",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "integer",
            "uniqueScope": "no"
        },
        "LDAPAuthorizationEnabled": {
            "description": "Read-only flag - indicates if LDAP is used for authorization for the enterprise. For detailed explanation, see definition in LDAPConfiguration class",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "boolean",
            "uniqueScope": "no"
        },
        "LDAPEnabled": {
            "description": "Read-only flag - indicates if LDAP is used for authentication for the enterprise. For detailed explanation, see definition in LDAPConfiguration class",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "boolean",
            "uniqueScope": "no"
        },
        "allowAdvancedQOSConfiguration": {
            "description": "Controls whether this enterprise has access to advanced QoS settings",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "boolean",
            "uniqueScope": "no"
        },
        "allowGatewayManagement": {
            "description": "This flag indicates if the enterprise/organization can manage gateways. If yes then it can create gateway templates, instantiate them etc.",
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
        "associatedEnterpriseSecurityID": {
            "description": "Readonly Id of the associated group key encryption profile",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        },
        "associatedGroupKeyEncryptionProfileID": {
            "description": "Readonly Id of the associated group key encryption profile",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        },
        "associatedKeyServerMonitorID": {
            "description": "Readonly Id of the associated keyserver monitor",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        },
        "avatarData": {
            "description": "URL to the avatar data associated with the enterprise. If the avatarType is URL then value of avatarData should an URL of the image. If the avatarType BASE64 then avatarData should be BASE64 encoded value of the image",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        },
        "avatarType": {
            "allowed_choices": [
                "COMPUTEDURL",
                "BASE64",
                "URL"
            ],
            "description": "Avatar type - URL or BASE64 Possible values are URL, BASE64, COMPUTEDURL, .",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "enum",
            "uniqueScope": "no"
        },
        "customerID": {
            "description": "CustomerID that is used by VSC to identify this enterprise. This is a read only attribute.",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "integer",
            "subtype": "long",
            "uniqueScope": "no"
        },
        "description": {
            "description": "A description of the enterprise",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": false,
            "type": "string",
            "min_length": 0,
            "max_length": 255,
            "uniqueScope": "no"
        },
        "encryptionManagementMode": {
            "description": "Readonly encryption management mode of the associated profile",
            "allowed_choices": [
                "DISABLED",
                "MANAGED"
            ],
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "enum",
            "uniqueScope": "no"
        },
        "enterpriseProfileID": {
            "description": "Enterprise profile id for this enterprise",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
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
        "floatingIPsUsed": {
            "description": "Number of floating IPs used by the enterprise from the assigned floatingIPsQuota",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "integer",
            "uniqueScope": "no"
        },
        "localAS": {
            "description": "Local autonomous system for the enterprise",
            "exposed": true,
            "filterable": false,
            "orderable": false,
            "type": "integer",
            "subtype": "long",
            "min_value": 1,
            "max_value": 64495,
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
            "description": "Readonly Id of the auto generated receive multicast list associated with this enterprise profile",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        },
        "sendMultiCastListID": {
            "description": "Readonly Id of the auto generated send multicast list associated with this enterprise profile",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        }
    },
    "children": {
        "alarm": {
            "get": true,
            "relationship": "child"
        },
        "application": {
            "create": true,
            "get": true,
            "relationship": "child"
        },
        "applicationservice": {
            "create": true,
            "get": true,
            "relationship": "child"
        },
        "bgpprofile": {
            "create": true,
            "get": true,
            "relationship": "child"
        },
        "domain": {
            "create": true,
            "get": true,
            "relationship": "child"
        },
        "domaintemplate": {
            "create": true,
            "get": true,
            "relationship": "child"
        },
        "dscpforwardingclasstable": {
            "create": true,
            "get": true,
            "relationship": "child"
        },
        "egressqospolicy": {
            "create": true,
            "get": true,
            "relationship": "child"
        },
        "enterprisenetwork": {
            "create": true,
            "get": true,
            "relationship": "child"
        },
        "eventlog": {
            "get": true,
            "relationship": "child"
        },
        "externalappservice": {
            "create": true,
            "get": true,
            "relationship": "child"
        },
        "externalservice": {
            "get": true,
            "relationship": "child"
        },
        "gateway": {
            "create": true,
            "get": true,
            "relationship": "child"
        },
        "gatewaytemplate": {
            "create": true,
            "get": true,
            "relationship": "child"
        },
        "globalmetadata": {
            "create": true,
            "get": true,
            "relationship": "child"
        },
        "group": {
            "create": true,
            "get": true,
            "relationship": "child"
        },
        "groupkeyencryptionprofile": {
            "get": true,
            "relationship": "child"
        },
        "ikev2encryptionprofile": {
            "create": true,
            "get": true,
            "relationship": "child"
        },
        "infrastructureportprofile": {
            "create": true,
            "get": true,
            "relationship": "child"
        },
        "job": {
            "create": true,
            "get": true,
            "relationship": "child"
        },
        "keyservermonitor": {
            "get": true,
            "relationship": "child"
        },
        "l2domain": {
            "create": true,
            "get": true,
            "relationship": "child"
        },
        "l2domaintemplate": {
            "create": true,
            "get": true,
            "relationship": "child"
        },
        "ldapconfiguration": {
            "get": true,
            "relationship": "child"
        },
        "metadatatag": {
            "create": true,
            "get": true,
            "relationship": "child"
        },
        "multicastlist": {
            "get": true,
            "relationship": "child"
        },
        "networkmacrogroup": {
            "create": true,
            "get": true,
            "relationship": "child"
        },
        "nsgateway": {
            "create": true,
            "get": true,
            "relationship": "child"
        },
        "nsgatewaytemplate": {
            "get": true,
            "relationship": "child"
        },
        "nsgredundancygroup": {
            "create": true,
            "get": true,
            "relationship": "child"
        },
        "publicnetwork": {
            "create": true,
            "get": true,
            "relationship": "child"
        },
        "patnatpool": {
            "get": true,
            "relationship": "child"
        },
        "ratelimiter": {
            "create": true,
            "get": true,
            "relationship": "child"
        },
        "redundancygroup": {
            "create": true,
            "get": true,
            "relationship": "child"
        },
        "sharednetworkresource": {
            "get": true,
            "relationship": "child"
        },
        "user": {
            "create": true,
            "get": true,
            "relationship": "child"
        },
        "vm": {
            "get": true,
            "relationship": "child"
        }
    },
    "model": {
        "delete": true,
        "description": "Definition of the enterprise object. This is the top level object that represents an enterprise or organization.",
        "entity_name": "Enterprise",
        "extends": [
            "@base",
            "@audited",
            "@metadata"
        ],
        "get": true,
        "package": "usermgmt",
        "resource_name": "enterprises",
        "rest_name": "enterprise",
        "update": true
    }
}