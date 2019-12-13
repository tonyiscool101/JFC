# Hey now hey now don't dream its over.

import pandas as pd
import csv

xls = pd.ExcelFile('SNA_DATA.xlsx')
df = xls.parse(xls.sheet_names[0])
df = df.drop_duplicates('Sender', keep='first')

senderlist = df['Sender'].tolist()
officelist = df['SendersOffice'].tolist()

bigList = []

bigList.append(senderlist) #Add senderlist to big list
bigList.append(officelist)

with open("midman2.csv", mode="w", newline='') as f:
        writer = csv.writer(f)
        writer.writerows(zip(*bigList))
