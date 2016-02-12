{
    "attributes": {
        "SSLEnabled": {
            "description": "Enable SSL for communication with the LDAP server",
            "exposed": true,
            "format": "free",
            "type": "boolean",
            "uniqueScope": "no"
        },
        "acceptAllCertificates": {
            "description": "Accept all certificates from the LDAP server",
            "exposed": true,
            "format": "free",
            "type": "boolean",
            "uniqueScope": "no"
        },
        "authorizationEnabled": {
            "description": "To enable LDAP authorization for an enterprise, both authorizationEnabled and enabled attributes must be set to true. If enabled attribute is not set, this attribute is ignored. The relationship between enabled and authorizationEnabled attributes is as follows, enabled = true, authorizationEnabled = false, LDAP is used only for Authentication. enabled = true, authorizationEnabled = true, LDAP is used for both authentication and authorization. enabled = false, authorizationEnabled = true, LDAP is not used. enabled = false, authorizationEnabled = false, LDAP is not used.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "type": "boolean",
            "uniqueScope": "no"
        },
        "authorizingUserDN": {
            "description": "This attribute is a mandatory field for LDAP authorization. When LDAP is used for authorization for an enterprise, the user DN that will be used to verify the integrity of groups and users in LDAP server for the enterprise. For example, CN=groupAdmin,OU=VSD_USERS,OU=Personal,OU=Domain Users,DC=company,DC=com",
            "exposed": true,
            "format": "free",
            "required": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "certificate": {
            "description": "The certificate to authenticate with the LDAP server",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "enabled": {
            "description": "To enable LDAP authentication for an enterprise, set this attribute to true. If enabled is set to false, authorizationEnabled attribute is ignored and LDAP is not used for authentication as well as authorization. The relationship between enabled and authorizationEnabled attributes is as follows, enabled = true, authorizationEnabled = false, LDAP is used only for Authentication enabled = true, authorizationEnabled = true, LDAP is used for both authentication and authorization. enabled = false, authorizationEnabled = true, LDAP is not used. enabled = false, authorizationEnabled = false, LDAP is not used.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "type": "boolean",
            "uniqueScope": "no"
        },
        "groupDN": {
            "description": "This attribute is a mandatory field for LDAP authorization. When LDAP is used for authorization for an enterprise, the group DN will be used to get the list of VSD specific groups in LDAP server for the enterprise. For example, OU=VSDGroups,DC=company,DC=com",
            "exposed": true,
            "format": "free",
            "required": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "password": {
            "description": "This attribute is a mandatory field for LDAP authorization. Password that will be used to verify the integrity of groups and users in LDAP server for the enterprise.",
            "exposed": true,
            "format": "free",
            "max_length": 255,
            "min_length": 1,
            "type": "string",
            "uniqueScope": "no"
        },
        "port": {
            "description": "Port to be used for the LDAP server",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "required": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "server": {
            "description": "The LDAP server IP or FQDN",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "required": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "userDNTemplate": {
            "description": "The DN template to be used for authentication. The template needs to have a string _USERID_ in it. This will be replaced by  the userId of the user who makes the REST API call. For example, template UID=_USERID_,OU=company,DC=com will converted to  UID=admin,OU=company,DC=com and this will be used as DN for LDAP authentication.",
            "exposed": true,
            "format": "free",
            "required": true,
            "type": "string",
            "uniqueScope": "no"
        }
    },
    "model": {
        "description": "Configuration of LDAP parameters associated with an enterprise. This will enable authentication through an external LDAP server for this enterprise.",
        "entity_name": "LDAPConfiguration",
        "extends": [
            "@audited",
            "@base",
            "@metadata"
        ],
        "get": true,
        "package": "usermgmt",
        "resource_name": "ldapconfigurations",
        "rest_name": "ldapconfiguration",
        "update": true
    }
}