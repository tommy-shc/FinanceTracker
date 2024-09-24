from FinanceTracker import FinanceTracker

def Main():

    account_list = []
    current_account = ""

    while(input("continue Y/N") == "Y"):

        choice = input("(a) Make New Account \n(b) Log into account ")
        print("----------------------------")

        if (choice == "a"):

            account_list.append(FinanceTracker(input("Enter your username: "),input("Enter your password: ")))
            
        elif(choice == "b"):

            username = input("Enter your username: ")

            try:
                for account in account_list:
                    if(username == account.get_userid()):
                       
                        login_status = account.login(username,input("Enter your password: "))

                        if(login_status == 1):
                            current_account = account
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

            if(account != ""):

                print("This is your account")

Main()

    