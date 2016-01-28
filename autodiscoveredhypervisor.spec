{
    "attributes": {
        "assocClusterId": {
            "description": "The ID of the cluster to which this host is attached",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string"
        }
    },
    "model": {
        "delete": true,
        "entity_name": "AutoDiscoverHypervisorFromCluster",
        "get": true,
        "resource_name": "autodiscoveredhypervisors",
        "rest_name": "autodiscoveredhypervisor",
        "update": true
    }
}