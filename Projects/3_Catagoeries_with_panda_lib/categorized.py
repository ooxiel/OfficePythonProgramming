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

    3. Setup Python Environment
    
    It is nessecary to install and import the following libarys via pip install:
        - pandas
        - pyodbc

'''
# ========================================================= #
'''
Setup Configuration
'''

# import libarys and modules
import pyodbc as odbc                           # import lib pyodbc as object odbc -> used to access locally created via odbc protocoll


# Server and Database Connection Configuration

DRIVER = input(r'Insert Driver name')           # input driver name -> use because of different driver names
print(f"you choose: {DRIVER} as your driver")   # print driver name for confirmation

SERVER = input(r'Insert Server name')           # input server name -> use because of different server names
print(f"you choose: {SERVER} as your server")   # print server name for confirmation

DB = input(r'Insert Database name')             # input database name -> use because of different database names
print(f"you choose: {DB} as your database")     # print database name for confirmation


# Build Connection
connect_string = f'DRIVER={DRIVER};SERVER={SERVER};DATABASE={DB};Trusted_Connection=yes;' # build connection string
conn = odbc.connect(connect_string) # connect to database
cursor = conn.cursor() # create cursor object to perform database operations

# ========================================================= #
'''
Setup Categorie table
'''

cursor.execute(f"CREATE TABLE dim_categorie (categorieID_pk INTEGER IDENTITY(1,1), categorie varchar(255) NOT NULL, PRIMARY KEY(categorieID_pk));") # create table if not exists
cursor.commit() # commit changes -> necessary

# ========================================================= #
'''
@Name:          newInsertinCategorie
@Description:   create new entry in categorie table

@Parameters:    name -> name of new column

@Return:        None
'''
def newInsertinCategorie(name):

    # f = format string -> use to insert variables into string

    cursor.execute(f'''INSERT INTO dim_categorie (categorie) VALUES ('{name}')''')
    cursor.commit() # commit changes

'''
@Name:          categorizeSize
@Description:   categorize sampleSize into three categories low, medium and high
                    low     sampleSize < 1000
                    medium  1000 <= sampleSize < 2000
                    high    sampleSize >= 2000

@Parameters:    row -> row of data
                table -> name of table
                columnName -> name of new column
                primaryKey -> name of primary key

@Return:        None
'''
def categorizeSize(row, table, columnName, primaryKey):

    cursor.execute(f'''ALTER TABLE {table} ADD {columnName} INTEGER;''') # add new column to table
    cursor.commit() # commit changes

    for I in range(0, len(row)): # iterate over row in from 0 to length of row
       
        # row is a list of tuples -> row[I] = Ith tuple of row
        # I used to access the I th element of the tuple
        # 0 used to access the first element of the tuple
        # -> only possible because of the structure of the input data

        if row[I][0] < 1000:
            list = cursor.execute(f"SELECT categorieID_pk FROM dim_categorie WHERE categorie = 'low'")
            low = list.fetchone()
            cursor.execute(f'''UPDATE {table} SET {columnName} = {low[0]} WHERE {primaryKey}={I+1};''') # primary key starts with 1 not with 0 -> +1
            cursor.commit() # commit changes
        elif row[I][0] < 2000:
            list = cursor.execute(f"SELECT categorieID_pk FROM dim_categorie WHERE categorie = 'medium'")
            low = list.fetchone()
            cursor.execute(f'''UPDATE {table} SET {columnName} = {low[0]} WHERE {primaryKey}={I+1};''') # update table with new value because of new column
            cursor.commit()
        elif row[I][0] >= 2000:
            list = cursor.execute(f"SELECT categorieID_pk FROM dim_categorie WHERE categorie = 'high'")
            low = list.fetchone()
            cursor.execute(f'''UPDATE {table} SET {columnName} = {low[0]} WHERE {primaryKey}={I+1};''')
            cursor.commit()
        
    cursor.execute(f'''ALTER TABLE {table} ADD FOREIGN KEY ({columnName}) REFERENCES dim_categorie(categorieID_pk);''') # add foreign key to table
    cursor.commit() # commit changes

'''
@Name:          categorizeDate
@Description:   categorize startDate and endDate into quarters
                    1. quarter -> 1.1 - 31.3
                    2. quarter -> 1.4 - 30.6
                    3. quarter -> 1.7 - 30.9
                    4. quarter -> 1.10 - 31.12

@Parameters:    row -> row of data
                table -> name of table
                columnName -> name of new column
                primaryKey -> name of primary key

@Return:        None
'''
def categorizeDate(row, table, columnName, primaryKey):

    cursor.execute(f'''ALTER TABLE {table} ADD {columnName} INTEGER;''') # add new column to table
    cursor.commit() # commit changes

    # row is a list of tuples -> row[I] = Ith tuple of row
    # I used to access the I th element of the tuple
    # 0 used to access the first element of the tuple
    # -> only possible because of the structure of the input data

    for J in range (0, len(row)):
        if 1 <= row[J][0] <= 31 and 1 <= row[J][1] <= 3:
            cursor.execute(f"SELECT categorieID_pk FROM dim_categorie WHERE categorie = '1st Quartal'")
            Q1 = cursor.fetchone()
            cursor.execute(f'''UPDATE {table} SET {columnName} = {Q1[0]} WHERE {primaryKey}={J+1};''') # primary key starts with 1 not with 0 -> +1
            cursor.commit() # commit changes
        elif 1 <= row[J][0] <= 31 and 4 <= row[J][1] <= 6:
            cursor.execute(f"SELECT categorieID_pk FROM dim_categorie WHERE categorie = '2nd Quartal'")
            Q2 = cursor.fetchone()
            cursor.execute(f'''UPDATE {table} SET {columnName} = {Q2[0]} WHERE {primaryKey}={J+1};''') # update table with new value because of new column
            cursor.commit()
        elif 1 <= row[J][0] <= 31 and 7 <= row[J][1] <= 9:
            cursor.execute(f"SELECT categorieID_pk FROM dim_categorie WHERE categorie = '3rd Quartal'")
            Q3 = cursor.fetchone()
            cursor.execute(f'''UPDATE {table} SET {columnName} = {Q3[0]} WHERE {primaryKey}={J+1};''')
            cursor.commit()
        elif 1 <= row[J][0] <= 31 and 10 <= row[J][1] <= 12:
            cursor.execute(f"SELECT categorieID_pk FROM dim_categorie WHERE categorie = '4th Quartal'")
            Q4 = cursor.fetchone()
            cursor.execute(f'''UPDATE {table} SET {columnName} = {Q4[0]} WHERE {primaryKey}={J+1};''')
            cursor.commit()

    cursor.execute(f'''ALTER TABLE {table} ADD FOREIGN KEY ({columnName}) REFERENCES dim_categorie(categorieID_pk);''') # add foreign key to table
    cursor.commit() # commit changes


'''
@Name:          categorizeVotes
@Description:   categorize votes into three categories minority, indecision and majority
                    minority     0 <= votes < 34 
                    indecision   34 <= votes < 67  
                    majority     67 <= votes < 100
                
@Parameters:    row -> row of data
                table -> name of table
                columnName -> name of new column
                primaryKey -> name of primary key

@Return:        None
'''
def categorizeVotes(row, table, columnName, primaryKey):

    cursor.execute(f'''ALTER TABLE {table} ADD {columnName} INTEGER;''') # add new column to table
    cursor.commit() # commit changes

    # row is a list of tuples -> row[I] = Ith tuple of row
    # I used to access the I th element of the tuple
    # 0 used to access the first element of the tuple
    # -> only possible because of the structure of the input data

    for J in range (0, len(row)):
        if 0 <= row[J][0] < 34:
            cursor.execute(f"SELECT categorieID_pk FROM dim_categorie WHERE categorie = 'minority'")
            cat = cursor.fetchone()
            cursor.execute(f'''UPDATE {table} SET {columnName} = {cat[0]} WHERE {primaryKey}={J+1};''')   # primary key starts with 1 not with 0 -> +1
            cursor.commit() # commit changes
        elif 34 <= row[J][0] < 67:
            cursor.execute(f"SELECT categorieID_pk FROM dim_categorie WHERE categorie = 'indecision'")
            cat = cursor.fetchone()
            cursor.execute(f'''UPDATE {table} SET {columnName} = {cat[0]} WHERE {primaryKey}={J+1};''') # update table with new value because of new column
            cursor.commit()
        elif 67 <= row[J][0] < 100:
            cursor.execute(f"SELECT categorieID_pk FROM dim_categorie WHERE categorie = 'majority'")
            cat = cursor.fetchone()
            cursor.execute(f'''UPDATE {table} SET {columnName} = {cat[0]} WHERE {primaryKey}={J+1};''')
            cursor.commit()
    
    cursor.execute(f'''ALTER TABLE {table} ADD FOREIGN KEY ({columnName}) REFERENCES dim_categorie(categorieID_pk);''') # add foreign key to table
    cursor.commit() # commit changes

# ========================================================= #
'''
Call methods
'''

# Config for TABLE -> survey
table_survey = 'survey'
pk_survey = 'surveyID_pk'

newInsertinCategorie('low')     # call newInsertinCategorie -> insert 'low' into table
newInsertinCategorie('medium')  # call newInsertinCategorie -> insert 'medium' into table
newInsertinCategorie('high')    # call newInsertinCategorie -> insert 'high' into table

#       sampleSize
#newColforExistingTable(table_survey, 'sampleSizeCategorie','varchar(10)')
cursor.execute(f'SELECT sampleSize FROM {table_survey};')
sampleSize_row = cursor.fetchall()
categorizeSize(sampleSize_row,table_survey,'sampleSizeCategorie_fk',pk_survey)

newInsertinCategorie('1st Quartal') # call newInsertinCategorie -> insert '1st Quartal' into table
newInsertinCategorie('2nd Quartal') # call newInsertinCategorie -> insert '2nd Quartal' into table
newInsertinCategorie('3rd Quartal') # call newInsertinCategorie -> insert '3rd Quartal' into table
newInsertinCategorie('4th Quartal') # call newInsertinCategorie -> insert '4th Quartal' into table

#       startDate
#newColforExistingTable(table_survey, 'startDateQuartal','varchar(2)')
cursor.execute(f'SELECT DAY(startDate),MONTH(startDate) FROM {table_survey};')
startDate_row = cursor.fetchall()
categorizeDate(startDate_row,table_survey,'startDateQuartal_fk',pk_survey)

#       endDate
#newColforExistingTable(table_survey, 'endDateQuartal','varchar(2)')
cursor.execute(f'SELECT DAY(endDate),MONTH(endDate) FROM {table_survey};')
endDate_row = cursor.fetchall()
categorizeDate(endDate_row,table_survey,'endDateQuartal_fk',pk_survey)


# Config for TABLE -> basicResultset
table_basic = 'basicResultset'
pk_basic = 'basicResultID_pk'

newInsertinCategorie('minority') # call newInsertinCategorie -> insert 'minority' into table
newInsertinCategorie('indecision') # call newInsertinCategorie -> insert 'indecision' into table
newInsertinCategorie('majority') # call newInsertinCategorie -> insert 'majority' into table

#       approve column
#newColforExistingTable(table_basic, 'approveCategorie','varchar(20)')
cursor.execute(f'SELECT approve FROM {table_basic};')
approve_row = cursor.fetchall()
categorizeVotes(approve_row,table_basic,'approveCategorie_fk',pk_basic)

#       disapprove column
#newColforExistingTable(table_basic, 'disapproveCategorie','varchar(20)')
cursor.execute(f'SELECT disapprove FROM {table_basic};')
disapprove_row = cursor.fetchall()
categorizeVotes(disapprove_row,table_basic,'disapproveCategorie_fk',pk_basic)

#       unsure column
#newColforExistingTable(table_basic, 'unsureCategorie','varchar(20)')
cursor.execute(f'SELECT unsure FROM {table_basic};')
unsure_row = cursor.fetchall()
categorizeVotes(unsure_row,table_basic,'unsureCategorie_fk',pk_basic)


# Config for TABLE -> extendedResultset
table_extend = 'extendedResultset'
pk_extend = 'extendedResultID_pk'

#       approveRepublicans
#newColforExistingTable(table_extend, 'approveRepublicansCategorie','varchar(20)')
cursor.execute(f'SELECT approveRepublicans FROM {table_extend};')
approveRep_row = cursor.fetchall()
categorizeVotes(approveRep_row, table_extend,'approveRepublicansCategorie_fk',pk_extend)

#       approveDemocrats
#newColforExistingTable(table_extend, 'approveDemocratsCategorie','varchar(20)')
cursor.execute(f'SELECT approveDemocrats FROM {table_extend};')
approveDem_row = cursor.fetchall()
categorizeVotes(approveDem_row, table_extend,'approveDemocratsCategorie_fk',pk_extend)