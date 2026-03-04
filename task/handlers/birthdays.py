from task.decorators import colored_output, input_error
from task.messages import no_upcoming_birthdays_message
from task.models import AddressBook


@colored_output()
@input_error
def birthdays(book: AddressBook) -> str:
    """
    Show all upcoming birthdays in the next 7 days.

    Args:
        book: AddressBook instance.

    Returns:
        Formatted list of upcoming birthdays or message if none found.

    Example:
        >>> book = AddressBook()
        >>> birthdays(book)
        "No upcoming birthdays in the next 7 days."
    """

    upcoming = book.get_upcoming_birthdays()

    if not upcoming:
        return no_upcoming_birthdays_message()

    lines = [f"{record['name']}: {record['birthday']}" for record in upcoming]
    return "\n".join(lines)
