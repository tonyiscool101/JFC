import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import heapq, operator, pprint, time, matplotlib, community
from modularity import modularity
import numpy as np
from simrank import simrank
import collections as cl
from makeNetwork import makeNetwork
import pymysql



db = pymysql.connect(
    host = "localhost",
    user = "root",
    passwd= "root",
    database="testdatabase",
autocommit = True)
data = pd.read_excel('SNA_DATA.xlsx')

ID = ['7db963d60e924dc7681152dd9c6be669']

data = pd.read_excel('SNA_DATA.xlsx')

mycursor = db.cursor()

mycursor.execute("SELECT ID FROM SIMPLEID")
IDlist =[]
for x in mycursor:
    IDlist.append(x[0])

mycursor.execute("ALTER TABLE SIMPLEID ADD COLUMN BetweenessCent float")
mycursor.execute("ALTER TABLE SIMPLEID ADD COLUMN ClosnessCent float")


def reccotest(G):
    closCent = nx.closeness_centrality(G, distance='distance')
    betCent = nx.betweenness_centrality(G, normalized=True, endpoints=True, weight='weight')

    # expensive conversion to list, should be replaced
    closCentValues = list(closCent.values())
    betCentValues = list(betCent.values())

    closCentValues.sort(reverse=True)
    betCentValues.sort(reverse=True)


    return (closCentValues,betCentValues, betCent,closCent)

def sqlbetweenesstatement(ID, Eveness):
    return "UPDATE SIMPLEID set BetweenessCent =" + str(Eveness) + " where ID = " + "'" + ID + "'"

def sqlclosnesstatement(ID, Eveness):
    return "UPDATE SIMPLEID set ClosnessCent =" + str(Eveness) + " where ID = " + "'" + ID + "'"

print('Calculating Network')

bestboys = []

for i in range(len(IDlist)):
    print('network calculated')
    (G, labels, edgeThicc, n_nodes, NWL) = makeNetwork(str(IDlist[i]), 'dskjfa', data)
    print('Calculating Closeness and Betweeness Centrality')
    (closCentValues, betCentValues, betCent, closCent) = reccotest(G)
    cutOff1 = 85
    target = str(IDlist[i])
    if closCent[target] > np.percentile(closCentValues, cutOff1) and betCent[target] > np.percentile(betCentValues, cutOff1):
        bill = 'invalid'
        bestboys.append(target)
    else:
        bill = 'valid'
        print(NWL)
        print(betCent)
        print(closCent)
    print(bill)

print(bestboys)
