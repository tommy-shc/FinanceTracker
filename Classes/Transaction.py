from datetime import datetime

class Transaction:
    def __init__(self, amount, transaction_type, category = "", date=None, description=""):

        self.amount = amount
        self.category = category.lower()
        self.type = transaction_type  #income or expense

        if date:
            self.date = date
        else:
            self.data = datetime.now()

        self.description = description

    def to_dict(self):
        return {
            "amount": self.amount,
            "category": self.category,
            "type": self.type,
            "date": self.date.isoformat(),
            "description": self.description
        }
