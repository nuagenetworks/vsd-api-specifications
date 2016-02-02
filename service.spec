{
    "attributes": {
        "IRBEnabled": {
            "description": "Determines whether Integrated Routing and Bridging is enabled on the WAN Service",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "boolean",
            "uniqueScope": "no"
        },
        "WANServiceIdentifier": {
            "description": "Identifier of the WAN Service",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 255,
            "min_length": 1,
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "associatedDomainID": {
            "description": "ID of the entity to which the WAN Service is attached to. This could be ID DOMAIN/L2DOMAIN",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "associatedVPNConnectID": {
            "description": "The associated vpn connect ID.",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "configType": {
            "allowed_choices": [
                "STATIC",
                "DYNAMIC"
            ],
            "description": "Type of the CONFIG -  STATIC Possible values are STATIC, DYNAMIC, .",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "enum",
            "uniqueScope": "no"
        },
        "description": {
            "description": "A description of the WAN Service",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 255,
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "domainName": {
            "description": "The associated domain name.",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "enterpriseName": {
            "description": "The associated enterprise name.",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "externalRouteTarget": {
            "description": "Route target associated with the WAN. It is an optional parameterthat can be provided by the user",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 255,
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "name": {
            "description": "Name of the WAN Service",
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
        "orphan": {
            "description": "Indicates if this WAN Service is orphan or not.",
            "exposed": true,
            "format": "free",
            "type": "boolean",
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
            "format": "free",
            "type": "enum",
            "uniqueScope": "no"
        },
        "servicePolicy": {
            "description": "Name of 7X50 Policy assoicated with service",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 32,
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "serviceType": {
            "allowed_choices": [
                "L2",
                "L3"
            ],
            "description": "Type of the SERVICE -  L3,L2 Possible values are L3, L2, .",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "required": true,
            "type": "enum",
            "uniqueScope": "no"
        },
        "tunnelType": {
            "allowed_choices": [
                "DC_DEFAULT",
                "VXLAN",
                "GRE"
            ],
            "description": "Type of the SERVICE - GRE,VXLAN Possible values are DC_DEFAULT, GRE, VXLAN, .",
            "exposed": true,
            "format": "free",
            "type": "enum",
            "uniqueScope": "no"
        },
        "useUserMnemonic": {
            "description": "Determines whether to use user mnemonic of the WAN Service",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "boolean",
            "uniqueScope": "no"
        },
        "userMnemonic": {
            "description": "user mnemonic of the WAN Service",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 255,
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "vnId": {
            "description": "VNID of the BackHaul Subnet of L3Domain /L2Domain to which this WANService is associated",
            "exposed": true,
            "format": "free",
            "type": "integer",
            "uniqueScope": "no"
        }
    },
    "children": {
        "alarm": {
            "get": true,
            "relationship": "child"
        },
        "enterprisepermission": {
            "create": true,
            "get": true,
            "relationship": "child"
        },
        "eventlog": {
            "get": true,
            "relationship": "child"
        },
        "permission": {
            "create": true,
            "get": true,
            "relationship": "child"
        }
    },
    "model": {
        "delete": true,
        "description": "Represents WAN Service Object.",
        "entity_name": "WANService",
        "extends": [
            "@audited",
            "@base",
            "@metadata"
        ],
        "get": true,
        "package": "gateway",
        "resource_name": "services",
        "rest_name": "service",
        "update": true
    }
}