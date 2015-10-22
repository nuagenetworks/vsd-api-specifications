{
    "attributes": {
        "entityParentID": {
            "description": "The entity parent id associated with this event. It can be null.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "entityParentType": {
            "description": "Event parent entity type.  Generally reported against enterprise.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "entityType": {
            "description": "The entity type of this event. It may be Domain, VirtualMachine, etc.,", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "entities": {
            "description": "List of entities associated with the event.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "list"
        }, 
        "user": {
            "description": "The authenticated user who triggered this event.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "enterprise": {
            "description": "The enterprise name of the user who triggered this event.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "diff": {
            "description": "Holds the results of diff between two objects of same type.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "entityID": {
            "description": "The entity id associated with this event.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "type": {
            "description": "The event type (CREATE, UPDATE or DELETE).", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "string"
        }, 
        "eventReceivedTime": {
            "description": "The time that event was received.", 
            "format": "free", 
            "filterable": true, 
            "exposed": true, 
            "uniqueScope": "no", 
            "orderable": true, 
            "type": "time"
        }
    }, 
    "model": {
        "resource_name": "eventlogs", 
        "description": "The API retrieves the events related to a particular entity", 
        "entity_name": "EventLog", 
        "package": "eventlog", 
        "get": true, 
        "rest_name": "eventlog", 
        "extends": [
            "@base", 
            "@metadata"
        ]
    }
}