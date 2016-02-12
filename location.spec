{
    "attributes": {
        "address": {
            "description": "Formatted address including property number, street name, suite or office number, ...",
            "exposed": true,
            "format": "free",
            "max_length": 255,
            "type": "string",
            "uniqueScope": "no"
        },
        "country": {
            "description": "Country",
            "exposed": true,
            "format": "free",
            "max_length": 255,
            "type": "string",
            "uniqueScope": "no"
        },
        "ignoreGeocode": {
            "description": "Request BSS to perform a geocode on the address - If no value passed, requestGeocode will be set to true",
            "exposed": true,
            "format": "free",
            "type": "boolean",
            "uniqueScope": "no"
        },
        "latitude": {
            "description": "Latitude in decimal format.",
            "exposed": true,
            "format": "free",
            "max_value": 90,
            "min_value": -90,
            "type": "float",
            "uniqueScope": "no"
        },
        "locality": {
            "description": "Locality/City/County",
            "exposed": true,
            "format": "free",
            "max_length": 255,
            "type": "string",
            "uniqueScope": "no"
        },
        "longitude": {
            "description": "Longitude in decimal format.",
            "exposed": true,
            "format": "free",
            "max_value": 180,
            "min_value": -180,
            "type": "float",
            "uniqueScope": "no"
        },
        "state": {
            "description": "State/Province/Region",
            "exposed": true,
            "format": "free",
            "max_length": 255,
            "type": "string",
            "uniqueScope": "no"
        },
        "timeZoneID": {
            "description": "Time zone in which the Gateway is located.  This can be in the form of a UTC/GMT offset, continent/city location, or country/region.  The available time zones can be found in /usr/share/zoneinfo on a Linux machine or retrieved with TimeZone.getAvailableIDs() in Java.  Refer to the IANA (Internet Assigned Numbers Authority) for a list of time zones.  URL :  http://www.iana.org/time-zones  Default value is UTC (translating to Etc/Zulu)",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        }
    },
    "model": {
        "description": "Gateway location details.",
        "entity_name": "Location",
        "extends": [
            "@audited",
            "@base",
            "@metadata"
        ],
        "get": true,
        "package": "gateway",
        "resource_name": "locations",
        "rest_name": "location",
        "update": true
    }
}