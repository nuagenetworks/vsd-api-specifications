{
    "attributes": {
        "eamServerPortType": {
            "description": "The EAM server port Type", 
            "format": "free", 
            "filterable": true, 
            "uniqueScope": "no", 
            "required": true, 
            "exposed": true, 
            "orderable": true, 
            "type": "string"
        }, 
        "eamServerIP": {
            "description": "The EAM server IP", 
            "format": "free", 
            "filterable": true, 
            "uniqueScope": "no", 
            "required": true, 
            "exposed": true, 
            "orderable": true, 
            "type": "string"
        }, 
        "ovfURL": {
            "description": "The url for the ovf", 
            "format": "free", 
            "filterable": true, 
            "uniqueScope": "no", 
            "required": true, 
            "exposed": true, 
            "orderable": true, 
            "type": "string"
        }, 
        "extensionKey": {
            "description": "Key of the extension that the solution registers", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "vibURL": {
            "description": "The url for the optional vib", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "eamServerPortNumber": {
            "description": "The EAM server port number", 
            "format": "free", 
            "filterable": true, 
            "uniqueScope": "no", 
            "required": true, 
            "exposed": true, 
            "orderable": true, 
            "type": "integer"
        }
    }, 
    "model": {
        "resource_name": "eamconfigs", 
        "description": "The EAM solution configuration", 
        "entity_name": "VCenterEAMConfig", 
        "package": "vmware", 
        "rest_name": "eamconfig", 
        "extends": [
            "@base", 
            "@metadata"
        ]
    }
}