'''
Following Code was used to 
    1. Access local SQL Server Database via ODBC protocoll
    2. Categorize data with pandas
'''

# import neccessary libarys via pip install ...

import pandas as pd     # import lib pandas as object pd -> used to perform data operations
import pyodbc as odbc   # import lib pyodbc as object odbc -> used to access locally created via odbc protocoll

 # Server and Database Connection Configuration

DRIVER = r'SQL Server'          # configure odbc driver in windows
SERVER = r'CUBRIM\SQLEXPRESS'   # server name
DB = r'mueller'                 # database name

 # Build Connection

connect_string = f'DRIVER={DRIVER};SERVER={SERVER};DATABASE={DB};Trusted_Connection=yes;'
conn = odbc.connect(connect_string)


# Create cursor object in database
cursor = conn.cursor()

# Add column 'sampleSizeCategorie' to table 'survey' -> First drop column 
cursor.execute("ALTER TABLE survey DROP COLUMN sampleSizeCategorie")
cursor.execute("ALTER TABLE survey ADD sampleSizeCategorie varchar(20)")
cursor.commit()

# Select-Statement to select values of sampleSize and fetch them to a list of tuples
cursor.execute('SELECT sampleSize FROM survey;')
sampleSize_row = cursor.fetchall()

# categorize sampleSize
for I in range(0, len(sampleSize_row)):
       
    if sampleSize_row[I][0] < 1000:
        cursor.execute(f'''UPDATE survey SET sampleSizeCategorie = 'low' WHERE surveyID_pk={I+1}''')
        cursor.commit()
    elif sampleSize_row[I][0] < 2000:
        cursor.execute(f'''UPDATE survey SET sampleSizeCategorie = 'medium' WHERE surveyID_pk={I+1};''')
        cursor.commit()
    elif sampleSize_row[I][0] >= 2000:
        cursor.execute(f'''UPDATE survey SET sampleSizeCategorie = 'high' WHERE surveyID_pk={I+1};''')
        cursor.commit()
