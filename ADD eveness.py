import pandas as pd
import csv
import numpy as np
from makeNetwork import makeNetwork
import mysql.connector
import pymysql
from evenness import evenness


db = pymysql.connect(
    host = "localhost",
    user = "root",
    passwd= "root",
    database="testdatabase"
)
data = pd.read_excel('SNA_DATA.xlsx')

mycursor = db.cursor()
IDs = ['61517f1dee116589b36c742cba2e32b5','16533b2009237712d34a5fe514d8fa31','0382e43c0a4a834cbba48c05fc219e41']
sql = "UPDATE SIMPLEID"
#mycursor.execute("ALTER TABLE SIMPLEID ADD COLUMN Evenness float")

evenesslist = [] # Caluculates evenness

for i in range(len(IDs)):
    evennesses = evenness(str(IDs[i]), data)
    print(str(evennesses))
    evenesslist.append(evennesses)

sql = "UPDATE Employee set DepartmentCode = 102 where id=121"
def sqlevennessstatement(ID,Eveness):
    return "UPDATE SIMPLEID set Evenness ="+str(Eveness) + " where ID = " + "'" + ID +"'"

for i in range(len(IDs)):
    mycursor.execute(sqlevennessstatement(str(IDs[i]),evenesslist[i]))
    db.commit()