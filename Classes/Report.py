import csv
import pandas as pd
from Transaction import Transaction
from Budget import Budget

class Report:
    def __init__(self, transactions):
        
        #Initializes the report class with a list of transactions
        self.transactions = transactions
        self.spending_report = {}

    def generate_spending_report(self):
        
        #Generates a report of spending based on category
        for transaction in self.transactions:
            if transaction.type == "expense":
                self.spending_report[transaction.category] = self.spending_report.get(transaction.category, 0) + transaction.amount

    def generate_income_vs_expense(self):

        #Generates a report comparing income vs expenses
        #Returns a dictionary of total income, expenses, and net savings
        income = 0
        expenses = 0

        for t in self.transactions:
            if t.type == "income":
                income += t.amount
            elif t.type == "expense":
                expenses += t.amount

        return {"Total Income": income, "Total Expenses": expenses, "Net Savings": income - expenses}

    def export_to_csv(self, filename, report_data):
        
        #report_data is a dictionary
        #filename is the name of the csv to be exported

        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Category", "Amount"])
            for key, value in report_data.items():
                writer.writerow([key, value])

    def export_to_excel(self, filename, report_data):
        
        #param: report_data is a dictionary 
        #filename is the name of the excel to be exported

        df = pd.DataFrame(report_data)
        
        # Export the DataFrame to an Excel file
        df.to_excel(filename, index=False)  # index=False to avoid writing row numbers

        print(f"Report exported to {filename} successfully.")

