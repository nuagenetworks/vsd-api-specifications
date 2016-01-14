{
    "attributes": {
        "addressType": {
            "allowed_choices": [
                "fqdn", 
                "ip"
            ], 
            "description": "Type for stats collector address Possible values are ip, fqdn, .", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "enum", 
            "uniqueScope": "no"
        }, 
        "ipAddress": {
            "description": "IP address(es) of the stats collector process", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "port": {
            "description": "Port(s) of the stats collector process", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "protoBufPort": {
            "description": "Protobuf Port(s) of the stats collector process", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }
    }, 
    "model": {
        "delete": true, 
        "description": "Identifies the IP address of the stats collector entity that must be used", 
        "entity_name": "StatsCollectorInfo", 
        "extends": [
            "@base", 
            "@audited",
            "@metadata"
        ], 
        "get": true, 
        "package": "stats", 
        "resource_name": "statisticscollector", 
        "rest_name": "statisticscollector", 
        "update": true
    }
}