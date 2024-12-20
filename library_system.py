#!/usr/bin/env python3
"""
Library System with Enumerations and Exceptions
"""
# Standard Library Imports
from enum import Enum, auto


class BookGenre(Enum):
    """
    Book Genre Enumeration
    """
    FICTION = auto()
    NON_FICTION = auto()
    SCIENCE = auto()
    HISTORY = auto()
    BIOGRAPHY = auto()


class MembershipLevel(Enum):
    """
    Membership Level Enumeration
    """
    BASIC = 100
    PREMIUM = 200
    GOLD = 500


class BookNotAvailableError(Exception):
    """
    Book Not Available Error
    """
    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(self.message)


class InvalidMembershipError(Exception):
    """
    Invalid Membership Error
    """
    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(self.message)


class LateReturnError(Exception):
    """
    Late Return Error
    """
    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(self.message)


class Book:
    """
    Book Class
    """
    def __init__(self, title: str, genre: BookGenre, is_available: bool = True) -> None:
        self.title = title
        self.genre = genre
        self.is_available = is_available

    def borrow(self) -> None:
        """
        Method to borrow a book
        """
        if not self.is_available:
            raise BookNotAvailableError("Book is not available")
        self.is_available = False

    def return_book(self, is_late: bool) -> None:
        """
        Method to return a book
        """
        if is_late:
            raise LateReturnError("Book is late")
        self.is_available = True


class Member:
    """
    Member Class
    """
    def __init__(self, name: str, membership_level: MembershipLevel) -> None:
        self.name = name
        self.membership_level = membership_level

    def get_fee(self) -> int:
        """
        Method to get the fee associated with membership level
        """
        # If membership level is invalid, raise an error
        if self.membership_level not in MembershipLevel.__members__.values():
            raise InvalidMembershipError("Invalid membership level")
        return self.membership_level.value
