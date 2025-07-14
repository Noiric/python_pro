from pydantic import BaseModel
from typing import List
import json


class Book(BaseModel):
    title: str
    author: str
    year: int


class Library:
    def __init__(self):
        self.books: List[Book] = []

    def add_book(self, book: Book):
        self.books.append(book)
        print(f"Додано книгу: {book.title}")

    def remove_book(self, title: str):
        self.books = [b for b in self.books if b.title != title]
        print(f"Книгу '{title}' видалено (якщо була).")

    def list_books(self):
        print("Список книг у бібліотеці:")
        for book in self.books:
            print(f"{book.title} — {book.author}, {book.year}")

    def find_by_author(self, author: str):
        print(f"Книги автора '{author}':")
        for book in self.books:
            if book.author == author:
                print(f"{book.title}, {book.year}")

    def save_to_file(self, filename: str):
        with open(filename, "w") as f:
            json.dump([book.model_dump() for book in self.books], f)
        print("Список збережено у файл.")

    def load_from_file(self, filename: str):
        with open(filename, "r") as f:
            data = json.load(f)
            self.books = [Book(**item) for item in data]
        print("Список завантажено з файлу.")


if __name__ == "__main__":
    lib = Library()
    book1 = Book(title="Тарас Бульба", author="Забув", year=1927)
    book2 = Book(title="Кобзар", author="Тарас Шевченко", year=1944)
    lib.add_book(book1)
    lib.add_book(book2)
    lib.list_books()
    lib.find_by_author("Забув")
    lib.save_to_file("books.json")
    lib.remove_book("Кобзар")
    lib.list_books()
    lib.load_from_file("books.json")
    lib.list_books()
