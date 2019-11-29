from library_project import *

print("""

Welcome to library automation!
------------------------------

1. Show All Books
2. Search a Book
3. Add Book
4. Delete Book
5. Update Publisher

Press 'Q' to Quit.
-------------------------------

""")

libr = Library()

while True:
    operation = input("What do you want to do: ")
    if operation == "q":
        print("Closing...")
        break

    elif operation == "1":
        libr.get_books()

    elif operation == "2":
        name = input("Enter a book name: ")
        libr.find_book_by_name(name)

    elif operation == "3":
        name = input("Name: ")
        author = input("Author: ")
        publisher = input("Publisher: ")
        pages = input("Pages: ")

        new_book = Book(name,author,publisher,pages)
        print("Adding the book...")
        libr.add_book(new_book)
        print("Book Added!")

    elif operation == "4":
        name = input("Which book do you want to delete: ")

        decision = input("Are you sure? (y/n): ")

        if decision == "y":
            print("Deleting the book...")
            libr.delete_book(name)
            print("Book deleted!")
        elif decision == "n":
            continue


    elif operation == "5":
        bookname = input("Which book's publisher would you like to update: ")
        new_publisher = input("Enter the name of new publisher: ")
        print("Publisher is updating...")
        libr.update_publisher_by_bookname(bookname,new_publisher)
        print("Publisher Updated!")

    else:
        print("Wrong option, choose correct!")