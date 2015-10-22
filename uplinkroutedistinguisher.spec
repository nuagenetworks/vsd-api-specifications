{
    "attributes": {
        "routeDistinguisher": {
            "description": "The uplink route distinguisher value is used to identify which route packets should be flowing through with regards to having multiple network ports on the VRS/NSG.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "uplinkType": {
            "description": "Indicates the uplink type associated with the instance of Uplink Route Distinguisher.  Default value is RD Primary1 Possible values are RD_PRIMARY1, RD_PRIMARY2, RD_SECONDARY1, RD_SECONDARY2, .", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "allowed_choices": [
                "RD_PRIMARY2", 
                "RD_PRIMARY1", 
                "RD_SECONDARY1", 
                "RD_SECONDARY2"
            ], 
            "orderable": true, 
            "type": "enum"
        }
    }, 
    "model": {
        "resource_name": "uplinkroutedistinguishers", 
        "description": "Represents a network port uplink Route Distinguisher value.", 
        "entity_name": "UplinkRD", 
        "package": "network", 
        "get": true, 
        "rest_name": "uplinkroutedistinguisher", 
        "extends": [
            "@base", 
            "@metadata"
        ]
    }
}