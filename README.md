Chatting App
This is built using Python,Javascript,HTML,Flask,Flask-Socketio
Flask-SocketIO gives Flask applications access to low latency bi-directional communications between the clients and the server.

Receiving Messages
When using SocketIO, messages are received by both parties as events. On the client side Javascript callbacks are used. With Flask-SocketIO the server needs to register handlers for these events, similarly to how routes are handled by view functions.

Sending Messages
SocketIO event handlers defined as shown in the previous section can send reply messages to the connected client using the send() and emit() functions.


Broadcasting
Another very useful feature of SocketIO is the broadcasting of messages. Flask-SocketIO supports this feature with the broadcast=True optional argument to send() and emit():

When a message is sent with the broadcast option enabled, all clients connected to the namespace receive it, including the sender. When namespaces are not used, the clients connected to the global namespace receive the message. Note that callbacks are not invoked for broadcast messages.

A common need of applications is to validate the identity of their users. The traditional mechanisms based on web forms and HTTP requests cannot be used in a SocketIO connection, since there is no place to send HTTP requests and responses. If necessary, an application can implement a customized login form that sends credentials to the server as a SocketIO message when the submit button is pressed by the user.

We use the heroku server to deploy our chatting app.Later it can be used on various devices such as phones and laptops and people can connect through chatting by the help of this app.