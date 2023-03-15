#%% 
odds = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,35,37,39,41,43,45,47,49,51,53,55,57,59]
# Liste
# lists can consists of any possible datatype, even objects
# lists are mutable
# lists are ordered
# lit times are addressable with an index

# Keep in mind. there are a lot of different operators:
#   arithmetic operator
#   logic operator (AND; OR; NOT)
#   comparrision operator (<; >; =;...)
#   assignment operator
#   membership operator (in; not in)
#   identity operator (is; is not)
#   bitwise operator ()

print(odds)

#%%

from datetime import datetime
import os

os.system('clear')  # clear terminal

odds = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,35,37,39,41,43,45,47,49,51,53,55,57,59]  # odds from 1 to 59
right_this_minute = datetime.today().minute # safe current minut in variable 'right_this_minute'

if right_this_minute in odds:   #check if current minute is an even or odd
    print('This minute seems a little bit odd')
else:
    print('Not an odd minute')
# %%

# 'Else' with moren than one condition
today = 'Wednesday'

if today == 'Saturday':
    print('Party!') # suite (intended block)
elif today == 'Sunday':
    print('Recover')
else:
    print('Work, work, work')
#%%

# Task: Insert a new condition, Test if the contestnat has a headache or not. What has to be done if headache is true?

# 'Else' with moren than one condition
today = 'Sunday'
headache= True

if today == 'Saturday':
    print('Party!') # suite (intended block)
elif today == 'Sunday':
    print('Recover and Sleep')

    if headache == True:
        print('Sleep and drink water')
    else:
        print('Just Sleep')

else:
    print('Work, work, work')

# %%

import random
dir(random)
# %%

import random
random.randint(1, 5)    # edges are included


# %%
