from src.Book import Book
from src.User import User


from typing import List, Tuple, Optional

class Library:
    def __init__(self) -> None:
        self.__books: list[Book] = []
        self.__users: list[User] = []
        self.__checked_out_books: list[tuple[str, int, str]] = []
        self.__checked_in_books: list[tuple[str, int, str]] = []

    # Getters
    def get_books(self) -> list[Book]:
        return self.__books

    def get_users(self) -> list[User]:
        return self.__users

    def get_checked_out_books(self) -> list[tuple[str, int, str]]:
        return self.__checked_out_books

    def get_checked_in_books(self) -> list[tuple[str, int, str]]:
        return self.__checked_in_books

    # 1.1 Add Book
    def add_book(self, isbn: str, title: str, author: str) -> None:
        new_book = Book(isbn, title, author)
        self.__books.append(new_book)

    # 1.2 List All Books
    def list_all_books(self) -> None:
        for book in self.__books:
            print(f"ISBN: {book.get_isbn()}, Title: {book.get_title()}, Author: {book.get_author()}")

    # 2.1 Check out book
    def check_out_book(self, isbn: str, dni: int, due_date: str) -> str:
        book = next((b for b in self.__books if b.get_isbn() == isbn), None)
        if not book:
            return f"Unable to find the data for the values: ISBN {isbn} and DNI: {dni}"
        
        user = next((u for u in self.__users if u.get_dni() == dni), None)
        if not user:
            return f"Unable to find the data for the values: ISBN {isbn} and DNI: {dni}"
        
        if not book.is_available():
            return f"Book {isbn} is not available"
        
        book.set_available(False)
        book.increment_checkout_num()
        self.__checked_out_books.append((isbn, dni, due_date))
        
        user.increment_checkouts()
        
        return f"User {dni} checked out book {isbn}"

    # 2.2 Check in book
    def check_in_book(self, isbn: str, dni: int, returned_date: str) -> str:
        book = next((b for b in self.__books if b.get_isbn() == isbn), None)
        if not book:
            return f"Book {isbn} is not available"
        
        checkout_entry = next((co for co in self.__checked_out_books if co[0] == isbn and co[1] == dni), None)
        if not checkout_entry:
            return f"Book {isbn} is not available"
        
        book.set_available(True)
        self.__checked_in_books.append((isbn, dni, returned_date))
        
        user = next((u for u in self.__users if u.get_dni() == dni), None)
        if user is None:
            return f"User with DNI {dni} not found"

        user.increment_checkins()
        
        self.__checked_out_books.remove(checkout_entry)
        
        return f"Book {isbn} returned"

    # Utils
    def add_user(self, dni: int, name: str) -> str:
        if any(user.get_dni() == dni for user in self.__users):
            return f"User with DNI {dni} already exists"
        new_user = User(dni, name)
        self.__users.append(new_user)
        return f"User {dni} added"
