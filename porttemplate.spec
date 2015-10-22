{
    "attributes": {
        "description": {
            "description": "A description of the Port", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "physicalName": {
            "description": "Identifier of the Port", 
            "format": "free", 
            "filterable": true, 
            "uniqueScope": "no", 
            "required": true, 
            "exposed": true, 
            "orderable": true, 
            "type": "string"
        }, 
        "VLANRange": {
            "description": "VLAN Range of the Port.  Format must conform to a-b,c,d-f where a,b,c,d,f are integers between 0 and 4095.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "associatedEgressQOSPolicyID": {
            "description": "ID of the Egress QOS Policy associated with this Vlan.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "portType": {
            "required": true, 
            "description": "Type of the Port - NETWORK, ACCESS Possible values are ACCESS, NETWORK, .", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "allowed_choices": [
                "ACCESS", 
                "NETWORK"
            ], 
            "orderable": true, 
            "type": "enum"
        }, 
        "name": {
            "description": "Name of the Port", 
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
        "resource_name": "porttemplates", 
        "description": "Represents Port Template object under a given gateway template object", 
        "entity_name": "PortTemplate", 
        "package": "gateway", 
        "get": true, 
        "update": true, 
        "rest_name": "porttemplate", 
        "extends": [
            "@base", 
            "@metadata"
        ], 
        "delete": true
    }, 
    "children": {
        "vlantemplate": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }
    }
}