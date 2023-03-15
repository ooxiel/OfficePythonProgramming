import os
os.system('clear')

# from os import getcwd
# where_am_i = getcwd()
# print(where_am_i)

# import sys
# print(sys.platform)
# print(sys.version)

import datetime
iso = datetime.date.isoformat(datetime.date.today())    # ISO 8601 Datumsformat
print(iso)

# today = datetime.datetime.today()
# print(today)

# day = datetime.date.today().day
# month = datetime.date.today().month
# year = datetime.date.today().year

# print(day, month, year)

import time
print(time.strftime('%H:%M:%S'))  # 24h format
print(time.strftime('%I:%M:%S'))  # 12h format

print(time.strftime('%A %p'))
