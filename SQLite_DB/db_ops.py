import sqlite3
con = sqlite3.connect("my_library.db")
cursor = con.cursor()

def create_table():
    crt_tbl_str = "CREATE TABLE IF NOT EXISTS BOOKS (BOOKNAME TEXT, AUTHOR TEXT,PUBLISHER TEXT, PAGES INT)"
    cursor.execute(crt_tbl_str)
    con.commit()

def add_book():
    add_book_str = "INSERT INTO BOOKS VALUES('1984','George Orwell','Güneş Yayınevi',350)"
    cursor.execute(add_book_str)
    con.commit()

def user_add_book(name,author,publisher,pages):
    add_book_str = "INSERT INTO BOOKS VALUES(?,?,?,?)"
    cursor.execute(add_book_str,(name,author,publisher,pages))
    con.commit()

def get_books(*args):
    if len(args) == 0: qry = "select * from books"
    else:
        qry="Select "
        for i in args:
            qry += "{},"

        qry = qry.rstrip(",")
        qry += " from books"

        qry = qry.format(*args)

        print(qry)

    cursor.execute(qry)
    booklist = cursor.fetchall()
    print("\n---BOOKS---\n")
    print(booklist)
    # for i in booklist:
    #     a,b,c,d = i
    #     print("Name: {}\nAuthor: {}\nPublisher: {}\nPages: {}\n".format(a,b,c,d))

def update_book(old_publisher,new_publisher):
    update_str = "update books set publisher = ? where publisher = ?"
    cursor.execute(update_str,(new_publisher,old_publisher))
    con.commit()

def delete_book(bookname):
    delete_str = "delete from books where bookname = ?"
    cursor.execute(delete_str,(bookname,))
    con.commit()

# create_table()

# add_book()

# name = input("Book name:")
# author = input("Author:")
# publisher = input("Publisher:")
# pages = int(input("Pages:"))
# user_add_book(name,author,publisher,pages)
# get_books("bookname","author","publisher","pages")

# update_book("Güneş Yayınevi","Venüs Yayınevi")
# get_books()

#delete_book("1984")



con.close()