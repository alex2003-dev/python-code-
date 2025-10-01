class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Member:
    def __init__(self, name):
        self.name = name

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        for b in self.books:
            if b.title == book.title and b.author == book.author:
                return "Book exists"
        self.books.append(book)

    def remove_book(self, title, author):
        for b in self.books:
            if b.title == title and b.author == author:
                self.books.remove(b)
                return

    def find_book(self, title, author):
        for b in self.books:
            if b.title == title and b.author == author:
                return b
        return None

    def add_member(self, member):
        for m in self.members:
            if m.name == member.name:
                return "Member exists"
        self.members.append(member)

    def remove_member(self, name):
        for m in self.members:
            if m.name == name:
                self.members.remove(m)
                return

    def find_member(self, name):
        for m in self.members:
            if m.name == name:
                return m
        return None
print("Library system started")        
