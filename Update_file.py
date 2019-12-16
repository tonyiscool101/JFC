from tempfile import NamedTemporaryFile
import shutil
import csv

filename = 'Employee_database.csv'
diledame = 'Employee_database1.csv'
tempfile = NamedTemporaryFile(mode='w', delete=False)

fields = ['ID', 'Branch', 'Jobtitle', 'Response', 'Evenness', 'Succession String']

with open(filename, 'r') as csvfile, tempfile:
    reader = csv.DictReader(csvfile, fieldnames=fields)
    writer = csv.DictWriter(tempfile,  lineterminator='\n', fieldnames=fields)
    for row in reader:
        if row['ID'] == str('038a87bac7a9bdb087028b0020374ce3'):
            row['Branch'], row['Jobtitle'] = 'bpo', 'sda'
        row = {'ID': row['ID'], 'Branch': row['Branch'], 'Jobtitle': row['Jobtitle'],'Response':row['Response'], 'Evenness':row['Evenness'], 'Succession String': row['Succession String']}
        print(row)
        writer.writerow(row)

shutil.move(tempfile.name, diledame)