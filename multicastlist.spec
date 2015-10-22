{
    "attributes": {
        "mcastType": {
            "allowed_choices": [
                "SEND", 
                "RECEIVE"
            ], 
            "description": "Type of multicast list - send or receive Possible values are SEND, RECEIVE, .", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "enum", 
            "uniqueScope": "no"
        }
    }, 
    "children": {
        "multicastchannelmap": {
            "get": true, 
            "relationship": "child", 
            "update": true
        }
    }, 
    "description": "This is the definition of a MultiCast Channel List", 
    "entity_name": "MultiCastList", 
    "extends": [
        "@base", 
        "@metadata"
    ], 
    "get": true, 
    "package": "/network", 
    "resource_name": "multicastlists", 
    "rest_name": "multicastlist"
}