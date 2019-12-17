import mysql.connector
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd= "root",
    database="testdatabase"
)
mycursor = db.cursor()
#mycursor.execute("CREATE TABLE SIMPLEID (ID VARCHAR(50), Branch VARCHAR(50), Jobtitle VARCHAR(50), PERSONID int PRIMARY KEY AUTO_INCREMENT")
mycursor.execute("INSERT INTO IDLIST (ID, Branch,Jobtitle,Response,Evenness) VALUES (%s,%s,%s,%s,%s)", ("d7e68a0d48f04fbaa78dbc6ed7a28e9e","North Sydney - Mount Street","DIGITAL ENGINEER LEADZ",0.71,0.84))
mycursor.execute("ALTER TABLE IDLIST CHANGE Evenness Evenness int")
#mycursor.execute("DESCRIBE IDLIST")
#mycursor.execute("DESCRIBE IDLIST")
db.commit()


mycursor.execute("SELECT * FROM IDLIST")
for x in mycursor:
  print(x)