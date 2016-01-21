{
    "attributes": {
        "actualType": {
            "description": "This will be used to send actual type instead of the hexadecimal. Note: If actualType is set, it will override the entry set in the type attribute",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "integer",
            "uniqueScope": "no"
        },
        "actualValues": {
            "description": "This will be used to send actual values instead of the hexadecimal. Note: If actualValues are set, it will override entry set in the value attribute",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "list",
            "subtype": "string",
            "uniqueScope": "no"
        },
        "length": {
            "description": "DHCP option length. Length should be a hexadecimal value(ie. Hex value 0x04 would be passed as '04')",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "required": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "type": {
            "description": "DHCP option type. Type should be a hexadecimal value(ie. Hex value 0x06 would be passed as '06')",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "required": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "value": {
            "description": "DHCP option value. Value should be a hexadecimal value(ie. Hex value 0xac40 would be passed as 'ac40')",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "required": true,
            "type": "string",
            "uniqueScope": "no"
        }
    },
    "children": {
        "eventlog": {
            "get": true,
            "relationship": "child"
        }
    },
    "model": {
        "delete": true,
        "description": "Allows the definition of one or more DHCP options that will be provided to all VMs that are associated with a given domain. DHCP options are provided as Type- Length-Value (TLV). There is no validation by VSD on whether these options are valid or not. It is up to the user to guarantee that the options make sense for their application",
        "entity_name": "DHCPOption",
        "extends": [
            "@base",
            "@audited",
            "@metadata"
        ],
        "get": true,
        "package": "network",
        "resource_name": "dhcpoptions",
        "rest_name": "dhcpoption",
        "update": true
    }
}