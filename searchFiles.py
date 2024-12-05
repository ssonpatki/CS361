#search for files with matching keyword (Port 5006)

import zmq
from pathlib import Path

def checkFiles(keyword):
    with open('config/username.txt', 'r') as file:
        # Read the entire content of the file
            username = file.readline().strip()

    base_path = Path(f'{username}')  

    keyword_var = keyword.lower()

    matching_files = [str(p) for p in base_path.rglob('*') if p.is_file() and keyword_var in p.name.lower()]

    if matching_files:
        print(f"Files matching '{keyword}': {matching_files}")
        return '\n'.join(matching_files)
    else:
        respond = f"No files found containing '{keyword}'."
        print(respond)
        return respond

def searchFiles():
    context = zmq.Context()
    socket = context.socket(zmq.REP)  
    socket.bind("tcp://*:5006")  

    while True:
        keyword = socket.recv_string()  
        print(f"Received request: {keyword}")
        listInfo = checkFiles(keyword) 
        socket.send_string(listInfo) 

if __name__ == '__main__':
    searchFiles()
