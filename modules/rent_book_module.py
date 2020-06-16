from modules import books_module
from database import users_db
from database import books_db
from database import rent_book_db
import sys
import os
from datetime import datetime,timedelta,date
mysign="-------$main/rent_book ----> "
def delivertime(day1):
    #nowtime=datetime.now()
    nowtime=date.today()
    timedelivery=nowtime+timedelta(days=day1)
    return timedelivery
def mydecorator(func):
    def wrapper():
        os.system("clear")
        func()
    return wrapper
def rent_book():
    rent_book_db.rent_book_create_database()
    show()
@mydecorator
def showallbooks():
    print("books : ")
    books_db.showallbook()
    input("please enter ....")
@mydecorator
def add_rent1_book():
    print("give me your first name : ")
    getfname=input(mysign)
    if getfname=="exit":
        sys.exit()
    elif getfname.isalpha()==True:
        print("give me your last name : ")
        getlname=input(mysign)
        if getlname=="exit":
            sys.exit()
        elif getlname.isalpha()==True:
            fullname=getfname+" "+getlname
            if users_db.recognizeuser(getfname,getlname)==True:
                showallbooks()
                print("give me your book id : ")
                bookid=input(mysign)
                if bookid=="exit":
                    sys.exit()
                elif bookid.isdigit()==True:
                    bookid=int(bookid)
                    if books_db.recognizebook(bookid)==True:
                        #im there countnue it
                        print("how many day do you want to rent : ")
                        getday=input(mysign)
                        if getday=="exit":
                            sys.exit()
                        elif getday.isdigit()==True:
                            if int(getday)>0:
                                getday=int(getday)
                                rent_book_db.add_rent(fullname,books_db.foundnameofbook(bookid),delivertime(getday))
                                print("Your information has been recorded!")
                                rent_book_db.show(fullname,books_db.foundnameofbook(bookid))
                            elif int(getday)<=0:
                                print("give me right number")
                                input("please enter ....")
                                add_rent1_book()
                        elif getday.isdigit()==False:
                            print("just say number")
                            input("please enter ....")
                            add_rent1_book()
                    elif books_db.recognizebook(bookid)==False:
                        print("Your book could not be found!")
                        input("please enter ....")
                        add_rent1_book()
                elif bookid.isdigit()==False:
                    print("it should be number")
                    input("please enter ....")
                    add_rent1_book()
            elif users_db.recognizeuser(getfname,getlname)==False:
                print("Your user could not be found")
                input("please enter ....")
                add_rent1_book()
        else:
            print("just use alphabetic character")
            input("please enter ....")
            add_rent1_book()
    else:
        print("just use alphabetic character")
        input("please enter ....")
        add_rent1_book()
    input("please enter ....")
@mydecorator
def remove_rent1_book():
    print("give me your first name : ")
    getfname=input(mysign)
    if getfname=="exit":
        sys.exit()
    elif getfname.isalpha()==True:
        print("give me your last name : ")
        getlname=input(mysign)
        if getlname=="exit":
            sys.exit()
        elif getlname.isalpha()==True:
            fullname=getfname+" "+getlname
            if rent_book_db.user_recognizer(fullname)==True:
                print("books : ")
                showallbooks()
                print("give me your book id : ")
                bookid=input(mysign)
                if bookid=="exit":
                    sys.exit()
                elif bookid.isdigit()==True:
                    bookid=int(bookid)
                    bookname=books_db.foundnameofbook(bookid)
                    if rent_book_db.book_recognizer(bookname)==True:
                        rent_book_db.remove_rent(fullname,bookname)
                    elif rent_book_db.book_recognizer(bookid)==False:
                        print("you didn't rent this book")
                        input("please enter ....")
                        remove_rent1_book()
                elif bookid.isdigit()==False:
                    print("it should be number")
                    input("please enter ....")
                    remove_rent1_book()
            elif rent_book_db.user_recognizer(fullname)==False:
                print("user could not be found try again or you didn't rent any book")
                input("please enter ....")
                remove_rent1_book()
        else:
            print("just use alphabetic character")
            input("please enter ....")
            remove_rent1_book()
    else:
        print("just use alphabetic character")
        input("please enter ....")
        remove_rent1_book()
    input("please enter ....")
@mydecorator
def add_remove():
    print("1-add rent")
    print("2-remove rent")
    get=input(mysign)
    if get=="1":
        add_rent1_book()
    elif get=="2":
        remove_rent1_book()
    elif get=="exit":
        sys.exit()
    else:
        print("your command is wrong,please try again")
        add_remove()
@mydecorator
def showallrent():
    rent_book_db.showallrent()
    input("please enter ....")
@mydecorator
def showbyname():
    print("give me your first name : ")
    firstname=input(mysign)
    print("give me your last name : ")
    lastname=input(mysign)
    fullname=firstname+" "+lastname
    rent_book_db.showwithname(fullname)
    input("please enter ....")
@mydecorator
def show():
    print("1-show all rents")
    print("2-show rent by name")
    print("3-add/remove rent")
    print("say <back> to go back")
    getmethod=input(mysign)
    if getmethod=="1":
        showallrent()
    elif getmethod=="2":
        showbyname()
    elif getmethod=="3":
        add_remove()
    elif getmethod=="exit":
        sys.exit()
    elif getmethod=="back":
        back1()
    else:
        print("your command is wrong,please try again")
        input("please enter ....")
        show()
def back1():
    return True
