import sqlite3
import random
import time
import datetime


con = sqlite3.connect("satilikdataabase.db")

cursor = con.cursor()


def tablo():
    cursor.execute("CREATE TABLE IF NOT EXISTS byneverkoo (username TEXT,password TEXT)")
def deger():
    cursor.execute("INSERT INTO byneverkoo VALUES ('admin','pass')")

tablo()
deger()

con = sqlite3.connect("satilikdaatabase.sb")


cursor = con.cursor()

def tabloolustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS Tablo1 (zaman REAL, tarih TEXT,anahtarkelime TEXT,deger REAL)")

def rastgeledegerekle():
    zaman = time.time()
    tarih = str(datetime.datetime.fromtimestamp(zaman).strftime('%Y-%m-%d $H:$M:$S'))
    anahtarkelime = "python sqlite3"
    deger =random.randrange(1,10)
    cursor.execute("INSERT INTO Tablo1 (zaman,tarih,anahtarkelime,deger)VALUES (?,?,?,?)",(zaman,tarih,anahtarkelime,deger))
    con.commit()

tabloolustur()

i=0
while (i < 10):
    rastgeledegerekle()
    time.sleep(1)
    i+=1

def degerial() -> object:
    cursor.execute("SELECT * FROM Tablo1")
    data = cursor.fetchall()
    for i in data:
        print(i)

con.close()

