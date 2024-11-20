#search for list

import zmq
from pathlib import Path

def checkList(list_keyword):
    base_path = Path('.') 
 
    keyword_var = list_keyword.lower()

    match = [str(p) for p in base_path.iterdir() if p.is_dir() and keyword_var in p.name.lower()]

    if match:
        print(f"Folders matching '{list_keyword}': {match}")
        return '\n'.join(match)
    else:
        respond = f"No folders found containing '{list_keyword}'."
        print(respond)
        return respond

def microservice_2():
    context = zmq.Context()
    socket = context.socket(zmq.REP)  
    socket.bind("tcp://*:5002")  

    while True:
        list_keyword = socket.recv_string()  
        print(f"Received request: {list_keyword}")
        listInfo = checkList(list_keyword)  
        socket.send_string(listInfo) 

if __name__ == '__main__':
    microservice_2()
