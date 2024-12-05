import zmq
from pathlib import Path

def checkFolder(itemFolder, username):
    # Construct the full path
    folder_path = Path(username) / itemFolder

    # Check if the folder exists
    if folder_path.is_dir():
        return 'yes'
    else:
        return 'no'

def checkFile(itemName, itemFolder, username):
    file_path = Path(username) / itemFolder / itemName
    if file_path.is_file():
        return 'yes'
    else:
        return 'no'

def createNew(itemName, itemFolder, username):
    folder_path = Path(username) / itemFolder  # Correct folder path construction

    folder_path.mkdir(parents=True, exist_ok=True)  # Ensure folder exists

    file_path = folder_path / itemName  # Correct file path construction

    with open(file_path, 'w') as file:
        file.write(f"ItemName: {itemName} \nDescription: \nStatus: \nDeadline: \nPriority")

def createFile():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5013") 

    while True:
        # Read the username from the file
        with open('config/username.txt', 'r') as file:
            username = file.readline().strip()

        # Receive itemFolder and itemName from the socket
        itemName, itemFolder = socket.recv_multipart()
        itemName = itemName.decode('utf-8').strip()
        itemFolder = itemFolder.decode('utf-8').strip()
        print(f"Received request: {itemName} in {itemFolder}")

        # Check if folder exists
        folderExist = checkFolder(itemFolder, username)
        
        if folderExist == 'yes':
            # Check if the file already exists
            exist = checkFile(itemName, itemFolder, username)

            if exist == 'yes':
                message = 'Item already exists'
            else:
                # Create the new file
                createNew(itemName, itemFolder, username)
                message = 'Item has been created.'
        else:
            message = 'Folder does not exist'

        # Send the response back
        socket.send_string(message)

if __name__ == '__main__':
    createFile()
