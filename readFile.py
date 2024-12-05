# search for item

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
    
def checkFile(itemName, itemFolder, username):
    
    file_path = Path(username) / itemFolder / itemName
    if file_path.is_file():
        return 'yes'
    else:
        return 'no'
    

def readFiles():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5001") 

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
            exist = checkFile(itemName, itemFolder, username)

            if (exist == 'yes'):
                #open the file
                file_path = Path(username) / itemFolder / itemName
                with open(file_path, 'r') as file:
                    message = file.read()
            else:
                message = 'Item does not exist.'
                
        else:
            message = 'Folder does not exist'

        socket.send_string(message)

if __name__ == '__main__':
    readFiles()