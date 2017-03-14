import pickle
from firebase import myFirebase
import time

class flaskFirebase:  
    '''
    Purpose inits myFirebase object and 
    then it will wait 3 seconds to allow 
    all the information to arrive before going any further.
    
    
        Attributes
            passwordLocation - is the location of the pickle
    '''    
    def __init__(self):
        1+1
        
        
        
    
    def init(self,callBackFunction):
        self.myFirebase = myFirebase(callBackFunction)
        time.sleep(3)
        self.myFirebase.getAllAccountInfo(self.loadAccountInfo())
        self.passwordLocation = "./password.pickle"

    '''
    loads all the users accounts and passwords
    
        OUTPUT
            Returen the pickle data
        Else
            a empty object
    '''
    def loadAccountInfo(self):
        try:
            data = pickle.load( open( "./password.pickle", "rb+" ) )
        except:
            data = {}
        return data
    
    '''
    saves all users accounts and passwords
    '''
    def saveAccountInfo(self, data):
        pickle.dump(data, open("./password.pickle", "wb+"))
    
    def removeUser(self,email):
        #-remove from the pickle
        #remove Stream
        #remove allUsersData
        data = self.loadAccountInfo()
        del data[email]
        self.saveAccountInfo(data)
        self.myFirebase.removeStream(email)
    
    '''
    
        
    '''
    
    def addUser(self, account,password):
        ifPass, otherValue = self.myFirebase.loginAccount(account,password)
        error = "no error"
        if(ifPass != 0):
            data = self.loadAccountInfo()
            print("\n\nthis is data\n")
            print(data)
            print(account)
            if (account in data):
                error = "alread here \n"
            else:
                data[account] = password
                self.saveAccountInfo(data)
                                            #userId,userToken, email
                self.myFirebase.setUpStream(ifPass,otherValue,account)
                
        else:
            error = "error\n"

        print(error)
        print(ifPass)
        
        return error 
    
    '''
        Gets all the information for to display on the webpage
        
        returns:
            email - email address
            notificaitons - a list of notifications with
                            name - of the notificaiton
                            disabledNotification - true or false
                            
        
    '''
    def getFlasksAccountInfo(self):
        print("looping through everthing")
        returnArray = []
        
        for i in self.myFirebase.allUsersData:
            listNotification = []
            print(self.myFirebase.allUsersData)
            print("\n\n")
            #'''
            if self.myFirebase.allUsersData[i] is not None:
                for j in self.myFirebase.allUsersData[i]:
                    print(self.myFirebase.allUsersData[i][j])
                    listNotification.append({
                        "name":self.myFirebase.allUsersData[i][j]["name"],
                        "disabledNotification":self.myFirebase.allUsersData[i][j]["disabledNotification"]
                    })
            returnArray.append({
                "email": i,
                "notifications": listNotification
            })
            #'''    
        return returnArray

