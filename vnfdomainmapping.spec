{
    "attributes": [
        {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": true,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "ID of the associated Domain",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "associatedDomainID",
            "orderable": false,
            "read_only": true,
            "required": false,
            "subtype": null,
            "transient": true,
            "type": "string",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Domain"
        },
        {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "Name of the associated Domain",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "associatedDomainName",
            "orderable": false,
            "read_only": true,
            "required": false,
            "subtype": null,
            "transient": true,
            "type": "string",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Domain Name"
        },
        {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "ID of the associated Enterprise",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "associatedEnterpriseID",
            "orderable": false,
            "read_only": true,
            "required": false,
            "subtype": null,
            "transient": true,
            "type": "string",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Enterprise"
        },
        {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "The associated IDP Profile ID",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 255,
            "max_value": null,
            "min_length": 0,
            "min_value": null,
            "name": "associatedIDPProfileID",
            "orderable": true,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "string",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "IDP Profile ID"
        },
        {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "Associated NS Gateway",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "associatedNSGatewayID",
            "orderable": false,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "string",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Network Services Gateway"
        },
        {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "Name of associated NSGateway",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "associatedNSGatewayName",
            "orderable": false,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": true,
            "type": "string",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "NS Gateway Name"
        },
        {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": true,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": "false",
            "deprecated": false,
            "description": "Indicates that this domain mapping was auto created by the system",
            "exposed": true,
            "filterable": false,
            "format": null,
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "autoCreated",
            "orderable": false,
            "read_only": true,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "boolean",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Auto Created"
        },
        {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "Name of the associated Enterprise",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 255,
            "max_value": null,
            "min_length": 0,
            "min_value": null,
            "name": "enterpriseName",
            "orderable": true,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "string",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Enterprise Name"
        },
        {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": true,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "The segmentation ID (1-4095).",
            "exposed": true,
            "filterable": false,
            "format": null,
            "max_length": null,
            "max_value": 4095,
            "min_length": null,
            "min_value": 1,
            "name": "segmentationID",
            "orderable": false,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "integer",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Segmentation ID"
        },
        {
            "allowed_chars": null,
            "allowed_choices": [
                "VLAN"
            ],
            "autogenerated": false,
            "channel": null,
            "creation_only": true,
            "default_order": false,
            "default_value": "VLAN",
            "deprecated": false,
            "description": "The type of segmentation that is used.",
            "exposed": true,
            "filterable": false,
            "format": null,
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "segmentationType",
            "orderable": false,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "enum",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Segmentation Type"
        },
        {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": true,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "Service ID of the associated Domain",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "serviceId",
            "orderable": false,
            "read_only": true,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "string",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Service ID"
        }
    ],
    "children": [],
    "model": {
        "allowed_job_commands": null,
        "create": null,
        "delete": true,
        "description": "This represents domain segment identifier which is unique for domain per NSGateway.",
        "entity_name": "VNFDomainMapping",
        "extends": [
            "@audited",
            "@base",
            "@metadata"
        ],
        "get": true,
        "package": "vnf",
        "resource_name": "vnfdomainmappings",
        "rest_name": "vnfdomainmapping",
        "root": null,
        "template": false,
        "update": false,
        "userlabel": "VNF Domain Mapping"
    }
}