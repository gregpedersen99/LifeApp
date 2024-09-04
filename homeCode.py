#This is going to include all of teh code necessary to crate a home screen here. Design wise, this will feature a calandar of events that I can maek changes to, a day countdown section and a daily tasks/events section 
#Structurally, I think the actual running of the window will be done in main, with all functions and objects created in sub folders that are then called into main. 
#it actually makes a lot of sense for us to break some of this down into objects. For example, a day can be an object of its own, and being able to reference a day as an object instead of building a day out of a bunch of functions might actually make the most sense 

#I think it makes sense for the first iteration of this to be a to do list. I add in items to my to do list, they 
#they are shown as items that can be accomplished every day, I can check them off, and I can view my progress over time 

#I will need to set up a very simple database that tracks my checkboxes for each of the to-dos as well. 




import tkinter as tk
#from tkinter import PhotoImage

from datetime import datetime 

#parent = tk.Tk()
#parent.title("The Life App")
#parent.mainloop()





dailyList = ["Read for 1 Hour", "Exercise", "Drink 1 gallon of water", "Do 2 Hours of independent work",
                 "10 minutes financial planning", "Stretch", "Eat a fruit and vegetable", "Journal", "Talk to someone",
                 "Clean for 30 minutes"]

def getDailyGoals():
    goals = []
    while True:
        input = input("Daily Goal: ")
        if input



print(len(dailyList))

#I want each Date object to have the following:
#Day month and year 
#A recurring to Do List of daily things, added by the user 
#A way to mark if each of these things were accomplished or not 
#Independent things that are happening on that date, added by the user 

class Date:
    def __init__(self, day, month, year,toDoList, items):
        self.day = day
        self.month = month 
        self.year = year 
        self.toDoList = toDoList
        self.items = items 








