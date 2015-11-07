#!/usr/bin/python
import sys
import requests

url = 'http://localhost:8000/accounts/login/'

client = requests.Session()

#First we send a GET request to the server at the url /accounts/register in order to get the CSRF token cookie
client.get(url)

#Now we get the CSRF token.
csrf_token = client.cookies['csrftoken']

#Now we need to send the data for registration. The data needed is username, email, password1 and password2.
#We send it as a POST request with the data as POST parameters.
#Along with the data we must send back the csrf token.

r = client.post(url, data={
				'csrfmiddlewaretoken'	: csrf_token,
				'username'		: 'redeyez',
				'password'		: 'passwor',
			},
		headers=dict(Referer=url))
print r.text

