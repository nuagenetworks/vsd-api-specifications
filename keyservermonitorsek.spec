{
    "attributes": {
        "creationTime": {
            "description": "The time this entry was created (milliseconds since epoch)",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "subtype": "long",
            "type": "integer",
            "uniqueScope": "no"
        },
        "lifetime": {
            "description": "The lifetime of this entry (seconds)",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "integer",
            "uniqueScope": "no"
        },
        "seedPayloadAuthenticationAlgorithm": {
            "allowed_choices": [
                "HMAC_SHA1",
                "HMAC_SHA256",
                "HMAC_SHA512"
            ],
            "description": "SEK Payload Signature Algorithm Possible values are HMAC_SHA1, HMAC_SHA256, HMAC_SHA512, .",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "enum",
            "uniqueScope": "no"
        },
        "seedPayloadEncryptionAlgorithm": {
            "allowed_choices": [
                "AES_128_CBC",
                "AES_256_CBC",
                "TRIPLE_DES_CBC"
            ],
            "description": "SEK Payload Encryption Algorithm Possible values are AES_128_CBC, AES_256_CBC, TRIPLE_DES_CBC, .",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "enum",
            "uniqueScope": "no"
        },
        "startTime": {
            "description": "The time this entry  was activated (milliseconds since epoch)",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "subtype": "long",
            "type": "integer",
            "uniqueScope": "no"
        }
    },
    "children": {
        "keyservermonitorencryptedseed": {
            "get": true,
            "relationship": "child"
        },
        "keyservermonitorencryptedsek": {
            "get": true,
            "relationship": "child"
        }
    },
    "model": {
        "delete": true,
        "description": "Represents a Keyserver Monitor SEK Snapshot.",
        "entity_name": "KeyServerMonitorSEK",
        "extends": [
            "@audited",
            "@base",
            "@metadata"
        ],
        "get": true,
        "package": "keyserver",
        "resource_name": "keyservermonitorseks",
        "rest_name": "keyservermonitorsek",
        "update": true
    }
}