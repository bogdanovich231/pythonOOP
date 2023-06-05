class Book:
    name = ""
    language = ""
    year = ""
    author = ""
    pages = ""

    # parameterized constructor
    def __init__(self, name, language, year, author, pages):
        self.name = name
        self.language = language
        self.year = year
        self.author = author
        self.pages = pages

    def read(self):
        print("Name: " + str(self.name))
        print("Language: " + str(self.language))
        print("Year:" + str(self.year))

    def sortByName(self, books):
        sorted_books = sorted(books, key=lambda book: book.name)
        return sorted_books

    def sortByYear(self, books):
        sorted_books = sorted(books, key=lambda book: book.year)
        return sorted_books

    def sortByPages(self, books):
        sorted_books = sorted(books, key=lambda book: book.pages)
        return sorted_books

    def sortByAuthor(self, books):
        sorted_books = sorted(books, key=lambda book: book.author)
        return sorted_books


# Creating book objects
book1 = Book("Python Crash Course", "English", 2019, "by Eric Matthes", "544 pages")
book2 = Book("The ChatGPT Millionaire", "English", 2023, "Paperback", "114 pages")
book3 = Book("JavaScript: The Definitive Guide", "English", 2020, "Hardcover", "704 pages")
book4 = Book("The Road to React", "English", 2018, "Paperback", "292 pages")
book5 = Book("JavaScript: The Good Parts", "English", 2008, "Hardcover", "176 pages")

# Using the read() method on book objects
book1.read()
book2.read()

# Creating a list of book objects
books = [book1, book2, book3, book4, book5]

# Sorting the books by name and printing the result
sorted_by_name = book1.sortByName(books)
for book in sorted_by_name:
    print(book.name)


sorted_by_year = book1.sortByYear(books)
for book in sorted_by_year:
    print(book.year)
