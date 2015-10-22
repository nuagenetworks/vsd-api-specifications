{
    "attributes": {
        "publicKey": {
            "description": "The public key contained in this certificate.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "pemEncoded": {
            "description": "The PEM encoded certificate.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "issuerDN": {
            "description": "The distinguished name of the authority that issued this certificate.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "subjectDN": {
            "description": "The distinguished name of this certificate's end entity.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "serialNumber": {
            "description": "The serial number of this certificate.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "float"
        }
    }, 
    "model": {
        "resource_name": "certificates", 
        "description": "This object represents a X509 Certificate Request", 
        "entity_name": "Certificate", 
        "package": "certificate", 
        "rest_name": "certificate", 
        "extends": [
            "@base", 
            "@metadata"
        ]
    }
}