{
    "attributes": {
        "associatedEnterpriseSecurityID": {
            "description": "Readonly Id of the associated group key encryption profile", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "associatedKeyServerMonitorID": {
            "description": "Readonly Id of the associated keyserver monitor", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "allowGatewayManagement": {
            "description": "This flag indicates if the enterprise/organization can manage gateways. If yes then it can create gateway templates, instantiate them etc.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "boolean"
        }, 
        "description": {
            "description": "A description of the enterprise", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "name": {
            "description": "The unique name of the enterprise. Valid characters are alphabets, numbers, space and hyphen( - ).", 
            "format": "free", 
            "filterable": true, 
            "uniqueScope": "no", 
            "required": true, 
            "exposed": true, 
            "orderable": true, 
            "type": "string"
        }, 
        "DHCPLeaseInterval": {
            "description": "DHCP Lease Interval (in hrs) to be used by an enterprise.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "integer"
        }, 
        "avatarData": {
            "description": "URL to the avatar data associated with the enterprise. If the avatarType is URL then value of avatarData should an URL of the image. If the avatarType BASE64 then avatarData should be BASE64 encoded value of the image", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "sendMultiCastListID": {
            "description": "Readonly Id of the auto generated send multicast list associated with this enterprise profile", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "floatingIPsQuota": {
            "description": "Quota set for the number of floating IPs to be used by an enterprise.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "integer"
        }, 
        "customerID": {
            "description": "CustomerID that is used by VSC to identify this enterprise. This is a read only attribute.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "float"
        }, 
        "avatarType": {
            "description": "Avatar type - URL or BASE64 Possible values are URL, BASE64, COMPUTEDURL, .", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "allowed_choices": [
                "COMPUTEDURL", 
                "BASE64", 
                "URL"
            ], 
            "orderable": true, 
            "type": "enum"
        }, 
        "encryptionManagementMode": {
            "description": "Readonly encryption management mode of the associated profile", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "associatedGroupKeyEncryptionProfileID": {
            "description": "Readonly Id of the associated group key encryption profile", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "LDAPAuthorizationEnabled": {
            "description": "Read-only flag - indicates if LDAP is used for authorization for the enterprise. For detailed explanation, see definition in LDAPConfiguration class", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "boolean"
        }, 
        "receiveMultiCastListID": {
            "description": "Readonly Id of the auto generated receive multicast list associated with this enterprise profile", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "enterpriseProfileID": {
            "description": "Enterprise profile id for this enterprise", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "floatingIPsUsed": {
            "description": "Number of floating IPs used by the enterprise from the assigned floatingIPsQuota", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "integer"
        }, 
        "allowedForwardingClasses": {
            "description": "Allowed Forwarding Classes for this enterprise. Possible values are NONE, A, B, C, D, E, F, G, H, .", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "allowed_choices": [
                "D", 
                "E", 
                "F", 
                "G", 
                "A", 
                "B", 
                "C", 
                "H", 
                "NONE"
            ], 
            "orderable": true, 
            "type": "enum"
        }, 
        "allowTrustedForwardingClass": {
            "description": "Controls whether QoS policies and templates created under this enterprise set the trusted flag to true", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "boolean"
        }, 
        "LDAPEnabled": {
            "description": "Read-only flag - indicates if LDAP is used for authentication for the enterprise. For detailed explanation, see definition in LDAPConfiguration class", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "boolean"
        }, 
        "allowAdvancedQOSConfiguration": {
            "description": "Controls whether this enterprise has access to advanced QoS settings", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "boolean"
        }
    }, 
    "model": {
        "resource_name": "enterprises", 
        "description": "Definition of the enterprise object. This is the top level object that represents an enterprise or organization.", 
        "entity_name": "Enterprise", 
        "package": "usermgmt", 
        "get": true, 
        "update": true, 
        "rest_name": "enterprise", 
        "extends": [
            "@base", 
            "@metadata"
        ], 
        "delete": true
    }, 
    "children": {
        "groupkeyencryptionprofile": {
            "relationship": "child", 
            "get": true
        }, 
        "domain": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }, 
        "multicastlist": {
            "relationship": "child", 
            "get": true
        }, 
        "egressqospolicy": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }, 
        "l2domaintemplate": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }, 
        "sharednetworkresource": {
            "relationship": "child", 
            "get": true
        }, 
        "domaintemplate": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }, 
        "vm": {
            "relationship": "child", 
            "get": true
        }, 
        "dscpforwardingclasstable": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }, 
        "redundancygroup": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }, 
        "gateway": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }, 
        "nsgateway": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }, 
        "group": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }, 
        "ratelimiter": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }, 
        "eventlog": {
            "relationship": "child", 
            "get": true
        }, 
        "application": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }, 
        "infrastructureportprofile": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }, 
        "nsgredundancygroup": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }, 
        "externalservice": {
            "relationship": "child", 
            "get": true
        }, 
        "applicationservice": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }, 
        "gatewaytemplate": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }, 
        "enterprisenetwork": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }, 
        "ldapconfiguration": {
            "relationship": "child", 
            "get": true
        }, 
        "l2domain": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }, 
        "externalappservice": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }, 
        "job": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }, 
        "user": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }, 
        "metadatatag": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }, 
        "keyservermonitor": {
            "relationship": "child", 
            "get": true
        }, 
        "alarm": {
            "relationship": "child", 
            "get": true
        }, 
        "globalmetadata": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }, 
        "nsgatewaytemplate": {
            "relationship": "child", 
            "get": true
        }, 
        "patnatpool": {
            "relationship": "child", 
            "get": true
        }, 
        "networkmacrogroup": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }
    }
}