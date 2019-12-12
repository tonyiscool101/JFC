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

with open('employee_file.csv', mode='w') as employee_file:
    fieldnames = ['ID_list']
    writer.writeheader()
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for i in range len(ID_list)
    employee_writer.writerow([ID_list])


