{
    "attributes": {
        "peerAS": {
            "description": "neighbor's autonomous system", 
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