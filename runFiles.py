# run all microservice files

import zmq
from pathlib import Path
import subprocess
import time 

"""
def accountServer():
    try:
        # Start server.js as a background process
        process = subprocess.Popen(
            ["node", "createAccount.js"],
            stdout=subprocess.DEVNULL,  # Suppress server logs
            stderr=subprocess.DEVNULL,  # Suppress server errors
            stdin=subprocess.DEVNULL,  # Prevent input interference
            start_new_session=True  # Detach the process
        )
        return process  # Return the process handle for potential later use
    except Exception as e:
        print(f"Failed to start createAccount.js: {e}")
        return None

def createAccount():
    try:
        subprocess.run(["node", "accountDetails.js"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while calling accountDetails.js: {e}")

def loginServer():
    try:
        # Start server.js as a background process
        process = subprocess.Popen(
            ["node", "server.js"],
            stdout=subprocess.DEVNULL,  # Suppress server logs
            stderr=subprocess.DEVNULL,  # Suppress server errors
            stdin=subprocess.DEVNULL,  # Prevent input interference
            start_new_session=True  # Detach the process
        )
        return process  # Return the process handle for potential later use
    except Exception as e:
        print(f"Failed to start server.js: {e}")
        return None
    
def login():
    try:
        subprocess.run(["node", "login.js"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while calling login.js: {e}")

"""
    
# Search an item using its exact name
def runMicroOne():
    try:
        subprocess.run(["python3", "microservice1.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while calling microservice1.py: {e}")


# Retrieve all item names from a specific list
def runMicroThree():
    try:
        subprocess.run(["python3", "microservice3.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while calling microservice3.py: {e}")

# Search using keyword
def runKeywordSearch():
    try:
        subprocess.run(["python3", "searchKeyword.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while calling searchKeyword.py: {e}")

# Edit file in specific folder
def runEditFile():
    try:
        subprocess.run(["python3", "editFile.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while calling editFile.py: {e}")
        
# Create new blank item in specific folder
def runBlankItem():
    try:
        subprocess.run(["python3", "createFile.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while calling createFile.py: {e}")
        
# Create new folder
def runNewFolder():
    try:
        subprocess.run(["python3", "createFolder.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while calling createFolder.py: {e}")
        
# Delete item in specific folder
def runDelete():
    try:
        subprocess.run(["python3", "deleteFile.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while calling deleteFile.py: {e}")
        

def runFiles():
    """
    accountServer()
    time.sleep(1)
    createAccount()
    time.sleep(1)
    loginServer()
    time.sleep(1)
    login()
    time.sleep(1)
    """

    runMicroOne()
    runMicroThree()
    runKeywordSearch()
    runEditFile()
    runBlankItem()
    runNewFolder()
    runDelete()
    

if __name__ == '__main__':
    runFiles()
