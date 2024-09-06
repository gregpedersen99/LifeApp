#Going to make a couple of pretty straightforward functions here that I can call in main, just easier to do 
#it this way than to create more classes 

from datetime import date


myDate = date.today()

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




