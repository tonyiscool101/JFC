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
mycursor.execute("CREATE DATABASE BranchDatabase")

brdb = pymysql.connect(
    host = "localhost",
    user = "root",
    passwd= "root",
    database="BranchDatabase",
autocommit = True)

data = pd.read_excel('SNA_DATA.xlsx')


brcursor = brdb.cursor()

#Creates list of unique Branches
mycursor.execute("SELECT BRANCH FROM SIMPLEID")
branchlist =[]
for x in mycursor:
    branchlist.append(x[0])
branchlist = list(dict.fromkeys(branchlist))

def callidbranch(branch):
    return "SELECT ID FROM SIMPLEID WHERE BRANCH = " +"'" + branch +"'"

def Createbranchtable(branch):
    return "CREATE TABLE " + branch + " (TargetID VARCHAR(50) PRIMARY KEY)"

def POPbranchTable(ID):
    return "INSERT INTO " + ID + " (TargetID) VALUES(%s)"

count = 0

uniquetableidlist = []

badwords = ["-", "&", "(", ")", ",", "/"]
badnames = ["JeffMcGrath", "MCIreland"]

for i in range(len(branchlist)):

    mycursor.execute((callidbranch(str(branchlist[i]))))
    uniquebranchids = []
    for x in mycursor:
        uniquebranchids.append(x[0])

    count = count +1
    print(count)
    print(branchlist[i])
    for t in range(len(badwords)):
        if badwords[t] in branchlist[i]:
            cool = branchlist[i].replace(badwords[t],"_")
            branchlist[i] = cool
            """
    for y in range(len(badnames)):
        if badnames[y] in branchlist[i]:
            print('true')
            cool = branchlist[i].replace(bad[t],"_")
            branchlist[i] = cool
"""
    if "logged" in branchlist[i]:
        branchlist[i] = "nan"
    x = str(branchlist[i]).split()
    tableidcreater = x[0]
    for j in range(1,len(x)):
        tableidcreater = tableidcreater + "_" + x[j]
    if "___" in tableidcreater:
        cool = tableidcreater.replace("___", "_")
        tableidcreater = cool


    if tableidcreater in uniquetableidlist:
        for j in range(len(uniquebranchids)):
            brcursor.execute(POPbranchTable(tableidcreater), (str(uniquebranchids[j])))
            print(tableidcreater + "HHEEEHEHEHHE")


    else:
        uniquetableidlist.append(tableidcreater)
        brcursor.execute((Createbranchtable(str(tableidcreater))))

        for j in range(len(uniquebranchids)):
            brcursor.execute(POPbranchTable(tableidcreater), (str(uniquebranchids[j])))

"""
    print(branchlist[i])
    x = str(branchlist[i]).split()
    tableidcreater = x[0]
    length=[]
    for j in range(len(x)):
        if "-" in x[j]:
            l = x[j].replace("-","_")
            length.append(l)
            tableidcreater = length[0]
"""