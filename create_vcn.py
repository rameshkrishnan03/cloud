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
    compartment_id="${{ github.event.client_payload.Compartment_id }}",
    display_name="${{ github.event.client_payload.DisplayName }}",
    cidr_block="${{ github.event.client_payload.CIDR_Block }}"
)

try:
    response = virtual_network_client.create_vcn(vcn_details)
    print("VCN created successfully!")
except oci.exceptions.ServiceError as e:
    print(f"Error creating VCN: {e}")
    exit(1)
