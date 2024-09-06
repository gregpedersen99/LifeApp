import sqlite3 
from homeCode import Goal
from datetime import date

conn = sqlite3.connect('goals.db') #Creating my database that will be used to storae goals 

c = conn.cursor() #setting up cursor value to begin writing sql commands 

#SQL command to generate my intial DB with initial goals, the goal is to have an edit button that allows me to 
#add some in eventually. Cannot use integer number 
#c.execute("""CREATE TABLE goals (
 #           date text, 
 #           Read for One Hour integer,
 #           Exercise integer,
#            Journal integer, 
 #           Stretch integer,
 #           Two Hour Personal Work integer
 #           )""")

conn.commit() #commits changes to the db 
conn.close() # close connections to db 

#unning twice breaks this because table already exists, so we're looking good here 

#Next here is to read our goals into our db, I am going to hardcode these up front with the possibility
#later on 

myDate1 = date.today()
goal_1 = Goal("Exercise")
goal_2 = Goal("Read for One Hour")
goal_3 = Goal("Journal")
goal_4 = Goal("Two Hours of Personal Work")
goal_5 = Goal("Stretch")



#c.execute("INSERT INTO goals VALUES (?,?,?)", (myDate1.))
#c.execute("INSERT INTO goals VALUES (?,?,?)", (goal_1.goal))
print(myDate1)
