# list all files in a given folder (Port 5002)

import zmq
from pathlib import Path
import json

def listAllFiles(folder_name):
    with open('config/username.txt', 'r') as file:
        # Read the entire content of the file
            username = file.readline().strip()

    folder = Path(username) / folder_name
    if folder.exists() and folder.is_dir():
        file_list = [file.name for file in folder.iterdir() if file.is_file()]
        return file_list
    else:
        return 'The folder does not exist.'

def microservice_3():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5002") 

    while True:
        folder_name = socket.recv_string()
        file_list = listAllFiles(folder_name)
        socket.send_string(json.dumps(file_list))

if __name__ == '__main__':
    microservice_3()
