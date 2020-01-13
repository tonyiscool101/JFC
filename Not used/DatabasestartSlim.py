import pandas as pd
import csv
import numpy as np

# Read data & separate into senders and recipient lists
xls = pd.ExcelFile('SNA_DATA.xlsx')
data = pd.read_excel('SNA_DATA.xlsx')

# Create dataframes
df = xls.parse(xls.sheet_names[0])
df = df.drop_duplicates('Sender', keep='first')
df2 = xls.parse(xls.sheet_names[0])
df2 = df2.drop_duplicates('Recipient', keep='first')

# Create sender and recipent and its respective office & job title lists
senderboys= []
recipientboys = []

senderboys.append(df['Sender'].tolist()) #Gets list of all unique senders with office and title
senderboys.append(df['SendersOffice'].tolist())
senderboys.append(df['SendersJobTitle'].tolist())
recipientboys.append(df2['Recipient'].tolist())#Gets list of all unique recipients with office and title
recipientboys.append(df2['RecipientsOffice'].tolist())
recipientboys.append(df2['RecipientsJobTitle'].tolist())

# Drop any duplicates in recipient list
uniqueRecipientList = [n for n in zip(*recipientboys) if n not in zip(*senderboys)] #we dont know how this works but it drops all the recipientboys already in senderboys list
uniqueRecipientList2 = list(map(list, zip(*uniqueRecipientList))) #transposes unique recipient list for us to add to the senderboys list

# Transpose ID list from vector to a list into 3 columns
ID_list = np.hstack((senderboys,uniqueRecipientList2)) # adds senderboys and uniquerecipient list to get a list of all unique IDs in the email database; is 3 rows and 1800ish columns


ID_list1 = list(map(list, zip(*ID_list)))#transpose ID_list into 3 columns and 1800ish rows

with open("Slim_database.csv", mode="w", newline='') as f:
    fieldnames = ['ID', 'Branch', 'Jobtitle', 'Response', 'Evenness', 'Succession String',
                  'NWL']  # Initalises Field names
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for i in range(len(ID_list1)):

            writer.writerow({'ID': ID_list1[i][0], 'Branch': ID_list1[i][1], "Jobtitle": ID_list1[i][2]})