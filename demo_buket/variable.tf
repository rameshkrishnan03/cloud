variable region{
    type = string
    default = "ap-mumbai-1"
    description = "enter the region"
}
variable compartment_ocid{
    type = string
    default = "ocid1.compartment.oc1..aaaaaaaapqrsts4pmvmisrzyprycvgl5jjapmaqsm2umcvuciaansete7s2q"
    description = "enter the compartment ocid"
}
variable tenancy_ocid{
    type = string
    default = "ocid1.tenancy.oc1..aaaaaaaal52gmqdp5vwuz2r744jjicjqdbzc7dp6ipbvzhv4z7c4kekgftvq"
    description = "enter the tenancy ocid"

}
variable project_tag{
    type = map
    default = {
        defined_tags = {

        }
        freeform_tags ={}
    }
}
variable bucket_name{
    type = string
    default = "demo_bucket"
    description = "enter the bucket name"
}

variable bucket_namespace{
    type = string
    default = "bmr5po5cv4zs"
    description = "enter the bucket namespace"
}
variable bucket_access_type{
    type = string
    default = "NoPublicAccess"

}
variable bucket_auto_tiering{
    type = string
    default = "Disabled"
}
variable bucket_object_events_enabled{
    type = bool
    default = "false"

}
variable bucket_storage_tier{
    type = string
    default = "Standard"
    description = "enter the bucket storage tier"

}
variable bucket_versioning{
    type = string
    default = "Disabled"
    description = "enter the bucket versioning"
}