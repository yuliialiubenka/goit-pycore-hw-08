# Python Core Homework 08

Solution for Python Core homework assignment, module 8.
This project contains a CLI contact assistant bot and address book models with OOP architecture.

## Quick Start

### 1. Create Virtual Environment

```cmd
python -m venv .venv
```

### 2. Activate Virtual Environment

**Windows (cmd or PowerShell):**

```cmd
.venv\Scripts\activate
```

**Mac/Linux:**

```bash
source .venv/bin/activate
```

### 3. Install Dependencies

```cmd
pip install -r requirements.txt
```

### 4. Run the CLI Bot

```cmd
python -m task.main
```

```bash
python -m task.main
```

### 5. Run Tests

```cmd
python test_add_users.py
```

## Overview

### CLI Contact Assistant Bot

Interactive console application for contact management with input validation and error handling.

**Technologies:**

- Modular architecture (separate modules for handlers, validators, messages)
- Decorators for error handling and output formatting
- `colorama` for colored terminal messages
- Validation for names and phones (local 10 digits format)
- Dictionary-based contact storage

**Available Commands:**

- `hello` — greeting
- `add <name> <phone>` — add contact with phone number (or add phone to existing contact)
- `change <name> <old_phone> <new_phone>` — change existing phone number
- `phone <name>` — show phone numbers for contact
- `delete <name>` — delete contact from address book
- `add-birthday <name> <birthday>` — add birthday to contact (DD.MM.YYYY format)
- `show-birthday <name>` — show birthday for contact
- `birthdays` — show contacts with upcoming birthdays (next 7 days)
- `all` — show all contacts with details
- `close` / `exit` — exit program

**Phone Format:**

- Accepts: `0501234567`, `050-123-4567`, `(050)123-4567`
- Must be 10 digits starting with 0
- No spaces or international prefix allowed

**Usage Examples:**

```cmd
python -m task.main

REM In interactive mode:
>>> add John 0501234567
>>> phone John
>>> change John 0509876543
>>> all
>>> close
```

### Address Book Models

OOP-based address book implementation in `task/models/` package with proper encapsulation and validation.

**Architecture:**

- **Field** — base class for all fields
- **Name** — name field with validation (min 2 chars, letters only)
- **Phone** — phone field with validation and normalization
- **Record** — contact record managing name and multiple phones
- **AddressBook** — main container inheriting from `UserDict`
- **Custom Exceptions** — hierarchy for error handling

**Key Features:**

- ✅ Type hints throughout all code
- ✅ Custom exception hierarchy (`AddressBookError`, `FieldError`, `RecordError`)
- ✅ Phone normalization (flexible input → 10 digits storage)
- ✅ Name validation (letters, spaces, hyphens, apostrophes)
- ✅ Centralized error messages in constants
- ✅ Full inheritance chain (Field → Name/Phone)

**Test File:**

Run [test_address_book_package.py](test_address_book_package.py) to see the implementation matching homework requirements:

```cmd
python test_address_book_package.py
```

## Project Structure

```
goit-pycore-hw-08/
├── task/
│   ├── handlers/               # Command handlers package
│   │   ├── __init__.py         # Package exports
│   │   ├── add_contact.py      # add command handler
│   │   ├── change_contact.py   # change command handler
│   │   ├── show_phone.py       # phone command handler
│   │   ├── delete_contact.py   # delete command handler
│   │   ├── show_all.py         # all command handler
│   │   ├── add_birthday.py     # add-birthday command handler
│   │   ├── show_birthday.py    # show-birthday command handler
│   │   ├── birthdays.py        # birthdays command handler
│   │   └── execute_command.py  # Command dispatcher
│   ├── decorators/             # Decorators package
│   │   ├── __init__.py         # Package exports
│   │   ├── validate_args.py    # Argument validation decorator
│   │   ├── input_error.py      # Exception handling decorator
│   │   ├── colored_output.py   # Semantic color formatting decorator
│   │   └── output_formatter.py # Fixed style formatting decorator
│   ├── models/                 # Address book models package
│   │   ├── __init__.py         # Package exports
│   │   ├── address_book.py     # AddressBook class
│   │   ├── exceptions.py       # Custom exceptions hierarchy
│   │   ├── field.py            # Base Field class
│   │   ├── name.py             # Name field with validation
│   │   ├── phone.py            # Phone field with validation
│   │   ├── record.py           # Record class
│   │   └── birthday.py         # Birthday field with validation
│   ├── input_parser.py         # Command parsing logic
│   ├── main.py                 # CLI bot entry point
│   ├── message_texts.py        # Centralized message constants
│   ├── messages.py             # Message formatting utilities
│   └── validators.py           # Input validation functions
├── test_add_users.py               # Comprehensive integration test
├── requirements.txt            # Dependencies
└── README.md                   # Documentation
```

## Architecture & Design Patterns

### Modular Organization

- **handlers/** — Command implementation (each command in separate file)
- **decorators/** — Reusable decorators for validation, error handling, and formatting
- **models/** — Data structures with validation and business logic
- **validators.py** — Pure validation functions (reusable across CLI and models)
- **messages.py** — Formatted user-facing messages with colors
- **main.py** — CLI event loop

### Decorator Stack Pattern

Handlers use layered decorators for clean separation:

```python
@colored_output()           # Automatic color formatting (outer)
@input_error                # Exception → friendly message
@validate_args(...)         # Argument validation (inner)
def handler(args, book):
    pass
```

### Error Handling

- **Custom exceptions** in models layer for strict validation
- **Decorator-based** exception handling in CLI layer
- **Two-phase validation:** CLI validators → model validators

## Birthday Feature

Contacts can store birthdays in DD.MM.YYYY format:

```cmd
add-birthday John 25.12.1990
show-birthday John
birthdays                    # Show upcoming (next 7 days)
```

**Features:**

- Birthday validation with leap year support
- Upcoming birthday calculation window
- Birthday display integrated with contact list (`all` command)
- Independent birthday management (can be added/removed anytime)

## Technologies and Concepts

- **Python 3.12+** — modern version with type hints support
- **OOP** — inheritance (Field → Name/Phone), encapsulation, custom exceptions
- **Type Hints** — comprehensive type annotations (`str | None`, `list[Phone]`, etc.)
- **Custom Exceptions** — exception hierarchy for clear error handling
- **Decorators** — for error handling and output formatting
- **colorama** — colored terminal output
- **re (regular expressions)** — for validation and text parsing
- **UserDict** — proper dictionary inheritance for AddressBook
- **Package Structure** — modular organization with `__init__.py` exports
- **Validation** — two-layer (CLI input + model level)
- **Data Normalization** — flexible phone input formats normalized to storage format

## Validation Rules

### Phone Numbers

- **Format:** Local 10-digit numbers only
- **Must start with:** 0
- **Accepted input:** `0501234567`, `050-123-4567`, `(050)123-4567`
- **Not allowed:** spaces, international prefix (`+380`)
- **Storage:** Normalized to 10 digits (`0501234567`)

### Names

- **Min length:** 2 characters
- **Allowed:** letters, spaces, hyphens, apostrophes
- **Not allowed:** numbers, special symbols
- **Examples:** `John`, `Mary-Jane`, `O'Brien`

## Requirements

See [requirements.txt](requirements.txt) for full dependency list.
