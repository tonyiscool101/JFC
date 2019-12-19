import pandas as pd
import numpy as np
import pymysql
from makeNetwork import makeNetwork
db = pymysql.connect(
    host = "localhost",
    user = "root",
    passwd= "root",
    database="testdatabase",
autocommit = True)

mycursor = db.cursor()
mycursor.execute("CREATE DATABASE NWdatabase")

nwdb = pymysql.connect(
    host = "localhost",
    user = "root",
    passwd= "root",
    database="NWdatabase",
autocommit = True)

data = pd.read_excel('SNA_DATA.xlsx')


nwcursor = nwdb.cursor()

mycursor.execute("SELECT ID FROM SIMPLEID")
IDlist =[]
for x in mycursor:
    IDlist.append(x[0])
print(IDlist)

def CreateNWtable(ID):
    return "CREATE TABLE TABLE" + ID + " (TargetID VARCHAR(50) PRIMARY KEY, Weight int)"

def POPNWLTable(ID):
    return "INSERT INTO TABLE" + ID + " (TargetID, Weight) VALUES(%s,%s)"

print(CreateNWtable(IDlist[0]))
print((POPNWLTable(IDlist[0])))

for i in range(len(IDlist)):
    nwcursor.execute(CreateNWtable(str(IDlist[i])))
    (G, labels, edgeThicc, n_nodes, NWL) = makeNetwork(str(IDlist[i]), 'Local', data)
    print(NWL)
    for j in range(len(NWL)):
        print(NWL[j])
        if str(IDlist[i]) == (str(NWL[j][0])): #Nodeweightlist contains messages going both in and out of target node; this code selects the node that is not the target
                nwcursor.execute(POPNWLTable(IDlist[i]), (str(NWL[j][1]), NWL[j][2])) # This code also adds duplicate edges together and combines them into one weight
        else:
                nwcursor.execute(POPNWLTable(IDlist[i]), (str(NWL[j][0]), NWL[j][2]))


