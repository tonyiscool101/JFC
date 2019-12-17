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
#mycursor.execute("CREATE DATABASE NWdatabase")

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
    IDlist.append(x)

AMOUNT = 1
def CreateNWtable(ID):
    return "CREATE TABLE " + ID + " (TargetID VARCHAR(50) PRIMARY KEY, Weight int)"

def POPNWLTable(ID):
    return "INSERT INTO" + ID + "(TargetID, Weight) VALUES(%s,%s)"
print(CreateNWtable(IDlist[0][0]))
#for i in range(len(IDlist)):
   # nwcursor.execute(CreateNWtable(str(IDlist[i][0])))
nwcursor.execute("INSERT INTO ")

for i in range(len(IDlist)):
    (G, labels, edgeThicc, n_nodes, NWL) = makeNetwork(str(IDlist[i][0]), 'Local', data)
    for j in range(len(NWL)):
        print(NWL[j])
        nwcursor.execute(POPNWLTable(IDlist[i][0]), (str(NWL[j][0]), NWL[j][2]))



