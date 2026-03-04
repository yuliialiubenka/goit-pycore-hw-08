from colorama import Fore

from task.decorators import colored_output, input_error
from task.messages import no_contacts_found_message
from task.models import AddressBook


@colored_output(success_color=Fore.BLUE, info_color=Fore.BLUE)
@input_error
def show_all(book: AddressBook) -> str:
    """
    Display all contacts in a formatted vertical table.

    Returns all contacts sorted alphabetically by name with complete information
    displayed in a vertical table format. Only displays fields that contain data.

    Args:
        book: AddressBook instance containing contact records.

    Returns:
        Formatted vertical table string with contact entries.
        Each contact displayed as a mini-table with aligned columns.
        Returns "No contacts found." if the address book is empty.

    Example:
        >>> book = AddressBook()
        >>> record = Record("John")
        >>> record.add_phone("0987654321")
        >>> book.add_record(record)
        >>> print(show_all(book))
        === Contact List ===
        Name    | John
        Phones  | 0987654321
    """

    if not book.data:
        return no_contacts_found_message()

    sorted_contacts = sorted(book.data.items(), key=lambda item: item[0].lower())

    all_labels = ["Name", "Phones", "Birthday"]
    global_col1_width = max(len(label) for label in all_labels)

    all_tables = []

    for name, record in sorted_contacts:
        rows = [("Name", name)]

        phones_str = ", ".join(p.value for p in record.phones) if record.phones else ""
        if phones_str:
            rows.append(("Phones", phones_str))

        if record.birthday:
            rows.append(("Birthday", record.birthday.value))

        col2_width = max(len(value) for _, value in rows)

        table_lines = []
        for label, value in rows:
            table_lines.append(f"{label:<{global_col1_width}} | {value:<{col2_width}}")

        all_tables.append("\n".join(table_lines))

    title = "=== Contact List ==="
    separator = " " * len(title)
    return f"{title}\n{separator}\n" + "\n\n".join(all_tables)
