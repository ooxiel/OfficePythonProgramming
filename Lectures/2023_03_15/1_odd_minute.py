from datetime import datetime
import os

os.system('clear')  # clear terminal

odds = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,35,37,39,41,43,45,47,49,51,53,55,57,59]  # odds from 1 to 59
right_this_minute = datetime.today().minute # safe current minut in variable 'right_this_minute'

if right_this_minute in odds:   #check if current minute is an even or odd
    print('This minute seems a little bit odd')
else:
    print('Not an odd minute')