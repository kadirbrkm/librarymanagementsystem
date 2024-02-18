import tkinter as tk
from tkinter import simpledialog, messagebox
from library import Library

class LibraryApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Library Management System ")

        self.label_title = tk.Label(master, text="Library Management System", font=("Helvetica", 16))
        self.label_title.grid(row=0, column=0, columnspan=2, pady=10)

        self.button_list_books = tk.Button(master, text="List Books", command=self.list_books)
        self.button_list_books.grid(row=1, column=0, padx=5)

        self.button_add_book = tk.Button(master, text="Add Book", command=self.add_book)
        self.button_add_book.grid(row=1, column=1, padx=5)

        self.button_search = tk.Button(master, text="Search Book", command=self.search_book)
        self.button_search.grid(row=2, column=0, padx=5)

        self.button_remove_book = tk.Button(master, text="Remove Book", command=self.remove_book)
        self.button_remove_book.grid(row=2, column=1, padx=5)

        self.library = Library()

    def list_books(self):
        books = self.library.list_books()
        messagebox.showinfo("Books", "\n".join(books))

    def add_book(self):
        book_name = simpledialog.askstring("Input", "Enter book name:")
        if not book_name:
            return
        author = simpledialog.askstring("Input", "Enter author name:")
        if not author:
            return
        release_date = simpledialog.askstring("Input", "Enter release date:")
        if not release_date:
            return
        number_of_pages = simpledialog.askstring("Input", "Enter number of pages:")
        if not number_of_pages:
            return
        information = f"{book_name},{author},{release_date},{number_of_pages}"
        self.library.add_book(information)
        messagebox.showinfo("Success", f"Book '{book_name}' added successfully!")

    def search_book(self):
        query = simpledialog.askstring("Input", "Enter search query:")
        if not query:
            return
        found_books = self.library.search_books(query)
        if found_books:
            messagebox.showinfo("Search Results", "\n".join(found_books))
        else:
            messagebox.showinfo("Search Results", "No matching books found.")

    def remove_book(self):
        book_title_to_remove = simpledialog.askstring("Input", "Enter book title to remove:")
        if not book_title_to_remove:
            return
        removed = self.library.remove_book(book_title_to_remove)
        if removed:
            messagebox.showinfo("Success", f"Book '{book_title_to_remove}' removed successfully!")
        else:
            messagebox.showinfo("Not Found", f"Book '{book_title_to_remove}' not found!")

if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryApp(root)
    root.mainloop()
