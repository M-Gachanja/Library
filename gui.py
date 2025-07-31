import tkinter as tk
from tkinter import messagebox
from library import Library
from book import Book
from member import Member
from storage import load_json, save_json

library = Library()
library.load_data(load_json("data/books.json"), load_json("data/members.json"))

def add_book():
    book_id = book_id_entry.get().strip()
    title = title_entry.get().strip()
    author = author_entry.get().strip()
    synopsis = synopsis_entry.get("1.0", tk.END).strip()

    if not book_id or not title or not author or not synopsis:
        messagebox.showwarning("Input Error", "All fields are required.")
        return

    if library.find_book(book_id):
        messagebox.showerror("Duplicate ID", f"Book ID '{book_id}' already exists.")
        return

    book = Book(book_id, title, author, synopsis)
    library.add_book(book)
    messagebox.showinfo("Success", f"Book '{title}' added.")
    save_data()

    book_id_entry.delete(0, tk.END)
    title_entry.delete(0, tk.END)
    author_entry.delete(0, tk.END)
    synopsis_entry.delete("1.0", tk.END)

def register_member():
    member_id = member_id_entry.get()
    name = name_entry.get()
    if member_id and name:
        library.register_member(Member(member_id, name))
        messagebox.showinfo("Success", "Member registered.")
        member_id_entry.delete(0, tk.END)
        name_entry.delete(0, tk.END)
        save_data()
    else:
        messagebox.showwarning("Input Error", "All fields required.")

def borrow_book():
    member_id = borrow_member_id.get()
    book_id = borrow_book_id.get()
    result = library.borrow_book(member_id, book_id)
    messagebox.showinfo("Borrow Book", result)
    save_data()

def return_book():
    member_id = return_member_id.get()
    book_id = return_book_id.get()
    result = library.return_book(member_id, book_id)
    messagebox.showinfo("Return Book", result)
    save_data()

def view_members():
    display_text.config(state="normal")
    display_text.delete("1.0", tk.END)
    for member in library.members:
        display_text.insert(tk.END, str(member) + "\n")
    display_text.config(state="disabled")

def view_books():
    display_text.config(state="normal")
    display_text.delete("1.0", tk.END)
    for book in library.books:
        display_text.insert(tk.END, str(book) + "\n\n")
    display_text.config(state="disabled")

def search_books():
    keyword = search_entry.get()
    results = library.search_books(keyword)
    display_text.config(state="normal")
    display_text.delete("1.0", tk.END)
    for book in results:
        display_text.insert(tk.END, str(book) + "\n\n")
    display_text.config(state="disabled")

def search_members():
    keyword = search_entry.get()
    results = library.search_members(keyword)
    display_text.config(state="normal")
    display_text.delete("1.0", tk.END)
    for member in results:
        display_text.insert(tk.END, str(member) + "\n")
    display_text.config(state="disabled")

def save_data():
    books, members = library.get_data()
    save_json("data/books.json", books)
    save_json("data/members.json", members)

root = tk.Tk()
root.title("Library Management System")

# Book Frame
book_frame = tk.Frame(root)
book_frame.pack(pady=10)

tk.Label(book_frame, text="Book ID").grid(row=0, column=0)
book_id_entry = tk.Entry(book_frame)
book_id_entry.grid(row=0, column=1)

tk.Label(book_frame, text="Title").grid(row=1, column=0)
title_entry = tk.Entry(book_frame)
title_entry.grid(row=1, column=1)

tk.Label(book_frame, text="Author").grid(row=2, column=0)
author_entry = tk.Entry(book_frame)
author_entry.grid(row=2, column=1)

tk.Label(book_frame, text="Synopsis").grid(row=3, column=0)
synopsis_entry = tk.Text(book_frame, height=4, width=30)
synopsis_entry.grid(row=3, column=1)

tk.Button(book_frame, text="Add Book", command=add_book, bg="#2f5ba3", fg="white", font=("Arial", 10, "bold")).grid(row=4, column=1, pady=5)

# Member Frame
member_frame = tk.LabelFrame(root, text="Register Member")
member_frame.pack(fill="x", padx=10, pady=5)

tk.Label(member_frame, text="Member ID:").grid(row=0, column=0)
member_id_entry = tk.Entry(member_frame)
member_id_entry.grid(row=0, column=1)

tk.Label(member_frame, text="Name:").grid(row=1, column=0)
name_entry = tk.Entry(member_frame)
name_entry.grid(row=1, column=1)

tk.Button(member_frame, text="Register", command=register_member, bg="#2f5ba3", fg="white", font=("Arial", 10, "bold")).grid(row=2, column=1, pady=5)

# Borrow/Return Frame
br_frame = tk.LabelFrame(root, text="Borrow/Return")
br_frame.pack(fill="x", padx=10, pady=5)

tk.Label(br_frame, text="Member ID:").grid(row=0, column=0)
borrow_member_id = tk.Entry(br_frame)
borrow_member_id.grid(row=0, column=1)

tk.Label(br_frame, text="Book ID:").grid(row=1, column=0)
borrow_book_id = tk.Entry(br_frame)
borrow_book_id.grid(row=1, column=1)

tk.Button(br_frame, text="Borrow", command=borrow_book, bg="#2f5ba3", fg="white", font=("Arial", 10, "bold")).grid(row=2, column=1)

tk.Label(br_frame, text="Return Member ID:").grid(row=3, column=0)
return_member_id = tk.Entry(br_frame)
return_member_id.grid(row=3, column=1)

tk.Label(br_frame, text="Return Book ID:").grid(row=4, column=0)
return_book_id = tk.Entry(br_frame)
return_book_id.grid(row=4, column=1)

tk.Button(br_frame, text="Return", command=return_book, bg="#2f5ba3", fg="white", font=("Arial", 10, "bold")).grid(row=5, column=1)

# Search Frame
search_frame = tk.LabelFrame(root, text="Search / View")
search_frame.pack(fill="x", padx=10, pady=5)

search_entry = tk.Entry(search_frame, width=30)
search_entry.grid(row=0, column=0)

tk.Button(search_frame, text="Search Books", command=search_books, bg="#2f5ba3", fg="white", font=("Arial", 10, "bold")).grid(row=0, column=1)
tk.Button(search_frame, text="Search Members", command=search_members, bg="#2f5ba3", fg="white", font=("Arial", 10, "bold")).grid(row=0, column=2)
tk.Button(search_frame, text="View Books", command=view_books, bg="#2f5ba3", fg="white", font=("Arial", 10, "bold")).grid(row=1, column=1)
tk.Button(search_frame, text="View Members", command=view_members, bg="#2f5ba3", fg="white", font=("Arial", 10, "bold")).grid(row=1, column=2)

# Display Area with Scrollbar and Custom Font
display_frame = tk.Frame(root)
display_frame.pack(fill="both", expand=True, padx=10, pady=10)

scrollbar = tk.Scrollbar(display_frame)
scrollbar.pack(side="right", fill="y")

display_text = tk.Text(display_frame, height=15, yscrollcommand=scrollbar.set, font=("Consolas", 11), bg="#f8f9fa")
display_text.pack(fill="both", expand=True)

scrollbar.config(command=display_text.yview)
display_text.config(state="disabled")

if __name__ == "__main__":
    root.mainloop()
