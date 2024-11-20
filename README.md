# Microservice A - Search Feature

## Requesting Data from the Microservice
### client.py
The client connects to the microservice running on localhost at port 5001, takes a keyword entered by the user, and sends the keyword as a string to the microservice, concurrently requesting a response from the microservice.

`socket.connect("tcp://localhost:5001")`

`keyword_name = input("Enter item keyword: ")`

`socket.send_string(keyword_name)`

### microservice1.py
Microservice is bound to localhost at port 5001. It receives the SOCKET request, originating from the client, and stores it into ‘keyword’, which will be called later in the microservice program. 

`socket.bind("tcp://*:5001")`

`keyword = socket.recv_string()` 

## Receiving Data from the Microservice

### microservice1.py
The microservice then connects to two other microservices using the ‘keyword’ it had received in the client’s request. It will then receive and store the responses from those two microservices as ‘response’, and send it in a SOCKET response, of type string, back to the client.  

`socket.send_string(response)`

### client.py
The client receives a string response from the microservice, prints the results, and then disconnects from the microservice running on localhost at port 5001.

`Response = socket.recv_string()`

`print(f"Results: \n{response}")`

`socket.disconnect("tcp://localhost:5001")`

### Additional Information

The `client.py` file is the only file that interacts with the user (the UI file). After recording the user inputted keyword, it connects to the socket of `microservices1.py`, utilizing ZeroMQ as a communication pipe. The socket of `microservices1.py` then sends REQs to `microservices2.py` 
and `microservices3.py`, both returning responses as `SEND_String()`. The `client.py` will receive the combined reponses from microservices 2 and 3, through microservice 1. However, throughout this process, the `client.py` socket will never interact with microservices 2 and 3 directly, and vice versa.

To use the Search Microservice, make a repository with microservice1.py, microservice2.py, and microservice3.py. The current folders and files in GitHub (All, listThree, listTwo and containing items) are empty and can be used as a test case. The client.py file is a UI, and can be altered, however, 
it is neccessary to maintain the following information in your UI: `socket.connect("tcp://localhost:5001")` and `socket.send_string(<some_user_input>)`. Changing the local port and the type of data sent to microservice1 without altering microservice1 
itself, can disrupt the program.

## UML Sequence Diagram

*Start : user submits keyword*

*End : search results are displayed* 

![CS361_asm6 drawio (1)](https://github.com/user-attachments/assets/b1c6712f-2110-4637-8359-0100683a4162)




