"""
Messages module for the contact assistant bot.

This module provides user-friendly message functions with formatting:
- Greeting messages
- Error messages
- Command prompts
"""

from colorama import Fore

from task.decorators import output_formatter
from task.message_texts import (
    INVALID_NAME_FORMAT,
    INVALID_PHONE_FORMAT,
    INVALID_BIRTHDAY_FORMAT,
    WELCOME_MESSAGE,
    HELLO_MESSAGE,
    GOODBYE_MESSAGE,
    ERROR_UNEXPECTED_ARGUMENTS,
    PROMPT_FOR_COMMAND,
    NO_CONTACTS_FOUND,
    BIRTHDAY_ADDED,
    CONTACT_DELETED,
    NO_UPCOMING_BIRTHDAYS,
    INPUT_ERROR_MISSING_ARGS_CHANGE,
    INPUT_ERROR_MISSING_ARGS_DELETE,
)


@output_formatter(color=Fore.CYAN, bold=True)
def welcome_message() -> str:
    """Return welcome message for the assistant bot."""
    return WELCOME_MESSAGE


@output_formatter(color=Fore.GREEN)
def hello_message() -> str:
    """Return greeting message."""
    return HELLO_MESSAGE


@output_formatter(color=Fore.CYAN)
def goodbye_message() -> str:
    """Return goodbye message."""
    return GOODBYE_MESSAGE


@output_formatter(color=Fore.RED)
def error_unexpected_arguments(command: str) -> str:
    """Return error message when a command receives unexpected arguments."""
    return ERROR_UNEXPECTED_ARGUMENTS.format(command=command)


@output_formatter(color=Fore.RED)
def error_invalid_name_format() -> str:
    """Return error message for invalid name format."""
    return INVALID_NAME_FORMAT


@output_formatter(color=Fore.RED)
def error_invalid_phone_format() -> str:
    """Return error message for invalid phone format."""
    return INVALID_PHONE_FORMAT


@output_formatter(color=Fore.RED)
def error_missing_args_change() -> str:
    """Return error message for missing arguments in change command."""
    return INPUT_ERROR_MISSING_ARGS_CHANGE


@output_formatter(color=Fore.RED)
def error_missing_args_delete() -> str:
    """Return error message for missing arguments in delete command."""
    return INPUT_ERROR_MISSING_ARGS_DELETE


@output_formatter(color=Fore.YELLOW)
def prompt_for_command() -> str:
    """Return prompt message for requesting a command."""
    return PROMPT_FOR_COMMAND


@output_formatter(color=Fore.BLUE)
def no_contacts_found_message() -> str:
    """Return message when there are no contacts."""
    return NO_CONTACTS_FOUND


@output_formatter(color=Fore.RED)
def error_invalid_birthday_format() -> str:
    """Return error message for invalid birthday format."""
    return INVALID_BIRTHDAY_FORMAT


@output_formatter(color=Fore.GREEN)
def birthday_added_message() -> str:
    """Return success message when birthday is added."""
    return BIRTHDAY_ADDED


@output_formatter(color=Fore.GREEN)
def contact_deleted_message() -> str:
    """Return success message when contact is deleted."""
    return CONTACT_DELETED


@output_formatter(color=Fore.BLUE)
def no_upcoming_birthdays_message() -> str:
    """Return message when there are no upcoming birthdays."""
    return NO_UPCOMING_BIRTHDAYS
