{
    "attributes": {
        "PEMEncoded": {
            "type": "string",
            "format": "free",
            "description": "PEM Encoded Certificate",
            "filterable": true,
            "orderable": true,
            "exposed": true,
            "uniqueScope": "no"
        },
        "associatedEnterpriseID": {
            "type": "string",
            "format": "free",
            "description": "The ID of the associated Enterprise",
            "exposed": true,
            "uniqueScope": "no"
        },
        "description": {
            "type": "string",
            "format": "free",
            "description": "Description of the IKEv2 Authentication",
            "filterable": true,
            "orderable": true,
            "exposed": true,
            "uniqueScope": "no"
        },
        "issuerDN": {
            "type": "string",
            "format": "free",
            "description": "Issuer Distinguished Name of the Certificate - Read Only Attribute",
            "filterable": true,
            "orderable": true,
            "exposed": true,
            "uniqueScope": "no"
        },
        "name": {
            "type": "string",
            "format": "free",
            "description": "Name of the Encryption Profile",
            "filterable": true,
            "orderable": true,
            "min_length": 1,
            "max_length": 255,
            "exposed": true,
            "uniqueScope": "no"
        },
        "notAfter": {
            "type": "time",
            "description": "Date this Certificate is valid to - Read Only Attribute",
            "filterable": true,
            "orderable": true,
            "exposed": true,
            "uniqueScope": "no"
        },
        "notBefore": {
            "type": "time",
            "description": "Date this Certificate is valid from - Read Only Attribute",
            "filterable": true,
            "orderable": true,
            "exposed": true,
            "uniqueScope": "no"
        },
        "serialNumber": {
            "type": "integer",
            "subtype": "long",
            "description": "Serial Number of the Certificate - Read Only Attribute",
            "filterable": true,
            "orderable": true,
            "exposed": true,
            "uniqueScope": "no"
        },
        "subjectDN": {
            "type": "string",
            "format": "free",
            "description": "Subject Distinguished Name of the Certificate - Read Only Attribute",
            "filterable": true,
            "orderable": true,
            "exposed": true,
            "uniqueScope": "no"
        }
    },
    "children": { },
    "model": {
        "description": "Represents an IKEv2 Trusted Certificate",
        "entity_name": "IKEv2Certificate",
        "extends": [ "@audited", "@base", "@metadata" ],
        "package": "ikev2",
        "resource_name": "ikev2certificates",
        "rest_name": "ikev2certificate",
        "get": true,
        "delete": true,
        "update": true
    }
}