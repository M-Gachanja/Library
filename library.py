from book import Book
from member import Member
from datetime import datetime, timedelta

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def generate_book_id(self):
        existing_ids = [int(book.book_id[1:]) for book in self.books if book.book_id.startswith("B")]
        next_id = max(existing_ids, default=0) + 1
        return f"B{next_id:03}"

    def add_book(self, book):
        self.books.append(book)

    def register_member(self, member):
        self.members.append(member)

    def borrow_book(self, member_id, book_id):
        member = self.find_member(member_id)
        if not member:
            return "Member not found."
        if len(member.borrowed_books) >= 3:
            return "Borrow limit reached (3 books)."

        book = self.find_book(book_id)
        if book and book.available:
            book.available = False
            book.borrower_id = member_id
            book.due_date = (datetime.now() + timedelta(days=14)).strftime("%Y-%m-%d")
            member.borrowed_books.append(book_id)
            return f"Book '{book.title}' borrowed. Due date: {book.due_date}"
        return "Book not available or not found."

    def return_book(self, member_id, book_id):
        member = self.find_member(member_id)
        book = self.find_book(book_id)
        if book and member and book_id in member.borrowed_books:
            book.available = True
            book.borrower_id = None
            book.due_date = None
            member.borrowed_books.remove(book_id)
            return f"Book '{book.title}' returned."
        return "Book/member mismatch or not found."

    def find_book(self, book_id):
        return next((book for book in self.books if book.book_id == book_id), None)

    def find_member(self, member_id):
        return next((member for member in self.members if member.member_id == member_id), None)

    def search_books(self, keyword):
        return [book for book in self.books if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower()]

    def search_members(self, keyword):
        return [member for member in self.members if keyword.lower() in member.name.lower()]

    def get_data(self):
        books = [book.to_dict() for book in self.books]
        members = [member.to_dict() for member in self.members]
        return books, members

    def load_data(self, books_data, members_data):
        self.books = [Book.from_dict(b) for b in books_data]
        self.members = [Member.from_dict(m) for m in members_data]
