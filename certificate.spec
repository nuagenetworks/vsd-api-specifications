{
    "attributes": {
        "issuerDN": {
            "description": "The distinguished name of the authority that issued this certificate.",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        },
        "pemEncoded": {
            "description": "The PEM encoded certificate.",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        },
        "publicKey": {
            "description": "The public key contained in this certificate.",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        },
        "serialNumber": {
            "description": "The serial number of this certificate.",
            "exposed": true,
            "filterable": false,
            "orderable": false,
            "type": "integer",
            "subtype": "long",
            "uniqueScope": "no"
        },
        "subjectDN": {
            "description": "The distinguished name of this certificate's end entity.",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        }
    },
    "model": {
        "description": "This object represents a X509 Certificate Request",
        "entity_name": "Certificate",
        "extends": [
            "@base",
            "@metadata"
        ],
        "package": "certificate",
        "resource_name": "certificates",
        "rest_name": "certificate"
    }
}