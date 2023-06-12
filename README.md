# Flask API for Number Summation, String Concatenation and User Authentication

This repository contains a simple Flask API that provides two endpoints: one for calculating the sum of a list of numbers and another for concatenating two strings. The API also includes error handling for invalid input.

## Installation

```shell
# Install the required dependencies
pip install flask
```
## Usage

```shell
# Start the Flask application
python list_processing.py [first endpoint]
python user_authentication.py [second endpoint]

# Send HTTP POST requests to the following endpoints:
/sum: Accepts a JSON object with a list of numbers and returns the sum of the numbers.
/concatenate: Accepts a JSON object with two strings and returns their concatenation.
    
/register: Accepts a JSON object with fields "username" and "password" to register a new user.
/login: Accepts a JSON object with fields "username" and "password" to log in as an existing user.

# Sum Endpoint
curl -X POST -H "Content-Type: application/json" -d '{"numbers":[1,2,3,4,5]}' http://localhost:5000/sum

# Concatenate Endpoint
curl -X POST -H "Content-Type: application/json" -d '{"string1":"Hello","string2":"World"}' http://localhost:5000/concatenate

# Register Endpoint
curl -X POST -H "Content-Type: application/json" -d '{"username":"john", "password":"secret"}' http://localhost:5000/register

# Login Endpoint
curl -X POST -H "Content-Type: application/json" -d '{"username":"john", "password":"secret"}' http://localhost:5000/login
