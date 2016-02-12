{
    "attributes": {
        "active": {
            "description": "If enabled, it means that this ACL or QOS entry is active",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "boolean",
            "uniqueScope": "no"
        },
        "associatedLiveEntityID": {
            "description": "In the draft mode, the ACL entry refers to this LiveEntity. In non-drafted mode, this is null.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "description": {
            "description": "A description of the entity",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 255,
            "type": "string",
            "uniqueScope": "no"
        },
        "name": {
            "description": "The name of the entity",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 255,
            "min_length": 1,
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "policyState": {
            "allowed_choices": [
                "DRAFT",
                "LIVE"
            ],
            "description": "",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "enum",
            "uniqueScope": "no"
        },
        "priority": {
            "description": "The priority of the ACL entry that determines the order of entries",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "integer",
            "uniqueScope": "no"
        },
        "priorityType": {
            "allowed_choices": [
                "BOTTOM",
                "NONE",
                "TOP"
            ],
            "description": "",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "enum",
            "uniqueScope": "no"
        }
    },
    "children": {
        "ingressadvfwdentrytemplate": {
            "create": true,
            "get": true,
            "relationship": "child"
        },
        "job": {
            "create": true,
            "relationship": "child"
        }
    },
    "model": {
        "delete": true,
        "description": "Defines the template for an Ingress Advanced Forwarding.",
        "entity_name": "IngressAdvFwdTemplate",
        "extends": [
            "@audited",
            "@base",
            "@metadata"
        ],
        "get": true,
        "package": "policy/acl",
        "resource_name": "ingressadvfwdtemplates",
        "rest_name": "ingressadvfwdtemplate",
        "update": true
    }
}