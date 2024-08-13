import sys

import config
from utils import *

_exit = sys.exit


def exit(message=None):
    if message:
        print("%s%s" % (message, ' ' * 20))
    _exit(1)


def change_config():
    config.DEFAULT_PASSWORD_LENGTH = int(input("Введите длину пароля (от 6 до 128): "))

    if input("Включить прописные буквы? (Y/N): ").lower() == "y":
        config.USE_UPPERCASE = True
    else:
        config.USE_UPPERCASE = False

    if input("Включить строчные буквы? (Y/N): ").lower() == "y":
        config.USE_LOWERCASE = True
    else:
        config.USE_LOWERCASE = False

    if input("Включить цифры? (Y/N): ").lower() == "y":
        config.USE_DIGITS = True
    else:
        config.USE_DIGITS = False

    if input("Включить специальные символы? (Y/N): ").lower() == "y":
        config.USE_SPECIAL_CHARACTERS = True
    else:
        config.USE_SPECIAL_CHARACTERS = False
    print()


def main():
    print("Добро пожаловать в Генератор Паролей!")
    if input("Вы хотите изменить config? (Y/N): ") == "y":
        change_config()

    while True:
        print(
            f"Сгенерированный пароль: {generate_password(password_length=config.DEFAULT_PASSWORD_LENGTH, uppercase_status=config.USE_UPPERCASE, lowercase_status=config.USE_LOWERCASE, digits_status=config.USE_DIGITS,
                                                         symbols_status=config.USE_SPECIAL_CHARACTERS)}\n")

        if input("Хотите сгенерировать новый пароль с этими же параметрами? (Y/N): ").lower() == "n":
            if input("Хотите изменить параметры и сгенерировать новый пароль? (Y/N): ").lower() == "y":
                change_config()
            else:
                print()
                exit("Спасибо за использование Генератора Паролей!")
        else:
            print()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit("Спасибо за использование Генератора Паролей!")
