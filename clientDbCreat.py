import sqlite3

db=sqlite3.connect('client.db')
cursor=db.cursor()

def creattable():
    cursor.execute("CREATE TABLE IF NOT EXISTS personnel(ID INTEGER,NAME TEXT,SURNAME TEXT,SSN INTEGER,PRIMARY KEY(ID))")
    db.commit()
def intserttable(data):
    cursor.execute("INSERT INTO personnel (NAME, SURNAME, SSN) VALUES(?,?,?)",data)

data1 = ["Isaac","Newton",12345678900]
data2=["Albert","Einstein",98765432100]
intserttable(data1)
intserttable(data2)
db.commit()