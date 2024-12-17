variable "compartment_ocid"{}

variable "project_tag"{
    type = map
    default = {
        defined_tags = {
            
        }
        freeform_tags ={}
    }
}

variable "bucket_name"{}

variable "bucket_auto_tiering"{}

variable "bucket_namespace"{}

variable "bucket_access_type"{}

variable "bucket_object_events_enabled"{}

variable "bucket_versioning"{}

variable "bucket_storage_tier"{}