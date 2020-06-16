from database import books_db
import sys
import os
mysign="-------$main/books ----> "
def books():
    books_db.creatdatabase()
    show()
def mydecorator(func):
    def wrapper():
        os.system("clear")
        func()
    return wrapper
@mydecorator
def showallbooks():
    books_db.showallbook()
    input("please enter ....")
def back(get):
    if get=="back":
        return True
    elif get!="back":
        return False
@mydecorator
def searchbookwithid():
    print("give me your book id : ")
    get=input(mysign)
    if get.isdigit()==True:
        books_db.searchbyid(get)
    else:
        print("give me number")
    input("please enter ....")
    
@mydecorator
def searchbookwithname():
    print("give me book name : ")
    get=input(mysign)
    books_db.searchbyname(get)
    input("please enter ....")
@mydecorator
def searchwithauthor():
    print("give me the author of the book : ")
    get=input(mysign)
    books_db.searchbyauthor(get)
    input("please enter ....")
@mydecorator
def searchbook():
    print("1-search by name")
    print("2-search by author")
    print("3-search with id")
    get=input(mysign)
    if get=="1":
        searchbookwithname()
    elif get=="2":
        searchwithauthor()
    elif get=="3":
        searchbookwithid()
    elif get=="exit":
        sys.exit()
    else:
        print("your command is wrong,please try again")
        searchbook()
@mydecorator
def add_book():
    print("give me book name : ")
    getname=input(mysign)
    print("give me book author : ")
    getauthor=input(mysign)
    if getauthor.isalpha()==True:
        print("give me year of book publish : ")
        getyear=input(mysign)
        if getyear.isdigit()==True:
            #import pdb;pdb.set_trace()
            books_db.add(getname,getauthor,getyear)
        else:
            print("the year of book should be a number")
            add_book()
    else:
        print("you should give me the author name")
        add_book()
    input("please enter ....")
@mydecorator
def remove_book():
    print("give me book name : ")
    getname=input(mysign)
    print("give me book author : ")
    getauthor=input(mysign)
    if getauthor.isalpha()==True:
        print("give me year of book publish : ")
        getyear=input(mysign)
        if getyear.isdigit()==True:
            books_db.remove(getname,getauthor,getyear)
        else:
            print("the year of book should be a number")
            remove_book()
    else:
        print("you should give me the author name")
        remove_book()
@mydecorator
def add_remove():
    print("1-add book")
    print("2-remove book")
    get=input(mysign)
    if get=="1":
        add_book()
    elif get=="2":
        remove_book()
    elif get=="exit":
        sys.exit()
    else:
        print("your command is wrong,please try again")
        add_remove()
def show():
    os.system("clear")
    print("1-show all books")
    print("2-search book")
    print("3-add/remove book")
    print("say <back> to go back")
    getmethod=input(mysign)
    if getmethod=="1":
        showallbooks()
    elif getmethod=="2":
        searchbook()
    elif getmethod=="3":
        add_remove()
    elif getmethod=="exit":
        sys.exit()
    elif getmethod=="back":
        back1()
    else:
        print("your command is wrong,please try again")
        input("please enter ....")
def back1():
    return True