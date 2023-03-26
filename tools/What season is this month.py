''' A program that reads a month and day from the user. '''

#                        INPUT
# The user will enter the name of the month as a string, 
# followed by the day within the month as an integer. 

#                        OUTPUT
# Then your program should display the season associated with the date that was entered.

# we will use the following dates for this exercise:
# | Season | First day     |
# |------------------------|
# | Spring | March 20      |
# | Summer | June 21       |
# | Fall   | September 22  |
# | Winter | December 21   |

def seasonOfThis(Date):
    months = ['January','February','March','April','May','June','July','August', 'September','October','November','December']
    first_days = {'March'    :['Winter',20,'Spring'],
                  'June'     :['Spring',21,'Summer'],
                  'September':['Summer',22,'Fall'],
                  'December' :['Fall',21,'Winter']}
    month, day = Date.split()
    
    if month in ['March','June','September','December']:
        if int(day) >= first_days[month][1]:
            return first_days[month][2]
        else:
            return first_days[month][0]

    if month in ['January','February']:
        return 'Winter'
    elif month in ['April','May']:
        return 'Spring'
    elif month in ['July','August']:
        return 'Summer'
    elif month in ['October','November']:
        return 'Fall'


if __name__ == '__main__':
    while True:
        Date = input("Date: ")
        if Date in ['q','quit','exit','stop','yamete']:
            break
        result = seasonOfThis(Date)
        print(f"{Date} is in {result}")