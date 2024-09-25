from Classes.Transaction import Transaction
from Classes.Report import Report
from Classes.Budget import Budget
from Classes.Goal import Goal
import BudgetManager

class ReportManager:
    def __init__(self):

        self.reports = []
        #Initialize a report generator


    def generate_spending_report(self):
        #Generate a report of spending by category.
        
        report = Report(self.transaction_manager.get_all_transactions())
        return report.generate_spending_report()

    def generate_income_vs_expense_report(self):
        
        #Generate an income vs. expenses report.
        
        report = Report(self.transaction_manager.get_all_transactions())
        return report.generate_income_vs_expense()

    def generate_budget_report(self,budget_manager: BudgetManager):
        
        #Generate a report summarizing budget performance.
        
        if budget_manager is None:
            return "No budgets to report."

        budget_report = {}
        for budget in budget_manager.budgets:
            budget_report[budget.category] = {
                "Limit": budget.limit,
                "Current Spending": budget.current_spending,
                "Exceeded": budget.is_exceeded()
            }
        return budget_report

    def generate_goal_progress_report(self,goal_manager):
        
        #Generate a report summarizing goal progress.
        if goal_manager is None:
            return "No goals to report."

        goal_report = {}
        for goal in goal_manager.goals:
            goal_report[goal.goal_name] = {
                "Target": goal.target_amount,
                "Current Savings": goal.current_savings,
                "Progress (%)": goal.progress(),
                "Goal Reached": goal.is_goal_reached()
            }
        return goal_report
