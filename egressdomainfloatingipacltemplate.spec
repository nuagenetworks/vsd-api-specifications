{
    "attributes": {
        "active": {
            "type": "boolean",
            "description": "If enabled, it means that this ACL or QOS entry is active",
            "filterable": true,
            "orderable": true,
            "exposed": true,
            "uniqueScope": "no"
        },
        "associatedLiveEntityID": {
            "type": "string",
            "format": "free",
            "description": "ID of the associated live entity",
            "filterable": true,
            "exposed": true,
            "uniqueScope": "no"
        },
        "defaultAllowIP": {
            "type": "boolean",
            "description": "If enabled a default ACL of Allow All is added as the last entry in the list of ACL entries",
            "filterable": true,
            "orderable": true,
            "exposed": true,
            "uniqueScope": "no"
        },
        "defaultAllowNonIP": {
            "type": "boolean",
            "description": "If enabled, non ip traffic will be dropped",
            "filterable": true,
            "orderable": true,
            "exposed": true,
            "uniqueScope": "no"
        },
        "description": {
            "type": "string",
            "format": "free",
            "description": "A description of the entity",
            "filterable": true,
            "min_length": 0,
            "max_length": 255,
            "exposed": true,
            "uniqueScope": "no"
        },
        "entries": {
            "type": "list",
            "subtype": "object",
            "description": "List of Egress Domain ACL entries associated with this ACL",
            "exposed": true,
            "uniqueScope": "no"
        },
        "name": {
            "type": "string",
            "format": "free",
            "description": "The name of the entity",
            "filterable": true,
            "orderable": true,
            "min_length": 1,
            "max_length": 255,
            "exposed": true,
            "uniqueScope": "no"
        },
        "policyState": {
            "type": "enum",
            "allowed_choices": [ "DRAFT", "LIVE" ],
            "description": "State of the policy",
            "filterable": true,
            "orderable": true,
            "exposed": true,
            "uniqueScope": "no"
        },
        "priority": {
            "type": "integer",
            "description": "The priority of the ACL entry that determines the order of entries",
            "filterable": true,
            "orderable": true,
            "min_value": 0,
            "default_value": 0,
            "exposed": true,
            "uniqueScope": "no"
        },
        "priorityType": {
            "type": "enum",
            "allowed_choices": [ "TOP", "BOTTOM", "NONE" ],
            "description": "",
            "filterable": true,
            "orderable": true,
            "exposed": true,
            "uniqueScope": "no"
        }
    },
    "children": {
        "egressdomainfloatingipaclentrytemplate": {
            "get": true,
            "create": true,
            "relationship": "child"
        }
    },
    "model": {
        "description": "Defines the template for an Domain Floating IP ACL",
        "entity_name": "DomainFIPAclTemplate",
        "extends": [ "@audited", "@base", "@metadata" ],
        "package": "policy",
        "resource_name": "egressdomainfloatingipacltemplates",
        "rest_name": "egressdomainfloatingipacltemplate",
        "create": true,
        "get": true,
        "update": true,
        "delete": true
    }
}