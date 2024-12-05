# search for folders and files with matching keyword (Port 5004)

import zmq
from pathlib import Path
import subprocess
import time 

def runFile(code, name):
    try:
        subprocess.run([f"{code}", f"{name}"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while calling {name}: {e}")

def checkLists(list_keyword):
    runFile('python3', 'searchLists.py')
    time.sleep(2)
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5005")

    socket.send_string(list_keyword)
    response = socket.recv_string() 

    return response
    
def checkFiles(keyword):
    runFile('python3', 'searchFiles.py')
    time.sleep(2)
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5006")

    socket.send_string(keyword)
    response = socket.recv_string() 

    return response

def searchKeyword():
    context = zmq.Context()
    socket = context.socket(zmq.REP)  
    socket.bind("tcp://*:5004")  

    while True:
        keyword = socket.recv_string()  
        print(f"Received request: {keyword}")

        listInfo = checkLists(keyword) 
        itemInfo = checkFiles(keyword)
        
        response = f"Folders (account_name/folder_name):\n{listInfo}\n\nFiles (parent_folder/file_name):\n{itemInfo}"
        socket.send_string(response) 

if __name__ == '__main__':
    searchKeyword()