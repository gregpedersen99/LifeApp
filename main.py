#Imports for all files


import homeCode as hc
import tkinter as tk
from datetime import date
import function as fc
#from tkinter import PhotoImage

#from datetime import datetime 

parent = tk.Tk()
parent.geometry("300x200")
parent.title("To Do List")
myDate = date.today()
todaysDate = tk.Label(parent, text = fc.convert_date(myDate), font = "50")
todaysDate.pack()

goals = [hc.Goal("Exercise"), hc.Goal("1 Hour of Reading"), hc.Goal("Journal"), hc.Goal("2 Hours of Personal Work"), hc.Goal("10 Minutes of Stretching")]


for goal in goals:
    hc.CheckButton(parent, goal)


button = tk.Button(parent, text="Save", command=lambda: fc.get_outputs(goals))
button.pack()

parent.mainloop()



