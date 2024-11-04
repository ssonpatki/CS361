import zmq
from pathlib import Path
import json

def listAllFiles(folder_name):
        folder = Path(folder_name)
        if folder.exists() and folder.is_dir():
            file_list = [file.name for file in folder.iterdir() if file.is_file()]
            return file_list
        else:
            return 'The folder does not exist.'

def microservice_3():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5003") 

    while True:
        folder_name = socket.recv_string()
        file_list = listAllFiles(folder_name)
        socket.send_string(json.dumps(file_list))

if __name__ == '__main__':
    microservice_3()
