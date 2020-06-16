import sqlite3
import time
import datetime
from tabulate import tabulate
def timenow():
    current=time.localtime()
    strtime=time.strftime('%Y/%m/%d ---> %A | %H:%M' , current)
    return strtime
conn=sqlite3.connect("database/rent_book.db")
c=conn.cursor()
def rent_book_create_database():
    c.execute('''CREATE TABLE IF NOT EXISTS rent(
        fullname TEXT,
        book_name TEXT,
        date TEXT,
        deliverdate TEXT
    )''')
    conn.commit()
def add_rent(fullname,book_name,delivertime):
    c.execute("INSERT INTO rent VALUES(?,?,?,?)",(fullname,book_name,timenow(),delivertime))
    conn.commit()
def show(fullname,book_name):
    c.execute("SELECT * FROM rent WHERE fullname=? AND book_name=?",(fullname,book_name))
    print(tabulate(c.fetchall(),headers=["name","bookname","rent date","delivery date"],tablefmt="fancy_grid"))
def showallrent():
    c.execute("SELECT * FROM rent")
    print(tabulate(c.fetchall(),headers=["name","bookname","rent date","delivery date"],tablefmt="fancy_grid"))
def showwithname(name):
    c.execute("SELECT * FROM rent WHERE fullname=?",(name,))
    if c.fetchone():
        c.execute("SELECT * FROM rent WHERE fullname=?",(name,))
        print(tabulate(c.fetchall(),headers=["name","bookname","rent date","delivery date"],tablefmt="fancy_grid"))
    else:
        print("Your name could not be found")   
def remove_rent(fullname ,bookname):
    c.execute("DELETE FROM rent WHERE fullname=? AND book_name=?",(fullname,bookname))
    print("your rent has been deleted")
    conn.commit()
def user_recognizer(fullname):
    c.execute("SELECT * FROM rent WHERE fullname=?",(fullname,))
    if c.fetchone():
        return True
    else:
        return False
def book_recognizer(bookname):
    c.execute("SELECT * FROM rent WHERE book_name=?",(bookname,))
    if c.fetchone():
        return True
    else:
        return False