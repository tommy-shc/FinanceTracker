from Classes.Transaction import Transaction

class Budget:

    def __init__(self, category: str, limit: float, period="monthly"):

        #Creates a budget for some category 
        #Limit represents the maximum money alloted 
        #Period represents the recurring time span
        self.category = category.lower()
        self.limit = limit
        self.period = period
        self.current_spending = 0.0
        self.transaction_list = []

    def add_transaction(self, transaction: Transaction):

        #Adds a transaction to the budget and updates the current total spending

        if transaction.category == self.category and transaction.type == "expense":
            self.current_spending +=  int(transaction.amount)
            self.transaction_list.append(transaction)
            print("Transaction successfully logged")
        else:
            print("Error logging transaction")
    
    def is_exceeded(self):

        return self.current_spending > self.limit
    
    def __repr__(self):

        return f"Budget for {self.category} ({self.period}): Limit = {self.limit}, Current Spending = {self.current_spending}"