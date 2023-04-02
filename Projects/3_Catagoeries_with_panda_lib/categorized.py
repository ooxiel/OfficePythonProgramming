'''
Following Code was used to 
    1. Access local SQL Server Database via ODBC protocoll
    2. Categorize data with pandas
'''

# import neccessary libarys via pip install ...

import pandas as pd     # import lib pandas as object pd -> used to perform data operations
import pyodbc as odbc   # import lib pyodbc as object odbc -> used to access locally created via odbc protocoll
import datetime as dt

# ====== #
# Server and Database Connection Configuration

DRIVER = r'SQL Server'          # configure odbc driver in windows
SERVER = r'CUBRIM\SQLEXPRESS'   # server name
DB = r'mueller'                 # database name

 # Build Connection

connect_string = f'DRIVER={DRIVER};SERVER={SERVER};DATABASE={DB};Trusted_Connection=yes;'
conn = odbc.connect(connect_string)

# Create cursor object in database
cursor = conn.cursor()

# ====== #

# Add column 'sampleSizeCategorie' to table 'survey' -> First drop column 
cursor.execute("ALTER TABLE survey DROP COLUMN IF EXISTS sampleSizeCategorie;")
cursor.commit()
cursor.execute("ALTER TABLE survey ADD sampleSizeCategorie varchar(20);")
cursor.commit()

# Select-Statement to select values of sampleSize and fetch them to a list of tuples
cursor.execute('SELECT sampleSize FROM survey;')
sampleSize_row = cursor.fetchall()

# categorize sampleSize
for I in range(0, len(sampleSize_row)):
       
    if sampleSize_row[I][0] < 1000:
        cursor.execute(f'''UPDATE survey SET sampleSizeCategorie = 'low' WHERE surveyID_pk={I+1};''')
        cursor.commit()
    elif sampleSize_row[I][0] < 2000:
        cursor.execute(f'''UPDATE survey SET sampleSizeCategorie = 'medium' WHERE surveyID_pk={I+1};''')
        cursor.commit()
    elif sampleSize_row[I][0] >= 2000:
        cursor.execute(f'''UPDATE survey SET sampleSizeCategorie = 'high' WHERE surveyID_pk={I+1};''')
        cursor.commit()

cursor.execute("ALTER TABLE survey DROP COLUMN IF EXISTS startDateQuartal;")
cursor.commit()
cursor.execute("ALTER TABLE survey ADD startDateQuartal varchar(2);")
cursor.commit()
cursor.execute('SELECT DAY(startDate),MONTH(startDate) FROM survey')

startDate_row = cursor.fetchall()

q1_start = dt.date(2000,1,1)
q1_end = dt.date(2000,3,31)

q2_start = dt.date(2000,4,1)
q2_end = dt.date(2000,6,30)

q3_start = dt.date(2000, 7,1)
q3_end = dt.date(2000, 9, 30)

q4_start = dt.date(2000, 10,1)
q4_end = dt.date(2000, 12, 31)

for K in range (0, len(startDate_row)):
    if q1_start.day <= startDate_row[K][0] <= q1_end.day and q1_start.month <= startDate_row[K][1] <= q1_start.month:
        cursor.execute(f'''UPDATE survey SET startDateQuartal = 'Q1' WHERE surveyID_pk={K+1};''')
        cursor.commit()
    elif q2_start.day <= startDate_row[K][0] <= q2_end.day and q2_start.month <= startDate_row[K][1] <= q2_start.month:
        cursor.execute(f'''UPDATE survey SET startDateQuartal = 'Q2' WHERE surveyID_pk={K+1};''')
        cursor.commit()
    elif q3_start.day <= startDate_row[K][0] <= q3_end.day and q3_start.month <= startDate_row[K][1] <= q3_start.month:
        cursor.execute(f'''UPDATE survey SET startDateQuartal = 'Q3' WHERE surveyID_pk={K+1};''')
        cursor.commit()
    elif q4_start.day <= startDate_row[K][0] <= q4_end.day and q4_start.month <= startDate_row[K][1] <= q4_start.month:
        cursor.execute(f'''UPDATE survey SET startDateQuartal = 'Q4' WHERE surveyID_pk={K+1};''')
        cursor.commit()