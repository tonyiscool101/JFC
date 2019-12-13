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

bigList = []

responselist = []
for i in range(len(ID_list)):
        #(G, labels, edgeThicc,n_nodes) = makeNetwork(str(ID_list[i]), 'Local', data)

        # Find the responsiveness and store in  a string
        response = Responsiveness(str(ID_list[i]), 2, data)
        responselist.append(response)

bigList.append(ID_list)
bigList.append(responselist)

with open("employee_ID.csv", mode="w", newline='') as f:
        writer = csv.writer(f)
        writer.writerows(zip(*bigList))
