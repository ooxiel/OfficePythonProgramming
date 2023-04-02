import pandas as pd

# convert into dataframe
df = pd.read_excel("C:\\Users\\becke\\OfficePythonProgramming\\Lectures\\2023_03_29\\testmap.xlsx",1)
print(df)

# convert into dictionary
dict = df.to_dict()
print(dict)
 