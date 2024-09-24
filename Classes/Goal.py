from datetime import datetime

class Goal:
    def __init__(self, goal_name, target_amount, due_date):
        #initializes a savings Goal
        self.goal_name = goal_name
        self.target_amount = target_amount
        self.current_savings = 0.0
        self.due_date = due_date

    def update_savings(self, amount):
        #Increases current savings
        self.current_savings += amount
    
    def progress(self):
        #Returns progress towards meeting the savings goal
        return round((self.current_savings / self.target_amount) * 100, 2)
    
    def is_goal_reached(self):
        
        return self.current_savings >= self.target_amount
