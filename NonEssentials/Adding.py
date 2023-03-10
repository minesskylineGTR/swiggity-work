import pandas as pd
import numpy as np
from pandas import DataFrame as df

# dictionaries/hashmaps are fucking useful. Learn it!


# clean excel sheet - delete unneccessary columns/combine addresses - save file
workWeek = pd.read_excel("../test.xlsx", sheet_name = "Sheet1")
df = pd.DataFrame(workWeek)
df['Address'] = df['ADDRESS 1'].astype(str) + ' ' + df['SUITE'].astype(str) + ' ' + df['City'].astype(str) + ' ' + df['State'].astype(str) + ' ' + df['Zip'].astype(str)
df = df.drop(df.columns[[2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 14, 16, 18, 20, 22]], axis=1)

installDT = df["InstallDate"].astype(str).str.split(" ", expand=True).rename(columns={0:"Date", 1:"Time"})
df[["Date", "Time"]] = df["InstallDate"].astype(str).str.split(" ", expand=True)
df = df.drop(df.columns[[3]], axis=1)
df.to_excel("../test.xlsx", sheet_name = "Sheet1", index=False)

print(df)
print("Pandas Version " + pd.__version__)

# automate downloading the email with excel - IMAP or POP3 Python Library
# incorporate map API to calculate distance
# pull data from certain cells
# enter data automatically into certain sites
# Create a for loop to print out column title strings to create a dictionary?
# How does pandas load columns? How does it work?
# Have python create a new xlsx and write over ONLY the data you need vs trying to fix the one you're given