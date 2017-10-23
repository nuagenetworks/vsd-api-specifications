{
    "attributes": [
        {
            "description": "Issuer DN",
            "exposed": true,
            "format": "free",
            "name": "issuerDN",
            "type": "string",
            "uniqueScope": "no"
        },
        {
            "description": "Subject DN",
            "exposed": true,
            "format": "free",
            "name": "subjectDN",
            "type": "string",
            "uniqueScope": "no"
        },
        {
            "description": "Public Key",
            "exposed": true,
            "format": "free",
            "name": "publicKey",
            "type": "string",
            "uniqueScope": "no"
        },
        {
            "description": "Certificate serial number associated to the keyserver private key which it is currently signing with",
            "exposed": true,
            "name": "certificateSerialNumber",
            "subtype": "long",
            "type": "integer",
            "uniqueScope": "no"
        },
        {
            "description": "FQDN of the keyserver member",
            "exposed": true,
            "format": "free",
            "name": "fqdn",
            "type": "string",
            "uniqueScope": "no"
        },
        {
            "description": "PEM Encoded Certificate",
            "exposed": true,
            "format": "free",
            "name": "pemEncoded",
            "type": "string",
            "uniqueScope": "no"
        }
    ],
    "children": [],
    "model": {
        "create": true,
        "delete": true,
        "description": "Represents a KeyServer",
        "entity_name": "KeyServerMember",
        "extends": [
            "@audited",
            "@base",
            "@metadata"
        ],
        "get": true,
        "package": "keyserver",
        "resource_name": "keyservermembers",
        "rest_name": "keyservermember",
        "update": true,
        "userlabel": "Key Server Member"
    }
}