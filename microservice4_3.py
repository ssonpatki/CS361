#search files

import zmq
from pathlib import Path

def checkFiles(keyword):
    base_path = Path('.')  

    keyword_var = keyword.lower()

    matching_files = [str(p) for p in base_path.rglob('*') if p.is_file() and keyword_var in p.name.lower()]

    if matching_files:
        print(f"Files matching '{keyword}': {matching_files}")
        return '\n'.join(matching_files)
    else:
        respond = f"No files found containing '{keyword}'."
        print(respond)
        return respond

def microservice4_3():
    context = zmq.Context()
    socket = context.socket(zmq.REP)  
    socket.bind("tcp://*:5006")  

    while True:
        keyword = socket.recv_string()  
        print(f"Received request: {keyword}")
        listInfo = checkFiles(keyword) 
        socket.send_string(listInfo) 

if __name__ == '__main__':
    microservice4_3()
