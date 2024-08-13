from string import ascii_lowercase, ascii_uppercase, digits
from random import randint


def generate_password(password_length=6, uppercase_status=False, lowercase_status=False, digits_status=False,
                      symbols_status=False):
    password = ""
    source = ""

    if uppercase_status:
        source += ascii_uppercase
    if lowercase_status:
        source += ascii_lowercase
    if digits_status:
        source += digits
    if symbols_status:
        symbols = "!@#$%^&*"
        source += symbols

    source_length = len(source)
    if source_length == 0:
        return "Некорректный выбор символов."

    for _ in range(password_length):
        password += source[randint(0, source_length - 1)]

    return password



