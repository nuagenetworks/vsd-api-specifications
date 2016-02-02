{
    "attributes": {
        "IPType": {
            "allowed_choices": [
                "IPV6",
                "IPV4"
            ],
            "description": "IPv4 or IPv6(only IPv4 is supported in R1.0) Possible values are IPV4, IPV6, .",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "enum",
            "uniqueScope": "no"
        },
        "address": {
            "description": "IP address of the subnet defined. In case of zone, this is an optional field for and allows users to allocate an IP address range to a zone. The VSD will auto-assign IP addresses to subnets from this range if a specific IP address is not defined for the subnet",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "associatedApplicationID": {
            "description": "The associated application ID.",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        },
        "associatedApplicationObjectID": {
            "description": "The associated application object ID.",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        },
        "associatedApplicationObjectType": {
            "description": "The associated application object type. Refer to API section for supported types.",
            "allowed_choices": [
                "UNSUPPORTED",
                "NETWORK_ELEMENT",
                "NETWORK_LAYOUT",
                "ENTERPRISE",
                "ENTERPRISE_PROFILE",
                "GROUP",
                "USER",
                "DOMAIN_FLOATING_IP_ACL_TEMPLATE",
                "DOMAIN_FLOATING_IP_ACL_TEMPLATE_ENTRY",
                "FLOATING_IP_ACL_TEMPLATE",
                "FLOATING_IP_ACL_TEMPLATE_ENTRY",
                "FLOATINGIP_ACL",
                "FLOATINGIP_ACL_ENTRY",
                "INGRESS_ACL_TEMPLATE",
                "INGRESS_ACL_TEMPLATE_ENTRY",
                "INGRESS_ACL",
                "INGRESS_ACL_ENTRY",
                "INGRESS_ADV_FWD_TEMPLATE",
                "INGRESS_ADV_FWD_TEMPLATE_ENTRY",
                "INGRESS_ADV_FWD",
                "INGRESS_ADV_FWD_ENTRY",
                "INGRESS_EXT_SERVICE_TEMPLATE",
                "INGRESS_EXT_SERVICE_TEMPLATE_ENTRY",
                "INGRESS_EXT_SERVICE",
                "INGRESS_EXT_SERVICE_ENTRY",
                "EGRESS_ACL_TEMPLATE",
                "EGRESS_ACL_TEMPLATE_ENTRY",
                "EGRESS_ACL",
                "EGRESS_ACL_ENTRY",
                "POLICING_POLICY",
                "SHAPING_POLICY",
                "QOS_PRIMITIVE",
                "EGRESS_QOS_PRIMITIVE",
                "EGRESS_QOS_QUEUE_MR",
                "EGRESS_QOS_MR",
                "PORT_MR",
                "RATE_LIMITER",
                "DSCP_FORWARDING_CLASS_MAPPING",
                "DSCP_FORWARDING_CLASS_TABLE",
                "APPLICATION",
                "VIRTUAL_MACHINE",
                "SUBNET",
                "ADDRESS_RANGE",
                "ADDRESS_RANGE_STATE",
                "IP_BINDING",
                "L2DOMAIN",
                "L2DOMAIN_SHARED",
                "L2DOMAIN_TEMPLATE",
                "SUBNET_ENTRY",
                "SUBNET_MAC_ENTRY",
                "ENTERPRISE_NETWORK",
                "NETWORK_MACRO_GROUP",
                "PUBLIC_NETWORK",
                "SUBNET_TEMPLATE",
                "VM_INTERFACE",
                "VM_DESCRIPTION",
                "POLICY_DECISION",
                "CUSTOMER_VRF_SEQUENCENO",
                "SERVICE_VRF_SEQUENCENO",
                "DOMAIN",
                "VPN_CONNECT",
                "ZONE",
                "FLOATINGIP",
                "SUBNET_POOL_ENTRY",
                "DOMAIN_TEMPLATE",
                "ZONE_TEMPLATE",
                "PERMISSION",
                "PERMITTED_ACTION",
                "STATS_TCA",
                "STATS_POLICY",
                "STATS_COLLECTOR",
                "STATISTICS",
                "ALARM",
                "EVENT_LOG",
                "DHCP_OPTION",
                "STATIC_ROUTE",
                "DC_CONFIG",
                "RESYNC",
                "VPRN_LABEL_SEQUENCENO",
                "LDAP_CONFIG",
                "LICENSE",
                "VPORT",
                "VPORT_GATEWAY_RESPONSE",
                "SERVICE_GATEWAY_RESPONSE",
                "SERVICES_GATEWAY_RESPONSE",
                "VPORTTAGTEMPLATE",
                "VPORTTAG",
                "POLICY_GROUP_TEMPLATE",
                "HOSTINTERFACE",
                "BRIDGEINTERFACE",
                "VIRTUAL_IP",
                "VPORT_TAG_BASE",
                "POLICY_GROUP",
                "VNID_SEQUENCENO",
                "ESI_SEQUENCENO",
                "SYSTEM_CONFIG",
                "SYSTEM_CONFIG_REQ",
                "SYSTEM_CONFIG_RESP",
                "SHARED_RESOURCE",
                "RTRD_SEQUENCENO",
                "RD_SEQUENCENO",
                "RTRD_ENTITY",
                "EVPN_BGP_COMMUNITY_TAG_SEQ_NO",
                "EVPN_BGP_COMMUNITY_TAG_ENTRY",
                "VPORT_MEDIATION_REQUEST",
                "NODE_EXECUTION_ERROR",
                "MIRROR_DESTINATION",
                "VPORT_MIRROR",
                "GATEWAY",
                "NSGATEWAY",
                "GATEWAY_TEMPLATE",
                "NSGATEWAY_TEMPLATE",
                "AUTO_DISC_GATEWAY",
                "PORT",
                "NSPORT",
                "NS_REDUNDANT_PORT",
                "VSG_REDUNDANT_PORT",
                "PORT_TEMPLATE",
                "NSPORT_TEMPLATE",
                "VLAN",
                "VLAN_TEMPLATE",
                "VLAN_CONFIG_RESPONSE",
                "REDUNDANT_GW_GRP",
                "NSREDUNDANT_GW_GRP",
                "WAN_SERVICE",
                "GATEWAY_VPORT_CONFIG",
                "GATEWAY_SERVICE_CONFIG",
                "GATEWAY_SERVICE_CONFIG_RESP",
                "GATEWAY_VPORT_CONFIG_RESP",
                "GATEWAY_CONFIG",
                "NSGATEWAY_CONFIG",
                "GATEWAY_CONFIG_RESP",
                "ENTERPRISE_CONFIG",
                "ENTERPRISE_CONFIG_RESP",
                "DHCP_CONFIG_RESP",
                "DHCP_ALLOC_MESSAGE",
                "VSC",
                "HSC",
                "VSD",
                "VRS",
                "STATSSERVER",
                "VSP",
                "VSD_COMPONENT",
                "SYSTEM_MONITORING",
                "DISKSTATS",
                "MONITORING_PORT",
                "BGPPEER",
                "JOB",
                "ENTERPRISE_PERMISSION",
                "VIRTUAL_MACHINE_REPORT",
                "BOOTSTRAP",
                "LOCATION",
                "BOOTSTRAP_ACTIVATION",
                "INFRASTRUCTURE_GATEWAY_PROFILE",
                "INFRASTRUCTURE_PORT_PROFILE",
                "INFRASTRUCTURE_VSC_PROFILE",
                "INFRASTRUCTURE_CONFIG",
                "NSPORT_STATIC_CONFIG",
                "NSG_NOTIFICATION",
                "SITE",
                "SITE_REQ",
                "HEALTH_REQ",
                "SITE_RES",
                "GEO_VM_REQ",
                "GEO_VM_RES",
                "GEO_VM_EVENT",
                "METADATA",
                "METADATA_TAG",
                "ENTITY_METADATA_BINDING",
                "CHILD_ENTITY_POLICY_CHANGE",
                "MULTI_NIC_VPORT",
                "BACK_HAUL_SERVICE_RESP",
                "MC_CHANNEL_MAP",
                "MC_LIST",
                "MC_RANGE",
                "LIBVIRT_INTERFACE",
                "APPD_APPLICATION",
                "APPD_SERVICE",
                "APPD_TIER",
                "APPD_FLOW",
                "APPD_FLOW_SECURITY_POLICY",
                "APPD_FLOW_FORWARDING_POLICY",
                "APPD_EXTERNAL_APP_SERVICE",
                "PATNATPOOL",
                "NATMAPENTRY",
                "PATCONFIG_CONFIG_RESP",
                "NETWORK_POLICY_GROUP",
                "ACLENTRY_LOCATION",
                "EXPORTIMPORT",
                "EXTERNAL_SERVICE",
                "ENDPOINT",
                "DOMAIN_CONFIG",
                "DOMAIN_CONFIG_RESP",
                "STATIC_ROUTE_RESP",
                "NEXT_HOP_RESP",
                "UPLINK_RD",
                "VMWARE_VCENTER_EAM_CONFIG",
                "VMWARE_VCENTER_VRS_CONFIG",
                "VMWARE_VCENTER",
                "VMWARE_VCENTER_DATACENTER",
                "VMWARE_VCENTER_CLUSTER",
                "VMWARE_VCENTER_HYPERVISOR",
                "VMWARE_VRS_ADDRESS_RANGE",
                "VMWARE_VCENTER_VRS_BASE_CONFIG",
                "VMWARE_RELOAD_CONFIG",
                "CLOUD_MGMT_SYSTEM",
                "IKEV2_ENCRYPTION_PROFILE",
                "IKEV2_GATEWAY",
                "GROUPKEY_ENCRYPTION_PROFILE",
                "KEYSERVER_MEMBER",
                "KEYSERVER_MONITOR",
                "KEYSERVER_MONITOR_SEED",
                "KEYSERVER_MONITOR_ENCRYPTED_SEED",
                "KEYSERVER_MONITOR_SEK",
                "KEYSERVER_NOTIFICATION",
                "ENTERPRISE_SECURITY",
                "ENTERPRISE_SECURED_DATA",
                "GATEWAY_SECURITY",
                "GATEWAY_SECURITY_REQUEST",
                "GATEWAY_SECURITY_RESPONSE",
                "GATEWAY_SECURITY_PROFILE",
                "GATEWAY_SECURITY_PROFILE_REQUEST",
                "GATEWAY_SECURITY_PROFILE_RESPONSE",
                "GATEWAY_SECURED_DATA",
                "CERTIFICATE",
                "BGP_PROFILE",
                "ROUTING_POLICY",
                "BGP_NEIGHBOR",
                "BGP_PROFILE_MED_RESPONSE",
                "ROUTING_POL_MED_RESPONSE",
                "BGP_NEIGHBOR_MED_RESPONSE"
            ],
            "exposed": true,
            "filterable": true,
            "orderable": true,
            "type": "enum",
            "uniqueScope": "no"
        },
        "associatedMulticastChannelMapID": {
            "description": "The ID of the Multi Cast Channel Map  this zone/zone template is associated with. This has to be set when  enableMultiCast is set to ENABLED",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        },
        "description": {
            "description": "A description of the zone",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": false,
            "type": "string",
            "min_length": 0,
            "max_length": 255,
            "uniqueScope": "no"
        },
        "encryption": {
            "allowed_choices": [
                "ENABLED",
                "INHERITED",
                "DISABLED"
            ],
            "description": "Determines whether or not IPSEC is enabled. Possible values are INHERITED, ENABLED, DISABLED.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": false,
            "type": "enum",
            "uniqueScope": "no"
        },
        "maintenanceMode": {
            "allowed_choices": [
                "DISABLED",
                "ENABLED",
                "ENABLED_INHERITED"
            ],
            "description": "maintenanceMode is an enum that indicates if the Zone is accepting VM activation requests. Possible values are DISABLED, ENABLED and ENABLED_INHERITED.",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "enum",
            "uniqueScope": "no"
        },
        "multicast": {
            "allowed_choices": [
                "ENABLED",
                "INHERITED",
                "DISABLED"
            ],
            "description": "multicast is enum that indicates multicast policy on zone/zone template. Possible values are ENABLED, DISABLED and INHERITED.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": false,
            "type": "enum",
            "uniqueScope": "no"
        },
        "name": {
            "description": "Name of the current entity(Zone or zone template or subnet etc..) Valid characters are alphabets, numbers, space and hyphen( - ).",
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
            "description": "Netmask of the subnet defined",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "numberOfHostsInSubnets": {
            "description": "Number of hosts in each of the subnets that can be created under a zone and are auto-assigned IP addresses",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "integer",
            "uniqueScope": "no"
        },
        "policyGroupID": {
            "description": "PG ID for the subnet. This is unique per domain and will be in the range 1-4095",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": false,
            "type": "integer",
            "subtype": "long",
            "min_value": 1,
            "max_value": 4095,
            "uniqueScope": "no"
        },
        "publicZone": {
            "description": "If a zone is marked as public, then it is lined to the public network associated with this data center",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "boolean",
            "uniqueScope": "no"
        },
        "templateID": {
            "description": "The ID of the template that this zone was derived from",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        }
    },
    "children": {
        "dhcpoption": {
            "create": true,
            "get": true,
            "bulk_update": true,
            "bulk_delete": true,
            "relationship": "child"
        },
        "eventlog": {
            "get": true,
            "relationship": "child"
        },
        "group": {
            "get": true,
            "relationship": "child",
            "update": true
        },
        "permission": {
            "create": true,
            "get": true,
            "relationship": "child"
        },
        "qos": {
            "create": true,
            "get": true,
            "relationship": "child"
        },
        "statistics": {
            "get": true,
            "relationship": "child"
        },
        "statisticspolicy": {
            "create": true,
            "get": true,
            "relationship": "child"
        },
        "subnet": {
            "create": true,
            "get": true,
            "relationship": "child"
        },
        "tca": {
            "create": true,
            "get": true,
            "relationship": "child"
        },
        "vm": {
            "get": true,
            "relationship": "child"
        },
        "vminterface": {
            "get": true,
            "relationship": "child"
        }
    },
    "model": {
        "delete": true,
        "description": "The zone is a collection of subnets attached to a domain. The zone concept enables the definition of policies for collections of subnets",
        "entity_name": "Zone",
        "extends": [
            "@base",
            "@audited",
            "@metadata"
        ],
        "get": true,
        "package": "network",
        "resource_name": "zones",
        "rest_name": "zone",
        "update": true
    }
}