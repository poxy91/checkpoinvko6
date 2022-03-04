import argparse
import os
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__
import os.path
import time

BLOB_CONTAINER = "blobstoragehenrik"
connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')


parser = argparse.ArgumentParser()
parser.add_argument("luku1", help="syota luku1", type=int)
args = parser.parse_args()

print(args.luku1)


def main():
    download_blob()
    wait()
    list2=create_list()
    print_list(args.luku1,list2)
   
def download_blob():
    
    blob = BlobClient.from_connection_string(conn_str=connect_str, container_name=BLOB_CONTAINER, blob_name="checkpoint.txt")

    with open("checkpoint1.txt", "wb") as my_blob:
        blob_data = blob.download_blob()
        blob_data.readinto(my_blob)

def wait():
    while not os.path.exists("checkpoint1.txt"):
        time.sleep(3)

def create_list():
    with open("checkpoint1.txt") as data:
        list1 = []
        for row in data:
            row = row.replace("\n", "")
            list1.append(row)
    #lista sorttaa aakkosjärjestyksessä
        list2= sorted(list1)
        print(list2)
    return list2

def print_list(args,list2):
    
    x=0
    while args > x:
        print(list2[x])
        x+=1



if __name__ == "__main__":
    main()
