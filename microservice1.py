# search for item

import zmq
from pathlib import Path

def getItem(item_name):
    file_path = Path('All') / item_name

    if file_path.is_file():
        print(f"The file '{item_name}' exists.")
        with open(file_path, 'r') as file:
            content = file.read()
            return content
    else:
        respond = f"The file '{item_name}' does not exist." 
        return respond

def microservice_1():
    context = zmq.Context()
    socket = context.socket(zmq.REP)  
    socket.bind("tcp://*:5001")  

    while True:
        item_name = socket.recv_string() 
        print(f"Received request: {item_name}")
        itemInfo = getItem(item_name)
        socket.send_string(itemInfo)

if __name__ == '__main__':
    microservice_1()
