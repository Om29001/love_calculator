import sqlite3

def dataput(a,c,d):
    conn = sqlite3.connect('database.db')
    conn.execute('CREATE TABLE if NOT EXISTS data (name1 TEXT, name2 TEXT,id integer primary key AUTOINCREMENT)')
    conn.commit()
    conn.execute("Insert into data (name1, name2,per) values (?,?,?)",(a,c,d))
    conn.commit()
    conn.close()


def dataget():
    conn = sqlite3.connect('database.db')
    conn.execute('CREATE TABLE if NOT EXISTS data (name1 TEXT, name2 TEXT,per integer,id integer primary key AUTOINCREMENT)')
    conn.commit()
    cursor = conn.execute("SELECT * from data")
    conn.commit()
    m = cursor.fetchall()
    conn.close()
    return m

def datadel(m):
    # print("poch gaya delete function me bhai")
    conn = sqlite3.connect('database.db')
    conn.execute('CREATE TABLE if NOT EXISTS data (name1 TEXT, name2 TEXT,per integer,id integer primary key AUTOINCREMENT)')
    conn.commit()
    cursor = conn.cursor()
    # print("ruk abhi puch ke type or value bolta hu",type(m),m)
    cursor.execute("DELETE FROM data WHERE id = '{}'".format(m))
    # print("udala saale ko")
    conn.commit()
    