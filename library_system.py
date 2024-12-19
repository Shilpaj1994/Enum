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
