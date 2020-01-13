# Hey now hey now don't dream its over.

import pandas as pd
import numpy as np
from evenness import evenness
from makeNetwork import makeNetwork
from highCostIdentifier import highCostIdentifier
from hiPoIdentifier import Responsiveness
import csv

data = pd.read_excel('SNA_DATA.xlsx')

senderlist = data['Sender'].unique().tolist()
recipientlist = data['Recipient'].unique().tolist()

uniqueRecipientList = [n for n in recipientlist if n not in senderlist]
ID_list = senderlist + uniqueRecipientList

print(np.shape(uniqueRecipientList))
print(np.shape(senderlist))
print(np.shape(ID_list))

bigList = []

responselist = []
for i in range(2):
        (G, labels, edgeThicc,n_nodes,NWL) = makeNetwork(str(ID_list[i]), 'Local', data)
        print(type(NWL))
        print(NWL)
        # Find the responsiveness and store in  a string
        response = Responsiveness(str(ID_list[i]), 2, data)
        responselist.append(response)
        print(response)

bigList.append(ID_list)
bigList.append(responselist)
ID_list1 = np.transpose(ID_list)
print(ID_list1)
with open("employee_ID.csv", mode="w", newline='') as f:
        fieldnames = ['ID','Response']
        writer = csv.DictWriter(f,fieldnames=fieldnames)
        writer.writeheader()

        for i in range(len(responselist)):
                writer.writerow({'ID': ID_list1[i],'Response': responselist[i]})
