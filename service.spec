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
            "orderable": true,
            "type": "string",
            "min_length": 1,
            "max_length": 255,
            "uniqueScope": "no"
        },
        "associatedDomainID": {
            "description": "ID of the entity to which the WAN Service is attached to. This could be ID DOMAIN/L2DOMAIN",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        },
        "associatedVPNConnectID": {
            "description": "The associated vpn connect ID.",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
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
            "orderable": true,
            "type": "string",
            "min_length": 0,
            "max_length": 255,
            "uniqueScope": "no"
        },
        "domainName": {
            "description": "The associated domain name.",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        },
        "enterpriseName": {
            "description": "The associated enterprise name.",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        },
        "externalRouteTarget": {
            "description": "Route target associated with the WAN. It is an optional parameterthat can be provided by the user",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string",
            "min_length": 0,
            "max_length": 255,
            "uniqueScope": "no"
        },
        "name": {
            "description": "Name of the WAN Service",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "required": true,
            "type": "string",
            "min_length": 1,
            "max_length": 255,
            "uniqueScope": "no"
        },
        "orphan": {
            "description": "Indicates if this WAN Service is orphan or not.",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
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
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "enum",
            "uniqueScope": "no"
        },
        "servicePolicy": {
            "description": "Name of 7X50 Policy assoicated with service",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string",
            "min_length": 0,
            "max_length": 32,
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
            "filterable": false,
            "format": "free",
            "orderable": false,
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
            "orderable": true,
            "type": "string",
            "min_length": 0,
            "max_length": 255,
            "uniqueScope": "no"
        },
        "vnId": {
            "description": "VNID of the BackHaul Subnet of L3Domain /L2Domain to which this WANService is associated",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "integer",
            "subtype": "long",
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
            "@base",
            "@audited",
            "@metadata"
        ],
        "get": true,
        "package": "gateway",
        "resource_name": "services",
        "rest_name": "service",
        "update": true
    }
}