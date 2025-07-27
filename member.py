class Member:
    def __init__(self, member_id, name, borrowed_books=None):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = borrowed_books or []

    def borrow_book(self, book_id):
        if len(self.borrowed_books) < 3:
            self.borrowed_books.append(book_id)
            return True
        return False

    def return_book(self, book_id):
        if book_id in self.borrowed_books:
            self.borrowed_books.remove(book_id)

    def to_dict(self):
        return {
            "member_id": self.member_id,
            "name": self.name,
            "borrowed_books": self.borrowed_books
        }

    @staticmethod
    def from_dict(data):
        return Member(data["member_id"], data["name"], data["borrowed_books"])

    def __str__(self):
        return f"ID: {self.member_id}, Name: {self.name}, Borrowed Books: {self.borrowed_books}"
