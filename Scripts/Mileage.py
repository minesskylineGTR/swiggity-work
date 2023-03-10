import pandas as pd
import numpy as np
from pandas import DataFrame as df
from pandas.tseries.offsets import DateOffset
import sys

mileage = pd.read_excel('/home/swiggityyy/Desktop/production.xlsx', sheet_name='Sheet1')

df = pd.DataFrame(mileage)

df.insert(0, 'ExpenseEntry', '1')
df.insert(0, 'Later', '')
df.insert(0, 'Earlier', '')
df.insert(0, 'LaterID', '')

df['Later'] = df['Time'].bfill().shift(-1)
df['Earlier'] = df['Time'].bfill().shift(+1)
df['LaterAgent'] = df['Name'].bfill().shift(-1)
df['LaterID'] = df['StAgtCd'].bfill().shift(-1)

for row in df.itertuples(index=False):
    allowance = 15
    
    if row.Time == '09:00:00':
        print(f'Home to {row.Name} ({row.StAgtCd}) {row.miles} miles - {allowance} miles = {row.diff}')
    
    if row.Time == '09:00:00':
        if row.Later == '13:00:00':
            print(f'{row.Name} ({row.StAgtCd}) to {row.LaterAgent} ({row.LaterID}) {row.miles} miles - {allowance} miles = {row.diff}')

    if row.Time == '13:00:00':
        print(f'{row.Name} ({row.StAgtCd}) to Home {row.miles} miles - {allowance} miles = {row.diff}')
    
    df.sort_values(by=['Date', 'Time'])










#This works, but returns only a print statement
# for row in df.itertuples(index=False):
#     allowance = 15
#     print('Home to', row.Name, '('+row.StAgtCd+')', row.miles, 'miles -',allowance, 'miles =', row.diff)
# Home to John Doe (12-3456) 55 miles-15 miles=40 miles'


# row = lambda a : a + 10
# print(row(5))

# time = df.loc[row, 'Time']
# date = df.loc[row, 'Date']
# name = df.loc[row, 'Name']
# id = df.loc[row, 'StAgtCd']
# miles = df.loc[row, 'miles']
# diff = df.loc[row, 'diff']

# for row in df.itertuples(index=False):
#     allowance = 15
#     df.at[row, 'ExpenseEntry'] = f"Home to {name} ({id}) {miles} miles - {allowance} miles = {diff}"
#     return
# Home to John Doe (12-3456) 55 miles-15 miles=40 miles'








































# import pandas as pd
# import numpy as np
# from pandas import DataFrame as df
# from pandas.tseries.offsets import DateOffset
# from collections import Counter
# import collections

# mileage = pd.read_excel('/home/swiggityyy/Desktop/production.xlsx', sheet_name='Sheet1')

# df = pd.DataFrame(mileage)

# df.insert(0, 'ExpenseEntry', '1')

# """ df.astype({'miles': 'float'}).dtypes
# df.astype({'allowance': 'float'}).dtypes

# expense = df.loc[:, 'ExpenseEntry']
# time = df.loc[:, 'Time']
# date = df.loc[:, 'Date']
# name = df.loc[:, 'Name']
# id = df.loc[:, 'StAgtCd']
# miles = df.loc[:, 'miles']
# allowance = df.loc[:, 'allowance']
# diff = miles - allowance
# print(diff)

# # While there are duplicate time entries for 9am, sort through and fill out the textbox for them
# df.sort_values(by='Date', inplace=True)



# today   = (df['Date'])
# yesterday = (df['Date']).shift(periods=-1)
# tomorrow = (df['Date']).shift(periods=1)

# curTime = (df['Time'])
# nxtTime = (df['Time']).shift(periods=1)"""


# for rows in df.index():
#     allowance = 15
#     print('Home to', df.Name, '('+ df.StAgtCd+')', df.miles)# 'miles -', allowance, 'miles =', df.diff, 'miles')






# #shit_df = pd.DataFrame(shit, columns='shit', index=['Home to', df.Name, '('+ df.StAgtCd+')', df.miles, 'miles -', allowance, 'miles =', df.diff, 'miles'])

#     #print('Home to', df.Name, '('+ df.StAgtCd+')', df.miles, 'miles -'), allowance, 'miles =', df.diff, 'miles')
#     # print("Home to", row[df.Name],'(', row[df.StAgtCd],')', row[df.miles], 'miles- ', row[df.allowance], 'miles=', row[df.diff], 'miles')
#     # Home to John Doe (12-3456) 55 miles-15 miles=40 miles'
#     # #first trip of the day 9am, next one on the list has the same date, but is scheduled for 1pm    if time is "'09:00:00":
#     # if df[today != yesterday]:
#     #     if curTime == "'09:00:00":
#     #         expense = "'Home to '+{name}+' ('+{id}+') '+{miles}+' miles-'+{allowance}+' miles='+{diff}+'miles']"

#     # #you just finished your first shift, now you gotta book it to the next agent's office
#     # if df[today == tomorrow]:
#     #     if df[today != yesterday]:
#     #         if df[curTime == "'09:00:00"]:
#     #             if nxtTime == "'13:00:00":
#     #                 expense = "{name}+' ('+{id}+') to '+""{name.shift(periods=1)}+'( '+id.shift(periods=1)"+')'' '+{miles}+' miles-'+{allowance}+' miles='+{diff}+' miles'

#     # #You're at your 1pm job, last one of the day. your next job doesn't start til tomorrow
#     #     if df[today != tomorrow]:
#     #         if df[today == yesterday]:
#     #             if df[curTime == "'13:00:00"]:    
#     #                 expense = "{name}+' ('+{id}+') to Home '+{miles}+' miles-'+{allowance}+' miles='+{diff}+' miles'"

# #print(df['ExpenseEntry'].to_string(index=False))
# #df.to_excel('../../../mileage.xlsx', sheet_name='Sheet1', index='False')
# #print(df)

# # '''
# # while date.duplicated().any() == True:
    
# #     countdown2 = Counter[time]
# #     countdownTime1 = Counter('13:00:00')

# #     if time.values() == "13:00:00":
# #         print('Agent to Agent')
# #         df.at[i, 'ExpenseEntry'] = ['test b']
   
# #     if date.duplicated.any() == False:
# #             print('same day. Agent to Home')
# #             df.at[i, 'ExpenseEntry'] = ['test c']

# #     i = i + 1
# # #'John Doe (12-3456) to Home 55 miles-15 miles=40 miles'

# #'=CONCAT'.upper() + '( "Home to ", E2, "(", D2, ") ", J2, "-", K2, "=", L2)' Home to Agent
# #'=CONCAT'.upper() + '( E3, " to Home", "(", D3, ") ", J3, "-", K3, "=", L3)' Agent to Home

# #for loop the unique count for the Dates column
# #while the date value stays the same, create the expense sheet statement
# #'Home to John Doe (12-3456) 55 miles-15 miles=40 miles'
# #'John Doe (12-3456) to Home 55 miles-15 miles=40 miles'
# #Reference columns for relevant information
# #Only include the 15 miles until 15 miles are up then switch it to zero / create a counter
# #sum up total miles driven or 3rd party maps API it
# #write final results onto an excel sheet for copypasta