from FinanceTracker import FinanceTracker

def Main():

    account_list = []
    logged_in_status = False
    current_account = ""
    new_account = True
    choice = ""

    while(choice != "z"):

        choice = input("(a) Make New Account \n(b) Log into account \n(z) Exit program")
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


def logged_in_interface(personal_account):

    choice = ""

    while choice != "z":

        print("(a) Add a budget")
        print("(b) See all Budgets")
        print("(c) Add a transaction to a budget")
        print("(d) Add a savings goal")
        print("(e) Add an amount to savings")
        print("(f) See all saving goals")
        print("(g) Generate a budget report")
        print("(z) Exit to Menu")
        choice = input()

        if choice == "a":
            personal_account.add_budget(input("Enter the category name: "), input("Enter the spending limit as an decimal: "))
        elif choice == "b" :
            personal_account.print_all_budgets()
        elif choice == "c" :
            personal_account.add_transaction_to_budget(input("Enter transaction amount: "),input("Enter transaction type (income) or (expense): "),input("Enter transaction category: "))
        elif choice == "d" :
            personal_account.add_goal(input("Enter your savings goal name: "),input("Enter the target amount: "),input("Enter the due date: "))
        elif choice == "e" :
            personal_account.add_amount_to_savings(input("Enter the goal's name: "),input("Enter the amount: "))
        elif choice == "f" :
            personal_account.print_all_savings()
        elif choice == "g" :
            personal_account.generate_budget_report()
        elif choice == "e" :
            continue
Main()

    