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
mycursor.execute("CREATE DATABASE BranchDatabase") # Initialises Branch database

brdb = pymysql.connect(
    host = "localhost",
    user = "root",
    passwd= "root",
    database="BranchDatabase",
autocommit = True)

data = pd.read_excel('SNA_DATA.xlsx') # reads data off excel file


brcursor = brdb.cursor()

#Creates list of unique Branches
mycursor.execute("SELECT BRANCH FROM SIMPLEID")
branchlist =[]
for x in mycursor:
    branchlist.append(x[0])
branchlist = list(dict.fromkeys(branchlist)) #Drops duplicates from branchlist

def callidbranch(branch): # statement for calling list of ids who are at that branch
    return "SELECT ID FROM SIMPLEID WHERE BRANCH = " +"'" + branch +"'"

def Createbranchtable(branch): #statement for making a table of that branch
    return "CREATE TABLE " + branch + " (TargetID VARCHAR(50) PRIMARY KEY)"

def POPbranchTable(branch): #statment to insert rows into branch
    return "INSERT INTO " + branch + " (TargetID) VALUES(%s)"
count = 0

uniquetableidlist = []

badwords = ["-", "&", "(", ")", ",", "/"] #list of characters that will be ommited because they are invalid table names

for i in range(len(branchlist)):

    mycursor.execute((callidbranch(str(branchlist[i])))) #calls list of ids who are at that branch
    uniquebranchids = [] #initalises vector of  ids that for each branchlist[i]
    for x in mycursor:
        uniquebranchids.append(x[0]) #populates vector with list of people who are at that branch

    count = count +1
    print(count)
    print(branchlist[i])
    for t in range(len(badwords)):
        if badwords[t] in branchlist[i]: #Checks if invalid characters are in that branch name and ommits them
            temp = branchlist[i].replace(badwords[t],"_")
            branchlist[i] = temp
            """
    for y in range(len(badnames)):
        if badnames[y] in branchlist[i]:
            print('true')
            cool = branchlist[i].replace(bad[t],"_")
            branchlist[i] = cool
"""
    if "logged" in branchlist[i]: #If branchname is something like Jeff_McGrath_logged_on_at_4:20:00_am_with_fred as it sometimes is it will change it to "nan"
        branchlist[i] = "nan"
    x = str(branchlist[i]).split() #spaces are invalid in table names so it turns them into underscores
    tableidcreater = x[0]
    for j in range(1,len(x)):
        tableidcreater = tableidcreater + "_" + x[j]
    if "___" in tableidcreater: #If theere
        cool = tableidcreater.replace("___", "_")
        tableidcreater = cool

    print(tableidcreater)
    if tableidcreater in uniquetableidlist: #Checks if that branch id  is already in the list
        for j in range(len(uniquebranchids)):
            brcursor.execute(POPbranchTable(tableidcreater), (str(uniquebranchids[j])))
        print(uniquebranchids)


    else:
        uniquetableidlist.append(tableidcreater) #adds new branch id  to unique id  list
        brcursor.execute((Createbranchtable(str(tableidcreater)))) #creates table with that id name

        for j in range(len(uniquebranchids)):
            brcursor.execute(POPbranchTable(tableidcreater), (str(uniquebranchids[j]))) #populates table with unique ids

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