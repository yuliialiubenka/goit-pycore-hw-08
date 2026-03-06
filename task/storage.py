"""Persistence helpers for saving and loading the address book."""

import pickle

from task.models import AddressBook


def save_data(book: AddressBook, filename: str = "addressbook.pkl") -> None:
    """
    Save the address book to a file using pickle serialization.

    Args:
        book: The AddressBook instance to save.
        filename: The name of the file to save to (default: "addressbook.pkl").
    """
    with open(filename, "wb") as file:
        pickle.dump(book, file)


def load_data(filename: str = "addressbook.pkl") -> AddressBook:
    """
    Load the address book from a file using pickle deserialization.

    Args:
        filename: The name of the file to load from (default: "addressbook.pkl").

    Returns:
        An AddressBook instance. If the file does not exist or is invalid,
        returns a new empty AddressBook.
    """
    try:
        with open(filename, "rb") as file:
            return pickle.load(file)

    # FileNotFoundError: file does not exist yet (first app run)
    # pickle.UnpicklingError: file content is not a valid pickle stream
    # EOFError: file is empty/truncated (e.g., interrupted write)
    except (FileNotFoundError, pickle.UnpicklingError, EOFError):
        return AddressBook()
