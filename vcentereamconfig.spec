{
    "attributes": {
        "eamServerIP": {
            "description": "The EAM server IP", 
            "exposed": true, 
            "required": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "eamServerPortNumber": {
            "description": "The EAM server port number", 
            "exposed": true, 
            "required": true, 
            "type": "integer", 
            "uniqueScope": "no"
        }, 
        "eamServerPortType": {
            "description": "The EAM server port Type", 
            "exposed": true, 
            "required": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "extensionKey": {
            "description": "Key of the extension that the solution registers", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "ovfURL": {
            "description": "The url for the ovf", 
            "exposed": true, 
            "required": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "vibURL": {
            "description": "The url for the optional vib", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }
    }, 
    "description": "The EAM solution configuration", 
    "entity_name": "VCenterEAMConfig", 
    "extends": [
        "@base", 
        "@metadata"
    ], 
    "package": "/vmware", 
    "resource_name": "eamconfigs", 
    "rest_name": "eamconfig"
}