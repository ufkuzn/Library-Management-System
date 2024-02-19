class Library:
    def __init__(self):
        self.load_books()

    def load_books(self):
        try:
            with open("books.txt", "r", encoding='utf-8') as file:
                self.books = file.read().splitlines()
        except FileNotFoundError:
            print("The file 'books.txt' does not exist. Creating a new file...")
            open("books.txt", "a+").close()
            self.books = []

    def list_books(self):
        [print(f"Book Name: {book.split(', ')[0]}, Author: {book.split(', ')[1]}") for book in self.books]

    def add_book(self):
        with open("books.txt", "a+", encoding='utf-8') as file:
            name = input("Please enter the book name: ")
            author = input("Please enter the book's author: ")
            year = input("Please enter the book's first release year: ")
            pages = input("Please enter the book's pages: ")
            info = name + ", " + author + ", " + year + ", " + pages
            file.writelines(info + "\n")
        self.load_books()

    def remove_book(self):
        call = input("Please enter the book name want to remove: ")
        with open("books.txt", "r", encoding='utf-8') as file:
            lines = file.readlines()
        with open("books.txt", "w", encoding='utf-8') as file:
            [file.write(line) for line in lines if call not in line]
        self.load_books()


lib = Library()
while 1:
    print("\nMENU\n1) List books\n2) Add book\n3) Remove book\nQ) Exit")
    opt = input("Please choose an option from the menu: ")
    if opt == '1':
        lib.list_books()
    elif opt == '2':
        lib.add_book()
    elif opt == '3':
        lib.remove_book()
    elif opt == 'Q' or opt == 'q':
        print("Have a good day")
        break
    else:
        print("Wrong value, please be careful")