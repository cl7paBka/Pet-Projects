# config.py

# Минимальная и максимальная длина пароля
MIN_PASSWORD_LENGTH = 6
MAX_PASSWORD_LENGTH = 128

# Типы символов, которые могут использоваться в пароле
USE_UPPERCASE = True      # Прописные буквы (A-Z)
USE_LOWERCASE = True      # Строчные буквы (a-z)
USE_DIGITS = True         # Цифры (0-9)
USE_SPECIAL_CHARACTERS = True  # Специальные символы (!@#$%^&*)

# Специальные символы, которые могут использоваться в пароле
SPECIAL_CHARACTERS = "!@#$%^&*()-_=+[]{}|;:,.<>?/"

# Настройки по умолчанию
DEFAULT_PASSWORD_LENGTH = 12  # Длина пароля по умолчанию
