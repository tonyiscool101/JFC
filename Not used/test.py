import numpy as np
import pandas as pd

sna=pd.read_csv('SNAdata.csv', sep=',',dtype=str)#,header=None)
file1 = open("a.json","w")

file1.write('{\n')
file1.write('\t"nodes": [\n')

IDlist = []


for i in range(len(sna)):
    if sna['SendersOffice'][i] not in IDlist:
        IDlist.append(sna['SendersOffice'][i])
for i in range(len(sna)):
    if sna['RecipientsOffice'][i] not in IDlist:
        IDlist.append(sna['RecipientsOffice'][i])

for i in range(len(IDlist)):
    file1.write('  \t{"name": "')
    file1.write(str(IDlist[i]))
    file1.write('", "group": 1},\n')

file1.write('\t],\n')
file1.write('\t"links": [')

for i in range(len(sna)):
    file1.write('  \t{"source": ')
    for j in range(len(IDlist)):
        if(IDlist[j] == sna['SendersOffice'][i]):
            file1.write(str(j))
            break

    file1.write(', "target": ')
    for j in range(len(IDlist)):
        if(IDlist[j] == sna['RecipientsOffice'][i]):
            file1.write(str(j))
            break
    file1.write(', "weight": 1')
    file1.write('},\n')

file1.write('\t]\n')
file1.write('}')
