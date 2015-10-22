{
    "attributes": {
        "allowGatewayManagement": {
            "description": "If set to true lets the enterprise admin create gateway templates and instances.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "boolean"
        }, 
        "description": {
            "description": "A description of the enterprise/organisation profile.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "DHCPLeaseInterval": {
            "description": "DHCP Lease Interval (in hours) to be used by an enterprise.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "integer"
        }, 
        "sendMultiCastListID": {
            "description": "Readonly ID of the auto generated send multicast list associated with this enterprise profile", 
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
        "encryptionManagementMode": {
            "description": "encryption management mode for this enterprise Possible values are DISABLED, MANAGED, .", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "allowed_choices": [
                "DISABLED", 
                "MANAGED"
            ], 
            "orderable": true, 
            "type": "enum"
        }, 
        "receiveMultiCastListID": {
            "description": "Readonly ID of the auto generated receive multicast list associated with this enterprise profile", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
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
        "allowAdvancedQOSConfiguration": {
            "description": "Controls whether this enterprise has access to advanced QoS settings.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "boolean"
        }
    }, 
    "model": {
        "resource_name": "enterpriseprofiles", 
        "description": "Enterprise profile, used to store an enterprise's policies, quota etc", 
        "entity_name": "EnterpriseProfile", 
        "package": "usermgmt", 
        "get": true, 
        "update": true, 
        "rest_name": "enterpriseprofile", 
        "extends": [
            "@base", 
            "@metadata"
        ], 
        "delete": true
    }, 
    "children": {
        "externalservice": {
            "update": true, 
            "relationship": "child", 
            "get": true
        }, 
        "multicastlist": {
            "relationship": "child", 
            "get": true
        }, 
        "eventlog": {
            "relationship": "child", 
            "get": true
        }, 
        "enterprise": {
            "relationship": "child", 
            "get": true
        }
    }
}