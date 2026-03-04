"""
Single end-to-end test for adding users and checking key bot features.

This test intentionally includes a symbolic birthday case:
- Yuliia Koliesnik, 0987654321, 02.03.<current year>
"""

from datetime import datetime
import re

from task.input_parser import parse_input
from task.handlers import execute_command
from task.models import AddressBook


ANSI_RE = re.compile(
    r"\x1b\[[0-9;]*m"
)  # Match terminal color/style ANSI escape sequences


def strip_ansi(text: str) -> str:
    """Remove ANSI color sequences to make assertions stable."""

    return ANSI_RE.sub("", text)


def run_command(command_line: str, book: AddressBook) -> str:
    """Execute one bot command and return plain (colorless) text."""

    command, args = parse_input(command_line)
    return strip_ansi(execute_command(command, args, book))


def main() -> None:
    """Run one combined test scenario for adding users and app features."""

    print("=" * 60)
    print("SYMBOLIC USER-ADDING TEST")
    print("=" * 60)

    book = AddressBook()

    # Symbolic birthday entry: 02.03.<current year>
    current_year = datetime.today().year
    today = datetime.today().date()
    yuliia_birthday = f"02.03.{current_year}"
    yuliia_birthday_date = datetime.strptime(yuliia_birthday, "%d.%m.%Y").date()

    if today <= yuliia_birthday_date:
        print(
            f"\n[SYMBOLIC] Yuliia Koliesnik is celebrating her birthday on {yuliia_birthday}"
        )
    else:
        print(
            f"\n[SYMBOLIC] Yuliia Koliesnik celebrated her birthday on {yuliia_birthday}"
        )

    # 1) Add users
    assert "Contact added." in run_command("add Yuliia Koliesnik 0987654321", book)
    assert "Contact added." in run_command("add John Carter 0501234567", book)
    assert "Contact added." in run_command("add Anna Bell 0670001122", book)

    # 2) Add second phone for one contact
    assert "Contact updated." in run_command("add John Carter 0509990001", book)

    # 3) Add birthdays
    assert "Birthday added." in run_command(
        f"add-birthday Yuliia Koliesnik {yuliia_birthday}",
        book,
    )
    assert "Birthday added." in run_command("add-birthday John Carter 01.03.2000", book)

    # 4) Verify single-contact views
    yuliia_phone = run_command("phone Yuliia Koliesnik", book)
    assert "Yuliia Koliesnik: 0987654321" in yuliia_phone

    yuliia_bday = run_command("show-birthday Yuliia Koliesnik", book)
    assert f"Yuliia Koliesnik: {yuliia_birthday}" in yuliia_bday

    # 5) Verify all-contacts view contains expected rows
    all_contacts = run_command("all", book)
    assert "Contact" in all_contacts
    assert "Yuliia Koliesnik" in all_contacts
    assert "Birthday" in all_contacts
    assert yuliia_birthday in all_contacts
    assert "John Carter" in all_contacts
    assert "0501234567, 0509990001" in all_contacts

    # 6) Verify birthdays output exists (John has fixed 01.03, Yuliia has 02.03)
    upcoming = run_command("birthdays", book)
    assert (
        "No upcoming birthdays" in upcoming
        or "John Carter" in upcoming
        or "Yuliia Koliesnik" in upcoming
    )

    # 7) Test delete contact
    print("\n[TEST DELETE] Removing Anna Bell from contacts")
    assert "Contact deleted." in run_command("delete Anna Bell", book)
    # Verify contact is gone by checking all contacts
    all_after_delete = run_command("all", book)
    assert "Anna Bell" not in all_after_delete
    print("Anna Bell successfully deleted")
    print("All checks passed.")

    # 8) Display all remaining contacts at the end
    print("\n" + "=" * 60)
    print("ALL REMAINING CONTACTS (after deletion):")
    print("=" * 60)
    all_final = run_command("all", book)
    print(all_final)
    print("=" * 60)


if __name__ == "__main__":
    main()
