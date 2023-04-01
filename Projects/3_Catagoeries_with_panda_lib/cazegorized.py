import pandas as pd
import pyodbc as odbc


DRIVER = r'SQL Server'          # configure odbc driver in windows
SERVER = r'CUBRIM\SQLEXPRESS'   # server name
DB = r'mueller'                 # database name

connect_string = f'DRIVER={DRIVER};SERVER={SERVER};DATABASE={DB};Trusted_Connection=yes;'
conn = odbc.connect(connect_string)
print(conn)
