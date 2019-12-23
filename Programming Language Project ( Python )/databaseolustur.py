import sqlite3

dataBase = sqlite3.connect('davaBilgiSistemi.db')
print("Data Based Opened")

def CreateUyeOl():
    dataBase.execute('''
    CREATE TABLE IF NOT EXISTS uyeOl(
    TCNO TEXT NOT NULL PRIMARY KEY,
    Name TEXT NOT NULL,
    Surname TEXT NOT NULL,
    sifre TEXT NOT NULL,
    email TEXT,
    cinsiyet TEXT,
    telefon TEXT
    )''')


def CreateDavalar():
    dataBase.execute('''
        CREATE TABLE IF NOT EXISTS Davalar(
        DavaID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        DavaciTC TEXT NOT NULL,
        DavaliTC TEXT NOT NULL,
        Detaylar TEXT,
        DavaAdi TEXT NOT NULL
    )''')

def insertUyeOl(TCNO,Name,Surname,sifre,email,cinsiyet,telefon):
    dataBase.execute('''
    INSERT INTO uyeOl(TCNO,Name,Surname,sifre,email,cinsiyet,telefon) VALUES(?,?,?,?,?,?,?)    
    ''',( TCNO,Name,Surname,sifre,email,cinsiyet,telefon))
    dataBase.commit()

def insertDavalar(DavaciTC,DavaliTC,Detaylar,DavaAdi):
    dataBase.execute('''
    INSERT INTO Davalar(DavaciTC,DavaliTC,Detaylar,DavaAdi) VALUES(?,?,?,?)    
    ''', (DavaciTC,DavaliTC,Detaylar,DavaAdi))
    dataBase.commit()

#CreateDavalar()
#CreateUyeOl()

#insertUyeOl("134","Recep","Ekşi","123","reccep","erkek","4431")
#insertDavalar(1341,253,"Detaay","Ornek")

dataBase.close()
print("Data Base Closed")