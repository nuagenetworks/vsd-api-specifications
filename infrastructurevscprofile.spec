{
    "attributes": {
        "description": {
            "description": "A description of the Profile instance created.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string",
            "min_length": 0,
            "max_length": 255,
            "uniqueScope": "no"
        },
        "enterprise": {
            "description": "Name of the enterprise/organisation associated with this Profile instance.  This is a read only attribute",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        },
        "enterpriseID": {
            "description": "Enterprise/Organisation associated with this Profile instance.",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        },
        "firstController": {
            "description": "First VSC Controller :  IP Address of the first VSC system NSG instances associated to this profile will be reaching for.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string",
            "min_length": 0,
            "max_length": 255,
            "uniqueScope": "no"
        },
        "name": {
            "description": "Name of the Infrastructure Profile",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "required": true,
            "type": "string",
            "min_length": 1,
            "max_length": 255,
            "uniqueScope": "no"
        },
        "probeInterval": {
            "description": "Openflow echo timer in millisecond",
            "exposed": true,
            "filterable": false,
            "orderable": false,
            "type": "integer",
            "min_value": 1000,
            "max_value": 60000,
            "default_value": 5000,
            "uniqueScope": "no"
        },
        "secondController": {
            "description": "Second VSC Controller :  IP Address of the secondary VSC system NSG instances associated to this profile will be reaching for.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string",
            "min_length": 0,
            "max_length": 255,
            "uniqueScope": "no"
        }
    },
    "model": {
        "delete": true,
        "description": "Represents an Infrastructure VSC Profile",
        "entity_name": "InfrastructureVscProfile",
        "extends": [
            "@base",
            "@metadata"
        ],
        "get": true,
        "package": "infrastructure",
        "resource_name": "infrastructurevscprofiles",
        "rest_name": "infrastructurevscprofile",
        "update": true
    }
}