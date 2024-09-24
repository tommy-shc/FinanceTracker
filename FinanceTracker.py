class FinanceTracker:
    
    def __init__(self, userid, password):
        
        self.userid = userid
        self.password = password


    def login(self, username, password):

        try:

            if ((self.userid == username) and (self.password == password)):

                return 1
            
            else:

                return 0

        except:

            return -1
        
    def get_userid(self):

        return self.userid

