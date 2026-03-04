"""AddressBook class for storing and managing contact records."""

from collections import UserDict
from datetime import datetime

from .record import Record


class AddressBook(UserDict):
    """Class for storing records and managing contacts."""

    def add_record(self, record: Record) -> None:
        """Add a record to the address book."""

        self.data[record.name.value] = record

    def find(self, name: str) -> Record | None:
        """Find a record by name."""

        return self.data.get(name)

    def delete(self, name: str) -> None:
        """Delete a record by name."""

        if name in self.data:
            del self.data[name]

    def get_upcoming_birthdays(self) -> list[dict[str, str]]:
        """
        Get a list of contacts whose birthdays occur in the next 7 days.

        Returns:
            List of dicts with 'name' and 'birthday' keys for upcoming birthdays.
            If no upcoming birthdays, returns empty list.
        """
        today = datetime.today().date()
        upcoming: list[dict[str, str]] = []

        for record in self.data.values():
            if record.birthday is None:
                continue

            # Get birthday date for this year
            birthday_date = record.birthday.date.date()
            birthday_this_year = birthday_date.replace(year=today.year)

            # If birthday already passed this year, check next year
            if birthday_this_year < today:
                birthday_this_year = birthday_date.replace(year=today.year + 1)

            # Check if birthday is within next 7 days
            days_until_birthday = (birthday_this_year - today).days

            if 0 <= days_until_birthday < 7:
                upcoming.append(
                    {
                        "name": record.name.value,
                        "birthday": birthday_this_year.strftime("%d.%m.%Y"),
                    }
                )

        return upcoming
