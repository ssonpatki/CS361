# main client CLI for program

import zmq
import textwrap
import time 
import subprocess
import sys 
import json

def loginServer():
    try:
        # Start server.js as a background process
        process = subprocess.Popen(
            ["node", "server.js"],
            stdout=subprocess.DEVNULL,  
            stderr=subprocess.DEVNULL, 
            stdin=subprocess.DEVNULL, 
            start_new_session=True 
        )
        return process 
    except Exception as e:
        print(f"Failed to start server.js: {e}")
        return None

# login.js is a part of the main program but has been split to another file
    # for usability and easier program readability
def loginClient():
    try:
        subprocess.run(["node", "login.js"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while calling login.js: {e}")

def accountServer():
    try:
        # Start server.js as a background process
        process = subprocess.Popen(
            ["node", "createAccount.js"],
            stdout=subprocess.DEVNULL,  
            stderr=subprocess.DEVNULL,  
            stdin=subprocess.DEVNULL,
            start_new_session=True 
        )
        return process  
    except Exception as e:
        print(f"Failed to start createAccount.js: {e}")
        return None
    

# accountDetails.js is a part of the main program but has been split to another file
    # for usability and easier program readability
def createAccount():
    try:
        subprocess.run(["node", "accountDetails.js"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while calling accountDetails.js: {e}")


def searchKeyword():
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5004")
    
    keyword_name = input("Enter keyword: ")
    print(f'Searching for keyword {keyword_name}.')

    socket.send_string(keyword_name)
    response = socket.recv_string() 
    print(f"Search Results: \n{response}")
    socket.disconnect("tcp://localhost:5004")


def retrieveList():
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5002")
    list_name = None

    check = 'no'
    while (check == 'no'):
        list_name = input("Enter list name: ")
        print("Is this the right name: ", list_name)
        check = input("Input yes or no: ")
    
    socket.send_string(list_name)
    response = socket.recv_string() 
    print(f"Items in {list_name} list are {response}")
    socket.disconnect("tcp://localhost:5002")


def readFile():
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5001")
    
    item_folder = None
    item_name = None

    check = 'no'
    while (check == 'no'):
        item_folder = input(f"\nEnter folder name that contains item exactly: ")
        item_name = input("Enter item name exactly: ")
        print("Is this the right name: ", item_folder, item_name)
        check = input("Input yes or no: ")

    socket.send_string(item_name, zmq.SNDMORE)
    socket.send_string(item_folder)

    response = socket.recv_string() 
    print("Response from Microservice 1:", response)
    socket.disconnect("tcp://localhost:5001")


def createList():
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5014")
    folder_name = None

    check = 'no'
    while (check == 'no'):
        print("Remember to use camelCase when entering item names.")
        folder_name = input("Enter name of folder to create: ")
        print("Is this the right folder name: ", folder_name)
        check = input("Input yes or no: ")
    socket.send_string(folder_name)

    response = socket.recv_string() 
    print(response)
    socket.disconnect("tcp://localhost:5014")

    
def createItem():
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5013")
    item_name = None
    item_folder = None

    check = 'no'
    while (check == 'no'):
        print("Remember to use camelCase when entering item names.")
        item_folder = input("Enter name of the folder that contains the item: ")
        item_name = input("Enter item name: ")
        print("Is this the right folder and name: ", item_folder, item_name)
        check = input("Input yes or no: ")
    socket.send_string(item_name, zmq.SNDMORE)
    socket.send_string(item_folder)

    response = socket.recv_string() 
    print(response)
    socket.disconnect("tcp://localhost:5013")


def editItem():
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5015")
    item_name = item_folder  = None
    description = status = deadline = priority = None

    check = 'no'
    while (check == 'no'):
        print("Remember to use camelCase when entering item names.")
        item_folder = input("Enter folder that contains item: ")
        item_name = input("Enter item name: ")
        print("Is this the right folder and name: ", item_folder, item_name)
        check = input("Input yes or no: ")
    
    description = input("Enter item description: ")
    status = input("Enter item status (future, in progress, completed): ")
    deadline = input("Enter item deadline (mm-dd-yyyy): ")
    priority = input("Enter item priority (low, medium, high): ")

    # Bundle data into a JSON object
    data = {
        "folder": item_folder,
        "name": item_name,
        "description": description,
        "status": status,
        "deadline": deadline,
        "priority": priority
    }

    # Convert to JSON string and send
    socket.send_string(json.dumps(data))

    response = socket.recv_string() 
    print(response)
    socket.disconnect("tcp://localhost:5015")


def deleteItem():
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5011")
    item_folder = None
    item_name = None

    check = 'no'
    while (check == 'no'):
        print("Remember to use camelCase when entering item names.")
        item_folder = input("Enter name of folder containing item: ")
        item_name = input("Enter name of item to delete: ")
        print("Is this the right folder and name: ", item_folder, item_name)
        check = input("Input yes or no: ")
    socket.send_string(item_name, zmq.SNDMORE)
    socket.send_string(item_folder)
    

    response = socket.recv_string() 
    print(response)
    socket.disconnect("tcp://localhost:5011")


def helpPage():
    try:
        subprocess.run(["python3", "help.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while calling help.py: {e}")


def userChoices():
    while True:
        print("\nSelect a service to access:")
        print("1. Search using keyword")
        print("2. Retrieve all item names from a list (exact list name required)")
        print("3. Read item contents (parent folder and exact item name required) ")
        print("4. Create new list")
        print("5. Create blank item in a list (exact list name required)")
        print("6. Edit item in a list (exact list name required)")
        print("7. Delete item in a list (exact list name required)")
        print("8. Help Page")
        print("9. Exit")
        

        print("\nInput your choice (1-9) below, then press the enter key when you've made your decision.")
        choice = input("User Choice: ")
        if choice == '1':
            searchKeyword()
            time.sleep(1)
        elif choice == '2':
            retrieveList()
            time.sleep(1)
        elif choice == '3':
            readFile()
            time.sleep(1)
        elif choice == '4':
            createList()
            time.sleep(1)
        elif choice == '5':
            createItem()
            time.sleep(1)
        elif choice == '6':
            editItem()
            time.sleep(1)
        elif choice == '7':
            deleteItem()
            time.sleep(1)
        elif choice == '8':
            helpPage()
            time.sleep(1)
        elif choice == '9':
            print("Exiting...")
            sys.exit()
        else:
            print("Invalid choice, please enter a number between 1 and 9.")
        
        time.sleep(1)


def main():
    context = zmq.Context()
    socket = context.socket(zmq.REQ)  

    print("Welcome to My Bucket List!")

    introText = ("Everywhere you ever wanted to go and anything you ever wanted to do now in a list at your fingertips - waiting for a rainy day.")
    wrapText = textwrap.fill(introText, width=90)

    print(wrapText)

    while True:
        allowLogin = 'no'

        while (allowLogin == 'no'):
            print("\nSelect a service to access:")
            print("1. Login")
            print("2. Create account")
            print("3. Exit")
            
            print("\nInput your choice (1-3) below, then press the enter key when you've made your decision.")
            choice = input("User Choice: ")
            
            if choice == '1':
                loginServer()
                time.sleep(1)
                loginClient()
                with open('config/username.txt', 'r') as f:
                    next(f) 
                    second_line = f.readline().strip()
                allowLogin = second_line
                time.sleep(1)
            elif choice == '2':
                accountServer()
                time.sleep(1)
                createAccount()
                time.sleep(2)
            elif choice == '3':
                print("Exiting...")
                return
            else:
                print("Invalid choice, please try again.")
                continue

        userChoices()


if __name__ == '__main__':
    main()
