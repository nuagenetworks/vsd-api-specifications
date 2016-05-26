{
    "attributes": [
        {
            "name": "issuerDN",
            "type": "string",
            "format": "free",
            "description": "Issuer DN",
            "exposed": true,
            "uniqueScope": "no"
        },
        {
            "name": "subjectDN",
            "type": "string",
            "format": "free",
            "description": "Subject DN",
            "exposed": true,
            "uniqueScope": "no"
        },
        {
            "name": "publicKey",
            "type": "string",
            "format": "free",
            "description": "Public Key",
            "exposed": true,
            "uniqueScope": "no"
        },
        {
            "name": "certificateSerialNumber",
            "type": "integer",
            "subtype": "long",
            "description": "Certificate serial number associated to the keyserver private key which it is currently signing with",
            "exposed": true,
            "uniqueScope": "no"
        },
        {
            "name": "fqdn",
            "type": "string",
            "format": "free",
            "description": "FQDN of the keyserver member",
            "exposed": true,
            "uniqueScope": "no"
        },
        {
            "name": "pemEncoded",
            "type": "string",
            "format": "free",
            "description": "PEM Encoded Certificate",
            "exposed": true,
            "uniqueScope": "no"
        }
    ],
    "children": [
    ],
    "model": {
        "description": "Represents a KeyServer",
        "entity_name": "KeyServerMember",
        "extends": [
            "@audited",
            "@base",
            "@metadata"
        ],
        "package": "keyserver",
        "resource_name": "keyservermembers",
        "rest_name": "keyservermember",
        "get": true,
        "update": true,
        "delete": true,
        "create": true
    }
}