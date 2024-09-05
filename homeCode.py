#This is going to include all of teh code necessary to crate a home screen here. Design wise, this will feature a calandar of events that I can maek changes to, a day countdown section and a daily tasks/events section 
#Structurally, I think the actual running of the window will be done in main, with all functions and objects created in sub folders that are then called into main. 
#it actually makes a lot of sense for us to break some of this down into objects. For example, a day can be an object of its own, and being able to reference a day as an object instead of building a day out of a bunch of functions might actually make the most sense 

#I think it makes sense for the first iteration of this to be a to do list. I add in items to my to do list, they 
#they are shown as items that can be accomplished every day, I can check them off, and I can view my progress over time 

#I will need to set up a very simple database that tracks my checkboxes for each of the to-dos as well. 

import tkinter as tk



#I want each Date object to have the following:
#Day month and year 
#A recurring to Do List of daily things, added by the user 
#A way to mark if each of these things were accomplished or not 
#Independent things that are happening on that date, added by the user 


#Initializing my date class here 




class Date:
    def __init__(self, day, month, year,toDoList, items):
        self.day = day
        self.month = month 
        self.year = year 
        self.toDoList = toDoList
        self.items = items 


#Creating the goal class, first step here is creating an output of a fixed list of goals, todays date,
#And the ability ot check them off or not. Going to use tkinter here in a different file for tkinter code
#keeping this as classes. 

class Goal:
    def __init__(self, goal=None, isAchieved=False):
        if goal is None:
            self.goal = input("Goal: ")
        else:
            self.goal=goal
        self.isAchieved = isAchieved #Default will be that goal is not achieved on a given day 

    def set_goal(self):
        self.goal = input("Goal: ")
    
    def __str__(self):
        return f"{self.goal}"
    



class CheckButton:
    def __init__(self, window, goal):
        self.goal = goal #we do it like this because it need to be passed directly through upon initializing the class
        self.var = tk.BooleanVar(value = goal.isAchieved) #referencing a method from another since we are relying on class Goal to be the variable used on initialization 
        self.checkbutton = tk.Checkbutton(window, text = str(goal), variable = self.var, command = self.update_status) #Set text = str(goal) so we can just take the vaue of goal itself and not the value of isAchieved in the output next to the button 
        self.checkbutton.pack() #Double . here since its a class on a class 

    def update_status(self):
        self.goal.isAchieved = self.var.get()

    




