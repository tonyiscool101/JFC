# Hey now hey now don't dream its over.

import pandas as pd
import csv
import numpy as np
from makeNetwork import makeNetwork
from highCostIdentifier import highCostIdentifier
from hiPoIdentifier import Responsiveness

# Read data & separate into senders and recipient lists
xls = pd.ExcelFile('SNA_DATA.xlsx')
data = pd.read_excel('SNA_DATA.xlsx')

df = xls.parse(xls.sheet_names[0])
df = df.drop_duplicates('Sender', keep='first')
df2 = xls.parse(xls.sheet_names[0])
df2 = df2.drop_duplicates('Recipient', keep='first')

# Create sender and recipent and its respective office & job title lists
senderboys= []
recipientboth = []

senderboys.append(df['Sender'].tolist())
senderboys.append(df['SendersOffice'].tolist())
senderboys.append(df['SendersJobTitle'].tolist())
recipientboth.append(df2['Recipient'].tolist())
recipientboth.append(df2['RecipientsOffice'].tolist())
recipientboth.append(df2['RecipientsJobTitle'].tolist())

# Drop any duplicates in recipient list
uniqueRecipientList = [n for n in zip(*recipientboth) if n not in zip(*senderboys)]
uniqueRecipientList2 = list(map(list, zip(*uniqueRecipientList)))

# Transpose ID list from vector to a list into 3 columns
ID_list = np.hstack((senderboys,uniqueRecipientList2))

bigList = []
bigList.append(ID_list) #Add senderlist to big list

ID_list1 = list(map(list, zip(*ID_list)))

print(np.shape(ID_list1))
responselist = []
for i in range(2):
        #(G, labels, edgeThicc,n_nodes) = makeNetwork(str(ID_list[i]), 'Local', data)

        # Find the responsiveness and store in  a string
        response = Responsiveness(str(ID_list1[i][0]), 2, data)
        responselist.append(response)
        print(response)

for i in range

# Open a separate new csv file as the database of employees
with open("Employee_database.csv", mode="w", newline='') as f:
        fieldnames = ['ID', 'Branch', 'Jobtitle', 'Response']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(len(ID_list1)):
                if i<len(responselist): #Delete if statement after make responsiveness faster
                        writer.writerow({'ID': ID_list1[i][0],'Branch': ID_list1[i][1], "Jobtitle" : ID_list1[i][2],'Response': responselist[i]})
                else:
                        writer.writerow({'ID': ID_list1[i][0], 'Branch': ID_list1[i][1], "Jobtitle": ID_list1[i][2]})



