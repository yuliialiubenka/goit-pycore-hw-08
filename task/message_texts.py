"""
Centralized user-facing text constants for the assistant bot.
"""

INPUT_ERROR_MISSING_ARGS = "Give me name and phone please."
INPUT_ERROR_MISSING_ARGS_CHANGE = (
    "To change a phone number, provide: name, old phone, new phone.\n"
    "Usage: change [name] [old phone] [new phone]"
)
INPUT_ERROR_MISSING_ARGS_DELETE = (
    "To delete a contact, provide: name. " 
	"Usage: delete [name]"
)
INPUT_ERROR_CONTACT_NOT_FOUND = "Contact not found."
INPUT_ERROR_ENTER_NAME = "Enter user name."

UNKNOWN_COMMAND = (
    "Unknown command. Try: hello, add, change, phone, all, delete, "
    "add-birthday, show-birthday, birthdays, close, exit"
)

WELCOME_MESSAGE = "Welcome to the assistant bot!"
HELLO_MESSAGE = "How can I help you?"
GOODBYE_MESSAGE = "Good bye!"

ERROR_UNEXPECTED_ARGUMENTS = "Error: The command '{command}' does not accept arguments."

# PROMPT_FOR_ARGUMENT = "Enter the {arg_description} for the command {command}: "
PROMPT_FOR_COMMAND = "Enter a command: "

NO_CONTACTS_FOUND = "No contacts found."

INVALID_NAME_FORMAT = (
    "Invalid name format. Use letters with optional spaces, hyphens, or apostrophes."
)
INVALID_PHONE_FORMAT = (
    "Invalid phone format. Use local number (10 digits, no spaces).\n"
    "Examples: 0501234567 | 050-123-4567 | (050)123-4567"
)
INVALID_BIRTHDAY_FORMAT = "Invalid date format. Use DD.MM.YYYY"
INVALID_ARGUMENT_FORMAT = "Invalid format for argument {arg_index}."

PHONE_NOT_FOUND_IN_RECORD = "Phone number {phone} not found in record"

BIRTHDAY_ADDED = "Birthday added."
BIRTHDAY_DELETED = "Birthday removed."
CONTACT_DELETED = "Contact deleted."
NO_UPCOMING_BIRTHDAYS = "No upcoming birthdays in the next 7 days."
