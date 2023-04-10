'''
Following Code was used to 
    1. Access local SQL Server Database via ODBC protocoll
    2. Categorize data and rewrite in SQL

To use this code you need to perform the following steps:

    1. setup a SQL Server Database

    For this specific project, you need to create a SQL Server Database (local or remote). All methods are written for the specific database 'mueller'. But you can rewrite the code to use your own database.
    You can create the database by yourself or use the following script to create the database 'mueller': 'mueller-init.sql'. 
    
    2. Setup ODBC Connection

    To use a ODBC Connection you need to setup a System driver. Under Windows:
        1. Open ODBC-Data Source Administrator
        2. Click on System DSN
        3. Click on Add
        4. Select SQL Server
        5. Give the connection a name
        6. Give a server name (local or remote server nessesary)
        7. Click on Finish

    3. Setup Python Environment wird pip install pyodbc
    
    Notice:
        - Code only fully functional if SQL Server, Driver and Database are setup before
        - Code is test with Local SQL Server Database and Windows Authentication
        -> other authentication methods or servers were not tested

'''

''' Import Libs'''

import pyodbc as odbc   # import lib pyodbc as object odbc -> used to access database via ODBC protocoll

''' Define Functions'''

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

def createCategorieTables() -> None:
    '''used to create categorie tables in database'''

    cursor.execute(f"CREATE TABLE dim_categorieSampleSize (categorieSampleSizeID_pk INTEGER IDENTITY(1,1), categorie varchar(255) NOT NULL, PRIMARY KEY(categorieSampleSizeID_pk));")   # create table dim_categorieSampleSize
    cursor.commit() # commit changes
    cursor.execute(f"CREATE TABLE dim_categorieDate (categorieDateID_pk INTEGER IDENTITY(1,1), categorie varchar(255) NOT NULL, PRIMARY KEY(categorieDateID_pk));")                     # create table dim_categorieDate
    cursor.commit() # commit changes
    cursor.execute(f"CREATE TABLE dim_categorieVotes (categorieVotesID_pk INTEGER IDENTITY(1,1), categorie varchar(255) NOT NULL, PRIMARY KEY(categorieVotesID_pk));")                  # create table dim_categorieVotes
    cursor.commit() # commit changes

def insertCategorieValues() -> None:
    '''used to insert categorie values into categorie tables -> categorie tables need to be created before'''

    cursor.execute(f''' INSERT INTO dim_categorieSampleSize (categorie) VALUES ('low'), ('medium'), ('high'), ('runaway')''') # insert new entry into categorie table
    cursor.commit() # commit changes
    cursor.execute(f''' INSERT INTO dim_categorieDate (categorie) VALUES ('1. quarter'), ('2. quarter'), ('3. quarter'), ('4. quarter')''') # insert new entry into categorie table
    cursor.commit() # commit changes
    cursor.execute(f''' INSERT INTO dim_categorieVotes (categorie) VALUES ('minority'), ('indecision'), ('majority')''')                    # insert new entry into categorie table
    cursor.commit() # commit changes

def getPrimary(table: str, primary: str, categorie: str) -> int:
    '''used to get primary key of specific categorie table'''

    cursor.execute(f"SELECT {primary} FROM {table} WHERE categorie = '{categorie}'")    # select specified primary key from categorie table
    list = cursor.fetchall()                                                            # fetch all data from cursor to list of tuples
    x = list[0][0]                                                                      # get first element of first tuple in list -> only possible because query returns only one value
    return x                                                                            # return primary key

def categorizeSize(row: list, table: str, columnName: str, primaryKey: str) -> None:

    cursor.execute(f'''ALTER TABLE {table} ADD {columnName} INTEGER;''') # add new column to table
    cursor.commit() # commit changes

    for I in range(0, len(row)):                                                                    # iterate over all rows from 0 to length of row

        if row[I][0] < 1000:                                                                        # if value in row is smaller than 1000 -> low
            x = getPrimary('dim_categorieSampleSize', 'categorieSampleSizeID_pk', 'low')            # get primary key of categorie 'low' from dim_categorieSampleSize
            cursor.execute(f'''UPDATE {table} SET {columnName} = {x} WHERE {primaryKey}={I+1};''')  # update table with new value because of new column -> primary key starts with 1 not with 0 -> +1
            cursor.commit() # commit changes
        elif row[I][0] < 1250:                                                                      # if value in row is smaller than 1250 -> medium
            x = getPrimary('dim_categorieSampleSize', 'categorieSampleSizeID_pk', 'medium')         # get primary key of categorie 'medium' from dim_categorieSampleSize
            cursor.execute(f'''UPDATE {table} SET {columnName} = {x} WHERE {primaryKey}={I+1};''')  # update table with new value because of new column
            cursor.commit() # commit changes
        elif row[I][0] <= 1500:                                                                     # if value in row is bigger or equal than 1500 -> high
            x = getPrimary('dim_categorieSampleSize', 'categorieSampleSizeID_pk', 'high')           # get primary key of categorie 'high' from dim_categorieSampleSize
            cursor.execute(f'''UPDATE {table} SET {columnName} = {x} WHERE {primaryKey}={I+1};''')  # update table with new value because of new column
            cursor.commit() # commit changes
        
        elif row[I][0] > 1500:                                                                     # if value in row is bigger or equal than 1500 -> high
            x = getPrimary('dim_categorieSampleSize', 'categorieSampleSizeID_pk', 'runaway')           # get primary key of categorie 'high' from dim_categorieSampleSize
            cursor.execute(f'''UPDATE {table} SET {columnName} = {x} WHERE {primaryKey}={I+1};''')  # update table with new value because of new column
            cursor.commit() # commit changes
        
    cursor.execute(f'''ALTER TABLE {table} ADD FOREIGN KEY ({columnName}) REFERENCES dim_categorieSampleSize(categorieSampleSizeID_pk);''') # add foreign key connection to fact table
    cursor.commit() # commit changes

def categorizeDate(row: list, table: str, columnName: str, primaryKey: str) -> None:
    '''used to categorize date into quarters'''

    cursor.execute(f'''ALTER TABLE {table} ADD {columnName} INTEGER;''') # add new column to table
    cursor.commit() # commit changes

    for J in range (0, len(row)):                                                                   # iterate over row in from 0 to length of row 

        if 1 <= row[J][0] <= 31 and 1 <= row[J][1] <= 3:                                            # check if day is in first quarter and month is in first quarter -> row is a list of tuples -> J used to access the J th element of the list -> 0 used to access the first element of the tuple -> only possible because of the structure of the input data
            x = getPrimary('dim_categorieDate', 'categorieDateID_pk', '1. quarter')                 # get primary key of 1. quarter in categorie table
            cursor.execute(f'''UPDATE {table} SET {columnName} = {x} WHERE {primaryKey}={J+1};''')  # update table with new value -> primary key starts with 1 not with 0 -> +1

        elif 1 <= row[J][0] <= 31 and 4 <= row[J][1] <= 6:                                          # check if day is in second quarter and month is in second quarter
            x = getPrimary('dim_categorieDate', 'categorieDateID_pk', '2. quarter')                 # get primary key of 2. quarter in categorie table
            cursor.execute(f'''UPDATE {table} SET {columnName} = {x} WHERE {primaryKey}={J+1};''')  # update table with new value 
            cursor.commit() # commit changes
        elif 1 <= row[J][0] <= 31 and 7 <= row[J][1] <= 9:                                          # check if day is in third quarter and month is in third quarter
            x = getPrimary('dim_categorieDate', 'categorieDateID_pk', '3. quarter')                 # get primary key of 3. quarter in categorie table
            cursor.execute(f'''UPDATE {table} SET {columnName} = {x} WHERE {primaryKey}={J+1};''')  # update table with new value 
            cursor.commit() #  commit changes
        elif 1 <= row[J][0] <= 31 and 10 <= row[J][1] <= 12:                                        # check if day is in fourth quarter and month is in fourth quarter
            x = getPrimary('dim_categorieDate', 'categorieDateID_pk', '4. quarter')                 # get primary key of 4. quarter in categorie table
            cursor.execute(f'''UPDATE {table} SET {columnName} = {x} WHERE {primaryKey}={J+1};''')  # update table with new value
            cursor.commit() # commit changes

    cursor.execute(f'''ALTER TABLE {table} ADD FOREIGN KEY ({columnName}) REFERENCES dim_categorieDate(categorieDateID_pk);''') # add foreign key to fact table
    cursor.commit() # commit changes

def categorizeVotes(row: list, table: str, columnName: str, primaryKey: str) -> None:
    '''used to categorize votes into minority, indecision and majority'''

    cursor.execute(f'''ALTER TABLE {table} ADD {columnName} INTEGER;''') # add new column to table
    cursor.commit() # commit changes

    for J in range (0, len(row)):                                                                   # iterate over row in from 0 to length of row

        if 0 <= row[J][0] <= 50:                                                                     # check if given yyvalue is in minority -> row is a list of tuples -> J used to access the J th element of the list -> 0 used to access the first element of the tuple -> only possible because of the structure of the input data
            x = getPrimary('dim_categorieVotes', 'categorieVotesID_pk', 'minority')                 # get primary key of categorie 'minority' from dim_categorieVotes
            cursor.execute(f'''UPDATE {table} SET {columnName} = {x} WHERE {primaryKey}={J+1};''')  # update table with new value because of new column -> primary key starts with 1 not with 0 -> +1
            cursor.commit() # commit changes
        elif row[J][0] == 50:                                                                       # check if given value is in indecision                           
            x = getPrimary('dim_categorieVotes', 'categorieVotesID_pk', 'majority')                 # get primary key of categorie 'indecision' from dim_categorieVotes
            cursor.execute(f'''UPDATE {table} SET {columnName} = {x} WHERE {primaryKey}={J+1};''')  # update table with new value because of new column
            cursor.commit() # commit changes
        elif 51 <= row[J][0] <= 100:                                                                # check if given value is in majority
            x = getPrimary('dim_categorieVotes', 'categorieVotesID_pk', 'majority')                 # get primary key of categorie 'majority' from dim_categorieVotes
            cursor.execute(f'''UPDATE {table} SET {columnName} = {x} WHERE {primaryKey}={J+1};''')  # update table with new value because of new column
            cursor.commit() # commit changes
    
    cursor.execute(f'''ALTER TABLE {table} ADD FOREIGN KEY ({columnName}) REFERENCES dim_categorieVotes(categorieVotesID_pk);''') # add foreign key to table
    cursor.commit() # commit changes

''' Call setup functions '''

connection = connect()          # connect to database
cursor = connection.cursor()    # create cursor object -> cursor is used to execute SQL statements

createCategorieTables()         # create tables
insertCategorieValues()         # insert values

'''Call categorize functions for survey table'''

# Config for TABLE -> survey
table_survey = 'fact_survey'                                                             # name of table -> survey
pk_survey = 'surveyID_pk'                                                           # primary key of table -> surveyID_pk                   

#       sampleSize
cursor.execute(f'SELECT sampleSize FROM {table_survey};')                           # get sampleSize column from table survey
sampleSize_row = cursor.fetchall()                                                  # fetch all rows -> list of tuples
categorizeSize(sampleSize_row,table_survey,'sampleSizeCategorie_fk',pk_survey)      # categorize sampleSize

#       startDate
cursor.execute(f'SELECT DAY(startDate),MONTH(startDate) FROM {table_survey};')      # get day and month seperately from startDate column
startDate_row = cursor.fetchall()                           	                    # fetch all rows -> list of tuples
categorizeDate(startDate_row,table_survey,'startDateQuartal_fk',pk_survey)          # categorize startDate

#       endDate
cursor.execute(f'SELECT DAY(endDate),MONTH(endDate) FROM {table_survey};')          # get day and month seperately from endDate column
endDate_row = cursor.fetchall()                                                     # fetch all rows -> list of tuples
categorizeDate(endDate_row,table_survey,'endDateQuartal_fk',pk_survey)              # categorize endDate


'''Call categorize functions for dim_basicResultset table'''

# Config for TABLE -> basicResultset
table_basic = 'dim_basicResultset'                                                  # name of table -> basicResultset
pk_basic = 'basicResultID_pk'                                                       # primary key of table -> basicResultID_pk

#       approve column
cursor.execute(f'SELECT approve FROM {table_basic};')                               # get approve column from table basicResultset
approve_row = cursor.fetchall()                                                     # fetch all rows -> list of tuples
categorizeVotes(approve_row,table_basic,'approveCategorie_fk',pk_basic)             # categorize approve

#       disapprove column
cursor.execute(f'SELECT disapprove FROM {table_basic};')                            # get disapprove column from table basicResultset       
disapprove_row = cursor.fetchall()                                                  # fetch all rows -> list of tuples
categorizeVotes(disapprove_row,table_basic,'disapproveCategorie_fk',pk_basic)       # categorize disapprove

'''Call categorize functions for dim_extendedResultset table'''

# Config for TABLE -> extendedResultset
table_extend = 'dim_extendedResultset'                                                      # name of table -> extendedResultset      
pk_extend = 'extendedResultID_pk'                                                           # primary key of table -> extendedResultID_pk          

#       approveRepublicans
cursor.execute(f'SELECT approveRepublicans FROM {table_extend};')                           # get approveRepublicans column from table extendedResultset
approveRep_row = cursor.fetchall()                                                          # fetch all rows -> list of tuples
categorizeVotes(approveRep_row, table_extend,'approveRepublicansCategorie_fk',pk_extend)    # categorize approveRepublicans

#       approveDemocrats
cursor.execute(f'SELECT approveDemocrats FROM {table_extend};')                             # get approveDemocrats column from table extendedResultset
approveDem_row = cursor.fetchall()                                                          # fetch all rows -> list of tuples            
categorizeVotes(approveDem_row, table_extend,'approveDemocratsCategorie_fk',pk_extend)      # categorize approveDemocrats