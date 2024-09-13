# from typing import Self


class Book:
    def __init__(self, isbn: str, title: str, author: str, available: bool =True, checkout_num: int =0):
        self.__isbn = isbn
        self.__title = title
        self.__author = author
        self.__available = available
        self.__checkout_num = checkout_num

    # Getters
    def get_isbn(self):
        return self.__isbn

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def is_available(self):
        return self.__available

    def get_checkout_num(self):
        return self.__checkout_num

    # Setters
    def set_available(self, available: bool):
        self.__available = available

    def increment_checkout_num(self):
        self.__checkout_num += 1


    # Utils
    def __str__(self) -> str:
        return f"ISBN: {self.__isbn}, Title: {self.__title}, Author: {self.__author}, Available: {self.__available}, Checkout Number: {self.__checkout_num}"

    def __eq__(self, other):
        if isinstance(other, Book):
            return (self.__isbn == other.__isbn and
                    self.__title == other.__title and
                    self.__author == other.__author and
                    self.__available == other.__available and
                    self.__checkout_num == other.__checkout_num)
        return False
