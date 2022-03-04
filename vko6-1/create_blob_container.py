import os


from azure.identity import AzureCliCredential
from azure.mgmt.storage import StorageManagementClient
from azure.mgmt.resource import ResourceManagementClient

SUBSCRIPTION_ID = os.environ.get("SUBSCRIPTION_ID", None)
GROUP_NAME = "henrikRG"
STORAGE_ACCOUNT = "henrikstorageaccount"
BLOB_CONTAINER = "blobstoragehenrik"

# Create client
# # For other authentication approaches, please see: https://pypi.org/project/azure-identity/
resource_client = ResourceManagementClient(
    credential=AzureCliCredential(),
    subscription_id=SUBSCRIPTION_ID
        )
storage_client = StorageManagementClient(
    credential=AzureCliCredential(),
    subscription_id=SUBSCRIPTION_ID
        )

resource_storage = list(storage_client.resource_storage.list())
        #print("List resource groups:\n{}".format(resource_groups))
    
for i in resource_storage:

            

    print("Name: {}\nLocation: {}\nTags: {}\n".format(i.name, i.location, i.tags))

        # - init depended resources -
    # Create resource group
resource_client.resource_groups.create_or_update(
    GROUP_NAME,
    {"location": "eastus"}
    )
    # Create storage account
storage_client.storage_accounts.begin_create(
        GROUP_NAME,
        STORAGE_ACCOUNT,
        {
          "sku": {
            "name": "Standard_GRS"
          },
          "kind": "StorageV2",
          "location": "eastus",
          "encryption": {
            "services": {
              "file": {
                "key_type": "Account",
                "enabled": True
              },
              "blob": {
                "key_type": "Account",
                "enabled": True
              }
            },
            "key_source": "Microsoft.Storage"
          },
          "tags": {
            "key1": "value1",
            "key2": "value2"
          }
        }
    ).result()
    # - end -



    
        # Create blob container
blob_container = storage_client.blob_containers.create(
    GROUP_NAME,
    STORAGE_ACCOUNT,
    BLOB_CONTAINER,
            {}
        )
print("Create blob container:\n{}".format(blob_container))
   