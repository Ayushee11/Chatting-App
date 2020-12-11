
from flask import Flask,jsonify,request
from flask_socketio import SocketIO


app = Flask(__name__)
app.config['SECRET_KEY'] = 'ayushee'
socketio = SocketIO(app)

users=[
{'id':2,'name':'Anne','age':20},
{'id':1,'name':'Cathy','age':21},
{'id':3,'name':'Bill','age':19}
]

@app.route('/')
def index():
	return app.send_static_file('index.html')

@socketio.on('msg')
def handle_msg(data):
	socketio.emit('push',data,broadcast=True,include_self=False)

@app.route("/users")
def getUsers():
	return jsonify(users)

@app.route("/users/<id>")
def getUser(id):
	result=list(filter(lambda u:str(u['id'])==id,users))
	return jsonify(result)

if __name__=="__main__":
	socketio.run(app)

