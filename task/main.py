from colorama import init

from task.input_parser import parse_input
from task.handlers import execute_command
from task.models import AddressBook
from task.messages import (
    welcome_message,
    goodbye_message,
    prompt_for_command,
)

# Initialize colorama for Windows compatibility
init(autoreset=True)


def main() -> None:
    """
    Main CLI loop for the contact assistant bot.

    Provides an interactive command-line interface for managing contacts.
    Supported commands:
    - hello: Display greeting
    - add <name> <phone>: Add a new contact
    - change <name> <old_phone> <new_phone>: Update phone number
    - phone <name>: Look up a contact's phone numbers
    - delete <name>: Remove a contact
    - all: Display all contacts in a formatted table
    - add-birthday <name> <date>: Add birthday (DD.MM.YYYY)
    - show-birthday <name>: Show birthday for a contact
    - birthdays: Show upcoming birthdays (next 7 days)
    - close/exit: Terminate the program

    The bot runs in an infinite loop until the user enters "close" or "exit".
    """

    book = AddressBook()

    print(welcome_message())

    try:
        while True:
            user_input = input(prompt_for_command())

            # Skip empty input
            if not user_input.strip():
                continue

            command, args = parse_input(user_input)

            if command in ["close", "exit"]:
                print(goodbye_message())
                break

            result = execute_command(command, args, book)

            if result:  # Only print if there's a result
                print(result)

    except (KeyboardInterrupt, EOFError):
        print()
        print(goodbye_message())


# For testing purposes
if __name__ == "__main__":
    main()
