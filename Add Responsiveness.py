import pandas as pd
import csv
import numpy as np
from makeNetwork import makeNetwork
import pymysql
from hiPoIdentifier import Responsiveness



db = pymysql.connect(
    host = "localhost",
    user = "root",
    passwd= "root",
    database="testdatabase",
autocommit = True)
data = pd.read_excel('SNA_DATA.xlsx')

IDs = ['0007f30bba2eef3df091a632e638320d',
'001ad6cfbf0481b2d29880161cbb3936']



responselist =[]

mycursor = db.cursor()

mycursor.execute("SELECT ID FROM SIMPLEID")
IDlist =[]
for x in mycursor:
    IDlist.append(x[0])

mycursor.execute("ALTER TABLE SIMPLEID ADD COLUMN Response float")
def returnresponse(ID):
    return "SELECT Response FROM SIMPLEID WHERE ID = " + "'" + ID + "'"
mycursor.execute(returnresponse(IDlist[3]))
for x in mycursor:
    print(x)
def sqlevennessstatement(ID, Eveness):
    return "UPDATE SIMPLEID set Response =" + str(Eveness) + " where ID = " + "'" + ID + "'"


joe =0
for i in range(len(IDlist)):
        mycursor.execute(returnresponse((IDlist[i])))
        for x in mycursor:
            if x[0] == None:
                print('caluculating '+ str(IDlist[i] + ' responsiveness'))
                response = Responsiveness(str(IDlist[i]), 2, data)
                responselist.append(response)
                mycursor.execute(sqlevennessstatement(str(IDlist[i]), responselist[i]))
            else:
                print(str(IDlist[i] + " responsiveness already calculated"))
                response = 0
                responselist.append(response)