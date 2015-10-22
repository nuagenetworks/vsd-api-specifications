{
    "attributes": {
        "issuerDN": {
            "description": "The distinguished name of the authority that issued this certificate.", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "pemEncoded": {
            "description": "The PEM encoded certificate.", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "publicKey": {
            "description": "The public key contained in this certificate.", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "serialNumber": {
            "description": "The serial number of this certificate.", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "float", 
            "uniqueScope": "no"
        }, 
        "subjectDN": {
            "description": "The distinguished name of this certificate's end entity.", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }
    }, 
    "description": "This object represents a X509 Certificate Request", 
    "entity_name": "Certificate", 
    "extends": [
        "@base", 
        "@metadata"
    ], 
    "package": "/certificate", 
    "resource_name": "certificates", 
    "rest_name": "certificate"
}