from src.Book import Book
from src.User import User


class Library:
    def __init__(self):
        self.__books = []
        self.__users = []
        self.__checked_out_books = []
        self.__checked_in_books = []
        

    # Getters
    def get_books(self):
        return self.__books

    def get_users(self):
        return self.__users

    def get_checked_out_books(self):
        return self.__checked_out_books

    def get_checked_in_books(self):
        return self.__checked_in_books

    # 1.1 Add Book
    def add_book(self, isbn, title, author):
        self.__books.append((isbn,title,author,True,1))
        

    # 1.2 List All Books
    def list_all_books(self):
        for book in self.__books:
            print(f"ISBN: {book[0]}, Title: {book[1]}, Author: {book[2]}")

    # 2.1 Check out book
    def check_out_book(self, isbn, dni, due_date):
        book = next((b for b in self.__books if b[0] == isbn), None)
        if not book:
            return f"Unable to find the data for the values: ISBN {isbn} and DNI: {dni}"
        
        user = next((u for u in self.__users if u[0] == dni), None)
        if not user:
            return f"Unable to find the data for the values: ISBN {isbn} and DNI: {dni}"
        
        if not book[3]:
            return f"Book {isbn} is not available"
        
        book[3] = False
        book[4] += 1
        self.__checked_out_books.append([isbn, dni, due_date])
        
        user[2] += 1
        
        return f"User {dni} checked out book {isbn}"
    

    # 2.2 Check in book
    def check_in_book(self, isbn, dni, returned_date):
        book = next((b for b in self.__books if b[0] == isbn), None)
        if not book:
            return f"Book {isbn} is not available"
        
        checkout_entry = next((co for co in self.__checked_out_books if co[0] == isbn and co[1] == dni), None)
        if not checkout_entry:
            return f"Book {isbn} is not available"
        
        book[3] = True
        self.__checked_in_books.append([isbn, dni, returned_date])
        
        user = next((u for u in self.__users if u[0] == dni), None)
        user[3] += 1
        
        self.__checked_out_books.remove(checkout_entry)
        
        return f"Book {isbn} returned"

    # Utils
    def add_user(self, dni, name):
        if any(user[0] == dni for user in self.__users):
            return f"User with DNI {dni} already exists"
        self.__users.append([dni, name, 0, 0])
