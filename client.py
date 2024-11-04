import zmq
import textwrap
import time 

def choiceOne():
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5001")
    
    item_name = None

    check = 'no'
    while (check == 'no'):
        item_name = input("Enter item name exactly: ")
        print("Is this the right name: ", item_name)
        check = input("Input yes or no: ")

    socket.send_string(item_name)
    response = socket.recv_string() 
    print("Response from Microservice 1:", response)
    socket.disconnect("tcp://localhost:5001")


def choiceTwo():
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5002")
    item_name = None

    check = 'no'
    while (check == 'no'):
        print("Remember to use camelCase when entering item names.")
        item_name = input("Enter item name: ")
        print("Is this the right name: ", item_name)
        check = input("Input yes or no: ")
    socket.send_string(item_name)

    response = socket.recv_string() 
    print(response)
    socket.disconnect("tcp://localhost:5002")


def choiceThree():
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5003")
    list_name = None

    check = 'no'
    while (check == 'no'):
        list_name = input("Enter list name: ")
        print("Is this the right name: ", list_name)
        check = input("Input yes or no: ")
    
    socket.send_string(list_name)
    response = socket.recv_string() 
    print(f"Items in {list_name} list are {response}")
    socket.disconnect("tcp://localhost:5003")


def choiceFour():
    print("This is the user help page")


def main():
    context = zmq.Context()
    socket = context.socket(zmq.REQ)  

    print("Welcome to My Bucket List!")

    introText = ("Everywhere you ever wanted to go and anything you ever wanted to do now in a list at your fingertips - waiting for a rainy day.")
    wrapText = textwrap.fill(introText, width=90)

    print(wrapText)

    while True:
        print("\nSelect a microservice to access:")
        print("1. Search an item using its name")
        print("2. Create a new item in your 'All' list")
        print("3. Retrieve all item names from a specific list")
        print("4. Help")
        print("5. Exit")
        
        print("Input your choice (1-4) below, then press the enter key when you've made your decision.")
        choice = input("User Choice: ")
        
        if choice == '1':
            choiceOne()
            time.sleep(1)
        elif choice == '2':
            choiceTwo()
            time.sleep(1)
        elif choice == '3':
            choiceThree()
            time.sleep(1)
        elif choice == '4':
            choiceFour()
            time.sleep(1)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")
            continue 


if __name__ == '__main__':
    main()
