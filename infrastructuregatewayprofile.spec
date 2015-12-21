{
    "attributes": {
        "NTPServerKey": {
            "description": "If set, this represents the security key for the Gateway to communicate with the NTP server (a VSC).", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "NTPServerKeyID": {
            "description": "Correspond to the key ID on the NTP server that matches the ntpServerKey value.  Valid values are from 1 to 255 as specified by SR-OS and 0 to specify unused (VSD/NSG only).", 
            "exposed": true, 
            "filterable": true,
            "orderable": true, 
            "type": "integer", 
            "min_value": 0,
            "max_value": 255,
            "default_value": 0,
            "uniqueScope": "no"
        }, 
        "activeController": {
            "description": "VSC Active Controller :  IP Address of the primary VSC system NSG instances associated to this profile will be reaching for.", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "min_length": 0,
            "max_length": 255,
            "uniqueScope": "no"
        }, 
        "datapathSyncTimeout": {
            "description": "Datapath flows sync-time-interval specified in milliseconds (default: 1000)", 
            "exposed": true, 
            "filterable": true,
            "orderable": true, 
            "type": "integer",
            "min_value": 1000,
            "max_value": 60000,
            "default_value": 1000,
            "uniqueScope": "no"
        }, 
        "deadTimer": {
            "allowed_choices": [
                "THREE_HOURS", 
                "THIRTY_MINUTES", 
                "TEN_MINUTES", 
                "ONE_HOUR", 
                "FOUR_HOURS", 
                "SIX_HOURS", 
                "MAXIMUM_DURATION", 
                "TWO_HOURS", 
                "FIVE_HOURS", 
                "NONE"
            ], 
            "description": "Time, in seconds, allowed for a Gateway to be inactive before the VSD revokes its certificates and marks it as untrusted.  Default value is 1 hour (3600) Possible values are NONE, TEN_MINUTES, THIRTY_MINUTES, ONE_HOUR, TWO_HOURS, THREE_HOURS, FOUR_HOURS, FIVE_HOURS, SIX_HOURS, MAXIMUM_DURATION, .", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "enum", 
            "uniqueScope": "no"
        }, 
        "description": {
            "description": "A description of the Profile instance created.", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "enterprise": {
            "description": "Name of the enterprise/organisation associated with this Profile instance.  This is a read only attribute", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "enterpriseID": {
            "description": "Enterprise/Organisation associated with this Profile instance.", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "flowEvictionThreshold": {
            "description": "Number of flows at which eviction from kernel flow table will be triggered (default: 2500)", 
            "exposed": true, 
            "filterable": true,
            "orderable": true, 
            "type": "integer",
            "min_value": 100,
            "max_value": 200000,
	    "default_value": 2500,
            "uniqueScope": "no"
        }, 
        "metadataUpgradePath": {
            "description": "Path/URL to retrieve the NSG Upgrade information meta data files.  From that meta data, the NSG will be able to retrieve the upgrade package files and perform some validations.  It is expected that the meta data file is in JSON format.  RFC 2616 states that there are no 'official' maximum length for a URL but different browsers and servers have limits.  Our friendly Internet Explorer has a maximum of 'around' 2048 characters, we shall use this as a limit here.", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "name": {
            "description": "Name of the Infrastructure Profile", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "required": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "proxyDNSName": {
            "description": "Proxy DNS Name :  DNS Name of the system acting as a proxy between the NSG instances and the VSD.", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "required": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "remoteLogDirPath": {
            "description": "Path on the remote log server where the logs generated by the NSG are to be stored.  This field is only useful for SCP and SFTP.", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "remoteLogMode": {
            "allowed_choices": [
                "SCP", 
                "RSYSLOG", 
                "SFTP", 
                "DISABLED"
            ], 
            "description": "Type of Log Server for system logs generated by Gateways associated with this Infrastructure Profile.  Valid values are SCP, SFTP, RSyslog, and Disabled.  This field is set to Disabled by default. Possible values are SCP, SFTP, RSYSLOG, DISABLED, .", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "enum", 
            "uniqueScope": "no"
        }, 
        "remoteLogPassword": {
            "description": "Password to be used when accessing the remote log server via SCP or SFTP.  This field is only useful for SCP and SFTP.", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "remoteLogServerAddress": {
            "description": "Primary Log Server for system logs generated by Gateways associated with this Infrastructure Profile.  Can be an IP address or a URL.  This field is optional.", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "remoteLogServerPort": {
            "description": "Port to be used to access the Remote Syslog server.  By default, this is port 514.", 
            "exposed": true, 
            "filterable": true,
            "orderable": true, 
            "type": "integer",
            "min_value": 1,
            "max_value": 65535,
            "default_value": 514,
            "uniqueScope": "no"
        }, 
        "remoteLogUsername": {
            "description": "Username to be used when accessing the remote log server via SCP or SFTP.  This field is only useful for SCP and SFTP.", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "standbyController": {
            "description": "VSC Standby Controller :  IP Address of the standby VSC system NSG instances associated to this profile will be reaching for.", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "statsCollectorPort": {
            "description": "The port to open by the proxy for stats collector to use", 
            "exposed": true, 
            "filterable": true,
            "orderable": true, 
            "type": "integer", 
            "uniqueScope": "no"
        }, 
        "systemSyncScheduler": {
            "description": "Time in a Cron format when configuration update are being applied on the Gateway (NSG).  This property is linked to systemSyncWindow.  Default value is every midnight (0 0 * * *).  Format:  Minutes Hours DayOfMonth Month DayOfWeek", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "systemSyncWindow": {
            "allowed_choices": [
                "THREE_HOURS", 
                "THIRTY_MINUTES", 
                "TEN_MINUTES", 
                "ONE_HOUR", 
                "FOUR_HOURS", 
                "SIX_HOURS", 
                "MAXIMUM_DURATION", 
                "TWO_HOURS", 
                "FIVE_HOURS", 
                "NONE"
            ], 
            "description": "Length of time, in seconds, given to a Gateway to apply a configuration change.  This property is closely linked to systemSyncScheduler.  Default value is 1 hour (3600 s) Possible values are NONE, TEN_MINUTES, THIRTY_MINUTES, ONE_HOUR, TWO_HOURS, THREE_HOURS, FOUR_HOURS, FIVE_HOURS, SIX_HOURS, MAXIMUM_DURATION, .", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "enum", 
            "uniqueScope": "no"
        }, 
        "upgradeAction": {
            "allowed_choices": [
                "UPGRADE_AT_BOOTSTRAPPING", 
                "DOWNLOAD_AND_UPGRADE_NOW", 
                "UPGRADE_NOW", 
                "NONE", 
                "DOWNLOAD_AND_UPGRADE_AT_WINDOW", 
                "DOWNLOAD_ONLY"
            ], 
            "description": "Upgrade action for NSG associated with this Infrastructure Gateway Profile instance.  By default, there is no upgrade. Possible values are DOWNLOAD_ONLY, DOWNLOAD_AND_UPGRADE_AT_WINDOW, DOWNLOAD_AND_UPGRADE_NOW, UPGRADE_NOW, UPGRADE_AT_BOOTSTRAPPING, NONE, .", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "enum", 
            "uniqueScope": "no"
        }, 
        "useTwoFactor": {
            "description": "Use Two Factor :  When set to true, the use of two independent authentication factors will be used to secure the installed NSG.  When set to false, there is an assumption that the NSG is being installed in a secure environment and the installer is also trusted.  The defaut value is true, using 2-factor.", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "boolean", 
            "uniqueScope": "no"
        }
    }, 
    "model": {
        "delete": true, 
        "description": "Represents Infrastructure Gateway Profile", 
        "entity_name": "InfrastructureGatewayProfile", 
        "extends": [
            "@base", 
            "@metadata"
        ], 
        "get": true, 
        "package": "infrastructure", 
        "resource_name": "infrastructuregatewayprofiles", 
        "rest_name": "infrastructuregatewayprofile", 
        "update": true
    }
}