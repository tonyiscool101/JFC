import sqlite3
import pandas as pd
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
print(ID_list1)
conn = sqlite3.connect('Bigboy.db')


c = conn.cursor()
purchases = [('2006-03-28', 'BUY', 'IBM'),
             ('2006-04-05', 'BUY', 'MSFT'),
             ('2006-04-06', 'SELL', 'IBM'),]
c.execute('''CREATE TABLE IDList
(ID text, Branch text , Jobtitle text)''')
c.executemany('INSERT INTO IDList VALUES (?,?,?)', purchases)

#, Response text, Evenness real, Succession String text, NWL real