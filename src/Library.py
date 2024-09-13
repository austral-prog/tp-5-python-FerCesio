from src.Book import Book
from src.User import User


from typing import List, Tuple, Optional

class Library:
    def __init__(self) -> None:
        self.__books: List[Tuple[str, str, str, bool, int]] = []
        self.__users: List[Tuple[int, str, int, int]] = []
        self.__checked_out_books: List[Tuple[str, int, str]] = []
        self.__checked_in_books: List[Tuple[str, int, str]] = []

    # Getters
    def get_books(self) -> List[Tuple[str, str, str, bool, int]]:
        return self.__books

    def get_users(self) -> List[Tuple[int, str, int, int]]:
        return self.__users

    def get_checked_out_books(self) -> List[Tuple[str, int, str]]:
        return self.__checked_out_books

    def get_checked_in_books(self) -> List[Tuple[str, int, str]]:
        return self.__checked_in_books

    # 1.1 Add Book
    def add_book(self, isbn: str, title: str, author: str) -> None:
        self.__books.append((isbn, title, author, True, 0))

    # 1.2 List All Books
    def list_all_books(self) -> None:
        for book in self.__books:
            print(f"ISBN: {book[0]}, Title: {book[1]}, Author: {book[2]}")

    # 2.1 Check out book
    def check_out_book(self, isbn: str, dni: int, due_date: str) -> str:
        book: Optional[Tuple[str, str, str, bool, int]] = next((b for b in self.__books if b[0] == isbn), None)
        if not book:
            return f"Unable to find the data for the values: ISBN {isbn} and DNI: {dni}"
        
        user: Optional[Tuple[int, str, int, int]] = next((u for u in self.__users if u[0] == dni), None)
        if not user:
            return f"Unable to find the data for the values: ISBN {isbn} and DNI: {dni}"
        
        if not book[3]:
            return f"Book {isbn} is not available"
        
        book[3] = False
        book[4] += 1
        self.__checked_out_books.append((isbn, dni, due_date))
        
        user[2] += 1
        
        return f"User {dni} checked out book {isbn}"

    
    def check_in_book(self, isbn: str, dni: int, returned_date: str) -> str:
        book: Optional[Tuple[str, str, str, bool, int]] = next((b for b in self.__books if b[0] == isbn), None)
        if not book:
            return f"Book {isbn} is not available"
        
        checkout_entry: Optional[Tuple[str, int, str]] = next((co for co in self.__checked_out_books if co[0] == isbn and co[1] == dni), None)
        if not checkout_entry:
            return f"Book {isbn} is not available"
        
        book[3] = True
        self.__checked_in_books.append((isbn, dni, returned_date))
        
        user: Optional[Tuple[int, str, int, int]] = next((u for u in self.__users if u[0] == dni), None)
        user[3] += 1
        
        self.__checked_out_books.remove(checkout_entry)
        
        return f"Book {isbn} returned"


    def add_user(self, dni: int, name: str) -> str:
        if any(user[0] == dni for user in self.__users):
            return f"User with DNI {dni} already exists"
        self.__users.append((dni, name, 0, 0))
        return f"User {dni} added"

