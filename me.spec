{
    "attributes": {
        "avatarData": {
            "description": "URL to the avatar data associated with the enterprise. If the avatarType is URL then value of avatarData should an URL of the image. If the avatarType BASE64 then avatarData should be BASE64 encoded value of the image",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
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
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "enum",
            "uniqueScope": "no"
        },
        "disabled": {
            "description": "Status of the user account; true=disabled, false=not disabled; default value = false",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "boolean",
            "uniqueScope": "no"
        },
        "email": {
            "description": "Email address of the user",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "required": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "enterpriseID": {
            "description": "Identifier of the enterprise.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "enterpriseName": {
            "description": "Name of the enterprise.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "firstName": {
            "description": "First name of the user",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "required": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "lastName": {
            "description": "Last name of the user",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "required": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "mobileNumber": {
            "description": "Mobile Number of the user",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "password": {
            "description": "User password stored as a hash (SHA-1 encrpted)",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "required": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "role": {
            "description": "Role of the user.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "userName": {
            "description": "Unique Username of the user. Valid characters are alphabets, numbers and hyphen( - ).",
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
        "applicationservice": {
            "create": true,
            "get": true,
            "relationship": "root"
        },
        "autodiscoveredgateway": {
            "get": true,
            "relationship": "root"
        },
        "certificate": {
            "create": true,
            "relationship": "root"
        },
        "cms": {
            "create": true,
            "get": true,
            "relationship": "root"
        },
        "domain": {
            "get": true,
            "relationship": "root"
        },
        "eamconfig": {
            "create": true,
            "get": true,
            "relationship": "root",
            "update": true
        },
        "egressaclentrytemplate": {
            "get": true,
            "relationship": "root"
        },
        "egressacltemplate": {
            "get": true,
            "relationship": "root"
        },
        "egressqospolicy": {
            "create": true,
            "get": true,
            "relationship": "root"
        },
        "enterprise": {
            "create": true,
            "get": true,
            "relationship": "root"
        },
        "enterpriseprofile": {
            "create": true,
            "get": true,
            "relationship": "root"
        },
        "externalappservice": {
            "create": true,
            "get": true,
            "relationship": "root"
        },
        "externalservice": {
            "create": true,
            "get": true,
            "relationship": "root"
        },
        "floatingip": {
            "get": true,
            "relationship": "root"
        },
        "gateway": {
            "create": true,
            "get": true,
            "relationship": "root"
        },
        "gatewaytemplate": {
            "create": true,
            "get": true,
            "relationship": "root"
        },
        "globalmetadata": {
            "create": true,
            "get": true,
            "relationship": "root"
        },
        "hostinterface": {
            "get": true,
            "relationship": "root"
        },
        "infrastructuregatewayprofile": {
            "create": true,
            "get": true,
            "relationship": "root"
        },
        "infrastructureportprofile": {
            "create": true,
            "get": true,
            "relationship": "root"
        },
        "infrastructurevscprofile": {
            "create": true,
            "get": true,
            "relationship": "root"
        },
        "ingressaclentrytemplate": {
            "get": true,
            "relationship": "root"
        },
        "ingressacltemplate": {
            "get": true,
            "relationship": "root"
        },
        "ingressadvfwdentrytemplate": {
            "get": true,
            "relationship": "root"
        },
        "job": {
            "create": true,
            "get": true,
            "relationship": "root"
        },
        "l2domain": {
            "get": true,
            "relationship": "root"
        },
        "license": {
            "create": true,
            "get": true,
            "relationship": "root"
        },
        "metadatatag": {
            "create": true,
            "get": true,
            "relationship": "root"
        },
        "mirrordestination": {
            "create": true,
            "get": true,
            "relationship": "root"
        },
        "multicastchannelmap": {
            "create": true,
            "get": true,
            "relationship": "root"
        },
        "networklayout": {
            "get": true,
            "relationship": "root"
        },
        "nsgateway": {
            "get": true,
            "relationship": "root"
        },
        "nsgatewaytemplate": {
            "create": true,
            "get": true,
            "relationship": "root"
        },
        "nsgredundancygroup": {
            "get": true,
            "relationship": "root"
        },
        "nsportstaticconfiguration": {
            "get": true,
            "relationship": "root"
        },
        "patmapper": {
            "create": true,
            "get": true,
            "relationship": "root"
        },
        "patnatpool": {
            "create": true,
            "get": true,
            "relationship": "root"
        },
        "policygroup": {
            "get": true,
            "relationship": "root"
        },
        "ratelimiter": {
            "create": true,
            "get": true,
            "relationship": "root"
        },
        "redirectiontarget": {
            "get": true,
            "relationship": "root"
        },
        "redundancygroup": {
            "create": true,
            "get": true,
            "relationship": "root"
        },
        "sharednetworkresource": {
            "create": true,
            "get": true,
            "relationship": "root"
        },
        "site": {
            "create": true,
            "get": true,
            "relationship": "root"
        },
        "staticroute": {
            "get": true,
            "relationship": "root"
        },
        "statisticscollector": {
            "get": true,
            "relationship": "root"
        },
        "subnet": {
            "get": true,
            "relationship": "root"
        },
        "systemconfig": {
            "get": true,
            "relationship": "root"
        },
        "tca": {
            "get": true,
            "relationship": "root"
        },
        "uplinkroutedistinguisher": {
            "get": true,
            "relationship": "root"
        },
        "user": {
            "create": true,
            "get": true,
            "relationship": "root"
        },
        "vcenter": {
            "create": true,
            "get": true,
            "relationship": "root"
        },
        "vcenterhypervisor": {
            "get": true,
            "relationship": "root"
        },
        "vm": {
            "create": true,
            "get": true,
            "relationship": "root"
        },
        "vminterface": {
            "get": true,
            "relationship": "root"
        },
        "vrsconfig": {
            "get": true,
            "relationship": "root"
        },
        "vsp": {
            "get": true,
            "relationship": "root"
        },
        "zone": {
            "get": true,
            "relationship": "root"
        }
    },
    "model": {
        "description": "Object that identifies the user functions",
        "entity_name": "Me",
        "extends": [
            "@audited",
            "@base",
            "@metadata"
        ],
        "package": "usermgmt",
        "resource_name": "me",
        "rest_name": "me",
        "root": true
    }
}