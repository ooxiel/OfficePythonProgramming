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


for K in range (0, len(startDate_row)):
    if (1 <= startDate_row[K][0] <= 31) and (1 <= startDate_row[K][1] <= 3):
        cursor.execute(f'''UPDATE survey SET startDateQuartal = 'Q1' WHERE surveyID_pk={K+1};''')
        cursor.commit()
    elif (1 <= startDate_row[K][0] <= 31) and (4 <= startDate_row[K][1] <= 6):
        cursor.execute(f'''UPDATE survey SET startDateQuartal = 'Q2' WHERE surveyID_pk={K+1};''')
        cursor.commit()
    elif (1 <= startDate_row[K][0] <= 31) and (7 <= startDate_row[K][1] <= 9):
        cursor.execute(f'''UPDATE survey SET startDateQuartal = 'Q3' WHERE surveyID_pk={K+1};''')
        cursor.commit()
    elif (1<= startDate_row[K][0] <= 31) and (10 <= startDate_row[K][1] <= 12):
        cursor.execute(f'''UPDATE survey SET startDateQuartal = 'Q4' WHERE surveyID_pk={K+1};''')
        cursor.commit()

cursor.execute("ALTER TABLE survey DROP COLUMN IF EXISTS endDateQuartal;")
cursor.commit()
cursor.execute("ALTER TABLE survey ADD endDateQuartal varchar(2);")
cursor.commit()
cursor.execute('SELECT DAY(endDate),MONTH(endDate) FROM survey')

endDate_row = cursor.fetchall()

for J in range (0, len(endDate_row)):
    if 1 <= endDate_row[J][0] <= 31 and 1<= endDate_row[J][1] <= 3:
        cursor.execute(f'''UPDATE survey SET endDateQuartal = 'Q1' WHERE surveyID_pk={J+1};''')
        cursor.commit()
    elif 1 <= endDate_row[J][0] <= 31 and 4 <= endDate_row[J][1] <= 6:
        cursor.execute(f'''UPDATE survey SET endDateQuartal = 'Q2' WHERE surveyID_pk={J+1};''')
        cursor.commit()
    elif 1 <= endDate_row[J][0] <= 31 and 7 <= endDate_row[J][1] <= 9:
        cursor.execute(f'''UPDATE survey SET endDateQuartal = 'Q3' WHERE surveyID_pk={J+1};''')
        cursor.commit()
    elif 1 <= endDate_row[J][0] <= 31 and 10 <= endDate_row[J][1] <= 12:
        cursor.execute(f'''UPDATE survey SET endDateQuartal = 'Q4' WHERE surveyID_pk={J+1};''')
        cursor.commit()