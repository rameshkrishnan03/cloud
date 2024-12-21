import oci
import os

# Set the config file location (defaults to ~/.oci/config)
oci_config_file = os.getenv('OCI_CONFIG_FILE', '~/.oci/config')
oci_config_file = os.path.expanduser(oci_config_file)

try:
    config = oci.config.from_file(oci_config_file, "DEFAULT")
except Exception as e:
    print(f"Error loading OCI config file: {e}")
    exit(1)  

virtual_network_client = oci.core.VirtualNetworkClient(config) 

# Create the VCN
vcn_details = oci.core.models.CreateVcnDetails(
    compartment_id="ocid1.compartment.oc1..aaaaaaaa7nhpsworbxrgut7cwvsjzpp6cba33sq6jnxwkotzo4toc3juqwqa",
    display_name="SDK_VCN",
    cidr_block="10.0.0.0/16"
)

try:
    response = virtual_network_client.create_vcn(vcn_details)
    print("VCN created successfully!")
except oci.exceptions.ServiceError as e:
    print(f"Error creating VCN: {e}")
    exit(1)
