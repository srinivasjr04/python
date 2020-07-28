## Program to calculate Gross pay of an Employee


duration = float(input('Enter number of hours in HH:MM format : '))
rate = float(input('Enter rate per hour : '))

# extract minutes from duration

minutes = round(duration % 1.0,2)

# check the minutes enter are between 0 to 60

if minutes * 100 < 0 or minutes*100 > 60 :
    print("invalid duration of minutes (0 - 60) : ", str(int(minutes*100)) + ' minutes')
else:
    # extract hours portion
    hours = duration // 1 

    # scale up the minutes portion from 0-60 to 0-100 
    minutes = ((minutes * 1/60) * 100)
    
    # concatenate hours portion and minutes portion
    duration = hours + minutes

    # calculate the gross pay
    pay = duration * rate

    # round off the change to nearest 100th place value
    pay = round(pay,2)
    print('Gross pay is : ',pay)