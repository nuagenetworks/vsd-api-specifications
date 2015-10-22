{
    "attributes": {
        "action": {
            "description": "The bootstrap action to perform", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "cacert": {
            "description": "The CA Certificate Chain", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "cert": {
            "description": "The signed Certificate", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "configURL": {
            "description": "The configuration URL", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "csr": {
            "description": "The CSR of the request", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "hash": {
            "description": "The authentication hash of this request", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "seed": {
            "description": "The random seed for this request", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "srkPassword": {
            "description": "TPM SRK passphrase", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "status": {
            "description": "The agent status for the request", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "tpmOwnerPassword": {
            "description": "TPM owner passphrase", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }
    }, 
    "description": "NSG Gateway initiated Bootstrap Activation", 
    "entity_name": "BootstrapActivation", 
    "extends": [
        "@base", 
        "@metadata"
    ], 
    "package": "/gateway", 
    "resource_name": "bootstrapactivations", 
    "rest_name": "bootstrapactivation", 
    "update": true
}