class Book:
    # Class attribute (private)
    __library_name = "City Library"

    # Instance attributes
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_book(self):
        print(f"Library: {Book.__library_name} | Title: {self.title} | Author: {self.author}")

    @classmethod 
    def display_libraryName(cls):
        print(f"Library: {cls.__library_name}")

    @classmethod
    def get_library_name(cls):
        return cls.__library_name

    @classmethod
    def set_library_name(cls, name):
        cls.__library_name = name

book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
book3 = Book("The Alchemist", "Paulo Coelho")

book1.display_book()
book2.display_book()
book3.display_book()

print(Book.get_library_name())
Book.set_library_name("Downtown Library")
print(Book.get_library_name())
