from flask import Flask,redirect
from flask import render_template
from flask import request
from flaskFirebase import flaskFirebase
from flask_socketio import SocketIO, send,emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app)








myFlaskFirebase = flaskFirebase()

port = 5028

def updateUsersData():
    accounts = myFlaskFirebase.getFlasksAccountInfo()
    with app.test_request_context('/'):
        emit("allAccounts",{"data":accounts}, broadcast=True,namespace='/')

def coolFunction():
    updateUsersData()

myFlaskFirebase.init(coolFunction)




@socketio.on('add_account')
def add_account(emailJson):
    print(emailJson)
    error = myFlaskFirebase.addUser(account=emailJson["emailAddress"], password=emailJson["password"])


@socketio.on('remove_account')
def remove_account(emailJson):
    myFlaskFirebase.removeUser(emailJson["emailAddress"])
    updateUsersData()

@socketio.on('connect')
def test_connect():
    updateUsersData()
    print("connected\n")


@app.route("/", methods=['GET', 'POST'])
def index():
    updateUsersData()
    return render_template("./index.html",port=port)



if __name__ == "__main__":
    socketio.run(app,port=port,debug=True)
    print("Running")
    
