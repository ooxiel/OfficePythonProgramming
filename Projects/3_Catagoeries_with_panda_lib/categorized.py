'''
Following Code was used to 
    1. Access local SQL Server Database via ODBC protocoll
    2. Categorize data with pandas
'''
# ========================================================= #
'''
Setup Configuration
'''
# import neccessary libarys via pip install ...

import pandas as pd     # import lib pandas as object pd -> used to perform data operations
import pyodbc as odbc   # import lib pyodbc as object odbc -> used to access locally created via odbc protocoll
import datetime as dt

# Server and Database Connection Configuration

DRIVER = r'SQL Server'          # configure odbc driver in windows
SERVER = r'CUBRIM\SQLEXPRESS'   # server name
DB = r'mueller'                 # database name

# Build Connection
connect_string = f'DRIVER={DRIVER};SERVER={SERVER};DATABASE={DB};Trusted_Connection=yes;'
conn = odbc.connect(connect_string)

# Create cursor object in database
cursor = conn.cursor()

'''
method implementation for categorization of attributes
'''

def newColforExistingTable(table, columnName, type):

    cursor.execute(f"ALTER TABLE {table} DROP COLUMN IF EXISTS {columnName};")
    cursor.commit()
    cursor.execute(f"ALTER TABLE {table} ADD {columnName} {type};")
    cursor.commit()

def categorizeSize(row, table, columnName, primaryKey):
    for I in range(0, len(row)):
       
        if row[I][0] < 1000:
            cursor.execute(f'''UPDATE {table} SET {columnName} = 'low' WHERE {primaryKey}={I+1};''')
            cursor.commit()
        elif row[I][0] < 2000:
            cursor.execute(f'''UPDATE {table} SET {columnName} = 'medium' WHERE {primaryKey}={I+1};''')
            cursor.commit()
        elif row[I][0] >= 2000:
            cursor.execute(f'''UPDATE {table} SET {columnName} = 'high' WHERE {primaryKey}={I+1};''')
            cursor.commit()

def categorizeDate(row, table, columnName, primaryKey):
    for J in range (0, len(row)):
        if 1 <= row[J][0] <= 31 and 1<= row[J][1] <= 3:
            cursor.execute(f'''UPDATE {table} SET {columnName} = 'Q1' WHERE {primaryKey}={J+1};''')
            cursor.commit()
        elif 1 <= row[J][0] <= 31 and 4 <= row[J][1] <= 6:
            cursor.execute(f'''UPDATE {table} SET {columnName} = 'Q2' WHERE {primaryKey}={J+1};''')
            cursor.commit()
        elif 1 <= row[J][0] <= 31 and 7 <= row[J][1] <= 9:
            cursor.execute(f'''UPDATE {table} SET {columnName} = 'Q3' WHERE {primaryKey}={J+1};''')
            cursor.commit()
        elif 1 <= row[J][0] <= 31 and 10 <= row[J][1] <= 12:
            cursor.execute(f'''UPDATE {table} SET {columnName} = 'Q4' WHERE {primaryKey}={J+1};''')
            cursor.commit()

def categorizeVotes(row, table, columnName, primaryKey):
    for J in range (0, len(row)):
        if 0 <= row[J][0] < 34:
            cursor.execute(f'''UPDATE {table} SET {columnName} = 'minority' WHERE {primaryKey}={J+1};''')
            cursor.commit()
        elif 34 <= row[J][0] < 67:
            cursor.execute(f'''UPDATE {table} SET {columnName} = 'indecision' WHERE {primaryKey}={J+1};''')
            cursor.commit()
        elif 67 <= row[J][0] < 100:
            cursor.execute(f'''UPDATE {table} SET {columnName} = 'majority' WHERE {primaryKey}={J+1};''')
            cursor.commit()



'''
Call methods
'''

##### TABLE survey
table_survey = 'survey'
pk_survey = 'surveyID_pk'

# sampleSize
newColforExistingTable(table_survey, 'sampleSizeCategorie','varchar(10)')
cursor.execute(f'SELECT sampleSize FROM {table_survey};')
sampleSize_row = cursor.fetchall()
categorizeSize(sampleSize_row,table_survey,'sampleSizeCategorie',pk_survey)

# startDate
newColforExistingTable(table_survey, 'startDateQuartal','varchar(2)')
cursor.execute(f'SELECT DAY(startDate),MONTH(startDate) FROM {table_survey};')
startDate_row = cursor.fetchall()
categorizeDate(startDate_row,table_survey,'startDateQuartal',pk_survey)

# endDate
newColforExistingTable(table_survey, 'endDateQuartal','varchar(2)')
cursor.execute(f'SELECT DAY(endDate),MONTH(endDate) FROM {table_survey};')
endDate_row = cursor.fetchall()
categorizeDate(endDate_row,table_survey,'endDateQuartal',pk_survey)


##### TABLE basicResultset
table_basic = 'basicResultset'
pk_basic = 'basicResultID_pk'

# approve column
newColforExistingTable(table_basic, 'approveCategorie','varchar(20)')
cursor.execute(f'SELECT approve FROM {table_basic};')
approve_row = cursor.fetchall()
categorizeVotes(approve_row,table_basic,'approveCategorie',pk_basic)

# disapprove column
newColforExistingTable(table_basic, 'disapproveCategorie','varchar(20)')
cursor.execute(f'SELECT disapprove FROM {table_basic};')
disapprove_row = cursor.fetchall()
categorizeVotes(disapprove_row,table_basic,'disapproveCategorie',pk_basic)

# unsure column
newColforExistingTable(table_basic, 'unsureCategorie','varchar(20)')
cursor.execute(f'SELECT unsure FROM {table_basic};')
unsure_row = cursor.fetchall()
categorizeVotes(unsure_row,table_basic,'unsureCategorie',pk_basic)

##### TABLE extendedResultset
table_extend = 'extendedResultset'
pk_extend = 'extendedResultID_pk'

# approveRepublicans
newColforExistingTable(table_extend, 'approveRepublicansCategorie','varchar(20)')
cursor.execute(f'SELECT approveRepublicans FROM {table_extend};')
approveRep_row = cursor.fetchall()
categorizeVotes(approveRep_row, table_extend,'approveRepublicansCategorie',pk_extend)

# approveDemocrats
newColforExistingTable(table_extend, 'approveDemocratsCategorie','varchar(20)')
cursor.execute(f'SELECT approveDemocrats FROM {table_extend};')
approveDem_row = cursor.fetchall()
categorizeVotes(approveDem_row, table_extend,'approveDemocratsCategorie',pk_extend)