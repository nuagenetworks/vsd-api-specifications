{
    "attributes": {
        "diff": {
            "description": "Holds the results of diff between two objects of same type.", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "enterprise": {
            "description": "The enterprise name of the user who triggered this event.", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "entities": {
            "description": "List of entities associated with the event.", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "list", 
            "uniqueScope": "no"
        }, 
        "entityID": {
            "description": "The entity id associated with this event.", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "entityParentID": {
            "description": "The entity parent id associated with this event. It can be null.", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "entityParentType": {
            "description": "Event parent entity type.  Generally reported against enterprise.", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "entityType": {
            "description": "The entity type of this event. It may be Domain, VirtualMachine, etc.,", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "eventReceivedTime": {
            "description": "The time that event was received.", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "time", 
            "uniqueScope": "no"
        }, 
        "type": {
            "description": "The event type (CREATE, UPDATE or DELETE).", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "user": {
            "description": "The authenticated user who triggered this event.", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }
    }, 
    "description": "The API retrieves the events related to a particular entity", 
    "entity_name": "EventLog", 
    "extends": [
        "@base", 
        "@metadata"
    ], 
    "get": true, 
    "package": "eventlog", 
    "resource_name": "eventlogs", 
    "rest_name": "eventlog"
}