# add item to All list

import zmq
from pathlib import Path

def checkExist(item_name):
    file_path = Path('All') / item_name
    if file_path.is_file():
        return 'yes'
    else:
        return 'no'
    
def createNew(item_name):
    folder_path = Path('All')

    folder_path.mkdir(parents=True, exist_ok=True)

    file_path = folder_path / item_name

    with open(file_path, 'w') as file:
        file.write(f"This is {item_name}.")

def microservice_2():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5002") 

    while True:
        itemName = socket.recv_string()
        print(f"Received request: {itemName}")
        exist = checkExist(itemName)
        if (exist == 'yes'):
            message = 'Item already exists'
        else:
            createNew(itemName)
            message = 'Item has been created.'

        socket.send_string(message)

if __name__ == '__main__':
    microservice_2()
