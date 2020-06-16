import sqlite3
import sys
from database import users_db
import os
mysign="-------$main/users ----> "
def users():
    users_db.creatdatabase()    
    show()
def mydecorator(func):
    def wrapper():
        os.system("clear")
        func()
    return wrapper
@mydecorator
def showallusers():
    users_db.showalluser()
    input("please enter ....")
@mydecorator
def searchusers():
    print("1-search by last name")
    print("2-search by id")
    getnum1=input(mysign)
    if getnum1=="1":
        print("your lastname : ")
        getnum2=input(mysign)
        users_db.searchbyuser(getnum2)
    elif getnum1=="2":
        print("your id : ")
        getnum3=input(mysign)
        users_db.searchbyid(getnum3)
    elif getnum1=="exit":
        sys.exit()
    else:
        print("your command is wrong,please try again")
        searchusers()
    input("please enter ....")
@mydecorator
def add_user():
    print("give me your first name : ")
    getfirst=input(mysign)
    if getfirst.isalpha()==True:
        print("give me your last name : ")
        getlast=input(mysign)
        if getlast.isalpha()==True:
            users_db.add(getfirst,getlast)
        elif getlast=="exit":
            sys.exit()
        else:
            print("just use alphabetic character")
            add_user()
    elif getfirst=="exit":
        sys.exit()
    else:
        print("just use alphabetic character")
        add_user()
    input("please enter ....")
@mydecorator
def remove_user():
    print("give me your first name : ")
    getfirst=input(mysign)
    if getfirst.isalpha()==True:
        print("give me your last name : ")
        getlast=input(mysign)
        if getlast.isalpha()==True:
            users_db.remove(getfirst,getlast)
        elif getlast=="exit":
            sys.exit()
        else:
            print("just use alphabetic character")
            add_user()
    elif getfirst=="exit":
        sys.exit()
    else:
        print("just use alphabetic character")
        remove_user()
    input("please enter ....")
@mydecorator
def add_remove():
    print("1-add user")
    print("2-remove user")
    getnum4=input(mysign)
    if getnum4=="1":
        add_user()
    elif getnum4=="2":
        remove_user()
    elif getnum4=="exit":
        sys.exit()
    else:
        print("your command is wrong,please try again")
        add_remove()
def show():
    os.system("clear")
    print("1-show all users")
    print("2-search users")
    print("3-add/remove user")
    print("say <back> to go back")
    ourusermethod=input(mysign)
    if ourusermethod=="1":
        showallusers()
    elif ourusermethod=="2":
        searchusers()
    elif ourusermethod=="3":
        add_remove()
    elif ourusermethod=="back":
        back1()
    elif ourusermethod=="exit":
        sys.exit()
    else:
        print("your command is wrong,please try again")
        input("please enter ....")
        show()
def back1():
    return True