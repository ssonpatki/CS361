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

#### Search using keyword (`searchKeyword.py`)

Calls `searchLists.py` and `searchFiles.py`. Combines the response and sends it back to the client.

##### `searchLists.py` 
Searches for folders in repository with corresponding keyword

##### `searchFiles.py` 
Searches for files in repository with corresponding keyword

#### Retrieve all item names from a specific list (`retrieveList.py`)

#### Read contents of a specific item from a specific list (`readFile.py`)

#### Edit contents of a specific item from a specific list (`editFile.py`)

#### Create new blank item in a specific list (`readItem.py`)

#### Create new list (`createFolder.py`)

#### Delete specific item from a specific list (`deleteItem.py`)





