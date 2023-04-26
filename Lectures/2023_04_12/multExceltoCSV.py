'''
Code is used to convert multiple sheets in an excel file to csv files
'''

import pandas as pd

for i in range(0,7):                                                                                            #   sheet count from 0 to 6
    df = pd.read_excel("C:\\Users\\becke\\OfficePythonProgramming\\Lectures\\2023-04-12\\gradebook_tn.xlsx",i)  #   read excel file at sheet i
    df.to_csv(f"C:\\Users\\becke\\OfficePythonProgramming\\Lectures\\2023-04-12\\{i}.csv")                      #   write csv file with name i.csv

