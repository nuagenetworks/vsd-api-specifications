{
    "attributes": {
        "DHCPManaged": {
            "description": "true if DHCP is enabled else it is false. This value is always true for network resource of type PUBLIC or FLOATING.",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "boolean",
            "uniqueScope": "no"
        },
        "ECMPCount": {
            "description": "Domain specific Equal-cost multi-path routing count, ECMPCount = 1 means no ECMP",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "integer",
            "uniqueScope": "no"
        },
        "accessRestrictionEnabled": {
            "description": "Boolean indicates that this shared network resource is avaiable to everyone by default or not",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "boolean",
            "uniqueScope": "no"
        },
        "address": {
            "description": "Address configured on the shared resource",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "required": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "backHaulRouteDistinguisher": {
            "description": "backHaulRouteDistinguisher of the Shared Resource",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "backHaulRouteTarget": {
            "description": "backHaulRouteTarget of the Shared Resource",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "backHaulVNID": {
            "description": "backHaulVNID of the Shared Resource",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "integer",
            "subtype": "long",
            "uniqueScope": "no"
        },
        "description": {
            "description": "Description of the shared resource",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        },
        "domainRouteDistinguisher": {
            "description": "Route distinguisher configured on the shared resource",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "domainRouteTarget": {
            "description": "Route target configured on the shared resource",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "gateway": {
            "description": "Gatemask configured on the shared resource",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "name": {
            "description": "Name of the shared resource. Valid characters are alphabets, numbers, space and hyphen( - ).",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "required": true,
            "type": "string",
            "min_length": 1,
            "max_length": 64,
            "uniqueScope": "no"
        },
        "netmask": {
            "description": "Netmask configured on the shared resource",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "required": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "permittedActionType": {
            "description": "Permitted action on this shared network resource",
            "allowed_choices": [
                "USE",
                "READ",
                "ALL",
                "INSTANTIATE",
                "EXTEND",
                "DEPLOY"
            ],
            "exposed": true,
            "filterable": true,
            "orderable": true,
            "type": "enum",
            "uniqueScope": "no"
        },
        "sharedResourceParentID": {
            "description": "Parent ID of the floating IP subnet to which this FIP subnet must be attached. If empty it will be created in a new domain.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "type": {
            "allowed_choices": [
                "PUBLIC",
                "FLOATING",
                "L2DOMAIN",
                "UPLINK_SUBNET"
            ],
            "description": "Type of the shared resource. This is an enum with possible values PUBLIC/FLOATING/L2DOMAIN/UPLINK_SUBNET",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "required": true,
            "type": "enum",
            "uniqueScope": "no"
        },
        "underlay": {
            "description": "Indicates whether this shared subnet is in underlay or not.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "boolean",
            "uniqueScope": "no"
        },
        "uplinkGWVlanAttachmentID": {
            "description": "VLAN ID to which this vport must be attached",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "uplinkInterfaceIP": {
            "description": "IP address of the host interface",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        },
        "uplinkInterfaceMAC": {
            "description": "MAC address of the host interface",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        },
        "uplinkVPortName": {
            "description": "Name of the uplink vport",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        },
        "vnID": {
            "description": "VNID of the Shared Resource",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "integer",
            "subtype": "long",
            "uniqueScope": "no"
        }
    },
    "children": {
        "addressrange": {
            "create": true,
            "get": true,
            "relationship": "child"
        },
        "dhcpoption": {
            "create": true,
            "get": true,
            "relationship": "child"
        },
        "enterprisepermission": {
            "create": true,
            "get": true,
            "relationship": "child"
        },
        "staticroute": {
            "create": true,
            "get": true,
            "relationship": "child"
        },
        "vpnconnection": {
            "create": true,
            "get": true,
            "relationship": "child"
        }
    },
    "model": {
        "delete": true,
        "description": "This defines shared infrastructure resources that are created by user with CSPROOT role. These resources can be used by all the enterprises in the data center for various purposes. Examples of  shared resources are public subnet, floating subnet, public L2 domain etc.",
        "entity_name": "SharedNetworkResource",
        "extends": [
            "@base",
            "@audited",
            "@metadata"
        ],
        "get": true,
        "package": "network",
        "resource_name": "sharednetworkresources",
        "rest_name": "sharednetworkresource",
        "update": true
    }
}