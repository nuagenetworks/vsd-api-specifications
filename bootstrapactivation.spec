{
    "attributes": {
        "action": {
            "allowed_choices": [
                "AUTHENTICATE",
                "BOOTSTRAP_COMPLETE",
                "CERTIFICATE_RENEW",
                "CERTIFICATE_REVOKE",
                "CERTIFICATE_SIGNED",
                "CONFIRM",
                "INITIATE",
                "INITIATE_RENEW",
                "NEW_NCPE_AUTH_REQUIRED",
                "NO_AUTH_REQUIRED",
                "ROLLBACK",
                "ROLLED_BACK",
                "UNSPECIFIED"
            ],
            "description": "The bootstrap action to perform",
            "exposed": true,
            "format": "free",
            "type": "enum",
            "uniqueScope": "no"
        },
        "cacert": {
            "description": "The CA Certificate Chain",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "cert": {
            "description": "The signed Certificate",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "configURL": {
            "description": "The configuration URL",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "csr": {
            "description": "The CSR of the request",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "hash": {
            "description": "The authentication hash of this request",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "seed": {
            "description": "The random seed for this request",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "srkPassword": {
            "description": "TPM SRK passphrase",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "status": {
            "description": "The agent status for the request",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "tpmOwnerPassword": {
            "description": "TPM owner passphrase",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "vsdTime": {
            "description": "VSD Server time when an NSG is initiating a Bootstrapping request",
            "exposed": true,
            "format": "free",
            "subtype": "long",
            "type": "integer",
            "uniqueScope": "no"
        }
    },
    "model": {
        "description": "NSG Gateway initiated Bootstrap Activation.",
        "entity_name": "BootstrapActivation",
        "extends": [
            "@audited",
            "@base",
            "@metadata"
        ],
        "package": "gateway",
        "resource_name": "bootstrapactivations",
        "rest_name": "bootstrapactivation",
        "update": true
    }
}