{
  "attributes" : {
    "IKEv2GatewayIdentifier" : {
      "type" : "string",
      "format" : "free",
      "description" : "IKEv2 Gateway Identifier. Null to take on the default 'ipaddress'",
      "filterable" : true,
      "orderable" : true,
      "exposed" : true,
      "uniqueScope" : "no"
    },
    "IKEv2GatewayIdentifierType" : {
      "type" : "enum",
      "allowed_choices" : [ "ID_IPV4_ADDR", "ID_FQDN", "ID_RFC822_ADDR", "ID_KEY_ID", "ID_DER_ASN1_DN" ],
      "description" : "IKEv2 Gateway Identifier Type. Null to take on the default ID_IPV4_ADDR",
      "filterable" : true,
      "orderable" : true,
      "exposed" : true,
      "uniqueScope" : "no"
    },
    "antiReplayCheck" : {
      "type" : "boolean",
      "description" : "Allow any local subnets to be used",
      "exposed" : true,
      "uniqueScope" : "no"
    },
    "associatedEnterpriseID" : {
      "type" : "string",
      "format" : "free",
      "description" : "The ID of the associated Enterprise",
      "exposed" : true,
      "uniqueScope" : "no"
    },
    "associatedIKEv2AuthenticationID" : {
      "type" : "string",
      "format" : "free",
      "description" : "???",
      "exposed" : true,
      "uniqueScope" : "no"
    },
    "associatedIKEv2AuthenticationType" : {
      "type" : "enum",
      "allowed_choices" : [ "UNSUPPORTED", "NETWORK_ELEMENT", "NETWORK_LAYOUT", "ENTERPRISE", "ENTERPRISE_PROFILE", "GROUP", "USER", "DOMAIN_FLOATING_IP_ACL_TEMPLATE", "DOMAIN_FLOATING_IP_ACL_TEMPLATE_ENTRY", "FLOATING_IP_ACL_TEMPLATE", "FLOATING_IP_ACL_TEMPLATE_ENTRY", "FLOATINGIP_ACL", "FLOATINGIP_ACL_ENTRY", "INGRESS_ACL_TEMPLATE", "INGRESS_ACL_TEMPLATE_ENTRY", "INGRESS_ACL", "INGRESS_ACL_ENTRY", "INGRESS_ADV_FWD_TEMPLATE", "INGRESS_ADV_FWD_TEMPLATE_ENTRY", "INGRESS_ADV_FWD", "INGRESS_ADV_FWD_ENTRY", "INGRESS_EXT_SERVICE_TEMPLATE", "INGRESS_EXT_SERVICE_TEMPLATE_ENTRY", "INGRESS_EXT_SERVICE", "INGRESS_EXT_SERVICE_ENTRY", "EGRESS_ACL_TEMPLATE", "EGRESS_ACL_TEMPLATE_ENTRY", "EGRESS_ACL", "EGRESS_ACL_ENTRY", "POLICING_POLICY", "SHAPING_POLICY", "QOS_PRIMITIVE", "EGRESS_QOS_PRIMITIVE", "EGRESS_QOS_QUEUE_MR", "EGRESS_QOS_MR", "PORT_MR", "RATE_LIMITER", "DSCP_FORWARDING_CLASS_MAPPING", "DSCP_FORWARDING_CLASS_TABLE", "APPLICATION", "VIRTUAL_MACHINE", "SUBNET", "ADDRESS_RANGE", "ADDRESS_RANGE_STATE", "IP_BINDING", "L2DOMAIN", "L2DOMAIN_SHARED", "L2DOMAIN_TEMPLATE", "SUBNET_ENTRY", "SUBNET_MAC_ENTRY", "ENTERPRISE_NETWORK", "NETWORK_MACRO_GROUP", "PUBLIC_NETWORK", "SUBNET_TEMPLATE", "VM_INTERFACE", "VM_DESCRIPTION", "POLICY_DECISION", "CUSTOMER_VRF_SEQUENCENO", "SERVICE_VRF_SEQUENCENO", "DOMAIN", "VPN_CONNECT", "ZONE", "FLOATINGIP", "SUBNET_POOL_ENTRY", "DOMAIN_TEMPLATE", "ZONE_TEMPLATE", "PERMISSION", "PERMITTED_ACTION", "STATS_TCA", "STATS_POLICY", "STATS_COLLECTOR", "STATISTICS", "ALARM", "EVENT_LOG", "DHCP_OPTION", "STATIC_ROUTE", "DC_CONFIG", "RESYNC", "VPRN_LABEL_SEQUENCENO", "LDAP_CONFIG", "LICENSE", "VPORT", "VPORT_GATEWAY_RESPONSE", "SERVICE_GATEWAY_RESPONSE", "SERVICES_GATEWAY_RESPONSE", "VPORTTAGTEMPLATE", "VPORTTAG", "POLICY_GROUP_TEMPLATE", "HOSTINTERFACE", "BRIDGEINTERFACE", "VIRTUAL_IP", "VPORT_TAG_BASE", "POLICY_GROUP", "VNID_SEQUENCENO", "ESI_SEQUENCENO", "SYSTEM_CONFIG", "SYSTEM_CONFIG_REQ", "SYSTEM_CONFIG_RESP", "SHARED_RESOURCE", "RTRD_SEQUENCENO", "RD_SEQUENCENO", "RTRD_ENTITY", "EVPN_BGP_COMMUNITY_TAG_SEQ_NO", "EVPN_BGP_COMMUNITY_TAG_ENTRY", "VPORT_MEDIATION_REQUEST", "NODE_EXECUTION_ERROR", "MIRROR_DESTINATION", "VPORT_MIRROR", "GATEWAY", "NSGATEWAY", "GATEWAY_TEMPLATE", "NSGATEWAY_TEMPLATE", "AUTO_DISC_GATEWAY", "PORT", "NSPORT", "NS_REDUNDANT_PORT", "VSG_REDUNDANT_PORT", "PORT_TEMPLATE", "NSPORT_TEMPLATE", "VLAN", "VLAN_TEMPLATE", "VLAN_CONFIG_RESPONSE", "REDUNDANT_GW_GRP", "NSREDUNDANT_GW_GRP", "WAN_SERVICE", "GATEWAY_VPORT_CONFIG", "GATEWAY_SERVICE_CONFIG", "GATEWAY_SERVICE_CONFIG_RESP", "GATEWAY_VPORT_CONFIG_RESP", "GATEWAY_CONFIG", "NSGATEWAY_CONFIG", "GATEWAY_CONFIG_RESP", "ENTERPRISE_CONFIG", "ENTERPRISE_CONFIG_RESP", "DHCP_CONFIG_RESP", "DHCP_ALLOC_MESSAGE", "VSC", "HSC", "VSD", "VRS", "STATSSERVER", "VSP", "VSD_COMPONENT", "SYSTEM_MONITORING", "DISKSTATS", "MONITORING_PORT", "BGPPEER", "JOB", "ENTERPRISE_PERMISSION", "VIRTUAL_MACHINE_REPORT", "BOOTSTRAP", "LOCATION", "BOOTSTRAP_ACTIVATION", "INFRASTRUCTURE_GATEWAY_PROFILE", "INFRASTRUCTURE_PORT_PROFILE", "INFRASTRUCTURE_VSC_PROFILE", "INFRASTRUCTURE_CONFIG", "NSPORT_STATIC_CONFIG", "NSG_NOTIFICATION", "SITE", "SITE_REQ", "HEALTH_REQ", "SITE_RES", "GEO_VM_REQ", "GEO_VM_RES", "GEO_VM_EVENT", "METADATA", "METADATA_TAG", "ENTITY_METADATA_BINDING", "CHILD_ENTITY_POLICY_CHANGE", "MULTI_NIC_VPORT", "BACK_HAUL_SERVICE_RESP", "MC_CHANNEL_MAP", "MC_LIST", "MC_RANGE", "LIBVIRT_INTERFACE", "APPD_APPLICATION", "APPD_SERVICE", "APPD_TIER", "APPD_FLOW", "APPD_FLOW_SECURITY_POLICY", "APPD_FLOW_FORWARDING_POLICY", "APPD_EXTERNAL_APP_SERVICE", "PATNATPOOL", "NATMAPENTRY", "PATCONFIG_CONFIG_RESP", "NETWORK_POLICY_GROUP", "ACLENTRY_LOCATION", "EXPORTIMPORT", "EXTERNAL_SERVICE", "ENDPOINT", "DOMAIN_CONFIG", "DOMAIN_CONFIG_RESP", "STATIC_ROUTE_RESP", "NEXT_HOP_RESP", "UPLINK_RD", "VMWARE_VCENTER_EAM_CONFIG", "VMWARE_VCENTER_VRS_CONFIG", "VMWARE_VCENTER", "VMWARE_VCENTER_DATACENTER", "VMWARE_VCENTER_CLUSTER", "VMWARE_VCENTER_HYPERVISOR", "VMWARE_VRS_ADDRESS_RANGE", "VMWARE_VCENTER_VRS_BASE_CONFIG", "VMWARE_RELOAD_CONFIG", "CLOUD_MGMT_SYSTEM", "IKEV2_ENCRYPTION_PROFILE", "IKEV2_GATEWAY", "IKEV2_GATEWAY_PROFILE", "IKEV2_GATEWAY_CONNECTION", "IKEV2_CERTIFICATE", "IKEV2_PSK", "IKEV2_SUBNET", "GROUPKEY_ENCRYPTION_PROFILE", "KEYSERVER_MEMBER", "KEYSERVER_MONITOR", "KEYSERVER_MONITOR_SEED", "KEYSERVER_MONITOR_ENCRYPTED_SEED", "KEYSERVER_MONITOR_SEK", "KEYSERVER_NOTIFICATION", "ENTERPRISE_SECURITY", "ENTERPRISE_SECURED_DATA", "GATEWAY_SECURITY", "GATEWAY_SECURITY_REQUEST", "GATEWAY_SECURITY_RESPONSE", "GATEWAY_SECURITY_PROFILE_REQUEST", "IKEV2_ENCRYPTION_PROFILE_REQUEST", "IKEV2_GATEWAY_CONNECTION_REQUEST", "GATEWAY_SECURITY_PROFILE_RESPONSE", "GATEWAY_SECURED_DATA", "CERTIFICATE", "BGP_PROFILE", "ROUTING_POLICY", "BGP_NEIGHBOR", "BGP_PROFILE_MED_RESPONSE", "ROUTING_POL_MED_RESPONSE", "BGP_NEIGHBOR_MED_RESPONSE", "BGP_DAMPENING_MED_RESPONSE", "PORT_VLAN_CONFIG", "NSPORT_VLAN_CONFIG", "PORT_VLAN_CONFIG_RESPONSE", "PORT_PUSH" ],
      "description" : "",
      "exposed" : true,
      "uniqueScope" : "no"
    },
    "associatedIKEv2EncryptionProfileID" : {
      "type" : "string",
      "format" : "free",
      "description" : "The ID of the associated IKEv2 Encryption Profile",
      "exposed" : true,
      "uniqueScope" : "no"
    },
    "associatedIKEv2GatewayID" : {
      "type" : "string",
      "format" : "free",
      "description" : "The IKEv2 Gateway associated with this Profile. This is a read only attribute",
      "exposed" : true,
      "uniqueScope" : "no"
    },
    "description" : {
      "type" : "string",
      "format" : "free",
      "description" : "Description of the IKEv2 Gateway Profile",
      "filterable" : true,
      "orderable" : true,
      "exposed" : true,
      "uniqueScope" : "no"
    },
    "name" : {
      "type" : "string",
      "format" : "free",
      "description" : "Name of the IKEv2 Gateway Profile",
      "filterable" : true,
      "orderable" : true,
      "exposed" : true,
      "uniqueScope" : "no"
    },
    "serviceClass" : {
      "type" : "enum",
      "allowed_choices" : [ "NONE", "A", "B", "C", "D", "E", "F", "G", "H" ],
      "description" : "Class of service to be used.  Service classes in order of priority are A, B, C, D, E, F, G, and H.",
      "filterable" : true,
      "orderable" : true,
      "default_value" : "H",
      "exposed" : true,
      "uniqueScope" : "no"
    }
  },
  "children" : { },
  "model" : {
    "description" : "Represents an IKEv2 Gateway",
    "entity_name" : "IKEv2GatewayProfile",
    "extends" : [ "@audited", "@base", "@metadata" ],
    "package" : "ikev2",
    "resource_name" : "ikev2gatewayprofiles",
    "rest_name" : "ikev2gatewayprofile",
    "get" : true,
    "delete" : true,
    "update" : true
  }
}