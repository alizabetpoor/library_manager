import sqlite3
from tabulate import tabulate
conn=sqlite3.connect("database/users.db")
c=conn.cursor()
def creatdatabase():
    global conn
    global c
    c.execute('''
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first TEXT COLLATE NOCASE,
        last TEXT COLLATE NOCASE
    )
    ''')
    conn.commit()
    #conn.close()
def showalluser():
    c.execute("SELECT * FROM users")
    print(tabulate(c.fetchall(),headers=["id","firstname","lastname"],tablefmt="fancy_grid"))
    conn.commit()
    #c.close()
def searchbyuser(last):
    c.execute("SELECT * FROM users WHERE last=? LIMIT 1",(last,))
    if c.fetchone():
        c.execute("SELECT * FROM users WHERE last=?",(last,))
        print(tabulate(c.fetchall(),headers=["id","firstname","lastname"],tablefmt="fancy_grid"))
    else:
        print("Your lastname could not be found")
    conn.commit()
    #c.close()
def searchbyid(id1):
    c.execute("SELECT * FROM users WHERE id=? LIMIT 1",(id1,))
    if c.fetchone():
        c.execute("SELECT * FROM users WHERE id=?",(id1,))
        print(tabulate(c.fetchall(),headers=["id","firstname","lastname"],tablefmt="fancy_grid"))
        conn.commit()
        #c.close()
    else:
        print("Your id could not be found")
def add(first,last):
    c.execute("INSERT into users values(?,?,?)",(None,first,last))
    c.execute("SELECT * FROM users WHERE first=? AND last=?",(first,last))
    print("user added to database!")
    print("your information : ")
    print(tabulate(c.fetchall(),headers=["id","firstname","lastname"],tablefmt="fancy_grid"))
    conn.commit()
    #c.close()
def remove(first,last):
    c.execute("SELECT * from users WHERE first=? AND last=?",(first,last))
    if c.fetchone():
        c.execute("DELETE from users WHERE first=? AND last=?",(first,last))
        print("user was removed succesfully!")
        conn.commit()
        #c.close()
    else:
        print("user could not be found")
def recognizeuser(first,last):
    c.execute("SELECT * FROM users WHERE first=? AND last=?",(first,last))
    if c.fetchone():
        return True
    else:
        return False
        