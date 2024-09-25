from Classes.Goal import Goal

class GoalManager:
    def __init__(self):
        
        #Initialize a goal manager to handle multiple savings goals
        
        self.goals = []

    def add_goal(self, goal: Goal):
        
        #Add a goal to the list

        self.goals.append(goal)

    def update_goal_savings(self, goal_name, amount):
        
        #Update savings for a specific goal

        for goal in self.goals:
            if goal.goal_name == goal_name:
                goal.update_savings(amount)

    def get_goal_by_name(self, goal_name):
        
        #Retrieve a goal by its name.

        for goal in self.goals:
            if goal.goal_name == goal_name:
                return goal
        return None
    
    def print_all_goals(self):

        for goal in self.goals:
            print(goal)

    def check_goal_completion(self):

        #Check which goals have been completed.

        completed_goals = []
        for goal in self.goals:

            if goal.is_goal_reached():
                completed_goals.append(goal)
        
        return completed_goals