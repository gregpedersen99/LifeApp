#Imports for all files


import homeCode as hc
import tkinter as tk
#from tkinter import PhotoImage

#from datetime import datetime 

parent = tk.Tk()
parent.geometry("300x200")
parent.title("To Do List")
todaysDate = tk.Label(parent, text = "September 5, 2024", font = "50")
todaysDate.pack()

goals = [hc.Goal("Exercise"), hc.Goal("Read a Book")]


for goal in goals:
    hc.CheckButton(parent, goal)

parent.mainloop()

