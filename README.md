# Program Details

## Microservices

### Create Account

`client.py` runs `accountDetails.js`, which is the UI, and runs `createAccount.js` in the background.

`accountDetails.js` sends HTTP request, with user's inputs, to `createAccount.js` which then adds a user document in the specified MongoDB database and initializes a new collection, named `<username`, in the database as well.

### Log into Account

`client.py` runs `login.js`, which is the UI, and runs `server.js` in the background.

`login.js` sends HTTP request, with user's inputs, to `server.js` which then verifies that the user's inputted credentials matches an existing account.

### Account Options
Each of these options using ZeroMQ as a communication pipe. 

The client connects to the specific microservice, then sends the inputs through a specified SOCKET as a string to be recieved by the microservice's SOCKET, concurrently requesting a response from the microservice.

`socket.connect("tcp://localhost:500x")`

`socket.send_string(<someInput>)`

#### 1. Search an item using its name (`microservice1.py`)


#### 2. Create a new item in your 'All' list (`microservice2.py`)


#### 3. Retrieve all item names from a specific list (`microservice3.py`)


#### 4. Search using keyword (`searchKeyword.py`)

Calls `searchLists.py` and `searchFiles.py`. Combines the response and sends it back to the client.

##### `searchLists.py` 
Searches for folders in repository with corresponding keyword

##### `searchFiles.py` 
Searches for files in repository with corresponding keyword