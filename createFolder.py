# make new folder 

import os
import zmq
from pathlib import Path

def checkFolder(itemFolder, username):
    
    base_path = Path(username) 
 
    keyword_var = itemFolder.lower()

    match = [str(p) for p in base_path.iterdir() if p.is_dir() and p.name.lower() == keyword_var]

    if match:
        return 'yes'
    else:
        return 'no'

    
def createNew(folderName, username):
    # Specify the path for the new subfolder
    subfolder_path = f"{username}/{folderName}"
    # Create the subfolder
    os.mkdir(subfolder_path)


def createFolder():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5014") 

    while True:

        with open('config/username.txt', 'r') as file:
        # Read the entire content of the file
            username = file.readline().strip()

        folderName = socket.recv_string()
        print(f"Received request: {folderName}")
        folderExist = checkFolder(folderName, username)
        if (folderExist == 'yes'):
            message = 'Folder already exists'
        else:
            createNew(folderName, username)
            message = 'Folder has been created.'

        socket.send_string(message)

if __name__ == '__main__':
    createFolder()
