{
    "attributes": {
        "LDAPSyncInterval": {
            "description": "LDAP Sync-Up task interval in seconds(min=600, max=86400).", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "float"
        }, 
        "customerKey": {
            "description": "Customer key associated with the licese", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "groupKeyMinimumTrafficEncryptionKeyLifetime": {
            "description": "Group Key Encryption Profile Minimum TEK Lifetime", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "integer"
        }, 
        "VSDUpgradeIsComplete": {
            "description": "This flag is used to indicate that whether VSD upgrade is complete,it is expected that csproot will set to true,after VSD upgrade is complete and also making sure that all VSC's audits and Gateway audits with VSD are done", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "boolean"
        }, 
        "EVPNBGPCommunityTagASNumber": {
            "description": " Autonomous System Number,Used for EVPNBGPCommunityTag auto-generation", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "float"
        }, 
        "offsetServiceID": {
            "description": "Service id offset, this value has to be set before jboss starts during install time, after that any change of value is ignored (minexclusive = 0, max = 40000) system wide value", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "float"
        }, 
        "groupKeyDefaultTrafficAuthenticationAlgorithm": {
            "description": "Group Key Encryption Profile Default Traffic Authentication Algorithm Possible values are HMAC_SHA1, HMAC_SHA256, HMAC_SHA384, HMAC_SHA512, HMAC_MD5, .", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "allowed_choices": [
                "HMAC_SHA384", 
                "HMAC_SHA512", 
                "HMAC_SHA1", 
                "HMAC_MD5", 
                "HMAC_SHA256"
            ], 
            "orderable": true, 
            "type": "enum"
        }, 
        "ejbcaVspRootCa": {
            "description": "EJBCA VSP CA", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "EVPNBGPCommunityTagUpperLimit": {
            "description": "EVPNBGPCommunityTag upper limit", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "float"
        }, 
        "APIKeyRenewalInterval": {
            "description": "Defines the interval in seconds, before the expiry time, that can used to renew the apiKey by making me API call. Minimum value is 1 min and maximum is 5 min.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "float"
        }, 
        "RDPublicNetworkUpperLimit": {
            "description": "route distinguisher public network upper limit", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "float"
        }, 
        "LDAPTrustStoreCertifcate": {
            "description": "Location of the truststore which is need to store LDAP server certificates. Default is cacerts located in java.home/lib/security/cacerts. Uncomment below setting if you need to use a different file", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "VMPurgeTime": {
            "description": "Timers in sec for undefined vms to be deleted(min =60, max = 600).", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "integer"
        }, 
        "APIKeyValidity": {
            "description": "Defines the apiKey validity duration in seconds. Default is 24 hours and minimum value is 10 min.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "float"
        }, 
        "avatarBaseURL": {
            "description": "Defines the url to read the avatar image files", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "nsgConfigEndpoint": {
            "description": "NSG Config Endpoint", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "groupKeyDefaultSeedPayloadAuthenticationAlgorithm": {
            "description": "Group Key Encryption Profile Default Seed Payload Authentication Algorithm Possible values are HMAC_SHA1, HMAC_SHA256, HMAC_SHA512, .", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "allowed_choices": [
                "HMAC_SHA512", 
                "HMAC_SHA1", 
                "HMAC_SHA256"
            ], 
            "orderable": true, 
            "type": "enum"
        }, 
        "inactiveTimeout": {
            "description": "Defines the inactive timeout for the client. If the client is inactive for more than timeout, server clears off all the cache/information regarding the client. This value should be greater than event processor max timeout", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "float"
        }, 
        "RTPublicNetworkLowerLimit": {
            "description": "route target public network lower limit", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "float"
        }, 
        "groupKeyGenerationIntervalOnForcedReKey": {
            "description": "Time in seconds before new keys will be generated in the case of a forced re-key event", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "integer"
        }, 
        "sysmonCleanupTaskInterval": {
            "description": "Sysmon cleanup task run interval in seconds (Min: 10 secs,  Max: 3600 secs)", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "float"
        }, 
        "groupKeyDefaultSEKGenerationInterval": {
            "description": "Group Key Encryption Profile Default SEK Generation Interval", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "integer"
        }, 
        "DHCPOptionSize": {
            "description": "Defines total DHCP options that can be set on a domain.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "integer"
        }, 
        "nsgLocalUiUrl": {
            "description": "NSG Local UI URL - will be redirected on NSG to localhost", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "RDPublicNetworkLowerLimit": {
            "description": "route distinguisher public network lower limit", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "float"
        }, 
        "statsTSDBServerAddress": {
            "description": "Specifies the TSDB server location.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "postProcessorThreadsCount": {
            "description": "Post processor thread count.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "integer"
        }, 
        "nsgBootstrapEndpoint": {
            "description": "NSG Bootstrap Endpoint", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "groupKeyMinimumSEKLifetime": {
            "description": "Group Key Encryption Profile Minimum SEK Lifetime", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "integer"
        }, 
        "VMResyncDeletionWaitTime": {
            "description": "After resync on vm , if no controller returns with a VM request with in the below timeframe then it will get deleted deletion wait time in min (min = 1, max =5)", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "integer"
        }, 
        "twoFactorCodeExpiry": {
            "description": "Two Factor Code Expiry in Seconds", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "integer"
        }, 
        "twoFactorCodeSeedLength": {
            "description": "Two Factor Seed length in bytes", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "integer"
        }, 
        "LRUCacheSizePerSubnet": {
            "description": "LRU Map size per subnet ( to hold the deleted vm's ip addresses min =32, max 256).", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "integer"
        }, 
        "RTLowerLimit": {
            "description": "route target lower limit", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "float"
        }, 
        "eventProcessorTimeout": {
            "description": "Defines the maximum time period in milliseconds for the Rest server to wait before sending the events from the system. Value should be between 25000ms to 100000ms.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "float"
        }, 
        "subnetResyncInterval": {
            "description": "After resync on a subnet , another resync on the same subnet is allowed based on the below value subnet resync complete wait time in min (min = 5, max =15)", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "integer"
        }, 
        "ejbcaNSGEndEntityProfile": {
            "description": "EJBCA NSG End Entity Profile", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "groupKeyDefaultSeedGenerationInterval": {
            "description": "Group Key Encryption Profile Default Seed Generation Interval", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "integer"
        }, 
        "VMCacheSize": {
            "description": "LRU Map size for vm (min = 1000, max =100000) this value has to set based on memory given to VSD jvm not finalized.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "integer"
        }, 
        "reflexiveACLTimeout": {
            "description": "Defines the timeout in seconds for reflexive ACLs. This value applies for both TCP and UDP connections. Default value is 180 seconds and the timeout should be between 10 to 86400 seconds.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "float"
        }, 
        "avatarBasePath": {
            "description": "Defines location where image files needs to be copied. Above URL should be configured to read the file from this location.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "syslogDestinationHost": {
            "description": "Specifies the remote syslog destination host", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "VNIDLowerLimit": {
            "description": "Virtual network ID offset", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "integer"
        }, 
        "VNIDPublicNetworkUpperLimit": {
            "description": "Virtual network ID public network upper limit", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "integer"
        }, 
        "customerIDUpperLimit": {
            "description": "Customer id upper limit, system wide value", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "float"
        }, 
        "statsCollectorProtoBufPort": {
            "description": "Specify the protobuf port number(s) of the stats collector.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "VNIDPublicNetworkLowerLimit": {
            "description": "Virtual network ID public network lower limit", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "integer"
        }, 
        "RDUpperLimit": {
            "description": "route distinguisher upper limit", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "float"
        }, 
        "ejbcaOCSPResponderCN": {
            "description": "EJBCA OCSP Responder CommonName", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "RTPublicNetworkUpperLimit": {
            "description": "route target public network upper limit", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "float"
        }, 
        "eventLogCleanupInterval": {
            "description": "Cleanup task run interval in seconds (Min: every hour, Max: every day)", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "float"
        }, 
        "VMUnreachableCleanupTime": {
            "description": "Timers in sec for unreachable VMs for cleanup(min = 3600, max = 86400).", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "integer"
        }, 
        "groupKeyDefaultSEKPayloadEncryptionAlgorithm": {
            "description": "Group Key Encryption Profile Default Sek Payload Encryption Algorithm Possible values are RSA_1024, .", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "allowed_choices": [
                "RSA_1024"
            ], 
            "orderable": true, 
            "type": "enum"
        }, 
        "eventLogEntryMaxAge": {
            "description": "Maximum age in days for cleanup of the eventlog entries (Min: 1 day, Max: 6 months). On every periodic interval run, any eventlog entries older than the maxage will be deleted.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "integer"
        }, 
        "VMUnreachableTime": {
            "description": "Timers in sec for unreachable VMs (min =1800, max = 7200)", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "integer"
        }, 
        "offsetCustomerID": {
            "description": "Customer id offset, this value has to be set before jboss starts , after that any change of value is ignored (minexclusive = 0, max = 20000) system wide value", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "float"
        }, 
        "ejbcaNSGCertificateProfile": {
            "description": "EJBCA NSG Certificate Profile", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "alarmsMaxPerObject": {
            "description": "Maximum alarms per object for example max distinct alarms for specific VM (min = 5, max =20)", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "integer"
        }, 
        "subnetResyncOutstandingInterval": {
            "description": "Outstanding subnet resync interval (in secs). (min = 10, max = 50) system wide value", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "integer"
        }, 
        "ASNumber": {
            "description": " Autonomous System Number,Used for RT/RD auto-generation", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "float"
        }, 
        "groupKeyDefaultSEKPayloadSigningAlgorithm": {
            "description": "Group Key Encryption Profile Default Sek Payload Signing Algorithm Possible values are SHA1withRSA, SHA224withRSA, SHA256withRSA, SHA384withRSA, SHA512withRSA, .", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "allowed_choices": [
                "SHA256withRSA", 
                "SHA1withRSA", 
                "SHA384withRSA", 
                "SHA224withRSA", 
                "SHA512withRSA"
            ], 
            "orderable": true, 
            "type": "enum"
        }, 
        "sysmonNodePresenceTimeout": {
            "description": "Node presence timeout in seconds if no messages (Min: 600,  Max: 86400)", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "float"
        }, 
        "groupKeyDefaultSeedLifetime": {
            "description": "Group Key Encryption Profile Default Seed Lifetime", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "integer"
        }, 
        "VSCOnSameVersionAsVSD": {
            "description": "This flag is used to indicate that whether VSC is on the same version as VSD or not.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "boolean"
        }, 
        "groupKeyMinimumSeedGenerationInterval": {
            "description": "Group Key Encryption Profile Default Seed Generation Interval", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "integer"
        }, 
        "maxFailedLogins": {
            "description": "Maximum failed login attempts before the account is locked (min = 5, max = 10). 0 = not enforced (unlimited attempts). This is not enforced if LDAP is used for authorization", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "integer"
        }, 
        "ACLAllowOrigin": {
            "description": "Defines the domains allowed for access control list.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "RTUpperLimit": {
            "description": "route target upper limit", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "float"
        }, 
        "staticWANServicePurgeTime": {
            "description": "Timers in sec for unreacheable static WAN Services to be deleted(min =3600, max = 7200)", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "integer"
        }, 
        "ECMPCount": {
            "description": "System Default Equal-cost multi-path routing count,Every Domain derives ECMP count from this value unless specifically set for the domain", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "integer"
        }, 
        "twoFactorCodeLength": {
            "description": "Two Factor Code Length", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "integer"
        }, 
        "statsMaxDataPoints": {
            "description": "Specifies the maximum number of data points to support.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "integer"
        }, 
        "esiID": {
            "description": "ESI ID offset", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "integer"
        }, 
        "pageMaxSize": {
            "description": "Defines upper bound for the page size (allowed max=1000). Configured or input page size should be less than this max page size.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "integer"
        }, 
        "syslogDestinationPort": {
            "description": "Specified the remote syslog destination port", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "integer"
        }, 
        "domainTunnelType": {
            "description": "Default Domain Tunnel Type .Possible values are VXLAN,GRE Possible values are DC_DEFAULT, GRE, VXLAN, .", 
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
        "ADGatewayPurgeTime": {
            "description": "Timers in sec for undefined vms to be deleted(min =7200, max = 86400).", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "integer"
        }, 
        "keyServerMonitorEnabled": {
            "description": "Enable the keyserver debug monitor (ie. ksmon command)", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "boolean"
        }, 
        "sysmonProbeResponseTimeout": {
            "description": "Probe response timeout in seconds (Min: 5,  Max: 60)", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "float"
        }, 
        "statsCollectorPort": {
            "description": "Specify the port number(s) of the stats collector.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "LDAPTrustStorePassword": {
            "description": "Password to access the truststore. Uncomment below line to change its value.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "groupKeyDefaultSeedPayloadSigningAlgorithm": {
            "description": "Group Key Encryption Profile Default Seed Payload Signature Algorithm Possible values are SHA1withRSA, SHA224withRSA, SHA256withRSA, SHA384withRSA, SHA512withRSA, .", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "allowed_choices": [
                "SHA256withRSA", 
                "SHA1withRSA", 
                "SHA384withRSA", 
                "SHA224withRSA", 
                "SHA512withRSA"
            ], 
            "orderable": true, 
            "type": "enum"
        }, 
        "eventProcessorMaxEventsCount": {
            "description": "Defines the maximum number of events to be collected in case of events burst. Value should be between 100 to 500.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "integer"
        }, 
        "keyServerVSDDataSynchronizationInterval": {
            "description": "KeyServer time in seconds between full resyncs of VSD data (just in case of missed events)", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "integer"
        }, 
        "RDLowerLimit": {
            "description": "route distinguisher lower limit", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "float"
        }, 
        "VSDReadOnlyMode": {
            "description": "True means VSD readonly mode enabled. False means VSD readonly mode disabled", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "boolean"
        }, 
        "maxResponse": {
            "description": "Defines maximum results returned by the REST call (allowed max=5000).", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "integer"
        }, 
        "VMResyncOutstandingInterval": {
            "description": "Outstanding VM resync interval (in secs). (min = 500, max =2000) system wide value", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "integer"
        }, 
        "VNIDUpperLimit": {
            "description": "Virtual network ID upper limit", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "integer"
        }, 
        "groupKeyDefaultSeedPayloadEncryptionAlgorithm": {
            "description": "Group Key Encryption Profile Default Seed Payload Encryption Algorithm Possible values are AES_128_CBC, AES_256_CBC, TRIPLE_DES_CBC, .", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "allowed_choices": [
                "AES_128_CBC", 
                "AES_256_CBC", 
                "TRIPLE_DES_CBC"
            ], 
            "orderable": true, 
            "type": "enum"
        }, 
        "groupKeyDefaultSEKLifetime": {
            "description": "Group Key Encryption Profile Default SEK Lifetime", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "integer"
        }, 
        "groupKeyDefaultTrafficEncryptionKeyLifetime": {
            "description": "Group Key Encryption Profile Default Traffic Encryption Key Lifetime", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "integer"
        }, 
        "stackTraceEnabled": {
            "description": "True to enable stacktrace in the REST call.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "boolean"
        }, 
        "groupKeyMinimumSEKGenerationInterval": {
            "description": "Group Key Encryption Profile Minimum SEK Generation Interval", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "integer"
        }, 
        "pageSize": {
            "description": "Defines the page size for the results returned by the REST call.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "integer"
        }, 
        "ejbcaOCSPResponderURI": {
            "description": "EJBCA OCSP Responder URI", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "statsMinDuration": {
            "description": "Default minimum duration for statistics to be displayed in UI is 30 days in seconds.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "float"
        }, 
        "groupKeyGenerationIntervalOnRevoke": {
            "description": "Time in seconds before new keys will be generated in the case of a revoke event", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "integer"
        }, 
        "eventProcessorInterval": {
            "description": "Defines time interval in milliseconds when events collected for a client should be processed. Minimum value is 250ms.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "float"
        }, 
        "dynamicWANServiceDiffTime": {
            "description": "Timers in sec for  dynamic WAN Services to be considered not seen by 7X50(min =1, max = 7200)", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "integer"
        }, 
        "statsNumberOfDataPoints": {
            "description": "Specifies number of data points.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "integer"
        }, 
        "statsCollectorAddress": {
            "description": "Specify the ip address(es) of the stats collector.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "EVPNBGPCommunityTagLowerLimit": {
            "description": "EVPNBGPCommunityTag lower limit", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "float"
        }, 
        "groupKeyDefaultTrafficEncryptionAlgorithm": {
            "description": "Group Key Encryption Profile Default Traffic Encryption Algorithm Possible values are AES_128_CBC, AES_192_CBC, AES_256_CBC, TRIPLE_DES_CBC, .", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "allowed_choices": [
                "AES_128_CBC", 
                "AES_256_CBC", 
                "AES_192_CBC", 
                "TRIPLE_DES_CBC"
            ], 
            "orderable": true, 
            "type": "enum"
        }, 
        "serviceIDUpperLimit": {
            "description": "Service id upper limit system wide value", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "float"
        }, 
        "groupKeyMinimumSeedLifetime": {
            "description": "Group Key Encryption Profile Default Seed Lifetime", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "integer"
        }
    }, 
    "model": {
        "resource_name": "systemconfigs", 
        "description": "The system configuration which can be dynamically managed using rest api.", 
        "entity_name": "SystemConfig", 
        "package": "systemconfig", 
        "get": true, 
        "update": true, 
        "rest_name": "systemconfig", 
        "extends": [
            "@base", 
            "@metadata"
        ]
    }
}