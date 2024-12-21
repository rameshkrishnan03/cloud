module "object_storage_bucket" {
    source                      = "./buckett_module"
    compartment_ocid            = var.compartment_ocid
    bucket_name                 = var.bucket_name
    bucket_namespace            = var.bucket_namespace
    project_tag                 = var.project_tag
    bucket_access_type          = var.bucket_access_type
    bucket_auto_tiering         = var.bucket_auto_tiering
    bucket_storage_tier         = var.bucket_storage_tier
    bucket_versioning           = var.bucket_versioning
    bucket_object_events_enabled = var.bucket_object_events_enabled
    
    
}