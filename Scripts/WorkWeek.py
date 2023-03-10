import pandas as pd
import numpy as np
from pandas import DataFrame as df

#replaces column heading names and turns excel file into a dataframe to be worked on
work_columns = ['EmployeeID', 'StAgtCd', 'InstallerName', 'Level3UserID', 'Name', 'ADDRESS1', 'SUITE', 'City', 'State', 'Zip', 'PHONE1', 'OFFICETYP', 'CloudName', 'WrkstationCount', 'HPM507XLANName', 'HP M507XLANCount', 'HP840G7Name', 'HP84G7Count', 'UPSBoxName', 'UPSBoxCount', 'HPG5USBCDockName', 'HPG5USBCDockCount', 'ReturnStockOnlyName', 'ReturnStockOnlyCount', 'InstallDate', 'InstallDuration']
workWeek = pd.read_excel("/home/swiggityyy/Desktop/test.xlsx", sheet_name="Sheet1")
df = pd.DataFrame(workWeek)
df.columns = work_columns

#combines address columns into one, seperates install date into date and time
df['Address'] = df['ADDRESS1'].astype(str) + ' ' + df['SUITE'].astype(str) + ' ' + df['City'].astype(str) + ' ' + df['State'].astype(str) + ' ' + df['Zip'].astype(str)
installDT = df["InstallDate"].astype(str).str.split(" ", expand=True).rename(columns={0:"Date", 1:"Time"})
df[["Date", "Time"]] = df["InstallDate"].astype(str).str.split(" ", expand=True)
df = df.drop(['InstallerName', 'Level3UserID', 'ADDRESS1', 'SUITE', 'City', 'State', 'Zip', 'OFFICETYP', 'CloudName', 'HPM507XLANName', 'HP840G7Name', 'UPSBoxName', 'HPG5USBCDockName', 'ReturnStockOnlyName', 'InstallDate'], axis=1)

#reorganizes columns and only keep the ones we're using adding allowance and miles columns
df.insert(7, 'miles', "1")
df.insert(8, 'allowance', "1")
df.insert(9, 'diff', "1")
df.insert(10, 'POC', "none")

df = df[['EmployeeID', 'StAgtCd', 'Name', 'PHONE1', 'Address', 'Date', 'Time', 'miles', 'allowance', 'diff', 'POC', 'WrkstationCount', 'HP M507XLANCount', 'HP84G7Count', 'UPSBoxCount', 'HPG5USBCDockCount', 'ReturnStockOnlyCount', 'InstallDuration']]
df.to_excel("/home/swiggityyy/Desktop/production.xlsx", sheet_name = "Sheet1", index=False)

print(df)
print("Pandas Version " + pd.__version__)

#Selenium


