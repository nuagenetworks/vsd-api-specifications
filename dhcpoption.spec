{
    "attributes": {
        "actualType": {
            "description": "This will be used to send actual type instead of the hexadecimal. Note: If actualType is set, it will override the entry set in the type attribute", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "integer"
        }, 
        "actualValues": {
            "description": "This will be used to send actual values instead of the hexadecimal. Note: If actualValues are set, it will override entry set in the value attribute", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "list"
        }, 
        "length": {
            "description": "DHCP option length. Length should be a hexadecimal value(ie. Hex value 0x04 would be passed as '04')", 
            "format": "free", 
            "filterable": true, 
            "uniqueScope": "no", 
            "required": true, 
            "exposed": true, 
            "orderable": true, 
            "type": "string"
        }, 
        "type": {
            "description": "DHCP option type. Type should be a hexadecimal value(ie. Hex value 0x06 would be passed as '06')", 
            "format": "free", 
            "filterable": true, 
            "uniqueScope": "no", 
            "required": true, 
            "exposed": true, 
            "orderable": true, 
            "type": "string"
        }, 
        "value": {
            "description": "DHCP option value. Value should be a hexadecimal value(ie. Hex value 0xac40 would be passed as 'ac40')", 
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
        "resource_name": "dhcpoptions", 
        "description": "Allows the definition of one or more DHCP options that will be provided to all VMs that are associated with a given domain. DHCP options are provided as Type- Length-Value (TLV). There is no validation by VSD on whether these options are valid or not. It is up to the user to guarantee that the options make sense for their application", 
        "entity_name": "DHCPOption", 
        "package": "network", 
        "get": true, 
        "update": true, 
        "rest_name": "dhcpoption", 
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