{
    "attributes": {
        "allowDataDHCP": {
            "description": "Whether to get the Data IP for the VRS VM from DHCP or statically",
            "exposed": true,
            "format": "free",
            "type": "boolean",
            "uniqueScope": "no"
        },
        "allowMgmtDHCP": {
            "description": "Whether to get the management IP for the VRS VM from DHCP or statically",
            "exposed": true,
            "format": "free",
            "type": "boolean",
            "uniqueScope": "no"
        },
        "assocVCenterDataCenterID": {
            "description": "The ID of the vcenter to which this host is attached",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "customizedScriptURL": {
            "description": "To provide a URL to install a custom app on VRS",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "dataDNS1": {
            "description": "Data DNS 1",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "dataDNS2": {
            "description": "Data DNS 2",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "dataGateway": {
            "description": "Data Gateway",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "dataNetworkPortgroup": {
            "description": "Data Network Port Group",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "datapathSyncTimeout": {
            "description": "Datapath Sync Timeout",
            "exposed": true,
            "format": "free",
            "type": "integer",
            "uniqueScope": "no"
        },
        "description": {
            "description": "Description of the Cluster",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "dhcpRelayServer": {
            "description": "To provide IP address of the interface from which you will connect to the DHCP relay server",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "flowEvictionThreshold": {
            "description": "Flow Eviction Threshold",
            "exposed": true,
            "format": "free",
            "type": "integer",
            "uniqueScope": "no"
        },
        "managedObjectID": {
            "description": "corresponds to the moid of the cluster in the vcenter",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "metadataServerIP": {
            "description": "Metadata Server IP",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "metadataServerListenPort": {
            "description": "Metadata Server Listen Port",
            "exposed": true,
            "format": "free",
            "type": "integer",
            "uniqueScope": "no"
        },
        "metadataServerPort": {
            "description": "Metadata Server Port",
            "exposed": true,
            "format": "free",
            "type": "integer",
            "uniqueScope": "no"
        },
        "metadataServiceEnabled": {
            "description": "Metadata Service Enabled",
            "exposed": true,
            "format": "free",
            "type": "boolean",
            "uniqueScope": "no"
        },
        "mgmtDNS1": {
            "description": "DNS server 1",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "mgmtDNS2": {
            "description": "DNS server 2",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "mgmtGateway": {
            "description": "Gateway for the IP address",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "mgmtNetworkPortgroup": {
            "description": "Management Network Port group",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "mtu": {
            "description": "Maximum Transmission Unit for eth2 interface",
            "exposed": true,
            "format": "free",
            "type": "integer",
            "uniqueScope": "no"
        },
        "multiVMSsupport": {
            "description": "Whether Multi VM is to be used or not",
            "exposed": true,
            "format": "free",
            "type": "boolean",
            "uniqueScope": "no"
        },
        "multicastReceiveInterface": {
            "description": "Multicast Receive Interface",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "multicastReceiveInterfaceIP": {
            "description": "IP address for eth3 interface",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "multicastReceiveInterfaceNetmask": {
            "description": "Multicast Interface netmask",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "multicastReceiveRange": {
            "description": "Allowed Range to receive the Multicast traffic from",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "multicastSendInterface": {
            "description": "Multicast Send Interface",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "multicastSendInterfaceIP": {
            "description": "IP address for eth3 interface",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "multicastSendInterfaceNetmask": {
            "description": "Multicast Interface netmask",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "multicastSourcePortgroup": {
            "description": "Multi Cast Source Port Group Name",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "name": {
            "description": "Name of the Cluster",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "required": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "networkUplinkInterface": {
            "description": "Network Upling Interface to support PAT/NAT with no tunnels on VRS-VM",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "networkUplinkInterfaceGateway": {
            "description": "Network Uplink Interface Gateway",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "networkUplinkInterfaceIp": {
            "description": "Ip Address to support PAT/NAT with no tunnels on VRS-VM",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "networkUplinkInterfaceNetmask": {
            "description": "Network Uplink Interface Netmask",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "nfsLogServer": {
            "description": "IP address of NFS server to send the VRS log",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "nfsMountPath": {
            "description": "Location to mount the NFS server",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "novaClientVersion": {
            "description": "Nova client Version ",
            "exposed": true,
            "format": "free",
            "type": "integer",
            "uniqueScope": "no"
        },
        "novaMetadataServiceAuthUrl": {
            "description": "Nova metadata service auth url",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "novaMetadataServiceEndpoint": {
            "description": "Nova metadata service endpoint",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "novaMetadataServicePassword": {
            "description": "Nova metadata service password",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "novaMetadataServiceTenant": {
            "description": "Nova metadata service tenant",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "novaMetadataServiceUsername": {
            "description": "Nova metadata service username",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "novaMetadataSharedSecret": {
            "description": "Nova metadata shared secret",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "novaRegionName": {
            "description": "Nova region name",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "ntpServer1": {
            "description": "IP of the NTP server 1",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "ntpServer2": {
            "description": "IP of the NTP server 1",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "personality": {
            "description": "VRS/VRS-G",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "portgroupMetadata": {
            "description": "Port Group Meta data",
            "exposed": true,
            "format": "free",
            "type": "boolean",
            "uniqueScope": "no"
        },
        "primaryNuageController": {
            "description": "IP address of the primary Controller (VSC)",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "scope": {
            "description": "vrs vms deployed or not",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "boolean",
            "uniqueScope": "no"
        },
        "secondaryNuageController": {
            "description": "IP address of the secondary Controller (VSC)",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "separateDataNetwork": {
            "description": "Whether Data will use the management network or not",
            "exposed": true,
            "format": "free",
            "type": "boolean",
            "uniqueScope": "no"
        },
        "siteId": {
            "description": "Site ID field for object profiles to support VSD Geo-redundancy",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "staticRoute": {
            "description": "static route to be configured in the VRS",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "staticRouteGateway": {
            "description": "Gateway for the static route given above",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "staticRouteNetmask": {
            "description": "Nova region name",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "vRequireNuageMetadata": {
            "description": "Whether split-activation or not (Openstack/CloudStack)",
            "exposed": true,
            "format": "free",
            "type": "boolean",
            "uniqueScope": "no"
        },
        "vmNetworkPortgroup": {
            "description": "VM Network Port Group Name",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "vrsPassword": {
            "description": "VRS password to be used by toolbox to communicate with VRS",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "vrsUserName": {
            "description": "VRS user name to be used by toolbox to communicate with VRS",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        }
    },
    "children": {
        "autodiscoveredhypervisor": {
            "get": true,
            "relationship": "child"
        },
        "vcenterhypervisor": {
            "create": true,
            "get": true,
            "relationship": "child",
            "update": true
        },
        "vrsaddressrange": {
            "create": true,
            "get": true,
            "relationship": "child"
        }
    },
    "model": {
        "delete": true,
        "description": "VCenter Clusters",
        "entity_name": "VCenterCluster",
        "extends": [
            "@audited",
            "@base",
            "@metadata"
        ],
        "get": true,
        "package": "vmware",
        "resource_name": "vcenterclusters",
        "rest_name": "vcentercluster",
        "update": true
    }
}