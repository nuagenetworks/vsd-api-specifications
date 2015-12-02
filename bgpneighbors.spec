{
    "attributes": {
        "peerAS": {
            "description": "neighbor's autonomous system", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "required": true, 
            "type": "integer"
        }, 
        "peerIP": {
            "description": "IP Address of the neighbor. If the neighbor is attached to a host vPort this is optional or must be the same as the host's IP.", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string"
        }
    }, 
    "model": {
        "delete": true, 
        "entity_name": "BgpNeighbor", 
        "get": true, 
        "resource_name": "bgpneighbors", 
        "rest_name": "bgpneighbors", 
        "update": true
    }
}