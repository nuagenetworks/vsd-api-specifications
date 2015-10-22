{
    "attributes": {
        "serviceType": {
            "required": true, 
            "description": "Type of the SERVICE -  L3,L2 Possible values are L3, L2, .", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "allowed_choices": [
                "L2", 
                "L3"
            ], 
            "orderable": true, 
            "type": "enum"
        }, 
        "associatedDomainID": {
            "description": "ID of the entity to which the WAN Service is attached to. This could be ID DOMAIN/L2DOMAIN", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "tunnelType": {
            "description": "Type of the SERVICE - GRE,VXLAN Possible values are DC_DEFAULT, GRE, VXLAN, .", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "allowed_choices": [
                "DC_DEFAULT", 
                "VXLAN", 
                "GRE"
            ], 
            "orderable": true, 
            "type": "enum"
        }, 
        "associatedVPNConnectID": {
            "description": "The associated vpn connect ID.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "domainName": {
            "description": "The associated domain name.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "userMnemonic": {
            "description": "user mnemonic of the WAN Service", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "IRBEnabled": {
            "description": "Determines whether Integrated Routing and Bridging is enabled on the WAN Service", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "boolean"
        }, 
        "vnId": {
            "description": "VNID of the BackHaul Subnet of L3Domain /L2Domain to which this WANService is associated", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "float"
        }, 
        "orphan": {
            "description": "Indicates if this WAN Service is orphan or not.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "boolean"
        }, 
        "name": {
            "description": "Name of the WAN Service", 
            "format": "free", 
            "filterable": true, 
            "uniqueScope": "no", 
            "required": true, 
            "exposed": true, 
            "orderable": true, 
            "type": "string"
        }, 
        "configType": {
            "description": "Type of the CONFIG -  STATIC Possible values are STATIC, DYNAMIC, .", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "allowed_choices": [
                "STATIC", 
                "DYNAMIC"
            ], 
            "orderable": true, 
            "type": "enum"
        }, 
        "enterpriseName": {
            "description": "The associated enterprise name.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "externalRouteTarget": {
            "description": "Route target associated with the WAN. It is an optional parameterthat can be provided by the user", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
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
        "WANServiceIdentifier": {
            "description": "Identifier of the WAN Service", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "useUserMnemonic": {
            "description": "Determines whether to use user mnemonic of the WAN Service", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "boolean"
        }, 
        "servicePolicy": {
            "description": "Name of 7X50 Policy assoicated with service", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "description": {
            "description": "A description of the WAN Service", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }
    }, 
    "model": {
        "resource_name": "services", 
        "description": "Represents WAN Service Object.", 
        "entity_name": "WANService", 
        "package": "gateway", 
        "get": true, 
        "update": true, 
        "rest_name": "service", 
        "extends": [
            "@base", 
            "@metadata"
        ], 
        "delete": true
    }, 
    "children": {
        "alarm": {
            "relationship": "child", 
            "get": true
        }, 
        "enterprisepermission": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }, 
        "eventlog": {
            "relationship": "child", 
            "get": true
        }, 
        "permission": {
            "create": true, 
            "relationship": "child", 
            "get": true
        }
    }
}