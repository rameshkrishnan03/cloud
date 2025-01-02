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

# Get variables passed as command-line arguments
if len(sys.argv) != 4:
    print("Usage: python create_vcn.py <Compartment_id> <DisplayName> <CIDR_Block>")
    exit(1)

# Create the VCN
vcn_details = oci.core.models.CreateVcnDetails(
    compartment_id=sys.argv[1],
    display_name=sys.argv[2],
    cidr_block=sys.argv[3]
)

try:
    response = virtual_network_client.create_vcn(vcn_details)
    print("VCN created successfully!")
except oci.exceptions.ServiceError as e:
    print(f"Error creating VCN: {e}")
    exit(1)
