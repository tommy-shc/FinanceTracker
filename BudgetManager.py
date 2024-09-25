from Classes.Budget import Budget
from Classes.Transaction import Transaction

class BudgetManager:
    def __init__(self):

        #Initializes a budget manager to handle multiple budgets

        self.budgets = []
        self.exceded_budgets = []

    def add_budget(self, budget: Budget):

        for b in self.budgets:
            if b.category == budget.category:
                return 0

        self.budgets.append(budget)

    def apply_transaction(self, transaction: Transaction):
        
        #Adds a transaction to the matching budget category
        for budget in self.budgets:
            if budget.category == transaction.category:
                budget.add_transaction(transaction)

    def get_budget_by_category(self, category):
        
        #Returns the budget of the specified catgory
        for budget in self.budgets:
            if budget.category == category:
                return budget
        return None

    def check_all_budgets(self):
        #Check if any budgets have been exceeded

        for budget in self.budgets:

            if budget.is_exceeded():

                self.exceded_budgets.append(budget)

        return self.exceeded_budgets

    def print_all_budgets(self):

        for budget in self.budgets:

            print(budget)
