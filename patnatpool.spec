{
    "attributes": {
        "addressRange": {
            "description": "Pool of IP Address that is available for use ex : 130.12.0.0/16", 
            "exposed": true, 
            "required": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "associatedGatewayId": {
            "description": "Default PAT IP Address, must belong to the pool above", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "associatedGatewayType": {
            "description": "", 
            "exposed": true, 
            "type": "enum", 
            "uniqueScope": "no"
        }, 
        "defaultPATIP": {
            "description": "Default PAT IP Address, must belong to the pool above", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "description": {
            "description": "A description of the PATNATPool", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "name": {
            "description": "Name of the PATNATPool", 
            "exposed": true, 
            "required": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "permittedAction": {
            "allowed_choices": [
                "EXTEND", 
                "INSTANTIATE", 
                "DEPLOY", 
                "USE", 
                "READ", 
                "ALL"
            ], 
            "description": "The permitted  action to USE/EXTEND  this Gateway Possible values are USE, READ, ALL, INSTANTIATE, EXTEND, DEPLOY, .", 
            "exposed": true, 
            "type": "enum", 
            "uniqueScope": "no"
        }
    }, 
    "children": {
        "enterprisepermission": {
            "create": true, 
            "get": true, 
            "relationship": "child"
        }, 
        "natmapentry": {
            "create": true, 
            "get": true, 
            "relationship": "child"
        }
    }, 
    "delete": true, 
    "description": "Represents PAT NAT Pool object.", 
    "entity_name": "PATNATPool", 
    "extends": [
        "@base", 
        "@metadata"
    ], 
    "get": true, 
    "package": "/gateway", 
    "resource_name": "patnatpools", 
    "rest_name": "patnatpool", 
    "update": true
}