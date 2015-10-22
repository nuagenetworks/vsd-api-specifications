{
    "attributes": {
        "mcastType": {
            "description": "Type of multicast list - send or receive Possible values are SEND, RECEIVE, .", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "allowed_choices": [
                "SEND", 
                "RECEIVE"
            ], 
            "orderable": true, 
            "type": "enum"
        }
    }, 
    "model": {
        "resource_name": "multicastlists", 
        "description": "This is the definition of a MultiCast Channel List", 
        "entity_name": "MultiCastList", 
        "package": "network", 
        "get": true, 
        "rest_name": "multicastlist", 
        "extends": [
            "@base", 
            "@metadata"
        ]
    }, 
    "children": {
        "multicastchannelmap": {
            "update": true, 
            "relationship": "child", 
            "get": true
        }
    }
}