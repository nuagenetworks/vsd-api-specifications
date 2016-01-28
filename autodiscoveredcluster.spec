{
    "attributes": {
        "assocVCenterDataCenterId": {
            "description": "The ID of the vcenter to which this host is attached",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string"
        },
        "name": {
            "description": "Name of the shared resource",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string"
        }
    },
    "model": {
        "delete": true,
        "entity_name": "AutoDiscoverClusters",
        "get": true,
        "resource_name": "autodiscoveredclusters",
        "rest_name": "autodiscoveredcluster",
        "update": true
    }
}