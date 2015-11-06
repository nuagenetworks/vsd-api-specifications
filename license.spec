{
    "attributes": {
        "allowedCPEsCount": {
            "description": "Maximum number of CPEs enabled with this license. A value of -1 indicates an unlimited number of CPEs", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "float", 
            "uniqueScope": "no"
        }, 
        "allowedNICsCount": {
            "description": "Maximum number of NICs allowed. A value of -1 indicates unlimited number of NICs", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "float", 
            "uniqueScope": "no"
        }, 
        "allowedVMsCount": {
            "description": "Maximum number of VMs enabled with this license. A value of -1 indicates an unlimited number of VMs", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "float", 
            "uniqueScope": "no"
        }, 
        "allowedVRSGsCount": {
            "description": "Maximum number of VRSGs enabled with this license. A value of -1 indicates an unlimited number of VRSGs", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "float", 
            "uniqueScope": "no"
        }, 
        "allowedVRSsCount": {
            "description": "Maximum number of VRSs enabled with this license. A value of -1 indicates an unlimited number of VRSs", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "float", 
            "uniqueScope": "no"
        }, 
        "city": {
            "description": "City of the owner associated with the license file", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "company": {
            "description": "Company of the owner associated with the license file", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "country": {
            "description": "Country of the owner associated with the license file", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "customerKey": {
            "description": "Customer key associated with the licese", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "email": {
            "description": "Email of the owner associated with the license file", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "expirationDate": {
            "description": "Expiration date of this license", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "time", 
            "uniqueScope": "no"
        }, 
        "isClusterLicense": {
            "description": "Indicates if the license is associated with standlone or cluster setup of VSD", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "boolean", 
            "uniqueScope": "no"
        }, 
        "license": {
            "description": "Base 64 value of the license", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "required": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "licenseID": {
            "description": "Unique identifier of the license file", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "integer", 
            "uniqueScope": "no"
        }, 
        "licenseType": {
            "description": "", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "enum", 
            "uniqueScope": "no"
        }, 
        "majorRelease": {
            "description": "Major software release associated with this license", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "integer", 
            "uniqueScope": "no"
        }, 
        "minorRelease": {
            "description": "Minor software release for which this license has been issued", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "integer", 
            "uniqueScope": "no"
        }, 
        "phone": {
            "description": "Phone number of the owner associated with the license file", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "productVersion": {
            "description": "Version of the product that this license applies to", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "provider": {
            "description": "Provider of the license file", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "state": {
            "description": "State of the owner associated with the license file", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "street": {
            "description": "Address of the owner associated with the license file", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "userName": {
            "description": "The name of the user associated with the license", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "zip": {
            "description": "Zipcode of the owner associated with the license file", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }
    }, 
    "children": {
        "eventlog": {
            "get": true, 
            "relationship": "child"
        }
    }, 
    "model": {
        "delete": true, 
        "description": "Enables retrieval/modification and creation of license files. Most of the attributes are retrieved from the encrypted license. The create API simply provides the encrypted license that is in base64 format", 
        "entity_name": "License", 
        "extends": [
            "@base", 
            "@metadata"
        ], 
        "get": true, 
        "package": "licensemgmt", 
        "resource_name": "licenses", 
        "rest_name": "license"
    }
}