# Login Microservice

Please run `npm install` after cloning

## Requesting data

To request data from the microservice send an HTTP POST request to localhost:5008/login that contains a JSON body with username and password fields.

Example JSON:

{
    "username": "myUsername",
    "password": "myPassword"
}

## Receiving data

The API will respond to the request with a JSON web token if the provided credentials are valid, or a HTTP Error response if not.

Example:

{
    "message": "Authenticated successfully",
    "Authorization": "token would be here"
}

{
    "message": "No user account information found"
}

## UML

![UML](/img/uml.png)