# server
Model and controller

Basically we have 2 kinds of requests to the server. They are called GET and POST.
GET requests are used to retrieve information from the server. For example after you login and you want to read the bio of yourself. You would send a GET request to the server.
POST requests are used to change things in the server usually. For example when you register an account, you are adding a new user to the server and so you have to use POST.
The GET and POST requests can have parameters.
When we register we need to provide 4 parameters: username, email, password1 and password2 (the user has to enter the password twice to be sure he doesn't make typos)

But for security reasons there is another parameter added called CSRF token.
This is how it works:
We first have to send a GET request to the server without any information. The server responds telling you that you can proceed and in this reponse he sends you a CSRF token (it is a string). You get the CSRF token that the server sent
and include it as a parameter in the POST request.

Example:

I send a GET request to http://www.mubsone.com/accounts/register

Server responds with CSRF token 'asdfkYsa7djasdkjS'

Now I send a POST request to http://www.mubsone.com/accounts/register with parameters: 

username=brajan, 

email=brajan@mail.com, 

password1=pass, 

password2=pass, 

csrfmiddlewaretoken=asdfkYsa7djasdkjS

The server checks if the csrf token is the same as the one that it sent before in the previous GET request. If it is, it says everything is ok and registers the user.

How to do POST http requests in java: http://stackoverflow.com/questions/3324717/sending-http-post-request-in-java

Just replace the parameters in the link above ('param-1' and 'param-2' etc) with parameters requested by the feature (example: 'username', 'email' and also add other parameters like 'password1', 'password2', 'csrfmiddlewaretoken')
