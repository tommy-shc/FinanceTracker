from Transaction import Transaction
from datetime import timedelta, datetime

class RecurringTransaction(Transaction):

    def __init__(self, amount, transaction_type, frequency, category="",date=None, description=""):

        super().__init__(amount, category.lower(), transaction_type, date, description)
        self.frequency = frequency 
    
    def next_due_date(self):

        #Calculates the next date for this transaction
        if self.frequency == "monthly":
            return self.date + timedelta(days=30)
        elif self.frequency == "weekly":
            return self.date + timedelta(days=7)
        
        else:
            raise ValueError("Unsupported frequency: choose weekly or monthly")
        
    def update_due_date(self):

        self.date = datetime.now()

    def update_due_date(self, date):

        self.date = date