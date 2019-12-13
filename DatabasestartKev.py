# Hey now hey now don't dream its over.

import pandas as pd
import csv
import numpy as np

xls = pd.ExcelFile('SNA_DATA.xlsx')
df = xls.parse(xls.sheet_names[0])
df = df.drop_duplicates('Sender', keep='first')
df2 = xls.parse(xls.sheet_names[0])
df2 = df2.drop_duplicates('Recipient', keep='first')

senderlist = df['Sender'].tolist()
officelist = df['SendersOffice'].tolist()
senderboys= []
recipientlist = df2['Recipient'].tolist()
recipientoffice = df2['RecipientsOffice'].tolist()
recipientboth = []

senderboys.append(df['Sender'].tolist())
senderboys.append(df['SendersOffice'].tolist())
recipientboth.append(df2['Recipient'].tolist())
recipientboth.append(df2['RecipientsOffice'].tolist())

uniqueRecipientList = [n for n in zip(*recipientboth) if n not in zip(*senderboys)]
uniqueRecipientList2 = list(map(list, zip(*uniqueRecipientList)))

ID_list = np.hstack((senderboys,uniqueRecipientList2))

bigList = []
bigList.append(ID_list) #Add senderlist to big list

with open("midman2.csv", mode="w", newline='') as f:
        writer = csv.writer(f)
        writer.writerows(zip(*ID_list))


