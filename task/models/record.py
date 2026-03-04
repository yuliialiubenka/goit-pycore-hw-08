"""Record class for storing contact information."""

from task.message_texts import PHONE_NOT_FOUND_IN_RECORD

from .birthday import Birthday
from .exceptions import PhoneNotFoundError
from .name import Name
from .phone import Phone


class Record:
    """Class for storing contact information including name, phones, and birthday."""

    def __init__(self, name: str) -> None:
        """Initialize record with contact name."""

        self.name: Name = Name(name)
        self.phones: list[Phone] = []
        self.birthday: Birthday | None = None

    def add_phone(self, phone: str) -> None:
        """Add a phone number to the record."""

        self.phones.append(Phone(phone))

    def remove_phone(self, phone: str) -> None:
        """Remove a phone number from the record."""

        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone: str, new_phone: str) -> None:
        """Edit an existing phone number in the record."""

        phone_found: bool = False

        for i, phone in enumerate(self.phones):
            if phone.value == old_phone:
                self.phones[i] = Phone(new_phone)
                phone_found = True
                break

        if not phone_found:
            raise PhoneNotFoundError(PHONE_NOT_FOUND_IN_RECORD.format(phone=old_phone))

    def find_phone(self, phone: str) -> str | None:
        """Find and return a phone number if it exists in the record."""

        for p in self.phones:
            if p.value == phone:
                return p.value

        return None

    def add_birthday(self, birthday: str) -> None:
        """Add a birthday to the record."""

        self.birthday = Birthday(birthday)

    def __str__(self) -> str:
        """Return string representation of contact record."""

        phones_str = '; '.join(p.value for p in self.phones)
        result = f"Contact name: {self.name.value}, phones: {phones_str}"

        if self.birthday:
            result += f", birthday: {self.birthday.value}"

        return result
