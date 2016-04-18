{
    "attributes": [],
    "children": [
        {
            "bulk_create": false,
            "bulk_delete": false,
            "bulk_update": false,
            "create": true,
            "delete": false,
            "deprecated": null,
            "get": true,
            "relationship": "child",
            "rest_name": "nexthop",
            "update": false
        }
    ],
    "model": {
        "create": null,
        "delete": true,
        "description": "This is the mechanism to interconnect a source domain to a destination domain. Is a child object of the Link object. There can be max one via object per Link.",
        "entity_name": "Via",
        "extends": [
            "@audited",
            "@base",
            "@metadata"
        ],
        "get": true,
        "package": null,
        "resource_name": "vias",
        "rest_name": "via",
        "root": null,
        "update": true
    }
}