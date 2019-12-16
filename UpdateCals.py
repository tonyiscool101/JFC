import pandas as pd
import csv
import numpy as np
from makeNetwork import makeNetwork
from highCostIdentifier import highCostIdentifier
from hiPoIdentifier import Responsiveness
from evenness import evenness
from successionPlanner import successionPlanner
from tempfile import NamedTemporaryFile
import shutil

data = pd.read_excel('SNA_DATA.xlsx')
filename = 'Slim_database.csv'
diledame = 'Slim_databasecopy.csv'
tempfile = NamedTemporaryFile(mode='w', delete=False)

ID = ['61517f1dee116589b36c742cba2e32b5','16533b2009237712d34a5fe514d8fa31','0382e43c0a4a834cbba48c05fc219e41']
print(len(ID))

fields = ['ID', 'Branch', 'Jobtitle', 'Response', 'Evenness', 'Succession String','NWL']


responselist = [] #initialises a bunch of matrices for us to caluculate a bunch of data
evenesslist = [] # Caluculates evenness
succstringlist = [] #String of possible successor IDS
candidates = 4
NWLlist = [] #List of Nodeweights
IDs_Calculated = 2
for i in range(len(ID)):
        (G, labels, edgeThicc,n_nodes,NWL) = makeNetwork(str(ID[i]), 'Local', data)
        NWLlist.append(NWL)
        print(NWLlist)
        # Find the responsiveness and store in  a string
        response = Responsiveness(str(ID[i]), 2, data)
        responselist.append(response)
        print(response)

        evennesses= evenness(str(ID[i]), data)
        print(str(evennesses))
        evenesslist.append(evennesses)

with open(filename, 'r') as csvfile, tempfile:
            reader = csv.DictReader(csvfile, fieldnames=fields)
            writer = csv.DictWriter(tempfile, lineterminator='\n', fieldnames=fields)
            for row in reader:
                for i in range(len(ID)):
                    if row['ID'] == str(ID[i]):
                            row['Response'], row['Evenness'], row['NWL'] = responselist[i],evenesslist[i], NWLlist[i]
                    row = {'ID': row['ID'], 'Branch': row['Branch'], 'Jobtitle': row['Jobtitle'],
                            'Response': row['Response'], 'Evenness': row['Evenness'], 'NWL': row['NWL']}


                writer.writerow(row)


shutil.move(tempfile.name, diledame)


