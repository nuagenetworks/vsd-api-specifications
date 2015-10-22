{
    "attributes": {
        "userName": {
            "description": "Unique Username of the user. Valid characters are alphabets, numbers and hyphen( - ).", 
            "format": "free", 
            "filterable": true, 
            "uniqueScope": "no", 
            "required": true, 
            "exposed": true, 
            "orderable": true, 
            "type": "string"
        }, 
        "mobileNumber": {
            "description": "Mobile Number of the user", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "firstName": {
            "description": "First name of the user", 
            "format": "free", 
            "filterable": true, 
            "uniqueScope": "no", 
            "required": true, 
            "exposed": true, 
            "orderable": true, 
            "type": "string"
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
        "enterpriseName": {
            "description": "Name of the enterprise.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "disabled": {
            "description": "Status of the user account; true=disabled, false=not disabled; default value = false", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "boolean"
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
        "enterpriseID": {
            "description": "Identifier of the enterprise.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "role": {
            "description": "Role of the user.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "lastName": {
            "description": "Last name of the user", 
            "format": "free", 
            "filterable": true, 
            "uniqueScope": "no", 
            "required": true, 
            "exposed": true, 
            "orderable": true, 
            "type": "string"
        }, 
        "password": {
            "description": "User password stored as a hash (SHA-1 encrpted)", 
            "format": "free", 
            "filterable": true, 
            "uniqueScope": "no", 
            "required": true, 
            "exposed": true, 
            "orderable": true, 
            "type": "string"
        }, 
        "email": {
            "description": "Email address of the user", 
            "format": "free", 
            "filterable": true, 
            "uniqueScope": "no", 
            "required": true, 
            "exposed": true, 
            "orderable": true, 
            "type": "string"
        }
    }, 
    "model": {
        "resource_name": "me", 
        "description": "Object that identifies the user functions", 
        "entity_name": "Me", 
        "package": "usermgmt", 
        "rest_name": "me", 
        "extends": [
            "@base", 
            "@metadata"
        ]
    }, 
    "children": {
        "vsp": {
            "relationship": "root", 
            "get": true
        }, 
        "ingressadvfwdentrytemplate": {
            "relationship": "root", 
            "get": true
        }, 
        "domain": {
            "relationship": "root", 
            "get": true
        }, 
        "egressqospolicy": {
            "create": true, 
            "relationship": "root", 
            "get": true
        }, 
        "autodiscoveredgateway": {
            "relationship": "root", 
            "get": true
        }, 
        "sharednetworkresource": {
            "create": true, 
            "relationship": "root", 
            "get": true
        }, 
        "mirrordestination": {
            "create": true, 
            "relationship": "root", 
            "get": true
        }, 
        "networklayout": {
            "relationship": "root", 
            "get": true
        }, 
        "multicastchannelmap": {
            "create": true, 
            "relationship": "root", 
            "get": true
        }, 
        "redundancygroup": {
            "create": true, 
            "relationship": "root", 
            "get": true
        }, 
        "gateway": {
            "create": true, 
            "relationship": "root", 
            "get": true
        }, 
        "tca": {
            "relationship": "root", 
            "get": true
        }, 
        "nsgateway": {
            "relationship": "root", 
            "get": true
        }, 
        "policygroup": {
            "relationship": "root", 
            "get": true
        }, 
        "ratelimiter": {
            "create": true, 
            "relationship": "root", 
            "get": true
        }, 
        "certificate": {
            "create": true, 
            "relationship": "root"
        }, 
        "floatingip": {
            "relationship": "root", 
            "get": true
        }, 
        "egressacltemplate": {
            "relationship": "root", 
            "get": true
        }, 
        "patnatpool": {
            "create": true, 
            "relationship": "root", 
            "get": true
        }, 
        "infrastructuregatewayprofile": {
            "create": true, 
            "relationship": "root", 
            "get": true
        }, 
        "infrastructureportprofile": {
            "create": true, 
            "relationship": "root", 
            "get": true
        }, 
        "nsgredundancygroup": {
            "relationship": "root", 
            "get": true
        }, 
        "externalservice": {
            "create": true, 
            "relationship": "root", 
            "get": true
        }, 
        "eamconfig": {
            "create": true, 
            "update": true, 
            "relationship": "root", 
            "get": true
        }, 
        "applicationservice": {
            "create": true, 
            "relationship": "root", 
            "get": true
        }, 
        "statisticscollector": {
            "relationship": "root", 
            "get": true
        }, 
        "vcenter": {
            "create": true, 
            "relationship": "root", 
            "get": true
        }, 
        "ingressaclentrytemplate": {
            "relationship": "root", 
            "get": true
        }, 
        "gatewaytemplate": {
            "create": true, 
            "relationship": "root", 
            "get": true
        }, 
        "vrsconfig": {
            "relationship": "root", 
            "get": true
        }, 
        "nsportstaticconfiguration": {
            "relationship": "root", 
            "get": true
        }, 
        "infrastructurevscprofile": {
            "create": true, 
            "relationship": "root", 
            "get": true
        }, 
        "subnet": {
            "relationship": "root", 
            "get": true
        }, 
        "l2domain": {
            "relationship": "root", 
            "get": true
        }, 
        "hostinterface": {
            "relationship": "root", 
            "get": true
        }, 
        "site": {
            "create": true, 
            "relationship": "root", 
            "get": true
        }, 
        "uplinkroutedistinguisher": {
            "relationship": "root", 
            "get": true
        }, 
        "externalappservice": {
            "create": true, 
            "relationship": "root", 
            "get": true
        }, 
        "job": {
            "create": true, 
            "relationship": "root", 
            "get": true
        }, 
        "vminterface": {
            "relationship": "root", 
            "get": true
        }, 
        "staticroute": {
            "relationship": "root", 
            "get": true
        }, 
        "vcenterhypervisor": {
            "relationship": "root", 
            "get": true
        }, 
        "metadatatag": {
            "create": true, 
            "relationship": "root", 
            "get": true
        }, 
        "redirectiontarget": {
            "relationship": "root", 
            "get": true
        }, 
        "zone": {
            "relationship": "root", 
            "get": true
        }, 
        "license": {
            "create": true, 
            "relationship": "root", 
            "get": true
        }, 
        "enterpriseprofile": {
            "create": true, 
            "relationship": "root", 
            "get": true
        }, 
        "egressaclentrytemplate": {
            "relationship": "root", 
            "get": true
        }, 
        "globalmetadata": {
            "create": true, 
            "relationship": "root", 
            "get": true
        }, 
        "nsgatewaytemplate": {
            "create": true, 
            "relationship": "root", 
            "get": true
        }, 
        "systemconfig": {
            "relationship": "root", 
            "get": true
        }, 
        "enterprise": {
            "create": true, 
            "relationship": "root", 
            "get": true
        }, 
        "vm": {
            "create": true, 
            "relationship": "root", 
            "get": true
        }, 
        "ingressacltemplate": {
            "relationship": "root", 
            "get": true
        }, 
        "cms": {
            "create": true, 
            "relationship": "root", 
            "get": true
        }, 
        "user": {
            "create": true, 
            "relationship": "root", 
            "get": true
        }
    }
}