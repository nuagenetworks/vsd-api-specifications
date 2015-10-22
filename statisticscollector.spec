{
    "attributes": {
        "protoBufPort": {
            "description": "Protobuf Port(s) of the stats collector process", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "addressType": {
            "description": "Type for stats collector address Possible values are ip, fqdn, .", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "allowed_choices": [
                "fqdn", 
                "ip"
            ], 
            "orderable": true, 
            "type": "enum"
        }, 
        "ipAddress": {
            "description": "IP address(es) of the stats collector process", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "port": {
            "description": "Port(s) of the stats collector process", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }
    }, 
    "model": {
        "resource_name": "statisticscollector", 
        "description": "Identifies the IP address of the stats collector entity that must be used", 
        "entity_name": "StatsCollectorInfo", 
        "package": "stats", 
        "get": true, 
        "update": true, 
        "rest_name": "statisticscollector", 
        "extends": [
            "@base", 
            "@metadata"
        ], 
        "delete": true
    }
}