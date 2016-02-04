{
    "attributes": {
        "ACLAllowOrigin": {
            "description": "Defines the domains allowed for access control list.",
            "exposed": true,
            "format": "free",
            "max_length": 255,
            "type": "string",
            "uniqueScope": "no"
        },
        "ADGatewayPurgeTime": {
            "description": "Timers in sec for undefined vms to be deleted(min =7200, max = 86400).",
            "exposed": true,
            "format": "free",
            "max_value": 86400,
            "min_value": 7200,
            "type": "integer",
            "uniqueScope": "no"
        },
        "APIKeyRenewalInterval": {
            "description": "Defines the interval in seconds, before the expiry time, that can used to renew the apiKey by making me API call. Minimum value is 1 min and maximum is 5 min.",
            "exposed": true,
            "format": "free",
            "max_value": 300,
            "min_value": 60,
            "type": "integer",
            "uniqueScope": "no"
        },
        "APIKeyValidity": {
            "description": "Defines the apiKey validity duration in seconds. Default is 24 hours and minimum value is 10 min.",
            "exposed": true,
            "format": "free",
            "max_value": 86400,
            "min_value": 600,
            "type": "integer",
            "uniqueScope": "no"
        },
        "ASNumber": {
            "description": " Autonomous System Number,Used for RT/RD auto-generation",
            "exposed": true,
            "format": "free",
            "max_value": 4294967295,
            "type": "integer",
            "uniqueScope": "no"
        },
        "DHCPOptionSize": {
            "description": "Defines total DHCP options that can be set on a domain.",
            "exposed": true,
            "format": "free",
            "type": "integer",
            "uniqueScope": "no"
        },
        "ECMPCount": {
            "description": "System Default Equal-cost multi-path routing count,Every Domain derives ECMP count from this value unless specifically set for the domain",
            "exposed": true,
            "format": "free",
            "max_value": 8,
            "min_value": 1,
            "type": "integer",
            "uniqueScope": "no"
        },
        "EVPNBGPCommunityTagASNumber": {
            "description": "Autonomous System Number,Used for EVPNBGPCommunityTag auto-generation",
            "exposed": true,
            "format": "free",
            "max_value": 4294967295,
            "type": "integer",
            "uniqueScope": "no"
        },
        "EVPNBGPCommunityTagLowerLimit": {
            "description": "EVPNBGPCommunityTag lower limit",
            "exposed": true,
            "format": "free",
            "max_value": 4294967294,
            "type": "integer",
            "uniqueScope": "no"
        },
        "EVPNBGPCommunityTagUpperLimit": {
            "description": "EVPNBGPCommunityTag upper limit",
            "exposed": true,
            "format": "free",
            "max_value": 4294967295,
            "min_value": 1,
            "type": "integer",
            "uniqueScope": "no"
        },
        "LDAPSyncInterval": {
            "description": "LDAP Sync-Up task interval in seconds(min=600, max=86400).",
            "exposed": true,
            "format": "free",
            "max_value": 86400,
            "min_value": 600,
            "type": "integer",
            "uniqueScope": "no"
        },
        "LDAPTrustStoreCertifcate": {
            "description": "Location of the truststore which is need to store LDAP server certificates. Default is cacerts located in java.home/lib/security/cacerts. Uncomment below setting if you need to use a different file",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "LDAPTrustStorePassword": {
            "description": "Password to access the truststore. Uncomment below line to change its value.",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "LRUCacheSizePerSubnet": {
            "description": "LRU Map size per subnet ( to hold the deleted vm's ip addresses min =32, max 256).",
            "exposed": true,
            "format": "free",
            "max_value": 256,
            "min_value": 32,
            "type": "integer",
            "uniqueScope": "no"
        },
        "RDLowerLimit": {
            "description": "route distinguisher lower limit",
            "exposed": true,
            "format": "free",
            "max_value": 4294967294,
            "type": "integer",
            "uniqueScope": "no"
        },
        "RDPublicNetworkLowerLimit": {
            "description": "route distinguisher public network lower limit",
            "exposed": true,
            "format": "free",
            "max_value": 4294967294,
            "type": "integer",
            "uniqueScope": "no"
        },
        "RDPublicNetworkUpperLimit": {
            "description": "route distinguisher public network upper limit",
            "exposed": true,
            "format": "free",
            "max_value": 4294967295,
            "min_value": 1,
            "type": "integer",
            "uniqueScope": "no"
        },
        "RDUpperLimit": {
            "description": "route distinguisher upper limit",
            "exposed": true,
            "format": "free",
            "max_value": 4294967295,
            "min_value": 1,
            "type": "integer",
            "uniqueScope": "no"
        },
        "RTLowerLimit": {
            "description": "route target lower limit",
            "exposed": true,
            "format": "free",
            "max_value": 4294967294,
            "type": "integer",
            "uniqueScope": "no"
        },
        "RTPublicNetworkLowerLimit": {
            "description": "route target public network lower limit",
            "exposed": true,
            "format": "free",
            "max_value": 4294967294,
            "type": "integer",
            "uniqueScope": "no"
        },
        "RTPublicNetworkUpperLimit": {
            "description": "route target public network upper limit",
            "exposed": true,
            "format": "free",
            "max_value": 4294967295,
            "min_value": 1,
            "type": "integer",
            "uniqueScope": "no"
        },
        "RTUpperLimit": {
            "description": "route target upper limit",
            "exposed": true,
            "format": "free",
            "max_value": 4294967295,
            "min_value": 1,
            "type": "integer",
            "uniqueScope": "no"
        },
        "VMCacheSize": {
            "description": "LRU Map size for vm (min = 1000, max =100000) this value has to set based on memory given to VSD jvm not finalized.",
            "exposed": true,
            "format": "free",
            "max_value": 100000,
            "min_value": 1000,
            "type": "integer",
            "uniqueScope": "no"
        },
        "VMPurgeTime": {
            "description": "Timers in sec for undefined vms to be deleted(min =60, max = 600).",
            "exposed": true,
            "format": "free",
            "max_value": 600,
            "min_value": 60,
            "type": "integer",
            "uniqueScope": "no"
        },
        "VMResyncDeletionWaitTime": {
            "description": "After resync on vm , if no controller returns with a VM request with in the below timeframe then it will get deleted deletion wait time in min (min = 1, max =5)",
            "exposed": true,
            "format": "free",
            "max_value": 5,
            "min_value": 1,
            "type": "integer",
            "uniqueScope": "no"
        },
        "VMResyncOutstandingInterval": {
            "description": "Outstanding VM resync interval (in secs). (min = 500, max =2000) system wide value",
            "exposed": true,
            "format": "free",
            "max_value": 2000,
            "min_value": 500,
            "type": "integer",
            "uniqueScope": "no"
        },
        "VMUnreachableCleanupTime": {
            "description": "Timers in sec for unreachable VMs for cleanup(min = 3600, max = 86400).",
            "exposed": true,
            "format": "free",
            "max_value": 86400,
            "min_value": 3600,
            "type": "integer",
            "uniqueScope": "no"
        },
        "VMUnreachableTime": {
            "description": "Timers in sec for unreachable VMs (min =1800, max = 7200)",
            "exposed": true,
            "format": "free",
            "max_value": 7200,
            "min_value": 1800,
            "type": "integer",
            "uniqueScope": "no"
        },
        "VNIDLowerLimit": {
            "description": "Virtual network ID offset",
            "exposed": true,
            "format": "free",
            "max_value": 1048574,
            "min_value": 1,
            "type": "integer",
            "uniqueScope": "no"
        },
        "VNIDPublicNetworkLowerLimit": {
            "description": "Virtual network ID public network lower limit",
            "exposed": true,
            "format": "free",
            "max_value": 1048574,
            "min_value": 1,
            "type": "integer",
            "uniqueScope": "no"
        },
        "VNIDPublicNetworkUpperLimit": {
            "description": "Virtual network ID public network upper limit",
            "exposed": true,
            "format": "free",
            "max_value": 1048575,
            "min_value": 2,
            "type": "integer",
            "uniqueScope": "no"
        },
        "VNIDUpperLimit": {
            "description": "Virtual network ID upper limit",
            "exposed": true,
            "format": "free",
            "max_value": 1048575,
            "min_value": 2,
            "type": "integer",
            "uniqueScope": "no"
        },
        "VSCOnSameVersionAsVSD": {
            "description": "This flag is used to indicate that whether VSC is on the same version as VSD or not.",
            "exposed": true,
            "format": "free",
            "type": "boolean",
            "uniqueScope": "no"
        },
        "VSDReadOnlyMode": {
            "description": "True means VSD readonly mode enabled. False means VSD readonly mode disabled",
            "exposed": true,
            "format": "free",
            "type": "boolean",
            "uniqueScope": "no"
        },
        "VSDUpgradeIsComplete": {
            "description": "This flag is used to indicate that whether VSD upgrade is complete,it is expected that csproot will set to true,after VSD upgrade is complete and also making sure that all VSC's audits and Gateway audits with VSD are done",
            "exposed": true,
            "format": "free",
            "type": "boolean",
            "uniqueScope": "no"
        },
        "alarmsMaxPerObject": {
            "description": "Maximum alarms per object for example max distinct alarms for specific VM (min = 5, max =20)",
            "exposed": true,
            "format": "free",
            "max_value": 20,
            "min_value": 5,
            "type": "integer",
            "uniqueScope": "no"
        },
        "avatarBasePath": {
            "description": "Defines location where image files needs to be copied. Above URL should be configured to read the file from this location.",
            "exposed": true,
            "format": "free",
            "max_length": 255,
            "min_length": 1,
            "type": "string",
            "uniqueScope": "no"
        },
        "avatarBaseURL": {
            "description": "Defines the url to read the avatar image files",
            "exposed": true,
            "format": "free",
            "max_length": 255,
            "min_length": 1,
            "type": "string",
            "uniqueScope": "no"
        },
        "customerIDUpperLimit": {
            "description": "Customer id upper limit, system wide value",
            "exposed": true,
            "format": "free",
            "max_value": 2147483647,
            "min_value": 10000,
            "type": "integer",
            "uniqueScope": "no"
        },
        "customerKey": {
            "description": "Customer key associated with the licese",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "domainTunnelType": {
            "allowed_choices": [
                "DC_DEFAULT",
                "VXLAN",
                "GRE"
            ],
            "description": "Default Domain Tunnel Type .Possible values are VXLAN,GRE Possible values are DC_DEFAULT, GRE, VXLAN, .",
            "exposed": true,
            "format": "free",
            "type": "enum",
            "uniqueScope": "no"
        },
        "dynamicWANServiceDiffTime": {
            "description": "Timers in sec for  dynamic WAN Services to be considered not seen by 7X50(min =1, max = 7200)",
            "exposed": true,
            "format": "free",
            "max_value": 7200,
            "min_value": 1,
            "type": "integer",
            "uniqueScope": "no"
        },
        "ejbcaNSGCertificateProfile": {
            "description": "EJBCA NSG Certificate Profile",
            "exposed": true,
            "format": "free",
            "max_length": 255,
            "min_length": 1,
            "type": "string",
            "uniqueScope": "no"
        },
        "ejbcaNSGEndEntityProfile": {
            "description": "EJBCA NSG End Entity Profile",
            "exposed": true,
            "format": "free",
            "max_length": 255,
            "min_length": 1,
            "type": "string",
            "uniqueScope": "no"
        },
        "ejbcaOCSPResponderCN": {
            "description": "EJBCA OCSP Responder CommonName",
            "exposed": true,
            "format": "free",
            "max_length": 255,
            "min_length": 1,
            "type": "string",
            "uniqueScope": "no"
        },
        "ejbcaOCSPResponderURI": {
            "description": "EJBCA OCSP Responder URI",
            "exposed": true,
            "format": "free",
            "max_length": 255,
            "min_length": 1,
            "type": "string",
            "uniqueScope": "no"
        },
        "ejbcaVspRootCa": {
            "description": "EJBCA VSP CA",
            "exposed": true,
            "format": "free",
            "max_length": 255,
            "min_length": 1,
            "type": "string",
            "uniqueScope": "no"
        },
        "esiID": {
            "description": "ESI ID offset",
            "exposed": true,
            "format": "free",
            "max_value": 40000,
            "min_value": 1,
            "type": "integer",
            "uniqueScope": "no"
        },
        "eventLogCleanupInterval": {
            "description": "Cleanup task run interval in seconds (Min: every hour, Max: every day)",
            "exposed": true,
            "format": "free",
            "max_value": 86400,
            "min_value": 3600,
            "type": "integer",
            "uniqueScope": "no"
        },
        "eventLogEntryMaxAge": {
            "description": "Maximum age in days for cleanup of the eventlog entries (Min: 1 day, Max: 6 months). On every periodic interval run, any eventlog entries older than the maxage will be deleted.",
            "exposed": true,
            "format": "free",
            "max_value": 180,
            "min_value": 1,
            "type": "integer",
            "uniqueScope": "no"
        },
        "eventProcessorInterval": {
            "description": "Defines time interval in milliseconds when events collected for a client should be processed. Minimum value is 250ms.",
            "exposed": true,
            "format": "free",
            "min_value": 250,
            "type": "integer",
            "uniqueScope": "no"
        },
        "eventProcessorMaxEventsCount": {
            "description": "Defines the maximum number of events to be collected in case of events burst. Value should be between 100 to 500.",
            "exposed": true,
            "format": "free",
            "max_value": 500,
            "min_value": 100,
            "type": "integer",
            "uniqueScope": "no"
        },
        "eventProcessorTimeout": {
            "description": "Defines the maximum time period in milliseconds for the Rest server to wait before sending the events from the system. Value should be between 25000ms to 100000ms.",
            "exposed": true,
            "format": "free",
            "max_value": 100000,
            "min_value": 25000,
            "type": "integer",
            "uniqueScope": "no"
        },
        "groupKeyDefaultSEKGenerationInterval": {
            "description": "Group Key Encryption Profile Default SEK Generation Interval",
            "exposed": true,
            "format": "free",
            "type": "integer",
            "uniqueScope": "no"
        },
        "groupKeyDefaultSEKLifetime": {
            "description": "Group Key Encryption Profile Default SEK Lifetime",
            "exposed": true,
            "format": "free",
            "type": "integer",
            "uniqueScope": "no"
        },
        "groupKeyDefaultSEKPayloadEncryptionAlgorithm": {
            "allowed_choices": [
                "RSA_1024"
            ],
            "description": "Group Key Encryption Profile Default Sek Payload Encryption Algorithm Possible values are RSA_1024, .",
            "exposed": true,
            "format": "free",
            "type": "enum",
            "uniqueScope": "no"
        },
        "groupKeyDefaultSEKPayloadSigningAlgorithm": {
            "allowed_choices": [
                "SHA256withRSA",
                "SHA1withRSA",
                "SHA384withRSA",
                "SHA224withRSA",
                "SHA512withRSA"
            ],
            "description": "Group Key Encryption Profile Default Sek Payload Signing Algorithm Possible values are SHA1withRSA, SHA224withRSA, SHA256withRSA, SHA384withRSA, SHA512withRSA, .",
            "exposed": true,
            "format": "free",
            "type": "enum",
            "uniqueScope": "no"
        },
        "groupKeyDefaultSeedGenerationInterval": {
            "description": "Group Key Encryption Profile Default Seed Generation Interval",
            "exposed": true,
            "format": "free",
            "type": "integer",
            "uniqueScope": "no"
        },
        "groupKeyDefaultSeedLifetime": {
            "description": "Group Key Encryption Profile Default Seed Lifetime",
            "exposed": true,
            "format": "free",
            "type": "integer",
            "uniqueScope": "no"
        },
        "groupKeyDefaultSeedPayloadAuthenticationAlgorithm": {
            "allowed_choices": [
                "HMAC_SHA512",
                "HMAC_SHA1",
                "HMAC_SHA256"
            ],
            "description": "Group Key Encryption Profile Default Seed Payload Authentication Algorithm Possible values are HMAC_SHA1, HMAC_SHA256, HMAC_SHA512, .",
            "exposed": true,
            "format": "free",
            "type": "enum",
            "uniqueScope": "no"
        },
        "groupKeyDefaultSeedPayloadEncryptionAlgorithm": {
            "allowed_choices": [
                "AES_128_CBC",
                "AES_256_CBC",
                "TRIPLE_DES_CBC"
            ],
            "description": "Group Key Encryption Profile Default Seed Payload Encryption Algorithm Possible values are AES_128_CBC, AES_256_CBC, TRIPLE_DES_CBC, .",
            "exposed": true,
            "format": "free",
            "type": "enum",
            "uniqueScope": "no"
        },
        "groupKeyDefaultSeedPayloadSigningAlgorithm": {
            "allowed_choices": [
                "SHA256withRSA",
                "SHA1withRSA",
                "SHA384withRSA",
                "SHA224withRSA",
                "SHA512withRSA"
            ],
            "description": "Group Key Encryption Profile Default Seed Payload Signature Algorithm Possible values are SHA1withRSA, SHA224withRSA, SHA256withRSA, SHA384withRSA, SHA512withRSA, .",
            "exposed": true,
            "format": "free",
            "type": "enum",
            "uniqueScope": "no"
        },
        "groupKeyDefaultTrafficAuthenticationAlgorithm": {
            "allowed_choices": [
                "HMAC_SHA384",
                "HMAC_SHA512",
                "HMAC_SHA1",
                "HMAC_MD5",
                "HMAC_SHA256"
            ],
            "description": "Group Key Encryption Profile Default Traffic Authentication Algorithm Possible values are HMAC_SHA1, HMAC_SHA256, HMAC_SHA384, HMAC_SHA512, HMAC_MD5, .",
            "exposed": true,
            "format": "free",
            "type": "enum",
            "uniqueScope": "no"
        },
        "groupKeyDefaultTrafficEncryptionAlgorithm": {
            "allowed_choices": [
                "AES_128_CBC",
                "AES_256_CBC",
                "AES_192_CBC",
                "TRIPLE_DES_CBC"
            ],
            "description": "Group Key Encryption Profile Default Traffic Encryption Algorithm Possible values are AES_128_CBC, AES_192_CBC, AES_256_CBC, TRIPLE_DES_CBC, .",
            "exposed": true,
            "format": "free",
            "type": "enum",
            "uniqueScope": "no"
        },
        "groupKeyDefaultTrafficEncryptionKeyLifetime": {
            "description": "Group Key Encryption Profile Default Traffic Encryption Key Lifetime",
            "exposed": true,
            "format": "free",
            "type": "integer",
            "uniqueScope": "no"
        },
        "groupKeyGenerationIntervalOnForcedReKey": {
            "description": "Time in seconds before new keys will be generated in the case of a forced re-key event",
            "exposed": true,
            "format": "free",
            "type": "integer",
            "uniqueScope": "no"
        },
        "groupKeyGenerationIntervalOnRevoke": {
            "description": "Time in seconds before new keys will be generated in the case of a revoke event",
            "exposed": true,
            "format": "free",
            "type": "integer",
            "uniqueScope": "no"
        },
        "groupKeyMinimumSEKGenerationInterval": {
            "description": "Group Key Encryption Profile Minimum SEK Generation Interval",
            "exposed": true,
            "format": "free",
            "type": "integer",
            "uniqueScope": "no"
        },
        "groupKeyMinimumSEKLifetime": {
            "description": "Group Key Encryption Profile Minimum SEK Lifetime",
            "exposed": true,
            "format": "free",
            "type": "integer",
            "uniqueScope": "no"
        },
        "groupKeyMinimumSeedGenerationInterval": {
            "description": "Group Key Encryption Profile Default Seed Generation Interval",
            "exposed": true,
            "format": "free",
            "type": "integer",
            "uniqueScope": "no"
        },
        "groupKeyMinimumSeedLifetime": {
            "description": "Group Key Encryption Profile Default Seed Lifetime",
            "exposed": true,
            "format": "free",
            "type": "integer",
            "uniqueScope": "no"
        },
        "groupKeyMinimumTrafficEncryptionKeyLifetime": {
            "description": "Group Key Encryption Profile Minimum TEK Lifetime",
            "exposed": true,
            "format": "free",
            "type": "integer",
            "uniqueScope": "no"
        },
        "inactiveTimeout": {
            "description": "Defines the inactive timeout for the client. If the client is inactive for more than timeout, server clears off all the cache/information regarding the client. This value should be greater than event processor max timeout",
            "exposed": true,
            "format": "free",
            "min_value": 25000,
            "type": "integer",
            "uniqueScope": "no"
        },
        "keyServerMonitorEnabled": {
            "description": "Enable the keyserver debug monitor (ie. ksmon command)",
            "exposed": true,
            "format": "free",
            "type": "boolean",
            "uniqueScope": "no"
        },
        "keyServerVSDDataSynchronizationInterval": {
            "description": "KeyServer time in seconds between full resyncs of VSD data (just in case of missed events)",
            "exposed": true,
            "format": "free",
            "type": "integer",
            "uniqueScope": "no"
        },
        "maxFailedLogins": {
            "description": "Maximum failed login attempts before the account is locked (min = 5, max = 10). 0 = not enforced (unlimited attempts). This is not enforced if LDAP is used for authorization",
            "exposed": true,
            "format": "free",
            "max_value": 10,
            "type": "integer",
            "uniqueScope": "no"
        },
        "maxResponse": {
            "description": "Defines maximum results returned by the REST call (allowed max=5000).",
            "exposed": true,
            "format": "free",
            "min_value": 1,
            "type": "integer",
            "uniqueScope": "no"
        },
        "nsgBootstrapEndpoint": {
            "description": "NSG Bootstrap Endpoint",
            "exposed": true,
            "format": "free",
            "max_length": 255,
            "min_length": 1,
            "type": "string",
            "uniqueScope": "no"
        },
        "nsgConfigEndpoint": {
            "description": "NSG Config Endpoint",
            "exposed": true,
            "format": "free",
            "max_length": 255,
            "min_length": 1,
            "type": "string",
            "uniqueScope": "no"
        },
        "nsgLocalUiUrl": {
            "description": "NSG Local UI URL - will be redirected on NSG to localhost",
            "exposed": true,
            "format": "free",
            "max_length": 255,
            "min_length": 1,
            "type": "string",
            "uniqueScope": "no"
        },
        "offsetCustomerID": {
            "description": "Customer id offset, this value has to be set before jboss starts , after that any change of value is ignored (minexclusive = 0, max = 20000) system wide value",
            "exposed": true,
            "format": "free",
            "max_value": 2147483646,
            "min_value": 10000,
            "type": "integer",
            "uniqueScope": "no"
        },
        "offsetServiceID": {
            "description": "Service id offset, this value has to be set before jboss starts during install time, after that any change of value is ignored (minexclusive = 0, max = 40000) system wide value",
            "exposed": true,
            "format": "free",
            "max_value": 2148007977,
            "min_value": 20001,
            "type": "integer",
            "uniqueScope": "no"
        },
        "pageMaxSize": {
            "description": "Defines upper bound for the page size (allowed max=1000). Configured or input page size should be less than this max page size.",
            "exposed": true,
            "format": "free",
            "min_value": 5,
            "type": "integer",
            "uniqueScope": "no"
        },
        "pageSize": {
            "description": "Defines the page size for the results returned by the REST call.",
            "exposed": true,
            "format": "free",
            "min_value": 1,
            "type": "integer",
            "uniqueScope": "no"
        },
        "postProcessorThreadsCount": {
            "description": "Post processor thread count.",
            "exposed": true,
            "format": "free",
            "min_value": 1,
            "type": "integer",
            "uniqueScope": "no"
        },
        "reflexiveACLTimeout": {
            "description": "Defines the timeout in seconds for reflexive ACLs. This value applies for both TCP and UDP connections. Default value is 180 seconds and the timeout should be between 10 to 86400 seconds.",
            "exposed": true,
            "format": "free",
            "max_value": 86400,
            "min_value": 10,
            "type": "integer",
            "uniqueScope": "no"
        },
        "serviceIDUpperLimit": {
            "description": "Service id upper limit system wide value",
            "exposed": true,
            "format": "free",
            "max_value": 2148007978,
            "min_value": 20002,
            "type": "integer",
            "uniqueScope": "no"
        },
        "stackTraceEnabled": {
            "description": "True to enable stacktrace in the REST call.",
            "exposed": true,
            "format": "free",
            "type": "boolean",
            "uniqueScope": "no"
        },
        "statefulAclTcpTimeout": {
            "default_value": "3600",
            "description": "defines the timeout in seconds for stateful ACLs that are of type TCP. Default value is 3600 secs and the timeout should be between 3600 to 86400 seconds",
            "exposed": true,
            "filterable": true,
            "orderable": true,
            "type": "integer"
        },
        "staticWANServicePurgeTime": {
            "description": "Timers in sec for unreacheable static WAN Services to be deleted(min =3600, max = 7200)",
            "exposed": true,
            "format": "free",
            "max_value": 7200,
            "min_value": 3600,
            "type": "integer",
            "uniqueScope": "no"
        },
        "statsCollectorAddress": {
            "description": "Specify the ip address(es) of the stats collector.",
            "exposed": true,
            "format": "free",
            "max_length": 255,
            "min_length": 1,
            "type": "string",
            "uniqueScope": "no"
        },
        "statsCollectorPort": {
            "description": "Specify the port number(s) of the stats collector.",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "statsCollectorProtoBufPort": {
            "description": "Specify the protobuf port number(s) of the stats collector.",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "statsMaxDataPoints": {
            "description": "Specifies the maximum number of data points to support.",
            "exposed": true,
            "format": "free",
            "min_value": 1,
            "type": "integer",
            "uniqueScope": "no"
        },
        "statsMinDuration": {
            "description": "Default minimum duration for statistics to be displayed in UI is 30 days in seconds.",
            "exposed": true,
            "format": "free",
            "type": "integer",
            "uniqueScope": "no"
        },
        "statsNumberOfDataPoints": {
            "description": "Specifies number of data points.",
            "exposed": true,
            "format": "free",
            "min_value": 1,
            "type": "integer",
            "uniqueScope": "no"
        },
        "statsTSDBServerAddress": {
            "description": "Specifies the TSDB server location.",
            "exposed": true,
            "format": "free",
            "max_length": 255,
            "min_length": 1,
            "type": "string",
            "uniqueScope": "no"
        },
        "subnetResyncInterval": {
            "description": "After resync on a subnet , another resync on the same subnet is allowed based on the below value subnet resync complete wait time in min (min = 5, max =15)",
            "exposed": true,
            "format": "free",
            "max_value": 15,
            "min_value": 5,
            "type": "integer",
            "uniqueScope": "no"
        },
        "subnetResyncOutstandingInterval": {
            "description": "Outstanding subnet resync interval (in secs). (min = 10, max = 50) system wide value",
            "exposed": true,
            "format": "free",
            "max_value": 50,
            "min_value": 10,
            "type": "integer",
            "uniqueScope": "no"
        },
        "syslogDestinationHost": {
            "description": "Specifies the remote syslog destination host",
            "exposed": true,
            "format": "free",
            "max_length": 255,
            "min_length": 1,
            "type": "string",
            "uniqueScope": "no"
        },
        "syslogDestinationPort": {
            "description": "Specified the remote syslog destination port",
            "exposed": true,
            "format": "free",
            "type": "integer",
            "uniqueScope": "no"
        },
        "sysmonCleanupTaskInterval": {
            "description": "Sysmon cleanup task run interval in seconds (Min: 10 secs,  Max: 3600 secs)",
            "exposed": true,
            "format": "free",
            "max_value": 3600,
            "min_value": 10,
            "type": "integer",
            "uniqueScope": "no"
        },
        "sysmonNodePresenceTimeout": {
            "description": "Node presence timeout in seconds if no messages (Min: 600,  Max: 86400)",
            "exposed": true,
            "format": "free",
            "max_value": 86400,
            "min_value": 600,
            "type": "integer",
            "uniqueScope": "no"
        },
        "sysmonProbeResponseTimeout": {
            "description": "Probe response timeout in seconds (Min: 5,  Max: 60)",
            "exposed": true,
            "format": "free",
            "max_value": 60,
            "min_value": 5,
            "type": "integer",
            "uniqueScope": "no"
        },
        "twoFactorCodeExpiry": {
            "description": "Two Factor Code Expiry in Seconds",
            "exposed": true,
            "format": "free",
            "type": "integer",
            "uniqueScope": "no"
        },
        "twoFactorCodeLength": {
            "description": "Two Factor Code Length",
            "exposed": true,
            "format": "free",
            "type": "integer",
            "uniqueScope": "no"
        },
        "twoFactorCodeSeedLength": {
            "description": "Two Factor Seed length in bytes",
            "exposed": true,
            "format": "free",
            "type": "integer",
            "uniqueScope": "no"
        }
    },
    "model": {
        "description": "The system configuration which can be dynamically managed using rest api.",
        "entity_name": "SystemConfig",
        "extends": [
            "@audited",
            "@base",
            "@metadata"
        ],
        "get": true,
        "package": "systemconfig",
        "resource_name": "systemconfigs",
        "rest_name": "systemconfig",
        "update": true
    }
}