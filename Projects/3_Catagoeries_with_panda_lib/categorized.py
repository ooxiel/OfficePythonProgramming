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
test = cursor.execute('ALTER TABLE survey ADD sampleSizeCategorie VARCHAR(20);')

cursor.execute('SELECT sampleSize FROM survey;')
row = cursor.fetchall()



# Categorie one: sample size 



# ALTER TABLE !!!!!!!!!!!!!

# cursor.execute(query)
# cnxn.commit()