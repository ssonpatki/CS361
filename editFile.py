# edit file from specific folder (Port 5015)

import zmq
from pathlib import Path
import json



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
    

def editFile():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5015") 

    while True:
        with open('config/username.txt', 'r') as file:
            username = file.readline().strip()

        # Receive and parse the JSON message
        message = socket.recv_string().strip()
        data = json.loads(message)

        itemFolder = data['folder']
        itemName = data['name']
        description = data['description']
        status = data['status']
        deadline = data['deadline']
        priority = data['priority']

        print(f"Received request: {itemName} in {itemFolder}")

        folderExist = checkFolder(itemFolder, username)
        if folderExist == 'yes':
            exist = checkFile(itemName, itemFolder, username)

            if exist == 'yes':
                file_path = Path(username) / itemFolder / itemName

                with open(file_path, 'w') as text_file:
                    text_file.write(f'Item Name: {itemName}\n')
                    text_file.write(f'Description: {description}\n')
                    text_file.write(f'Status: {status}\n')
                    text_file.write(f'Deadline: {deadline}\n')
                    text_file.write(f'Priority: {priority}\n')

                message = 'Changes have been saved.'
            else:
                message = 'Item does not exist.'
        else:
            message = 'Folder does not exist'

        # Send response back to client
        socket.send_string(message)

if __name__ == '__main__':
    editFile()