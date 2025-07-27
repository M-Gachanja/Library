class Book:
    def __init__(self, book_id, title, author, synopsis=""):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.synopsis = synopsis
        self.available = True
        self.borrower_id = None
        self.due_date = None

    def __str__(self):
        status = "Available" if self.available else f"Borrowed by {self.borrower_id}, Due: {self.due_date}"
        return (
            f"[{self.book_id}] {self.title} by {self.author}\n"
            f"  Synopsis: {self.synopsis}\n"
            f"  Status: {status}"
        )

    def to_dict(self):
        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "synopsis": self.synopsis,
            "available": self.available,
            "borrower_id": self.borrower_id,
            "due_date": self.due_date
        }

    @classmethod
    def from_dict(cls, data):
        book = cls(data["book_id"], data["title"], data["author"], data.get("synopsis", ""))
        book.available = data.get("available", True)
        book.borrower_id = data.get("borrower_id")
        book.due_date = data.get("due_date")
        return book
