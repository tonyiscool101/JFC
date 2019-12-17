import pandas as pd
import csv
import numpy as np
from makeNetwork import makeNetwork
import mysql.connector
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

#mycursor.execute("ALTER TABLE SIMPLEID ADD COLUMN Response int")

for i in range(len(IDs)):
        response = Responsiveness(str(IDs[i]), 2, data)
        responselist.append(response)

def sqlevennessstatement(ID, Eveness):
            return "UPDATE SIMPLEID set Response =" + str(Eveness) + " where ID = " + "'" + ID + "'"

for i in range(len(IDs)):
    mycursor.execute(sqlevennessstatement(str(IDs[i]),responselist[i]))