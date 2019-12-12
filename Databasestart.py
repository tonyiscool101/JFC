# Hey now hey now don't dream its over.

import pandas as pd
import numpy as np

data = pd.read_excel('SNA_DATA.xlsx')

senderlist = data['Sender'].unique().tolist()
recipientlist = data['Recipient'].unique().tolist()

uniqueRecipientList = [n for n in recipientlist if n not in senderlist]
ID_list = senderlist + uniqueRecipientList