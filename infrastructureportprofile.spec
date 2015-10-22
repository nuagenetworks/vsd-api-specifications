{
    "attributes": {
        "uplinkTag": {
            "description": "To allow prioritisation of traffic, the NSG network ports must be configured with an uplink type or tag value which will be used in the identification of packets being forwarded.  That identification is at the base of the selection of which network port will serve in sending packets to the outside world.  The default value is PRIMARY. Possible values are PRIMARY, SECONDARY, TERTIARY, UNKNOWN, .", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "allowed_choices": [
                "SECONDARY", 
                "PRIMARY", 
                "UNKNOWN", 
                "TERTIARY"
            ], 
            "orderable": true, 
            "type": "enum"
        }, 
        "description": {
            "description": "A description of the Profile instance created.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "duplex": {
            "description": "Port Duplex :  Supported values are FULL where both parties can communicate to the other simultaneously and HALF where each party can only communicate to each other in one direction at a time. Possible values are FULL, HALF, SIMPLEX, .", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "allowed_choices": [
                "SIMPLEX", 
                "FULL", 
                "HALF"
            ], 
            "orderable": true, 
            "type": "enum"
        }, 
        "mtu": {
            "description": "Port MTU (Maximum Transmission Unit) :  The size in octets of the largest protocol data unit (PDU) that the layer can pass on.  The default value is normally 1500 octets for Ethernet v2 and can go up to 9198 for Jumbo Frames.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "integer"
        }, 
        "enterpriseID": {
            "description": "Enterprise/Organisation associated with this Profile instance.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "enterprise": {
            "description": "Name of the enterprise/organisation associated with this Profile instance.  This is a read only attribute", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "speed": {
            "description": "Port Speed in Mb/s :  Supported Ethernet speeds are 10 (10Base-T), 100 (Fast-ethernet 100Base-TX), 1000 (Gigabit Ethernet 1000Base-T), 10 000 (10 Gigabit Ethernet 10GBase-X), and Auto-Negotiate. Possible values are BASET10, BASETX100, BASET1000, BASEX10G, AUTONEGOTIATE, .", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "allowed_choices": [
                "BASETX100", 
                "BASET10", 
                "AUTONEGOTIATE", 
                "BASEX10G", 
                "BASET1000"
            ], 
            "orderable": true, 
            "type": "enum"
        }, 
        "name": {
            "description": "Name of the Infrastructure Profile", 
            "format": "free", 
            "filterable": true, 
            "uniqueScope": "no", 
            "required": true, 
            "exposed": true, 
            "orderable": true, 
            "type": "string"
        }
    }, 
    "model": {
        "resource_name": "infrastructureportprofiles", 
        "description": "Represents an Infrastructure Port Profile", 
        "entity_name": "InfrastructurePortProfile", 
        "package": "infrastructure", 
        "get": true, 
        "update": true, 
        "rest_name": "infrastructureportprofile", 
        "extends": [
            "@base", 
            "@metadata"
        ], 
        "delete": true
    }
}