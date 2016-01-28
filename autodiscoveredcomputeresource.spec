{
    "attributes": {
        "assocVCenterDataCenterId": {
            "description": "The ID of the vcenter datacenter to which this host is attached",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string"
        }
    },
    "model": {
        "delete": true,
        "entity_name": "AutoDiscoverHypervisorFromDatacenter",
        "get": true,
        "resource_name": "autodiscoveredcomputeresources",
        "rest_name": "autodiscoveredcomputeresource",
        "update": true
    }
}