import pyrebase
#import requests
import sys
import time
from raspberryPiInterface.myAuth import  config

class myFirebase:
    '''
    pupose 
        initilase firebase
        log in with my cred's
        intinize the datebase
        
        Attributes Variables
            allUserData - basicall all the data of the users that are log in
            
        
    '''
    def __init__(self,callBackFunction):
        self.firebase = pyrebase.initialize_app(config)
        self.auth = self.firebase.auth()
        self.db = self.firebase.database()
        self.Streams = {}
        self.callBackFunction = callBackFunction

        
        self.allUsersData = {}
        self.allTokenData = {}


    '''
    log a user into firebase
    
        OUTPUT
            userId and userToken 
            else 0,0
            
            
    '''
    def loginAccount(self,email,password):
        try:
            user = self.auth.sign_in_with_email_and_password(email,password)
            
            localId = self.auth.get_account_info(user['idToken'])['users'][0]['localId']
            return localId, user['idToken']
        
        #bad password, or bad log in.    
        #except requests.exceptions.HTTPError as e:
        #    print(e)
            
        except:
            e = sys.exc_info()
            print(e)
        return 0,0

    ''' 
    Gets called every time firebase gets updated
    
        OUTPUT
            Adds all values to allUsersData
            
            
    '''
    def streamHandler(self,message):
        print("got a update")
        #print("steam_id: " + str(message["stream_id"]))
        
        SID = message['stream_id']
        
        path = str(message["path"]).replace("/",  "")
        #if first object
        if(message["path"]  == "/"):
            print("initial object")
            self.allUsersData[SID]  = message["data"]
        #if data exists
        elif self.allUsersData[SID].get(path):
            if(message["data"] == None):
                print("deleting")
                del self.allUsersData[SID][path]
            else:
                print("updating")
                for attributes in message["data"]:
                    self.allUsersData[SID][path][attributes] = message["data"][attributes]
        else:
            print("is a new thing")
            time.sleep(2)
            self.allUsersData[SID][path] = message["data"]
        self.callBackFunction()
        
        
    '''
        just a wrapper to set up the stream function
        
        
    '''
    def setUpStream(self,userId,userToken, email):
        self.Streams[email] = self.db.child("users").child(userId).stream(self.streamHandler, token=userToken, stream_id=email)
    
    def streamHandlerToken(self,message):
        print(message)
        self.allTokenData[message["stream_id"]] = {
            "token" : message["data"]["token"]
        }
        
        

    def setUpTokenStream(self,userId,userToken, email):
        self.StreamToken = self.db.child("notification_token").child(userId).stream(self.streamHandlerToken, token=userToken, stream_id=email)

    def removeStream(self,email):
        del self.Streams[email]
        del self.allUsersData[email]
    '''
        this will loop through all the accounts and set up stream functions
        
        
    '''
    def getAllAccountInfo(self,allUsers):
        for user in allUsers: 
            #                                    "email", "password
            userId, userToken = self.loginAccount(user,allUsers[user])
            if(userId != 0):            #user is the email
                self.setUpStream(userId,userToken,user)
                self.setUpTokenStream(userId,userToken, user)
                
    def addUserToAccountInfo(self, email,password):
        userId, userToken = self.loginAccount(email,password)
        if(userId != 0):            
            self.setUpStream(userId,userToken,email)
            self.setUpTokenStream(userId, userToken, email)
    

        
        


    

    