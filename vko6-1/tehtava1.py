import requests
import os
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__

BLOB_CONTAINER = "blobstoragehenrik"
connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
def main():
    readjson()
    create_blob()
    upload_blobfile()
    #list_blobfiles()
    
def readjson():
           
    responsee = requests.get('https://2ri98gd9i4.execute-api.us-east-1.amazonaws.com/dev/academy-checkpoint2-json')
    data = responsee.json()
    with open('checkpoint.txt', 'w') as new_document:
        for i in data['items']:
            print(i['parameter'])
                
            new_document.write(i['parameter'])
            new_document.write('\n')
   
def create_blob():
        
    try:
        
        # Create the BlobServiceClient object which will be used to create a container client
        blob_service_client = BlobServiceClient.from_connection_string(connect_str)

        # Create a unique name for the container
        container_name = str(BLOB_CONTAINER)

        # Create the container
        blob_service_client.create_container(container_name)
        
    except Exception as ex:
        print('Exception:')
        print(ex)        

def upload_blobfile():
    
    blob = BlobClient.from_connection_string(conn_str=connect_str , container_name=BLOB_CONTAINER, blob_name="checkpoint.txt")

    with open("checkpoint.txt", "rb") as data:
        blob.upload_blob(data)   

def list_blobfiles():
    
    container = ContainerClient.from_connection_string(conn_str=connect_str, container_name=BLOB_CONTAINER)

    blob_list = container.list_blobs()

    for blob in blob_list:
        print(blob.name + '\n')


if __name__ == "__main__":
    main()