{
    "attributes": {
        "lastUpdateTime": {
            "description": "The time the latest SEK or Seed was created/removed (milliseconds since epoch)", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "float"
        }, 
        "keyserverMonitorSeedCount": {
            "description": "Total number of Keyserver Monitor Seed records", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "float"
        }, 
        "keyserverMonitorEncryptedSeedCount": {
            "description": "Total number of Keyserver Monitor Encrypted Seed records", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "float"
        }, 
        "enterpriseSecuredDataRecordCount": {
            "description": "Total number of Enterprise Secured Data records", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "float"
        }, 
        "gatewaySecuredDataRecordCount": {
            "description": "Total number of Gateway Secured Data records", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "float"
        }, 
        "keyserverMonitorSEKCount": {
            "description": "Total number of Keyserver Monitor SEK records", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "float"
        }, 
        "keyserverMonitorEncryptedSEKCount": {
            "description": "Total number of Keyserver Monitor Encrypted SEK records", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "float"
        }
    }, 
    "model": {
        "resource_name": "keyservermonitors", 
        "description": "Represents a Keyserver Monitor Snapshot", 
        "entity_name": "KeyServerMonitor", 
        "package": "keyserver", 
        "get": true, 
        "update": true, 
        "rest_name": "keyservermonitor", 
        "extends": [
            "@base", 
            "@metadata"
        ]
    }, 
    "children": {
        "keyservermonitorsek": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }, 
        "keyservermonitorencryptedseed": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }, 
        "keyservermonitorencryptedsek": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }, 
        "keyservermonitorseed": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }
    }
}