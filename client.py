import zmq
import textwrap
import time 

def choiceOne():
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5001")
    
    keyword_name = input("Enter item keyword: ")
    print(f'Searching for {keyword_name}.')

    socket.send_string(keyword_name)
    response = socket.recv_string() 
    print(f"Results: \n{response}")
    socket.disconnect("tcp://localhost:5001")

def main():
    context = zmq.Context()
    socket = context.socket(zmq.REQ)  

    print("Welcome to my microservice!")

    introText = ("This is a search microservice, which will allow users to search for lists and files with a keyword input.")
    wrapText = textwrap.fill(introText, width=90)

    print(wrapText)

    while True:
        print("\nSelect a service to access:")
        print("1. Search for list or item using keyword")
        print("2. Exit")
        
        print("Input your choice (1 or 2) below, then press the enter key when you've made your decision.")
        choice = input("User Choice: ")
        
        if choice == '1':
            choiceOne()
            time.sleep(1)
        elif choice == '2':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")
            continue 


if __name__ == '__main__':
    main()
