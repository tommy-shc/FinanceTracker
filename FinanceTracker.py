from BudgetManager import BudgetManager
from Classes.Budget import Budget
from Classes.Transaction import Transaction
from Classes.Goal import Goal
from SavingsManager import GoalManager
from CurrencyConverter import CurrencyConverter
from ReportManager import ReportManager

class FinanceTracker:
    
    def __init__(self, userid, password):
        
        self.userid = userid
        self.password = password

        self.budget_manager = BudgetManager()
        self.currency_converter = CurrencyConverter()
        self.savings_manager = GoalManager()
        self.report_manager = ReportManager()

    def add_budget(self, category, limit):

        budget = Budget(category, limit, "Monthly")
        self.budget_manager.add_budget(budget)

    def print_all_budgets(self):
        self.budget_manager.print_all_budgets()

    def add_transaction_to_budget(self, amount, transaction_type, category=""):

        self.budget_manager.apply_transaction(Transaction( amount, transaction_type, category))
    
    def add_goal(self,goal_name, target_amount, due_date):

        self.savings_manager.add_goal(Goal(goal_name, target_amount, due_date))
    
    def add_amount_to_savings(self,name,amount):

        self.savings_manager.update_goal_savings(name,amount)

    def print_all_savings(self):
        
        self.savings_manager.print_all_goals()

    def generate_budget_report(self):

        print(self.report_manager.generate_budget_report(self.budget_manager))

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

