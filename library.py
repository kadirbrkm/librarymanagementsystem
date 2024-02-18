import os

class Library:
    def __init__(self):
        self.file = open("books.txt", "a+")

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)
        lines = self.file.read().splitlines()
        books = []
        for line in lines:
            book_info = line.split(",")
            book_title, book_author = book_info[0], book_info[1]
            books.append(f"Book: {book_title}, Author: {book_author}")
        return books

    def add_book(self, information):
        self.file.write(information)
        self.file.write("\n")

    def remove_book(self, book_title_to_remove):
        self.file.seek(0)
        lines = self.file.readlines()
        updated_lines = [line for line in lines if book_title_to_remove not in line]
        self.file.seek(0)
        self.file.truncate()
        for line in updated_lines:
            self.file.write(line)
        return len(lines) != len(updated_lines)

    def search_books(self, query):
        self.file.seek(0)
        lines = self.file.readlines()
        found_books = []
        for line in lines:
            book_info = line.split(",")
            book_title, book_author = book_info[0], book_info[1]
            if query.lower() in book_title.lower() or query.lower() in book_author.lower():
                found_books.append(f"Book: {book_title}, Author: {book_author}")
        return found_books
