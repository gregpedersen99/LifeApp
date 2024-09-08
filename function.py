#Going to make a couple of pretty straightforward functions here that I can call in main, just easier to do 
#it this way than to create more classes 

from datetime import date
import sqlite3


def convert_date(myDate): #Need if statements to coinvert the month to a str month because I think it looks nicer 
    

    if myDate.month == 1: #Im sure there is a much more elegant way of doing this but this is just really readable and easy 
        month = 'January'
    if myDate.month == 2:
        month = 'February'
    if myDate.month == 3:
        month = 'March'
    if myDate.month == 4:
        month = 'April'
    if myDate.month == 5:
        month = 'May'
    if myDate.month == 6:
        month = 'June'
    if myDate.month == 7:
        month = 'July'
    if myDate.month == 8:
        month = 'August'
    if myDate.month == 9:
        month = 'September'
    if myDate.month == 10:
        month = 'October'
    if myDate.month == 11:
        month = 'November'
    if myDate.month == 12:
        month = 'December'
    
    adjustedDate = str(month) + " " + str(myDate.day) + " , " + str(myDate.year)

    return adjustedDate

def get_outputs(goals):
    status = []
    for goal in goals:
        status.append(int(goal.isAchieved))
    status = tuple(status)
    push_to_goalsDB(status) #Push changes to the goal database 
    return status 


def push_to_goalsDB(results):
    myDate1 = date.today()
    conn = sqlite3.connect('goals.db') #Creating my database that will be used to storae goals 

    c = conn.cursor() #setting up cursor value to begin writing sql commands 

    #By running this in a function here, we are able to call it in get_outputs and commit the changes to 
    #a database every time submit is clicked 
    c.execute("""CREATE TABLE IF NOT EXISTS goals (
            date text, 
            Read for One Hour integer,
            Exercise integer,
            Journal integer, 
            Stretch integer,
            Two Hour Personal Work integer
            )""")
    
    c.execute("INSERT INTO goals VALUES (?,?,?,?,?,?)", (myDate1, results[0], results[1], results[2], results[3], results[4])) #Inserting 1 for yes, 0 for no, can change this later but for now it is this 
    conn.commit()
    #conn.close()
    #adding in a sql function that will clean up the database by only including the most recent value for a given date 
    
    #This query/subquery will delete all rows from our DB except for the most recent saved input row,
    #Cleaning up our values
    #Inner most subquery selects the maximum row ID for rach date
    #The middle subquery then filters the table to include only the latest entries 
    #The outer subquery deletes the rows from the original table that are not a part of the unique date 
    c.execute ("""DELETE FROM goals
               WHERE rowid NOT IN (
               SELECT rowid
               FROM (
                    SELECT rowid, date
                    FROM goals
                    WHERE (date, rowid) IN (
                        SELECT date, MAX (rowid) 
                        FROM goals
                        GROUP BY date
                    )
                )
            )
        
    """)
    conn.commit()
    conn.close()
