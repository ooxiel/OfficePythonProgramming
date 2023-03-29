import pandas as pd

# convert into dataframe
df = pd.read_excel("/workspaces/OfficePythonProgramming/Lectures/2023_03_29/testmap.xlsx")
print(df)


# convert into dictionary
dict = df.to_dict()
print(dict)
