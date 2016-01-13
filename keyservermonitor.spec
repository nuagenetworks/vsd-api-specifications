{
    "attributes": {
        "enterpriseSecuredDataRecordCount": {
            "description": "Total number of Enterprise Secured Data records",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "integer",
            "subtype": "long",
            "uniqueScope": "no"
        },
        "gatewaySecuredDataRecordCount": {
            "description": "Total number of Gateway Secured Data records",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "integer",
            "subtype": "long",
            "uniqueScope": "no"
        },
        "keyserverMonitorEncryptedSEKCount": {
            "description": "Total number of Keyserver Monitor Encrypted SEK records",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "integer",
            "subtype": "long",
            "uniqueScope": "no"
        },
        "keyserverMonitorEncryptedSeedCount": {
            "description": "Total number of Keyserver Monitor Encrypted Seed records",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "integer",
            "subtype": "long",
            "uniqueScope": "no"
        },
        "keyserverMonitorSEKCount": {
            "description": "Total number of Keyserver Monitor SEK records",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "integer",
            "subtype": "long",
            "uniqueScope": "no"
        },
        "keyserverMonitorSeedCount": {
            "description": "Total number of Keyserver Monitor Seed records",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "integer",
            "subtype": "long",
            "uniqueScope": "no"
        },
        "lastUpdateTime": {
            "description": "The time the latest SEK or Seed was created/removed (milliseconds since epoch)",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "integer",
            "subtype": "long",
            "uniqueScope": "no"
        }
    },
    "children": {
        "keyservermonitorencryptedseed": {
            "create": true,
            "get": true,
            "relationship": "child"
        },
        "keyservermonitorencryptedsek": {
            "create": true,
            "get": true,
            "relationship": "child"
        },
        "keyservermonitorseed": {
            "create": true,
            "get": true,
            "relationship": "child"
        },
        "keyservermonitorsek": {
            "create": true,
            "get": true,
            "relationship": "child"
        }
    },
    "model": {
        "description": "Represents a Keyserver Monitor Snapshot",
        "entity_name": "KeyServerMonitor",
        "extends": [
            "@base",
            "@metadata"
        ],
        "get": true,
        "package": "keyserver",
        "resource_name": "keyservermonitors",
        "rest_name": "keyservermonitor",
        "update": true
    }
}