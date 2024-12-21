variable region{
    type = string
    default = "ap-mumbai-1"
    description = "enter the region"
}
variable compartment_ocid{
    type = string
    default = "ocid1.compartment.oc1..aaaaaaaa7nhpsworbxrgut7cwvsjzpp6cba33sq6jnxwkotzo4toc3juqwqa"
    description = "enter the compartment ocid"
}
variable tenancy_ocid{
    type = string
    default = "ocid1.tenancy.oc1..aaaaaaaavc76ja77ynos2lfgdfwbbten7l25irg2wpm4asuyighwsbsdyj6a"
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
    default = "bmzqkkm7b0th"
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
