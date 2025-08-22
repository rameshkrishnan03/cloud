import oci
import os
import sys

# 1. Build the config dictionary from Environment Variables
oci_config_dict = {
  "user": os.getenv('OCI_USER_OCID'),          # Get value for env var 'OCI_USER_OCID'
  "tenancy": os.getenv('OCI_TENANCY_OCID'),
  "region": os.getenv('OCI_REGION'),
  "fingerprint": os.getenv('OCI_FINGERPRINT'),
  "key_content": os.getenv('OCI_PRIVATE_KEY')   # Use KEY_CONTENT, not key_file
}

try:
    oci.config.validate_config(oci_config_dict)
except Exception as e:
    print(f"Error validating OCI config: {e}")
    exit(1)  

try:
    virtual_network_client = oci.core.VirtualNetworkClient(oci_config_dict)
except Exception as e:
    print(f"Error creating OCI client: {e}")
    exit(1)


compartment_id = os.getenv('OCI_COMPARTMENT_ID')
display_name = os.getenv('OCI_DISPLAY_NAME')
cidr_block = os.getenv('OCI_CIDR_BLOCK')

# 3. Create the VCN
vcn_details = oci.core.models.CreateVcnDetails(
    compartment_id=compartment_id,
    display_name=display_name,
    cidr_block=cidr_block
)

try:
    response = virtual_network_client.create_vcn(vcn_details)
    print("VCN created successfully!")
    vcn = response.data
    print(f"VCN OCID: {vcn.id}")
except oci.exceptions.ServiceError as e:
    print(f"Error creating VCN: {e}")
    exit(1)
