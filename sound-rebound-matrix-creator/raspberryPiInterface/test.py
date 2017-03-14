import pyrebase
import time
from myAuth import  config
from myAuth import  myEmail 

#https://github.com/thisbejim/Pyrebase
#!!! going to have to make sure tokens get refreshed


firebase = pyrebase.initialize_app(config)


auth = firebase.auth()

user = auth.sign_in_with_email_and_password(myEmail['email'],myEmail['password'])

#print(user['idToken'])

db = firebase.database()

#db.child("test").push({"test": "data"}, user['idToken'])

localId = auth.get_account_info(user['idToken'])['users'][0]['localId']

'''
so this get updated 
'''

notificationInfo = {}

def steamHandler(message):
    global notificationInfo
    print("got a update")
    print("event: " + str(message["event"]))
    print("path: " + str(message["path"]))
    print("data: " + str(message["data"]))
    
    path = str(message["path"]).replace("/",  "")
    if(message["path"]  == "/"):
        print("initial object")
        notificationInfo = message["data"]
    elif notificationInfo.get(path):
        if(message["data"] == None):
            print("deleting")
            del notificationInfo[path]
        else:
            print("updating")
            for attributes in message["data"]:
                notificationInfo[path][attributes] = message["data"][attributes]
    else:
        print("is a new thing")
        notificationInfo[path] = message["data"]
               
    print("my object \n")
    print(notificationInfo)
    print("\n\n\n")
    
    

'''
this is a stream function so it will call this 
above function whenever it recieve new informations
'''
my_steam = db.child("users").child(localId).stream(steamHandler, token=user['idToken'])

print(my_steam)

if __name__ == '__main__':
    while True:
        time.sleep(5)