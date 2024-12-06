# delete file from specific list (Port 5011)

import zmq
from pathlib import Path
import os

def checkFolder(itemFolder, username):
    
    base_path = Path(username) 
 
    keyword_var = itemFolder.lower()

    match = [str(p) for p in base_path.iterdir() if p.is_dir() and p.name.lower() == keyword_var]

    if match:
        return 'yes'
    else:
        return 'no'
    
def remove(itemName, itemFolder, username):
    file_path = f"{username}/{itemFolder}/{itemName}"

    if os.path.exists(file_path):
        os.remove(file_path)
        return 'Item successfully deleted'
    else:
        return 'Item does not exist'

def deleteFile():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5011") 

    while True:

        with open('config/username.txt', 'r') as file:
        # Read the entire content of the file
            username = file.readline().strip()

        itemName, itemFolder = socket.recv_multipart()
        itemName = itemName.decode('utf-8').strip()
        itemFolder = itemFolder.decode('utf-8').strip()
        print(f"Received request: {itemName} in {itemFolder}")
        folderExist = checkFolder(itemFolder, username)
        if (folderExist == 'yes'):
            message = remove(itemName, itemFolder, username)
        else:
            message = 'Folder does not exist'

        socket.send_string(message)

if __name__ == '__main__':
    deleteFile()
