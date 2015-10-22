{
    "attributes": {
        "routeDistinguisher": {
            "description": "The uplink route distinguisher value is used to identify which route packets should be flowing through with regards to having multiple network ports on the VRS/NSG.", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "uplinkType": {
            "allowed_choices": [
                "RD_PRIMARY2", 
                "RD_PRIMARY1", 
                "RD_SECONDARY1", 
                "RD_SECONDARY2"
            ], 
            "description": "Indicates the uplink type associated with the instance of Uplink Route Distinguisher.  Default value is RD Primary1 Possible values are RD_PRIMARY1, RD_PRIMARY2, RD_SECONDARY1, RD_SECONDARY2, .", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "enum", 
            "uniqueScope": "no"
        }
    }, 
    "model": {
        "description": "Represents a network port uplink Route Distinguisher value.", 
        "entity_name": "UplinkRD", 
        "extends": [
            "@base", 
            "@metadata"
        ], 
        "get": true, 
        "package": "network", 
        "resource_name": "uplinkroutedistinguishers", 
        "rest_name": "uplinkroutedistinguisher"
    }
}