{
    "attributes": {
        "allowDataDHCP": {
            "description": "Whether to get the Data IP for the VRS VM from DHCP or statically", 
            "exposed": true, 
            "type": "boolean", 
            "uniqueScope": "no"
        }, 
        "allowMgmtDHCP": {
            "description": "Whether to get the management IP for the VRS VM from DHCP or statically", 
            "exposed": true, 
            "type": "boolean", 
            "uniqueScope": "no"
        }, 
        "assocVCenterDataCenterID": {
            "description": "The ID of the vcenter to which this host is attached", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "customizedScriptURL": {
            "description": "To provide a URL to install a custom app on VRS", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "dataDNS1": {
            "description": "Data DNS 1", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "dataDNS2": {
            "description": "Data DNS 2", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "dataGateway": {
            "description": "Data Gateway", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "dataNetworkPortgroup": {
            "description": "Data Network Port Group", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "datapathSyncTimeout": {
            "description": "Datapath Sync Timeout", 
            "exposed": true, 
            "type": "integer", 
            "uniqueScope": "no"
        }, 
        "description": {
            "description": "Description of the Cluster", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "dhcpRelayServer": {
            "description": "To provide IP address of the interface from which you will connect to the DHCP relay server", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "flowEvictionThreshold": {
            "description": "Flow Eviction Threshold", 
            "exposed": true, 
            "type": "integer", 
            "uniqueScope": "no"
        }, 
        "metadataServerIP": {
            "description": "Metadata Server IP", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "metadataServerListenPort": {
            "description": "Metadata Server Listen Port", 
            "exposed": true, 
            "type": "integer", 
            "uniqueScope": "no"
        }, 
        "metadataServerPort": {
            "description": "Metadata Server Port", 
            "exposed": true, 
            "type": "integer", 
            "uniqueScope": "no"
        }, 
        "metadataServiceEnabled": {
            "description": "Metadata Service Enabled", 
            "exposed": true, 
            "type": "boolean", 
            "uniqueScope": "no"
        }, 
        "mgmtDNS1": {
            "description": "DNS server 1", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "mgmtDNS2": {
            "description": "DNS server 2", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "mgmtGateway": {
            "description": "Gateway for the IP address", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "mgmtNetworkPortgroup": {
            "description": "Management Network Port group", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "mtu": {
            "description": "Maximum Transmission Unit for eth2 interface", 
            "exposed": true, 
            "type": "integer", 
            "uniqueScope": "no"
        }, 
        "multiVMSsupport": {
            "description": "Whether Multi VM is to be used or not", 
            "exposed": true, 
            "type": "boolean", 
            "uniqueScope": "no"
        }, 
        "multicastReceiveInterface": {
            "description": "Multicast Receive Interface", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "multicastReceiveInterfaceIP": {
            "description": "IP address for eth3 interface", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "multicastReceiveInterfaceNetmask": {
            "description": "Multicast Interface netmask", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "multicastReceiveRange": {
            "description": "Allowed Range to receive the Multicast traffic from", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "multicastSendInterface": {
            "description": "Multicast Send Interface", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "multicastSendInterfaceIP": {
            "description": "IP address for eth3 interface", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "multicastSendInterfaceNetmask": {
            "description": "Multicast Interface netmask", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "multicastSourcePortgroup": {
            "description": "Multi Cast Source Port Group Name", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "name": {
            "description": "Name of the Cluster", 
            "exposed": true, 
            "required": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "networkUplinkInterface": {
            "description": "Network Upling Interface to support PAT/NAT with no tunnels on VRS-VM", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "networkUplinkInterfaceGateway": {
            "description": "Network Uplink Interface Gateway", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "networkUplinkInterfaceIp": {
            "description": "Ip Address to support PAT/NAT with no tunnels on VRS-VM", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "networkUplinkInterfaceNetmask": {
            "description": "Network Uplink Interface Netmask", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "nfsLogServer": {
            "description": "IP address of NFS server to send the VRS log", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "nfsMountPath": {
            "description": "Location to mount the NFS server", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "novaClientVersion": {
            "description": "Nova client Version ", 
            "exposed": true, 
            "type": "integer", 
            "uniqueScope": "no"
        }, 
        "novaMetadataServiceAuthUrl": {
            "description": "Nova metadata service auth url", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "novaMetadataServiceEndpoint": {
            "description": "Nova metadata service endpoint", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "novaMetadataServicePassword": {
            "description": "Nova metadata service password", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "novaMetadataServiceTenant": {
            "description": "Nova metadata service tenant", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "novaMetadataServiceUsername": {
            "description": "Nova metadata service username", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "novaMetadataSharedSecret": {
            "description": "Nova metadata shared secret", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "novaRegionName": {
            "description": "Nova region name", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "ntpServer1": {
            "description": "IP of the NTP server 1", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "ntpServer2": {
            "description": "IP of the NTP server 1", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "personality": {
            "description": "VRS/VRS-G", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "portgroupMetadata": {
            "description": "Port Group Meta data", 
            "exposed": true, 
            "type": "boolean", 
            "uniqueScope": "no"
        }, 
        "primaryNuageController": {
            "description": "IP address of the primary Controller (VSC)", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "secondaryNuageController": {
            "description": "IP address of the secondary Controller (VSC)", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "separateDataNetwork": {
            "description": "Whether Data will use the management network or not", 
            "exposed": true, 
            "type": "boolean", 
            "uniqueScope": "no"
        }, 
        "siteId": {
            "description": "Site ID field for object profiles to support VSD Geo-redundancy", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "staticRoute": {
            "description": "static route to be configured in the VRS", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "staticRouteGateway": {
            "description": "Gateway for the static route given above", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "staticRouteNetmask": {
            "description": "Nova region name", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "vRequireNuageMetadata": {
            "description": "Whether split-activation or not (Openstack/CloudStack)", 
            "exposed": true, 
            "type": "boolean", 
            "uniqueScope": "no"
        }, 
        "vmNetworkPortgroup": {
            "description": "VM Network Port Group Name", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "vrsPassword": {
            "description": "VRS password to be used by toolbox to communicate with VRS", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "vrsUserName": {
            "description": "VRS user name to be used by toolbox to communicate with VRS", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }
    }, 
    "children": {
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
    "delete": true, 
    "description": "VCenter Clusters", 
    "entity_name": "VCenterCluster", 
    "extends": [
        "@base", 
        "@metadata"
    ], 
    "get": true, 
    "package": "/vmware", 
    "resource_name": "vcenterclusters", 
    "rest_name": "vcentercluster", 
    "update": true
}