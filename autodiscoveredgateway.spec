{
    "attributes": {
        "controllers": {
            "description": "Controllers to which this gateway instance is associated with.",
            "exposed": true,
            "format": "free",
            "subtype": "string",
            "type": "list",
            "uniqueScope": "no"
        },
        "description": {
            "description": "A description of the Gateway",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 255,
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "gatewayID": {
            "description": "The Gateway associated with this  Auto Discovered Gateway  . This is a read only attribute",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "name": {
            "description": "Name of the Gateway",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 255,
            "min_length": 1,
            "orderable": true,
            "required": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "peer": {
            "description": "The System ID of the peer gateway associated with this Gateway instance when it is discovered by the network manager (VSD) as being redundant.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 255,
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "personality": {
            "allowed_choices": [
                "DC7X50",
                "HARDWARE_VTEP",
                "NSG",
                "OTHER",
                "VRSG",
                "VSA",
                "VSG"
            ],
            "description": "Personality of the Gateway - VSG,VRSG,NONE,OTHER, cannot be changed after creation. Possible values are VSG, VSA, VRSG, DC7X50, NSG, HARDWARE_VTEP, OTHER, .",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "required": true,
            "type": "enum",
            "uniqueScope": "no"
        },
        "systemID": {
            "description": "Identifier of the Gateway",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 255,
            "min_length": 1,
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "vtep": {
            "description": "Represent the system ID or the Virtual IP of a service used by a Gateway (VSG for now) to establish a tunnel with a remote VSG or hypervisor.  The format of this field is consistent with an IP address.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 255,
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        }
    },
    "children": {
        "eventlog": {
            "get": true,
            "relationship": "child"
        },
        "nsport": {
            "get": true,
            "relationship": "child"
        },
        "port": {
            "get": true,
            "relationship": "child"
        },
        "service": {
            "get": true,
            "relationship": "child"
        }
    },
    "model": {
        "description": "Represents Auto discovered Gateway.",
        "entity_name": "AutoDiscoveredGateway",
        "extends": [
            "@audited",
            "@base",
            "@metadata"
        ],
        "get": true,
        "package": "gateway",
        "resource_name": "autodiscoveredgateways",
        "rest_name": "autodiscoveredgateway"
    }
}