{
    "attributes": [
        {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "IKE Gateway Identifier. Null to take on the default 'ipaddress'",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "IKEGatewayIdentifier",
            "orderable": true,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "string",
            "unique": false,
            "uniqueScope": null
        },
        {
            "allowed_chars": null,
            "allowed_choices": [
                "ID_DER_ASN1_DN",
                "ID_FQDN",
                "ID_IPV4_ADDR",
                "ID_KEY_ID",
                "ID_RFC822_ADDR"
            ],
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "IKE Gateway Identifier Type.",
            "exposed": true,
            "filterable": true,
            "format": null,
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "IKEGatewayIdentifierType",
            "orderable": true,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "enum",
            "unique": false,
            "uniqueScope": null
        },
        {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "Allow any local subnets to be used",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "antiReplayCheck",
            "orderable": false,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "boolean",
            "unique": false,
            "uniqueScope": null
        },
        {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "The ID of the associated Enterprise",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "associatedEnterpriseID",
            "orderable": false,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "string",
            "unique": false,
            "uniqueScope": null
        },
        {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "Associated IKE Authentication ID",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "associatedIKEAuthenticationID",
            "orderable": false,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "string",
            "unique": false,
            "uniqueScope": null
        },
        {
            "allowed_chars": null,
            "allowed_choices": [
                "ACLENTRY_LOCATION",
                "ADDRESS_RANGE",
                "ADDRESS_RANGE_STATE",
                "ALARM",
                "APPD_APPLICATION",
                "APPD_EXTERNAL_APP_SERVICE",
                "APPD_FLOW",
                "APPD_FLOW_FORWARDING_POLICY",
                "APPD_FLOW_SECURITY_POLICY",
                "APPD_SERVICE",
                "APPD_TIER",
                "APPLICATION",
                "AUTO_DISC_GATEWAY",
                "BACK_HAUL_SERVICE_RESP",
                "BGPPEER",
                "BGP_DAMPENING_MED_RESPONSE",
                "BGP_NEIGHBOR",
                "BGP_NEIGHBOR_MED_RESPONSE",
                "BGP_PROFILE",
                "BGP_PROFILE_MED_RESPONSE",
                "BOOTSTRAP",
                "BOOTSTRAP_ACTIVATION",
                "BRIDGEINTERFACE",
                "CERTIFICATE",
                "CHILD_ENTITY_POLICY_CHANGE",
                "CLOUD_MGMT_SYSTEM",
                "CUSTOMER_VRF_SEQUENCENO",
                "DC_CONFIG",
                "DHCP_ALLOC_MESSAGE",
                "DHCP_CONFIG_RESP",
                "DHCP_OPTION",
                "DISKSTATS",
                "DOMAIN",
                "DOMAIN_CONFIG",
                "DOMAIN_CONFIG_RESP",
                "DOMAIN_FLOATING_IP_ACL_TEMPLATE",
                "DOMAIN_FLOATING_IP_ACL_TEMPLATE_ENTRY",
                "DOMAIN_TEMPLATE",
                "DSCP_FORWARDING_CLASS_MAPPING",
                "DSCP_FORWARDING_CLASS_TABLE",
                "EGRESS_ACL",
                "EGRESS_ACL_ENTRY",
                "EGRESS_ACL_TEMPLATE",
                "EGRESS_ACL_TEMPLATE_ENTRY",
                "EGRESS_QOS_MR",
                "EGRESS_QOS_PRIMITIVE",
                "EGRESS_QOS_QUEUE_MR",
                "ENDPOINT",
                "ENTERPRISE",
                "ENTERPRISE_CONFIG",
                "ENTERPRISE_CONFIG_RESP",
                "ENTERPRISE_NETWORK",
                "ENTERPRISE_PERMISSION",
                "ENTERPRISE_PROFILE",
                "ENTERPRISE_SECURED_DATA",
                "ENTERPRISE_SECURITY",
                "ENTITY_METADATA_BINDING",
                "ESI_SEQUENCENO",
                "EVENT_LOG",
                "EVPN_BGP_COMMUNITY_TAG_ENTRY",
                "EVPN_BGP_COMMUNITY_TAG_SEQ_NO",
                "EXPORTIMPORT",
                "EXTERNAL_SERVICE",
                "FLOATINGIP",
                "FLOATINGIP_ACL",
                "FLOATINGIP_ACL_ENTRY",
                "FLOATING_IP_ACL_TEMPLATE",
                "FLOATING_IP_ACL_TEMPLATE_ENTRY",
                "GATEWAY",
                "GATEWAY_CONFIG",
                "GATEWAY_CONFIG_RESP",
                "GATEWAY_SECURED_DATA",
                "GATEWAY_SECURITY",
                "GATEWAY_SECURITY_PROFILE_REQUEST",
                "GATEWAY_SECURITY_PROFILE_RESPONSE",
                "GATEWAY_SECURITY_REQUEST",
                "GATEWAY_SECURITY_RESPONSE",
                "GATEWAY_SERVICE_CONFIG",
                "GATEWAY_SERVICE_CONFIG_RESP",
                "GATEWAY_TEMPLATE",
                "GATEWAY_VPORT_CONFIG",
                "GATEWAY_VPORT_CONFIG_RESP",
                "GEO_VM_EVENT",
                "GEO_VM_REQ",
                "GEO_VM_RES",
                "GROUP",
                "GROUPKEY_ENCRYPTION_PROFILE",
                "HEALTH_REQ",
                "HOSTINTERFACE",
                "HSC",
                "IKEV2_CERTIFICATE",
                "IKEV2_ENCRYPTION_PROFILE",
                "IKEV2_ENCRYPTION_PROFILE_REQUEST",
                "IKEV2_GATEWAY",
                "IKEV2_GATEWAY_CONNECTION",
                "IKEV2_GATEWAY_CONNECTION_REQUEST",
                "IKEV2_GATEWAY_PROFILE",
                "IKEV2_PSK",
                "IKEV2_SUBNET",
                "INFRASTRUCTURE_CONFIG",
                "INFRASTRUCTURE_GATEWAY_PROFILE",
                "INFRASTRUCTURE_PORT_PROFILE",
                "INFRASTRUCTURE_VSC_PROFILE",
                "INGRESS_ACL",
                "INGRESS_ACL_ENTRY",
                "INGRESS_ACL_TEMPLATE",
                "INGRESS_ACL_TEMPLATE_ENTRY",
                "INGRESS_ADV_FWD",
                "INGRESS_ADV_FWD_ENTRY",
                "INGRESS_ADV_FWD_TEMPLATE",
                "INGRESS_ADV_FWD_TEMPLATE_ENTRY",
                "INGRESS_EXT_SERVICE",
                "INGRESS_EXT_SERVICE_ENTRY",
                "INGRESS_EXT_SERVICE_TEMPLATE",
                "INGRESS_EXT_SERVICE_TEMPLATE_ENTRY",
                "IP_BINDING",
                "JOB",
                "KEYSERVER_MEMBER",
                "KEYSERVER_MONITOR",
                "KEYSERVER_MONITOR_ENCRYPTED_SEED",
                "KEYSERVER_MONITOR_SEED",
                "KEYSERVER_MONITOR_SEK",
                "KEYSERVER_NOTIFICATION",
                "L2DOMAIN",
                "L2DOMAIN_SHARED",
                "L2DOMAIN_TEMPLATE",
                "LDAP_CONFIG",
                "LIBVIRT_INTERFACE",
                "LICENSE",
                "LOCATION",
                "MC_CHANNEL_MAP",
                "MC_LIST",
                "MC_RANGE",
                "METADATA",
                "METADATA_TAG",
                "MIRROR_DESTINATION",
                "MONITORING_PORT",
                "MULTI_NIC_VPORT",
                "NATMAPENTRY",
                "NETWORK_ELEMENT",
                "NETWORK_LAYOUT",
                "NETWORK_MACRO_GROUP",
                "NETWORK_POLICY_GROUP",
                "NEXT_HOP_RESP",
                "NODE_EXECUTION_ERROR",
                "NSGATEWAY",
                "NSGATEWAY_CONFIG",
                "NSGATEWAY_TEMPLATE",
                "NSG_NOTIFICATION",
                "NSPORT",
                "NSPORT_STATIC_CONFIG",
                "NSPORT_TEMPLATE",
                "NSPORT_VLAN_CONFIG",
                "NSREDUNDANT_GW_GRP",
                "NS_REDUNDANT_PORT",
                "PATCONFIG_CONFIG_RESP",
                "PATNATPOOL",
                "PERMISSION",
                "PERMITTED_ACTION",
                "POLICING_POLICY",
                "POLICY_DECISION",
                "POLICY_GROUP",
                "POLICY_GROUP_TEMPLATE",
                "PORT",
                "PORT_MR",
                "PORT_PUSH",
                "PORT_TEMPLATE",
                "PORT_VLAN_CONFIG",
                "PORT_VLAN_CONFIG_RESPONSE",
                "PUBLIC_NETWORK",
                "QOS_PRIMITIVE",
                "RATE_LIMITER",
                "RD_SEQUENCENO",
                "REDUNDANT_GW_GRP",
                "RESYNC",
                "ROUTING_POLICY",
                "ROUTING_POL_MED_RESPONSE",
                "RTRD_ENTITY",
                "RTRD_SEQUENCENO",
                "SERVICES_GATEWAY_RESPONSE",
                "SERVICE_GATEWAY_RESPONSE",
                "SERVICE_VRF_SEQUENCENO",
                "SHAPING_POLICY",
                "SHARED_RESOURCE",
                "SITE",
                "SITE_REQ",
                "SITE_RES",
                "STATIC_ROUTE",
                "STATIC_ROUTE_RESP",
                "STATISTICS",
                "STATSSERVER",
                "STATS_COLLECTOR",
                "STATS_POLICY",
                "STATS_TCA",
                "SUBNET",
                "SUBNET_ENTRY",
                "SUBNET_MAC_ENTRY",
                "SUBNET_POOL_ENTRY",
                "SUBNET_TEMPLATE",
                "SYSTEM_CONFIG",
                "SYSTEM_CONFIG_REQ",
                "SYSTEM_CONFIG_RESP",
                "SYSTEM_MONITORING",
                "UNSUPPORTED",
                "UPLINK_RD",
                "USER",
                "VIRTUAL_IP",
                "VIRTUAL_MACHINE",
                "VIRTUAL_MACHINE_REPORT",
                "VLAN",
                "VLAN_CONFIG_RESPONSE",
                "VLAN_TEMPLATE",
                "VMWARE_RELOAD_CONFIG",
                "VMWARE_VCENTER",
                "VMWARE_VCENTER_CLUSTER",
                "VMWARE_VCENTER_DATACENTER",
                "VMWARE_VCENTER_EAM_CONFIG",
                "VMWARE_VCENTER_HYPERVISOR",
                "VMWARE_VCENTER_VRS_BASE_CONFIG",
                "VMWARE_VCENTER_VRS_CONFIG",
                "VMWARE_VRS_ADDRESS_RANGE",
                "VM_DESCRIPTION",
                "VM_INTERFACE",
                "VNID_SEQUENCENO",
                "VPN_CONNECT",
                "VPORT",
                "VPORTTAG",
                "VPORTTAGTEMPLATE",
                "VPORT_GATEWAY_RESPONSE",
                "VPORT_MEDIATION_REQUEST",
                "VPORT_MIRROR",
                "VPORT_TAG_BASE",
                "VPRN_LABEL_SEQUENCENO",
                "VRS",
                "VSC",
                "VSD",
                "VSD_COMPONENT",
                "VSG_REDUNDANT_PORT",
                "VSP",
                "WAN_SERVICE",
                "ZONE",
                "ZONE_TEMPLATE"
            ],
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "Associated IKE Authentication Type",
            "exposed": true,
            "filterable": false,
            "format": null,
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "associatedIKEAuthenticationType",
            "orderable": false,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "enum",
            "unique": false,
            "uniqueScope": null
        },
        {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "The ID of the associated IKE Encryption Profile",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "associatedIKEEncryptionProfileID",
            "orderable": false,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "string",
            "unique": false,
            "uniqueScope": null
        },
        {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "The IKE Gateway associated with this Profile. This is a read only attribute",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "associatedIKEGatewayID",
            "orderable": false,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "string",
            "unique": false,
            "uniqueScope": null
        },
        {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "Description of the IKEv2 Gateway Profile",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "description",
            "orderable": true,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "string",
            "unique": false,
            "uniqueScope": null
        },
        {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "Name of the IKEv2 Gateway Profile",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "name",
            "orderable": true,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "string",
            "unique": false,
            "uniqueScope": null
        },
        {
            "allowed_chars": null,
            "allowed_choices": [
                "A",
                "B",
                "C",
                "D",
                "E",
                "F",
                "G",
                "H",
                "NONE"
            ],
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "Class of service to be used.  Service classes in order of priority are A, B, C, D, E, F, G, and H.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "serviceClass",
            "orderable": true,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "enum",
            "unique": false,
            "uniqueScope": null
        }
    ],
    "children": [],
    "model": {
        "create": false,
        "delete": true,
        "description": "Represents an IKE Gateway",
        "entity_name": "IKEGatewayProfile",
        "extends": [
            "@audited",
            "@base",
            "@metadata"
        ],
        "get": true,
        "package": "ike",
        "resource_name": "ikegatewayprofiles",
        "rest_name": "ikegatewayprofile",
        "root": false,
        "update": true
    }
}
