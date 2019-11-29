import sqlite3

class Book:
    def __init__(self,name,author,publisher,pages):

        self.name = name
        self.author = author
        self.publisher = publisher
        self.pages = pages

    def __str__(self):
        return "Name: {}\nAuthor: {}\nPublisher: {}\nPages: {}\n".format(self.name,self.author,self.publisher,self.pages)



class Library:
    def __init__(self):
        self.open_connection()

    def open_connection(self):
        self.con = sqlite3.connect("library_project.db")
        self.cursor = self.con.cursor()

        query = "create table if not exists books (name TEXT, author TEXT, publisher TEXT, pages INT)"
        self.cursor.execute(query)
        self.con.commit()

    def close_connection(self):
        self.con.close()


    def get_books(self):
        query = "select * from books"
        self.cursor.execute(query)

        books = self.cursor.fetchall()

        if len(books) == 0:
            print("No books found!")
        else:
            for i in books:
                book = Book(i[0],i[1],i[2],i[3])
                print(book)


    def find_book_by_name(self,name):
        query = "select * from books where name = ?"
        self.cursor.execute(query,(name,))
        book = self.cursor.fetchall()
        if len(book) == 0:
            print("Couldn't find that book!")
        else:
            found_book = Book(book[0][0],book[0][1],book[0][2],book[0][3])
            print(found_book)


    def add_book(self,book):
        query = "insert into books values(?,?,?,?)"

        self.cursor.execute(query,(book.name,book.author,book.publisher,book.pages))
        self.con.commit()


    def delete_book(self,name):
        query = "delete from books where name = ?"

        self.cursor.execute(query,(name,))
        self.con.commit()


    def update_publisher_by_bookname(self,name,new_publisher):
        query = "select publisher from books where name = ?"

        self.cursor.execute(query,(name,))

        book_to_update = self.cursor.fetchall()
        if len(book_to_update) == 0:
            print("Couldn't find that book!")
        else:
            publisher = book_to_update[0][0]
            publisher = new_publisher

            query2 = "update books set publisher = ? where name = ?"

            self.cursor.execute(query2,(publisher,name))
            self.con.commit()
