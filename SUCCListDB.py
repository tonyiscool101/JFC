import pandas as pd
import numpy as np
import pymysql
from successionPlanner import successionPlanner
db = pymysql.connect(
    host = "localhost",
    user = "root",
    passwd= "root",
    database="testdatabase",
autocommit = True)

mycursor = db.cursor()
mycursor.execute("CREATE DATABASE SLDB") #creates NW database

SCdb = pymysql.connect(
    host = "localhost",
    user = "root",
    passwd= "root",
    database="SLDB",
autocommit = True)

data = pd.read_excel('SNA_DATA.xlsx')


sccursor = SCdb.cursor()

#Calls list of unique IDs

mycursor.execute("SELECT ID FROM SIMPLEID")
IDlist =[]
for x in mycursor:
    IDlist.append(x[0])
print(IDlist)

def CreateNWtable(ID): #statement for making a table of that id (the nw is added because for some reason some id strings were unable to be made into table names directly; to fix this we added nw before all the ids as explained above)
    return "CREATE TABLE sc" + ID + " (Candidate1 varchar(100), Candidate2 varchar(100), Candidate3 varchar(100) )"

def POPNWLTable(ID):#statment to insert rows into network list
    return "INSERT INTO sc" + ID + " (Candidate1, Candidate2, Candidate3) VALUES(%s,%s,%s)"

print(CreateNWtable(IDlist[0]))

candidates = 4

for i in range(len(IDlist)):
    sccursor.execute(CreateNWtable(str(IDlist[i]))) #Creates table
    (succCandidates, succLabels) = successionPlanner(str(IDlist[i]), data, candidates)
    print(POPNWLTable(IDlist[i]), str(succCandidates[0][0]), str(succCandidates[1][0]), str(succCandidates[2][0]))

    sccursor.execute(POPNWLTable(IDlist[i]), (str(succCandidates[0][0]), str(succCandidates[1][0]), str(succCandidates[2][0])))

