'''
Following Code was use as a preparation for the analysis and presentation of the data.
It is used get in touch with certain functions and methods of the pandas library.
'''

import pandas as pd
import pyodbc as odbc

# Connect to the database

def connect() -> odbc.Connection:
    '''define function connect -> used to connect to database'''

    DRIVER = input(r'Insert Driver name')           # input driver name -> use because of different driver names
    print(f"you choose: {DRIVER} as your driver")   # print driver name for confirmation

    SERVER = input(r'Insert Server name')           # input server name -> use because of different server names
    print(f"you choose: {SERVER} as your server")   # print server name for confirmation

    DB = input(r'Insert Database name')             # input database name -> use because of different database names
    print(f"you choose: {DB} as your database")     # print database name for confirmation

    # Build Connection
    connect_string = f'DRIVER={DRIVER};SERVER={SERVER};DATABASE={DB};Trusted_Connection=yes;' # build connection string
    conn = odbc.connect(connect_string) # connect to database

    return  conn


connection = connect()          # connect to database
cursor = connection.cursor()    # create cursor object -> cursor is used to execute SQL statements


# Create a dataframe with the data from the database

df = pd.read_sql_query("SELECT * FROM [dbo].[Table]", connection) # read data from database and create dataframe


