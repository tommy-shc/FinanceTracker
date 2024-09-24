from FinanceTracker import FinanceTracker

def Main():

    account_list = []
    logged_in_status = False
    current_account = ""
    new_account = True

    while(input("continue Y/N") == "Y"):

        choice = input("(a) Make New Account \n(b) Log into account ")
        print("----------------------------")

        if (choice == "a"):

            username = input("Enter your username: ")
            
            for account in account_list:

                if username == account.get_userid():
                    new_account = True
                    print("This username already exisits, please try a different name.")

            if new_account == True:
                account_list.append(FinanceTracker(username,input("Enter your password: ")))
                new_account = False
            
        elif(choice == "b"):

            username = input("Enter your username: ")

            try:
                for account in account_list:
                    if(username == account.get_userid()):
                       
                        login_status = account.login(username,input("Enter your password: "))

                        if(login_status == 1):
                            current_account = account
                            logged_in_status = True
                            print("Log in Successful")
                            print("----------------------------")
                            

                        elif(login_status == 0):
                            print("Password is incorrect")
                            print("----------------------------")
                            

                        elif(login_status == -1):
                            print("Error: Login issue")
                            print("----------------------------")
                            
                    continue          

            except:
                print("Error: No accounts found")
                print("----------------------------")

            if(logged_in_status == True):

                logged_in_interface(current_account)

def logged_in_interface(account):

    print("(a) Display current status")
    print("(b) Add")

    
    print(account.get_userid())

Main()

    