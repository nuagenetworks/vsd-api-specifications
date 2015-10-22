{
    "attributes": {
        "direction": {
            "required": true, 
            "description": "Direction of the service. Default is UNIDIRECTIONAL. Possible values are UNIDIRECTIONAL, REFLEXIVE, .", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "allowed_choices": [
                "REFLEXIVE", 
                "UNIDIRECTIONAL"
            ], 
            "orderable": true, 
            "type": "enum"
        }, 
        "protocol": {
            "description": "Protocol that must be matched.  Needs to be 6 (TCP) or 17 (UDP)", 
            "format": "free", 
            "filterable": true, 
            "uniqueScope": "no", 
            "required": true, 
            "exposed": true, 
            "orderable": true, 
            "type": "string"
        }, 
        "description": {
            "description": "Description of the application service.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "etherType": {
            "description": "Ether type of the packet to be matched. Ether type can be * or a valid hexadecimal value", 
            "format": "free", 
            "filterable": true, 
            "uniqueScope": "no", 
            "required": true, 
            "exposed": true, 
            "orderable": true, 
            "type": "string"
        }, 
        "DSCP": {
            "description": "DSCP match condition to be set in the rule. It is either * or from 0-63. Required for etherType 0x0800", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "destinationPort": {
            "description": "The destination port to be matched if protocol is UDP or TCP. Value should be either * or single port number or a port range.", 
            "format": "free", 
            "filterable": true, 
            "uniqueScope": "no", 
            "required": true, 
            "exposed": true, 
            "orderable": true, 
            "type": "string"
        }, 
        "sourcePort": {
            "description": "Source port to be matched if protocol is UDP or TCP. Value can be either * or single port number or a port range.", 
            "format": "free", 
            "filterable": true, 
            "uniqueScope": "no", 
            "required": true, 
            "exposed": true, 
            "orderable": true, 
            "type": "string"
        }, 
        "name": {
            "description": "Name of the application service.", 
            "format": "free", 
            "filterable": true, 
            "uniqueScope": "no", 
            "required": true, 
            "exposed": true, 
            "orderable": true, 
            "type": "string"
        }
    }, 
    "model": {
        "resource_name": "applicationservices", 
        "description": "Represents a networking communication service.", 
        "entity_name": "ApplicationService", 
        "package": "appd", 
        "get": true, 
        "update": true, 
        "rest_name": "applicationservice", 
        "extends": [
            "@base", 
            "@metadata"
        ], 
        "delete": true
    }, 
    "children": {
        "eventlog": {
            "relationship": "child", 
            "get": true
        }
    }
}