#!/usr/bin/python
import sys
import requests

url = 'http://localhost:8000/accounts/logout/'

client = requests.Session()

#First we send a GET request to the server at the url /accounts/register in order to get the CSRF token cookie
r = client.get(url)

print r.text

