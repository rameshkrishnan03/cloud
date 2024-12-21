resource "oci_objectstorage_bucket" "test_bucket" {
    compartment_id        = var.compartment_ocid
    name                  = var.bucket_name
    namespace             = var.bucket_namespace
    defined_tags          = var.project_tag.defined_tags
    freeform_tags         = var.project_tag.freeform_tags
    access_type           = var.bucket_access_type
    auto_tiering          = var.bucket_auto_tiering
    object_events_enabled = var.bucket_object_events_enabled
    versioning            = var.bucket_versioning
    storage_tier          = var.bucket_storage_tier    

}