from modules import rent_book_module
from modules import users_module
from modules import books_module
import sys
import os
import time
mysign="-------$main ----> "
def banner():
    print(r'''
        __   __        __                               __   ___  __  
|    | |__) |__)  /\  |__) \ /     |\/|  /\  |\ |  /\  / _` |__  |__) 
|___ | |__) |  \ /~~\ |  \  |      |  | /~~\ | \| /~~\ \__> |___ |  \ 
                                                                      
    ''')
def main():
    os.system("clear")
    time.sleep(0.1)
    banner()
    print("1-books")
    time.sleep(0.1)
    print("2-users")
    time.sleep(0.1)
    print("3-rent book")
    time.sleep(0.1)
    print("say <exit> when you want to stop program")
    time.sleep(0.1)
    ourmethod=input(mysign)
    if ourmethod=="1":
        books_module.books()
    elif ourmethod=="2":
        users_module.users()
    elif ourmethod=="3":
        rent_book_module.rent_book()
    elif ourmethod=="exit":
        sys.exit()
    else:
        print("dastor shoma eshtebah ast dobare emtehan konid")
        main()
    get1=users_module.back1()
    if get1==True:
        main()
    get2=books_module.back1()
    if get2==True:
        main()
    get3=rent_book_module.back1()
    if get3==True:
        main()
main()
