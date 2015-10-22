{
    "attributes": {
        "associatedGatewayId": {
            "description": "Default PAT IP Address, must belong to the pool above", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "associatedGatewayType": {
            "description": "", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "enum"
        }, 
        "name": {
            "description": "Name of the PATNATPool", 
            "format": "free", 
            "filterable": true, 
            "uniqueScope": "no", 
            "required": true, 
            "exposed": true, 
            "orderable": true, 
            "type": "string"
        }, 
        "addressRange": {
            "description": "Pool of IP Address that is available for use ex : 130.12.0.0/16", 
            "format": "free", 
            "filterable": true, 
            "uniqueScope": "no", 
            "required": true, 
            "exposed": true, 
            "orderable": true, 
            "type": "string"
        }, 
        "permittedAction": {
            "description": "The permitted  action to USE/EXTEND  this Gateway Possible values are USE, READ, ALL, INSTANTIATE, EXTEND, DEPLOY, .", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "allowed_choices": [
                "EXTEND", 
                "INSTANTIATE", 
                "DEPLOY", 
                "USE", 
                "READ", 
                "ALL"
            ], 
            "orderable": true, 
            "type": "enum"
        }, 
        "defaultPATIP": {
            "description": "Default PAT IP Address, must belong to the pool above", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "description": {
            "description": "A description of the PATNATPool", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }
    }, 
    "model": {
        "resource_name": "patnatpools", 
        "description": "Represents PAT NAT Pool object.", 
        "entity_name": "PATNATPool", 
        "package": "gateway", 
        "get": true, 
        "update": true, 
        "rest_name": "patnatpool", 
        "extends": [
            "@base", 
            "@metadata"
        ], 
        "delete": true
    }, 
    "children": {
        "natmapentry": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }, 
        "enterprisepermission": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }
    }
}