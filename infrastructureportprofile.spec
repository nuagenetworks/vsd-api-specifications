{
    "attributes": {
        "description": {
            "description": "A description of the Profile instance created.", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "duplex": {
            "allowed_choices": [
                "SIMPLEX", 
                "FULL", 
                "HALF"
            ], 
            "description": "Port Duplex :  Supported values are FULL where both parties can communicate to the other simultaneously and HALF where each party can only communicate to each other in one direction at a time. Possible values are FULL, HALF, SIMPLEX, .", 
            "exposed": true, 
            "type": "enum", 
            "uniqueScope": "no"
        }, 
        "enterprise": {
            "description": "Name of the enterprise/organisation associated with this Profile instance.  This is a read only attribute", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "enterpriseID": {
            "description": "Enterprise/Organisation associated with this Profile instance.", 
            "exposed": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "mtu": {
            "description": "Port MTU (Maximum Transmission Unit) :  The size in octets of the largest protocol data unit (PDU) that the layer can pass on.  The default value is normally 1500 octets for Ethernet v2 and can go up to 9198 for Jumbo Frames.", 
            "exposed": true, 
            "type": "integer", 
            "uniqueScope": "no"
        }, 
        "name": {
            "description": "Name of the Infrastructure Profile", 
            "exposed": true, 
            "required": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "speed": {
            "allowed_choices": [
                "BASETX100", 
                "BASET10", 
                "AUTONEGOTIATE", 
                "BASEX10G", 
                "BASET1000"
            ], 
            "description": "Port Speed in Mb/s :  Supported Ethernet speeds are 10 (10Base-T), 100 (Fast-ethernet 100Base-TX), 1000 (Gigabit Ethernet 1000Base-T), 10 000 (10 Gigabit Ethernet 10GBase-X), and Auto-Negotiate. Possible values are BASET10, BASETX100, BASET1000, BASEX10G, AUTONEGOTIATE, .", 
            "exposed": true, 
            "type": "enum", 
            "uniqueScope": "no"
        }, 
        "uplinkTag": {
            "allowed_choices": [
                "SECONDARY", 
                "PRIMARY", 
                "UNKNOWN", 
                "TERTIARY"
            ], 
            "description": "To allow prioritisation of traffic, the NSG network ports must be configured with an uplink type or tag value which will be used in the identification of packets being forwarded.  That identification is at the base of the selection of which network port will serve in sending packets to the outside world.  The default value is PRIMARY. Possible values are PRIMARY, SECONDARY, TERTIARY, UNKNOWN, .", 
            "exposed": true, 
            "type": "enum", 
            "uniqueScope": "no"
        }
    }, 
    "delete": true, 
    "description": "Represents an Infrastructure Port Profile", 
    "entity_name": "InfrastructurePortProfile", 
    "extends": [
        "@base", 
        "@metadata"
    ], 
    "get": true, 
    "package": "/infrastructure", 
    "resource_name": "infrastructureportprofiles", 
    "rest_name": "infrastructureportprofile", 
    "update": true
}