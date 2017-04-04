from flask import Flask,redirect
from flask import render_template
from flask import request
from raspberryPiInterface.flaskFirebase import flaskFirebase
from flask_socketio import SocketIO, send,emit
import pickle
import random
import copy

class myServer():
    def __init__(self, pickleLocation):
        self.contactPickle = pickleLocation
    def runServer(self):
        

        app = Flask(__name__)
        app.config['SECRET_KEY'] = 'mysecret'
        socketio = SocketIO(app)

        port = random.randint(1, 1000) + 5000


        '''!!!!!!#!!!!!!!!!!!!!!!!!#!!!!!!!!!!!!#!!!!
        /$$$$$$$$$$$$$____bad_code____$$$$$$$$$$$$$$$
        /!!!!!!#!!!!!!!!!!!!!!!!!#!!!!!!!!!!!!#!!!!!!
        /
        /   The below code is for updating the
        /   account object.  I have to attach
        /   a function to the firebase stream
        /   so when it changes it fire and
        /   sends the data to all the clients
        /
        /   This is what the callBackFunction
        /   is for.  It get pushed down to the
        /   base firebase.py object.  
        /
        /   `Order Matters`
        /   I need to first create myFlaskFirebase
        /   because updateUsersData uses myFlaskFirebase.
        /   So i have to first create myFlaskFirebase,
        /   and pase the callBackFunction with the init
        /   method.
        /
        !!!!!!#!!!!!!!!!!!!!!!!!#!!!!!!!!!!!!#!!!!'''
        myFlaskFirebase = flaskFirebase()

        def updateUsersData():
            print("updating all the info")
            accounts = myFlaskFirebase.getFlasksAccountInfo()

            pickle.dump( {"accounts": accounts,
                            "token": None},
                    open( self.contactPickle, "wb+" ) )
            
            #self.managedDict["token"] = myFlaskFirebase.myFirebase.allTokenData
            ''' reason for with app.test
            http://stackoverflow.com/questions/31647081/flask-python-and-socket-io-multithreading-app-is-giving-me-runtimeerror-work'''
            with app.test_request_context('/'):
                emit("allAccounts",{"data":accounts}, broadcast=True,namespace='/')

        def callBackFunction():
            updateUsersData()

        myFlaskFirebase.init(callBackFunction)

        '''!!!!!!#!!!!!!!!!!!!!!!!!#!!!!!!!!!!!!#!!!!
        /$$$$$$___end_of_bad_code____$$$$$$$$$$$$$$$
        !!!!!!#!!!!!!!!!!!!!!!!!#!!!!!!!!!!!!#!!!!'''


        '''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        / on `add_account` add account and the 
        / information will be updated when it get the
        / information from the stream.
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
        @socketio.on('add_account')
        def add_account(emailJson):
            print("add_account")
            error = myFlaskFirebase.addUser(account=emailJson["emailAddress"], password=emailJson["password"])


        '''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        / on `remove_account` remove account and
        / resend all the data.
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
        @socketio.on('remove_account')
        def remove_account(emailJson):
            print("remove_account")
            myFlaskFirebase.removeUser(emailJson["emailAddress"])
            updateUsersData()

        '''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        / on `connection` send all the users data
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
        @socketio.on('connect')
        def test_connect():
            print("conencted")
            updateUsersData()


        @app.route("/", methods=['GET', 'POST'])
        def index():
            updateUsersData()
            return render_template("./index.html")



        socketio.run(app,port=port,host="192.168.1.108")#,host="0.0.0.0",debug=True , ssl_context='adhoc'
        print("Running")
