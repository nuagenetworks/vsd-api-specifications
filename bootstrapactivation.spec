{
    "attributes": {
        "action": {
            "description": "The bootstrap action to perform",
            "allowed_choices": [
                "INITIATE",
                "AUTHENTICATE",
                "CONFIRM",
                "ROLLBACK",
                "NEW_NCPE_AUTH_REQUIRED",
                "NO_AUTH_REQUIRED",
                "CERTIFICATE_SIGNED",
                "ROLLED_BACK",
                "BOOTSTRAP_COMPLETE",
                "UNSPECIFIED",
                "INITIATE_RENEW",
                "CERTIFICATE_RENEW",
                "CERTIFICATE_REVOKE"
            ],
            "exposed": true,
            "filterable": false,
            "orderable": false,
            "type": "enum",
            "uniqueScope": "no"
        },
        "cacert": {
            "description": "The CA Certificate Chain",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        },
        "cert": {
            "description": "The signed Certificate",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        },
        "configURL": {
            "description": "The configuration URL",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        },
        "csr": {
            "description": "The CSR of the request",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        },
        "hash": {
            "description": "The authentication hash of this request",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        },
        "seed": {
            "description": "The random seed for this request",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        },
        "srkPassword": {
            "description": "TPM SRK passphrase",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        },
        "status": {
            "description": "The agent status for the request",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        },
        "tpmOwnerPassword": {
            "description": "TPM owner passphrase",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        },
        "vsdTime": {
            "description": "VSD Server time when an NSG is initiating a Bootstrapping request",
            "exposed": true,
            "filterable": false,
            "orderable": false,
            "type": "integer",
            "subtype": "long",
            "uniqueScope": "no"
        }
    },
    "model": {
        "description": "NSG Gateway initiated Bootstrap Activation",
        "entity_name": "BootstrapActivation",
        "extends": [
            "@base",
            "@audited",
            "@metadata"
        ],
        "package": "gateway",
        "resource_name": "bootstrapactivations",
        "rest_name": "bootstrapactivation",
        "update": true
    }
}