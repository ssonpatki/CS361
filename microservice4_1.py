#search for folders and files with keyword

import zmq
from pathlib import Path

def checkLists(list_keyword):
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5005")

    socket.send_string(list_keyword)
    response = socket.recv_string() 

    return response
    
def checkFiles(keyword):
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5006")

    socket.send_string(keyword)
    response = socket.recv_string() 

    return response

def microservice4_1():
    context = zmq.Context()
    socket = context.socket(zmq.REP)  
    socket.bind("tcp://*:5004")  

    while True:
        keyword = socket.recv_string()  
        print(f"Received request: {keyword}")

        listInfo = checkLists(keyword) 
        itemInfo = checkFiles(keyword)
        
        response = f"Folders:\n{listInfo}\n\nFiles (parent_folder/file_name):\n{itemInfo}"
        socket.send_string(response) 

if __name__ == '__main__':
    microservice4_1()