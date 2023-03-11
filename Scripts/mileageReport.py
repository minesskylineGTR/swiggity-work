import pandas as pd
import numpy as np
from pandas import DataFrame as df
from pandas.tseries.offsets import DateOffset
from collections import Counter
import collections
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-e", "--excelfile")
parser.add_argument("-s", "--sheet")
args = parser.parse_args()

mileage = pd.read_excel(args.excelfile, sheet_name=args.sheet)
df = pd.DataFrame(mileage)

df.insert(0, 'ExpenseEntry', '')

time = df['Time']
date = df['Date']
name = df['NAME']
id = df['StAgtCd']
miles = df['miles']
allowance = 5
mileage = print('Float Value =', miles)
#mileage = miles.astype(float)
diff = 'mileage - allowance'
print(diff)

# While there are duplicate time entries for 9am, sort through and fill out the textbox for them
numrows = df.shape[0]
i=0
df.sort_values(by='Date', inplace=True)
while i < numrows:
    
    

    #you just finished your first shift, now you gotta book it to the next agent's office
    if time == "'09:00:00":
         if date == date.shift(periods=1) and time.shift(periods=1) == "'13:00:00":
            i = i + 1 
            df.at[i, {df.ExpenseEntry}] = "{name}+' ('+{id}+') to '+""{name.shift(periods=1)}+'( '+id.shift(periods=1)"+')'' '+{miles}+' miles-'+{allowance}+' miles='+{diff}+' miles'
    #You're at your 1pm job, last one of the day. your next job doesn't start til tomorrow
    if time == "'13:00:00":
        if date != date.shift(periods=1) or time.shift(periods=1) == "'09:00:00":
            i = i + 1 
            df.at[i, df.ExpenseEntry] = "{name}+' ('+{id}+') to Home '+{miles}+' miles-'+{allowance}+' miles='+{diff}+' miles'"
    
    print(numrows)  
#'Home to John Doe (12-3456) 55 miles-15 miles=40 miles'
# '''
# while date.duplicated().any() == True:
    
#     countdown2 = Counter[time]
#     countdownTime1 = Counter('13:00:00')

#     if time.values() == "13:00:00":
#         print('Agent to Agent')
#         df.at[i, 'ExpenseEntry'] = ['test b']
   
#     if date.duplicated.any() == False:
#             print('same day. Agent to Home')
#             df.at[i, 'ExpenseEntry'] = ['test c']

#     i = i + 1
# #'John Doe (12-3456) to Home 55 miles-15 miles=40 miles'
   


df.to_excel('../../mileage.xlsx', sheet_name='Sheet1', index='False')
print(df)


#'=CONCAT'.upper() + '( "Home to ", E2, "(", D2, ") ", J2, "-", K2, "=", L2)' Home to Agent
#'=CONCAT'.upper() + '( E3, " to Home", "(", D3, ") ", J3, "-", K3, "=", L3)' Agent to Home

#for loop the unique count for the Dates column
#while the date value stays the same, create the expense sheet statement
#'Home to John Doe (12-3456) 55 miles-15 miles=40 miles'
#'John Doe (12-3456) to Home 55 miles-15 miles=40 miles'
#Reference columns for relevant information
#Only include the 15 miles until 15 miles are up then switch it to zero / create a counter
#sum up total miles driven or 3rd party maps API it
#write final results onto an excel sheet for copypasta
