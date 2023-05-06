'''
Following Code was used as a preparation for the analysis and presentation of the data.
It is used get in touch with certain functions and methods of the pandas library.
'''

# Importing the libraries
import pandas as pd
from datetime import datetime
import pip._internal

# Installing the libraries automatically, if not already installed
# First tried it with a requirements.txt file, but it didn't work because of path possible path issues on different machines

pip._internal.main(['install', 'pandas'])
pip._internal.main(['install', 'datetime'])


# Importing the dataset with usecols to reduce the size of the dataset
df = pd.read_csv('C:\\Users\\becke\\OfficePythonProgramming\\Projects\\Ressources\\mueller-approval-polls.csv', usecols=['Pollster', 'Start', 'End', 'Text', 'Approve', 'Approve (Republican)','Approve (Democrat)','Url'])


# Variable 1: Mean of Approve columns
def meanApprove(df):

    resultList = []

    for i in df.index:
        x = df.loc[i, 'Approve']+df.loc[i, 'Approve (Republican)']+df.loc[i, 'Approve (Democrat)']
        resultList.append(x/3)

    return resultList

print(meanApprove(df))
df['Approve'] = meanApprove(df)

# Variable 2: Weekday of Start and End
def getweekdaybyDate(df,columName):
    
        resultList = []

        for i in df.index:
            x = datetime.strptime(df.loc[i, columName], '%m/%d/%y')
            
            match x.weekday():
                case 0: 
                    resultList.append("Monday")

                case 1:
                    resultList.append("Tuesday")

                case 2:
                    resultList.append("Wednesday")

                case 3:
                    resultList.append("Thursday")

                case 4:
                    resultList.append("Friday")

                case 5:
                    resultList.append("Saturday")

                case 6:
                    resultList.append("Sunday")
                case _:
                    resultList.append("Error")

        return resultList

print(getweekdaybyDate(df, 'Start'))
print(getweekdaybyDate(df, 'End'))

df['weekdayStart'] = getweekdaybyDate(df, 'Start')
df['weekdayEnd'] = getweekdaybyDate(df, 'End')

# Variable 3: Duration
def getDuration(df):
    resultList = []

    for i in df.index:
        x = datetime.strptime(df.loc[i, 'End'], '%m/%d/%y') - datetime.strptime(df.loc[i, 'Start'], '%m/%d/%y')

        if(x.days < 0):
           resultList.append(x.days * -1)
        else:
            resultList.append(x.days)

    return resultList

print(getDuration(df))

df['Duration'] = getDuration(df)

# Variable 4: Mean of Approve column
def topPollster(df):
    df = pd.DataFrame(df['Pollster'].value_counts())
    return df

print(topPollster(df))

# Variable 5: Count PDF and HTML
def countPDFResults(df):
    list = []
    listPDForHTML = []

    for i in df.index:
        x = df.loc[i, 'Url'].count('pdf')
        list.append(x)

        if x == 1:
            listPDForHTML.append('PDF')
        else:
            listPDForHTML.append('HTML or else')
    
    df2 = pd.DataFrame()
    df2['PDF or HTML'] = listPDForHTML
    df2['Count'] = list

    df2 = pd.DataFrame(df2['PDF or HTML'].value_counts().rename('Count'))

    return df2

print(countPDFResults(df))

# Variable 6: Top 10 questions with most approval in mean
def top10Questions(df):
    df2 = pd.DataFrame(df.groupby('Text')['Approve'].mean().sort_values(ascending=False))
    df2 = df2.head(10)

    return df2

print(top10Questions(df))

# Variable 7: Rebuplican vs Democrat Approval by Question
def repubVsDemocrat(df):
    df2 = pd.DataFrame(df.groupby('Text')[['Approve (Republican)', 'Approve (Democrat)']].mean())

    if df2['Approve (Republican)'].mean() > df2['Approve (Democrat)'].mean():
        df2['Winner'] = 'Republican'
    else:
        df2['Winner'] = 'Democrat'
        
    return df2

print(repubVsDemocrat(df))